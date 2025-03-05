# 📝 Rationale - Validation of the Extraction Process

This document explains how the data extraction from **scientific articles** has been validated.

## 1️⃣ **Validation of Extracted Data**
- **Title** → Checked against manually inspected PDFs.
- **Abstract** → Verified by comparing extracted text with Grobid output (`output.xml`).
- **Figures Count** → Cross-checked using PDF manual inspection.
- **Links** → Extracted URLs are validated by checking accessibility.

## 2️⃣ **Word Cloud Validation**
- **Stopwords removed** to avoid bias.
- **Checked against abstracts** to ensure meaningful keywords.

## 3️⃣ **Bar Chart Validation**
- Manually counted figures in PDFs to verify automated extraction.
- Visual inspection of the **CSV output** to ensure correctness.

## 4️⃣ **Error Handling**
✔ If Grobid fails, script shows **clear error messages**.  
✔ If PDFs are malformed, script **skips the file** and logs the error.  

## ✅ Conclusion
All extracted data has been **cross-validated** using both **automated scripts and manual checks**.

