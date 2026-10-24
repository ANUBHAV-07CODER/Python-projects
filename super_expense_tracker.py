
import sys
from PyQt5.QtWidgets import (
            QApplication,
            QWidget,
            QLabel,
            QLineEdit,
            QPushButton,
            QVBoxLayout,
            QComboBox
)


class ExpenseTracker(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expense Tracker")
        self.setFixedSize(350, 400)

        self.total_expense = 0.0

        self.title = QLabel("Personal Expense Tracker")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount (₹)")

        self.category_input = QComboBox()
        self.category_input.addItems([
            "Food",
            "Travel",
            "Shopping",
            "Education",
            "Other"
        ])

        self.add_button = QPushButton("Add Expense")
        self.add_button.clicked.connect(self.add_expense)

        self.total_label = QLabel("Total Expenses: ₹0.00")
        self.message_label = QLabel("Enter your first expense")

        self.expense_list = QLabel("Your expenses will appear here")

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.category_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.total_label)
        layout.addWidget(self.message_label)
        layout.addWidget(self.expense_list)
        self.setLayout(layout)

    def add_expense(self):

        try:
            amount = float(self.amount_input.text())

            if amount <= 0:
                self.message_label.setText(
                    "Amount must be greater than zero."
                )
                return

            category = self.category_input.currentText()

            self.total_expense += amount

            self.total_label.setText(
                f"Total Expenses: ₹{self.total_expense:.2f}"
            )

            old_text = self.expense_list.text()

            if old_text == "Your expenses will appear here":
                old_text = ""

            self.expense_list.setText(
                old_text
                + f"\n{category}: ₹{amount:.2f}"
            )

            self.message_label.setText("Expense added!")

            self.amount_input.clear()

        except ValueError:
            self.message_label.setText(
                "Please enter a valid number."
            )

app = QApplication(sys.argv)
window = ExpenseTracker()
window.show()

sys.exit(app.exec_())
