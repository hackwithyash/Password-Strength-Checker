# 🔐 Password Strength Checker - PyQt5

A stylish, intuitive, and user-friendly **Password Strength Checker** built using **Python** and **PyQt5**. This tool evaluates the strength of your password and provides helpful suggestions to make it stronger. Features include real-time feedback, progress bar visualization, and optional show/hide password functionality.


<img width="532" height="387" alt="image" src="https://github.com/user-attachments/assets/6e8db0ca-c7b7-440b-8d22-e9720db12925" />

---

## 🚀 Features

- ✅ Real-time password strength evaluation
- ✅ Feedback with improvement suggestions
- ✅ Visual strength meter (progress bar with colors)
- ✅ Show/Hide password with toggle icon
- ✅ Clean, responsive UI with dark mode support (optional)
- ✅ Modular codebase (easy to expand or customize)

---

## 🧠 How It Works

The password is evaluated based on:

- Minimum length (8 characters)
- Contains numbers (`0-9`)
- Contains lowercase letters (`a-z`)
- Contains uppercase letters (`A-Z`)
- Contains special symbols (`!@#$%^&*()` etc.)

Each satisfied condition increases the strength score (out of 5). Based on the total score:

- 🔴 **Weak** (0–2)
- 🟠 **Moderate** (3–4)
- 🟢 **Strong** (5)

---

## 🖼️ UI Overview

| Strength      | Progress Bar | Message                |
|---------------|--------------|------------------------|
| Weak (0–2)    | Red          | Weak suggestions shown |
| Moderate (3–4)| Orange       | Moderate suggestions   |
| Strong (5)    | Green        | All checks passed ✅   |

---

## 🧰 Requirements

- Python 3.x
- PyQt5

> Install dependencies:

```bash
pip install PyQt5
```

## 🛠️ How to Run

```bash
python password_checker.py
```

## 📦password-strength-checker
- ┣ 📄 password_checker.py     # Main application code
- ┣ 📄 eye.png                  # Icon to show password
- ┣ 📄 eye-off.png              # Icon to hide password
- ┗ 📄 README.md                # Project documentation

## 🤝 Contributing
- Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change or improve.

## 📜 License
- This project is licensed under the MIT License.

## 🙌 Acknowledgements
- Icons from FontAwesome / Custom SVG
- Inspiration from KeePass, LastPass, and browser security checkers

