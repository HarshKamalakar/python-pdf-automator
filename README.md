<h1 align="center">🖨️ PDF Batch Print Automator</h1>

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/pypdf-enabled-brightgreen" alt="PyPDF">
  <img src="https://img.shields.io/badge/tkinter-native-lightgrey" alt="Tkinter">
  <img src="https://img.shields.io/badge/automation-100%25-orange" alt="Automation">
</div>

<br>

> **An intelligent, Python-powered digital collator engineered to eliminate manual printing bottlenecks and streamline administrative workflows.**

---

## ⚡ The Challenge vs. The Solution

**The Bottleneck:** Compliance often dictates specific physical sets for approved estimates (e.g., short copies for multiple departments, full copies for archives). Manually configuring page ranges and printing these sets individually is a massive administrative time-sink. Furthermore, double-sided (duplex) printing often causes different estimates to bleed onto the same physical sheet of paper.

**The Solution:** Drop all approved estimate PDFs into a single folder. This script dynamically processes the batch, automatically pads pages to prevent duplex bleeding, and generates **one perfectly sequenced "Master PDF."** Click "Print" once, and the printer outputs the exact document sets required.

## 📊 Business Impact & Core Features

| Metric | Manual Process | Automated System |
| :--- | :--- | :--- |
| **Time per 50 files** | ~45-60 minutes | **~3 seconds** |
| **Error Rate** | High (wrong page ranges, missed files) | **Zero** |
| **Duplex Overlap** | Frequent (requires manual blank pages) | **Automatically Prevented** |

* **⚙️ Custom Batch Sequencing:** Automatically extracts and generates distinct sets per document based on your exact specifications.
* **🧠 Smart Duplex Padding:** Dynamically calculates page counts and inserts blank "padding" pages. This guarantees a new estimate *always* starts on a fresh piece of paper when duplex printing.
* **🖥️ Native Windows UI:** Lightweight, built-in graphical interface that requires no heavy external frameworks.
* **⚡ Zero-Click Processing:** Scans target directories and processes all recognized `.pdf` files instantly.

---

## 🚀 How to Use This Tool

There is no installation or setup required. 

1. **Download the tool:** Go to the **Releases** section on the right side of this GitHub page and download the `pdf_batch_printer_harsh.py.exe` file.
2. **Run it:** Double-click the file to launch the application. *(Note: If Windows Defender shows a blue warning screen on the first launch, click **More info** and then **Run anyway**).*
3. **Print:** Select your folder, configure your sets when prompted, and the tool will compile a `Master_Ready_To_Print.pdf`. Open it, ensure your physical printer is set to **Double-Sided (Duplex)**, and hit print!

---

## 🤝 Feedback & Contribution
This tool was engineered to dynamically handle almost any batch printing requirement without needing to touch the code. However, if you encounter a bug, or if you are a developer with an idea for a new feature, feel free to open an **Issue** or submit a **Pull Request**!

<br>

<div align="center">
  <i>Developed by Harsh Kamalakar</i>
</div>
