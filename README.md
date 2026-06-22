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

**Option A: Run from Source Code**
1. Install the required dependency via your terminal: `pip install pypdf`
2. Run the script: `python pdf_batch_printer.py`
3. Paste your target folder path when prompted. The tool will compile a `Master_Ready_To_Print.pdf`. Open it, ensure your physical printer is set to **Double-Sided (Duplex)**, and hit print!

**Option B: Build a Standalone Executable (.exe)**
*(For users without Python installed)*
1. Install the compiler tool: `pip install auto-py-to-exe`
2. Launch the visual interface: `python -m auto_py_to_exe`
3. Select your `pdf_batch_printer.py` file, choose **One File**, and select **Window Based (hide the console)**.
4. Click convert! You can now share the resulting `.exe` file with anyone. *(Note: Executables built with modern Python are designed for Windows 10/11 and are not officially supported on older systems like Windows 7/8).*

---

## 🤝 Customization & Contribution
This automation logic is highly adaptable. If your workflow requires a different number of sets, alternate page ranges, or unique padding rules, the code can be easily modified to fit your exact requirements. Feel free to open an Issue or submit a Pull Request!

<br>

<div align="center">
  <i>Developed by Harsh Kamalakar</i>
</div>
