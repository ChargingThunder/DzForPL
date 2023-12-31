from PyQt6 import QtCore, QtGui, QtWidgets

centralwidget = QtWidgets.QWidget()
centralwidget.setObjectName("centralwidget")
label = QtWidgets.QLabel(parent=centralwidget)
label.setGeometry(QtCore.QRect(300, 90, 141, 71))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(16)
font.setBold(True)
font.setWeight(75)
label.setFont(font)
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setObjectName("label")
label_2 = QtWidgets.QLabel(parent=centralwidget)
label_2.setGeometry(QtCore.QRect(30, 220, 161, 21))
font = QtGui.QFont()
font.setPointSize(12)
label_2.setFont(font)
label_2.setObjectName("label_2")
label_3 = QtWidgets.QLabel(parent=centralwidget)
label_3.setGeometry(QtCore.QRect(250, 320, 181, 16))
font = QtGui.QFont()
font.setPointSize(12)
label_3.setFont(font)
label_3.setObjectName("label_3")
label_4 = QtWidgets.QLabel(parent=centralwidget)
label_4.setGeometry(QtCore.QRect(430, 220, 161, 16))
font = QtGui.QFont()
font.setPointSize(12)
label_4.setFont(font)
label_4.setObjectName("label_4")
lineEdit = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit.setGeometry(QtCore.QRect(190, 220, 121, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(12)
lineEdit.setFont(font)
lineEdit.setObjectName("lineEdit")
lineEdit_2 = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit_2.setGeometry(QtCore.QRect(590, 220, 121, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(12)
lineEdit_2.setFont(font)
lineEdit_2.setObjectName("lineEdit_2")
lineEdit_3 = QtWidgets.QLineEdit(parent=centralwidget)
lineEdit_3.setGeometry(QtCore.QRect(410, 320, 121, 21))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(12)
lineEdit_3.setFont(font)
lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
lineEdit_3.setObjectName("lineEdit_3")
pushButton = QtWidgets.QPushButton(parent=centralwidget)
pushButton.setGeometry(QtCore.QRect(310, 390, 121, 41))
font = QtGui.QFont()
font.setFamily("Times New Roman")
font.setPointSize(14)
pushButton.setFont(font)
pushButton.setObjectName("pushButton")

label.setText("Угадай число")
label_2.setText("Минимальное число:")
label_3.setText("Количество попыток:")
label_4.setText("Максимальное число:")
lineEdit.setText("1")
lineEdit_2.setText("100")
lineEdit_3.setText("10")
pushButton.setText("Начать")