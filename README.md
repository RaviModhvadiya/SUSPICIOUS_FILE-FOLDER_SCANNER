# SUSPICIOUS_FOLDER_SCANNER

# 🛡️ Simple SOC File & Folder Scanner (Python)

## 📌 Overview
A **beginner-level SOC Tier-1 project** built with Python that scans folders and files to identify **potentially suspicious files** using basic static indicators.  
This tool simulates how **SOC analysts validate file alerts** during investigations.

⚠️ The tool performs **safe static analysis only** and **never executes files**.

---

## 🎯 Purpose
- Practice **SOC Tier-1 alert triage**
- Learn **basic malware indicators**
- Automate file scanning using **Python**
- Build a **job-relevant SOC beginner project**

---

## 🔍 Features
- Scan all files in a selected folder
- Detect suspicious files based on:
  - File extensions
  - File name keywords
- Generate **SHA256 hash**
- Assign simple **risk level (Medium / High)**

---

## 🧠 Detection Logic
**Suspicious Extensions:**  
`.exe`, `.bat`, `.ps1`, `.vbs`, `.scr`

**Suspicious Keywords:**  
`invoice`, `payment`, `urgent`, `password`

---

## 🏢 SOC Usage
- **SOC Tier-1**: File alert validation, phishing attachment checks  
- **SOC Tier-2**: Initial static file investigation  

⭐ **Importance:** High — reflects real SOC workflow.

---

## 🛠️ Tech Stack
- Python 3  
- Libraries: `os`, `hashlib`  

---

⚠️ Disclaimer

For educational purposes only.
Not a replacement for antivirus, EDR, or SIEM tools.
