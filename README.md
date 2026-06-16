# PDF Batch Print Automator for Administrative Workflows

## 📌 Project Overview
In administrative and project management workflows, processing approved project estimates often requires printing multiple, specific physical sets (e.g., short copies for specific departments, full copies for archives). Manually opening, configuring, and printing these sets one by one is highly time-consuming and prone to clerical errors.

I developed this Python automation tool to completely eliminate that bottleneck. This script takes a folder of approved estimate PDFs and compiles them into a single, perfectly sequenced "Master PDF." An employee only needs to click "Print" once, and the printer will output the exact document sets required.

## 🚀 Features & Business Value
* **Custom 3-Set Sequencing:** Engineered to meet specific administrative compliance requirements by automatically generating exactly three distinct sets per estimate (two 4-page department copies and one full master copy).
* **Duplex Printing Optimization (The "Padding" Logic):** Calculates the page count of every document and automatically inserts blank pages to ensure sets are padded to multiples of 4. This guarantees that when printing double-sided (duplex), distinct estimates never overlap onto the same physical sheet of paper.
* **Massive Time Savings:** Reduces a manual, multi-step printing task down to a single 3-second script execution. 

## 🛠️ Prerequisites
You will need Python installed on your system, along with the `pypdf` library. 

To install the required library, open your terminal or command prompt and run:
`pip install pypdf`

## ⚙️ How to Use
1. Place all your approved estimate PDFs into a single folder.
2. Run the script: `python pdf_batch_printer.py`
3. Paste the folder path when prompted.
4. The script will generate a `Master_Ready_To_Print.pdf` in the same directory.
5. Open the Master PDF, set your printer to "Double-Sided (Duplex)", and hit print.

## 🤝 Custom Requirements?
This script was built to solve a specific workflow, but automation is highly adaptable. If your administrative process requires a different number of sets, specific page ranges, or a different style of printing, please let me know! I would be happy to update or modify the Python code to fit your exact workflow needs.
