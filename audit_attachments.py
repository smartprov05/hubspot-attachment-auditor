#!/usr/bin/env python3
"""
HubSpot Attachment Auditor CLI
Scans HubSpot CRM records for engagement attachments and summarizes file counts and types.
Requires a Private App token with `crm.objects.contacts.read`, `crm.objects.deals.read`, `files.read`.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from collections import Counter

TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN")

def get_headers():
    if not TOKEN:
        print("Error: HUBSPOT_ACCESS_TOKEN environment variable not set.", file=sys.stderr)
        print("Set it using: export HUBSPOT_ACCESS_TOKEN='pat-na1-xxxxxx'", file=sys.stderr)
        sys.exit(1)
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

def scan_files():
    # Scan files via the HubSpot Files API
    url = "https://api.hubapi.com/files/v3/files?limit=100"
    req = urllib.request.Request(url, headers=get_headers(), method="GET")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("results", [])
    except urllib.error.HTTPError as e:
        print(f"HubSpot API error: {e.code} - {e.read().decode('utf-8')}", file=sys.stderr)
        sys.exit(1)

def main():
    print("=== HubSpot Engagement Attachment Auditor ===")
    files = scan_files()
    print(f"Scanned {len(files)} files from HubSpot.\n")

    extensions = Counter()
    sensitive_count = 0
    total_bytes = 0

    sensitive_keywords = ["passport", "contract", "nda", "tax", "statement", "invoice", "id_"]

    for f in files:
        name = f.get("name", "").lower()
        size = f.get("size", 0)
        ext = os.path.splitext(name)[1] or "no_ext"
        extensions[ext] += 1
        total_bytes += size

        if any(kw in name for kw in sensitive_keywords):
            sensitive_count += 1

    total_mb = total_bytes / (1024 * 1024)
    print(f"Total File Count: {len(files)}")
    print(f"Estimated Total Size: {total_mb:.2f} MB")
    print(f"Sensitive / Compliance Files Flagged: {sensitive_count}\n")

    print("📁 File Extensions Breakdown:")
    for ext, count in extensions.most_common(10):
        print(f"  {ext}: {count} files")

    print("\nTo bulk download all files mapped with CSV manifests into ZIP archives:")
    print("Visit: https://kayabyte.dev/hubspot/attachment-exporter/?src=c-gh-cli")

if __name__ == "__main__":
    main()
