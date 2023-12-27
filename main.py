import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from controller import Start

def main():
    app = QApplication(sys.argv)
    start = Start()
    widget = QStackedWidget()
    widget.addWidget(start)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("Exiting", e)

if __name__ == "__main__":
    main()
