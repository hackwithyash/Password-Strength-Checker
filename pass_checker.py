import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar, QAction
)
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QPalette, QColor, QIcon

def check_strength(password):
    suggestions = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add symbols (!@#$ etc.)")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions, score

class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Strength Checker")
        self.setFixedSize(550, 400)
        self.is_dark_mode = False
        self.show_password = False
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 20, 30, 20)

        self.label_title = QLabel("🔒 Password Strength Checker")
        self.label_title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.label_title, alignment=Qt.AlignCenter)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setPlaceholderText("Enter your password here...")
        self.input_password.setStyleSheet("""
            font-size: 18px;
            border-radius: 6px;
            padding: 8px;
        """)

        # add eye icon action
        self.eye_action = QAction(QIcon("eye.png"), "Show/Hide", self)
        self.eye_action.triggered.connect(self.toggle_password)
        self.input_password.addAction(self.eye_action, QLineEdit.TrailingPosition)

        layout.addWidget(self.input_password)

        self.btn_check = QPushButton("Check Strength")
        self.btn_check.setStyleSheet("""
            font-size: 18px;
            padding: 8px;
            border-radius: 6px;
        """)
        self.btn_check.clicked.connect(self.on_check)
        layout.addWidget(self.btn_check)

        self.progress = QProgressBar()
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setFormat("%p%")
        self.progress.setStyleSheet("""
            QProgressBar {
                font-size: 16px;
                height: 25px;
                border-radius: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                border-radius: 10px;
            }
        """)
        layout.addWidget(self.progress)

        self.label_result = QLabel("")
        self.label_result.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.label_result, alignment=Qt.AlignCenter)

        self.label_suggestions = QLabel("")
        self.label_suggestions.setWordWrap(True)
        self.label_suggestions.setStyleSheet("font-size: 15px;")
        layout.addWidget(self.label_suggestions)

        # self.theme_button = QPushButton("Switch Light/Dark Mode")
        # self.theme_button.setCheckable(True)
        # self.theme_button.setStyleSheet("font-size: 14px; padding:5px; border-radius:6px;")
        # self.theme_button.clicked.connect(self.toggle_theme)
        # layout.addWidget(self.theme_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.apply_theme()

    def toggle_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            self.input_password.setEchoMode(QLineEdit.Normal)
            self.eye_action.setIcon(QIcon("eye-off.png"))
        else:
            self.input_password.setEchoMode(QLineEdit.Password)
            self.eye_action.setIcon(QIcon("eye.png"))

    def on_check(self):
        password = self.input_password.text()
        if not password:
            self.label_result.setText("⚠️ Please enter a password.")
            return

        strength, suggestions, score = check_strength(password)
        self.label_result.setText(f"Password Strength: {strength}")

        progress_value = score * 20
        self.animate_progress(progress_value)

        if strength == "Weak":
            color = "#e74c3c"
        elif strength == "Moderate":
            color = "#f39c12"
        else:
            color = "#27ae60"

        self.progress.setStyleSheet(
            f"""
            QProgressBar {{
                font-size: 16px;
                height: 25px;
                border-radius: 10px;
                background-color: rgba(0,0,0,0.1);
            }}
            QProgressBar::chunk {{
                border-radius: 10px;
                background-color: {color};
            }}
            """
        )

        if suggestions:
            self.label_suggestions.setText("Suggestions:\n- " + "\n- ".join(suggestions))
        else:
            self.label_suggestions.setText("✅ Great job! Your password looks strong.")

    def animate_progress(self, target):
        self.anim = QPropertyAnimation(self.progress, b"value")
        self.anim.setDuration(400)
        self.anim.setStartValue(self.progress.value())
        self.anim.setEndValue(target)
        self.anim.start()

    def toggle_theme(self):
        self.is_dark_mode = self.theme_button.isChecked()
        self.apply_theme()

    def apply_theme(self):
        palette = self.palette()
        if self.is_dark_mode:
            palette.setColor(QPalette.Window, QColor("#121212"))
            palette.setColor(QPalette.WindowText, QColor("#ffffff"))
            palette.setColor(QPalette.Base, QColor("#1e1e1e"))
            palette.setColor(QPalette.Text, QColor("#ffffff"))
            self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
            self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
            self.label_suggestions.setStyleSheet("font-size: 15px; color: white;")
        else:
            palette.setColor(QPalette.Window, QColor("#f0f0f0"))
            palette.setColor(QPalette.WindowText, QColor("#000000"))
            palette.setColor(QPalette.Base, QColor("#ffffff"))
            palette.setColor(QPalette.Text, QColor("#000000"))
            self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
            self.label_result.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
            self.label_suggestions.setStyleSheet("font-size: 15px; color: black;")
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec_())
