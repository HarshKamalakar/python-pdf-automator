<h1 align="center">🖨️ PDF Batch Print Automator</h1>

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/pypdf-enabled-brightgreen" alt="PyPDF">
  <img src="https://img.shields.io/badge/automation-100%25-orange" alt="Automation">
</div>

<br>

> **An intelligent, Python-powered digital collator engineered to eliminate manual printing bottlenecks and streamline administrative workflows.**

---

## ⚡ The Challenge vs. The Solution

**The Bottleneck:** Compliance often dictates specific physical sets for approved estimates (e.g., short copies for multiple departments, full copies for archives). Manually configuring page ranges and printing these sets individually is a massive administrative time-sink. Furthermore, double-sided (duplex) printing often causes different estimates to bleed onto the same physical sheet of paper.

**The Solution:** Drop all approved estimate PDFs into a single folder. This script dynamically processes the batch, automatically pads pages to prevent duplex bleeding, and generates **one perfectly sequenced "Master PDF."** Click "Print" once, and the printer outputs the exact document sets required.

---

## 📊 Business Impact

| Metric | Manual Process | Automated System |
| :--- | :--- | :--- |
| **Time per 50 files** | ~45-60 minutes | **~3 seconds** |
| **Error Rate** | High (wrong page ranges, missed files) | **Zero** |
| **Duplex Overlap** | Frequent (requires manual blank pages) | **Automatically Prevented** |

---

## ✨ Core Features

* **⚙️ Custom 3-Set Sequencing:** Automatically extracts and generates exactly three distinct sets per estimate: **two 4-page department copies** and **one full master copy**.
* **🧠 Smart Duplex Padding:** Dynamically calculates page counts and inserts blank "padding" pages so every set is a multiple of 4. This guarantees a new estimate *always* starts on a fresh piece of paper when duplex printing.

---

## 🚀 Quick Start

**1. Install Dependencies:**
```bash
pip install pypdf
```

**2. Run the Automator:**
```bash
python pdf_batch_printer.py
```
*Paste your target folder path when prompted. The script will instantly compile a `Master_Ready_To_Print.pdf`. Open it, set your physical printer to **"Double-Sided (Duplex)"**, and hit print!*

---

## 🤝 Customization
This automation logic is highly adaptable. If your workflow requires a different number of sets, alternate page ranges, or unique padding rules, the code can be easily modified to fit your exact requirements. Feel free to open an Issue or pull request!
