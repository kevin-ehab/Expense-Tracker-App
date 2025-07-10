# 📊 Expense-Tracker-App
💰💸An interactive desktop Expense Tracker built using 🐍Python with Tkinter, Pandas, Matplotlib, Jinja2, and PyWebview. It allows users to 🔒securely manage their expenses, track spending patterns, 📈visualize insights, and save for future goals🥇.

---

## 🚀 Features

- ✅ User Authentication (Sign Up & Login)
- 🔒 Password & Budget Encryption (Custom-made `simple_encrypter` module)
- 💾 Persistent Data Storage with CSV
- 📈 Visual Insights using Pie Charts, Trends & Spending Analysis
- 📊 Auto-generated HTML Dashboard with graphs and tables
- 🛡 Secure handling of financial data

---
## 📸 Screenshots:
- Loading screen: <br>
![loading](https://github.com/user-attachments/assets/e9d44479-827e-401e-9f2b-1a1f888db6e9)<br>
- Login screen: <br>
![login](https://github.com/user-attachments/assets/ca409f35-254b-43ec-b070-5d0289f513dc)<br>
- Options screen: <br>
![options](https://github.com/user-attachments/assets/723cf590-57b9-4bd2-8d0b-6c29c7a35057)<br>
- Entries screen: <br>
![Entries](https://github.com/user-attachments/assets/25371390-0ade-4959-b862-b5651aab828c)<br>
- Dashboard example: <br>
![dashboard1](https://github.com/user-attachments/assets/c4cc3328-8da3-4f45-a021-c665aaf2e6e2)<br>
![dashboard2](https://github.com/user-attachments/assets/a177efe4-3cac-4cd4-88e3-a5dcb11f21eb)

---
## 📂 Files Overview

| File | Description |
|------|-------------|
| `main.py` | Main Python script with all app logic |
| `simple_encrypter.py` | Custom encryption and decryption module |
| `template.html` | HTML template for insights dashboard |
| `Classified.csv` | Stores user credentials and settings |
| `Expenses.csv` | Stores expenses data |
| `logo.png` | App logo image |
| `icon.ico` | App icon |

---

## 🛠 Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **Pandas** for data management
- **Matplotlib** for plotting charts
- **Jinja2** for dynamic HTML generation
- **PyWebview** for in-app web views
- **PIL (Pillow)** for image handling

---

## 🔑 How It Works

1. **Sign Up / Login:** Users create an account or log into an existing one.
2. **Secure Storage:** Passwords and budgets are encrypted and saved in `Classified.csv`.
3. **Track Expenses:** Users add daily expenses across various categories.
4. **View Insights:** Generates an interactive HTML dashboard with:
   - Category-wise spending breakdown
   - Daily average & saving suggestions
   - Interactive charts and tables
5. **Edit Budget:** Users can update their budget and saving goals anytime.

---

## 📋 Running the App

1. Install required packages:

```bash
pip install pandas matplotlib jinja2 pillow pywebview
```

2. Run the app:

```bash
python main.py
```

---

## 🔐 Encryption Module (`simple_encrypter.py`)
I have a github repo only for it -> [simple-encrypter](https://github.com/kevin-ehab/simple-encrypter) <br>
- Randomly applies one of 5 basic encryption methods to obfuscate passwords and budgets.
- Supports both encryption and decryption.
- Although simplistic, it's designed to prevent plain-text storage.

---

## 💻 Dashboard Example

The dashboard includes:

- 🥧 **Pie Chart**: Category-wise expenses
- 📉 **Trend Chart**: Spending over time vs average
- 📊 **Bar Chart**: Daily spending as % of budget
- 📝 **Table**: Detailed breakdown of daily expenses

---

## 📦 Packaging (Optional)

To distribute the project without sharing the raw code:

👉 You can convert the project into a standalone `.exe` using **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "logo.png;." --add-data "icon.ico;." --add-data "template.html;." main.py
```

Place your `Classified.csv` and `Expenses.csv` alongside the `.exe`.

---

## 📜 License

© 2025 Kevin Ehab. All rights reserved.

---

## 🙌 Acknowledgments

Built from scratch for personal use, learning, and fun. 😊


