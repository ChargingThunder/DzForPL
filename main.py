from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys, random

stacked = 0
mini = 1
maxi = 100
attempts = 10
answer = 0

def main():
    app = QApplication(sys.argv)
    import proga, proga2

    global stacked
    win = QMainWindow()
    stacked = QStackedWidget()
    stacked.addWidget(proga.centralwidget)
    stacked.addWidget(proga2.centralwidget)
    stacked.setCurrentWidget(proga.centralwidget)
    win.resize(800,600)
    win.setCentralWidget(stacked)

    proga.pushButton.clicked.connect(win2)
    proga2.pushButton_2.clicked.connect(win1)
    proga2.pushButton_3.clicked.connect(app.quit)
    proga2.pushButton.clicked.connect(guess)

    win.show()
    sys.exit(app.exec())

def win2():
    import proga, proga2
    global stacked, mini, maxi, answer, attempts
    mini = int(proga.lineEdit.text())
    maxi = int(proga.lineEdit_2.text())
    attempts = int(proga.lineEdit_3.text())
    stacked.setCurrentWidget(proga2.centralwidget)
    proga2.label_2.setText("Осталось попыток: " + str(attempts))
    proga2.lineEdit.setText("")
    answer = random.randint(mini, maxi)
    proga2.pushButton.setDisabled(False)

def win1():
    import proga, proga2
    global stacked
    stacked.setCurrentWidget(proga.centralwidget)

def guess():
    import proga2
    global attempts
    user_attempt = int(proga2.lineEdit.text())
    if user_attempt<answer:
        attempts-=1
        proga2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ больше.")
        proga2.lineEdit.setText("")
    if user_attempt>answer:
        attempts-=1
        proga2.label_2.setText(f"Осталось попыток: {str(attempts)}. Правильный ответ меньше.")
    if attempts == 0 and user_attempt != answer:
        proga2.label_2.setText(f"Правильный ответ был {str(answer)}.")
        proga2.pushButton.setDisabled(True)
    if user_attempt == answer:
        proga2.label_2.setText("Вы Угадали!")

if __name__ == "__main__":
    main()

