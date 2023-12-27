from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QStackedWidget, QApplication, QWidget


class Start(QDialog):
    def __init__(self):
        super(Start, self).__init__()
        uic.loadUi("startview.ui", self)

        self.loginButton = self.findChild(QtWidgets.QPushButton, 'login')  # Znajdź przycisk 'login'
        self.signinButton = self.findChild(QtWidgets.QPushButton, 'signin')  # Znajdź przycisk 'signin'

        self.loginButton.clicked.connect(self.gotologin)
        self.signinButton.clicked.connect(self.gotosignin)
        #
        #
        # self.stack =QStackedWidget()
        # self.layout().addWidget(self.stack)


    def gotologin(self):
        login = Login()

        self.stack.addWidget(login)
        self.stack.setCurrentWidget(login)
        #widget = QStackedWidget()
        #widget.addWidget(login)
        #widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignin(self):
        signin = Signin()

        self.stack.addWidget(signin)
        self.stack.setCurrentWidget(signin)
        #widget = QStackedWidget()
        #widget.addWidget(signin)
        #widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("loginview.ui", self)


class Signin(QDialog):
    def __init__(self):
        super(Signin, self).__init__()
        uic.loadUi("signinview.ui", self)


app = QApplication([])
start = Start()
start.show()
app.exec_()