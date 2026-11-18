# HubSpot Attachment Auditor & File Scanner

A free, open-source script to audit files attached to HubSpot CRM emails, notes, calls, meetings, and tickets before CRM migrations or compliance audits.

---

## 🎯 What it Solves

In HubSpot, files uploaded directly to CRM timelines (such as email attachments, signed contracts, passport copies, or receipts) are stored as engagement attachments. 

Standard HubSpot data exports only export record properties (name, email, deal stage) to CSV, leaving attachment columns blank or showing numeric internal IDs.

This tool queries the HubSpot API to:
1. Scan all engagement attachments across Contacts, Companies, Deals, and Tickets.
2. Count total files and calculate approximate storage volume.
3. Classify files by type (`.pdf`, `.png`, `.xlsx`, `.docx`, etc.).
4. Flag potentially sensitive compliance documents (e.g., filenames containing `passport`, `tax`, `contract`, `nda`, `statement`).

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.8+
- HubSpot Private App Token with scopes: `crm.objects.contacts.read`, `crm.objects.deals.read`, `files.read`

### 2. Run the Audit
```bash
export HUBSPOT_ACCESS_TOKEN="pat-na1-xxxxxx"
python3 audit_attachments.py
```

### 3. Example Terminal Output
```text
=== HubSpot Engagement Attachment Audit Report ===

Audited Records: 150 Deals, 420 Contacts, 85 Tickets
Total Attached Files Found: 642 files (~1.4 GB)

📁 File Types Breakdown:
- PDF Documents (.pdf): 412 files (64.2%)
- Spreadsheets (.xlsx, .csv): 118 files (18.4%)
- Images (.png, .jpg): 86 files (13.4%)
- Other: 26 files (4.0%)

🔒 Sensitive Document Flags Detected:
- 48 contracts / agreements (e.g. "Acme_Signed_Contract_2026.pdf")
- 12 tax / financial statements (e.g. "Q3_Tax_Return.pdf")
- 4 identification / passport scans
```

---

## ⚡ Want to Bulk Download All Files in One Click?

If you need to download all attached files in organized ZIP batches with a CSV manifest mapping each file back to its CRM record:

👉 **[Attachment Exporter for HubSpot](https://kayabyte.dev/hubspot/attachment-exporter/?src=c-gh-export)**

- **Bulk Download:** Downloads all timeline files into clean ZIP folders organized by record.
- **CSV Manifest:** Generates an itemized CSV linking every filename to its associated Contact, Company, or Deal ID.
- **Audit & Sensitive File Detection:** Built-in security scan for GDPR compliance.
- **Fair Pricing:** First 250 files are 100% free. One-off credit packs from $49 (no recurring subscription).

*(Note: Attachment Exporter installs directly from kayabyte.dev while in marketplace review; includes standard HubSpot unverified-app screen where you type 'I accept the risk').*

---

## 📄 License
MIT License. Free to use, adapt, and run for your CRM migrations.
