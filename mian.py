import sys
from PyQt6 import QtWidgets
from tictactoe_ui import Ui_MainWindow  # Importa a classe da interface

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
