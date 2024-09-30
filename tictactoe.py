import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.current_player = "X"  # Inicia com o jogador X
        self.board = [""] * 9  # Representa o estado do tabuleiro

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(129, 130, 411, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # Criar botões do jogo
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
                button.setText("")
                button.setObjectName(f"pushButton_{i * 3 + j + 1}")
                button.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.gridLayout.addWidget(button, i, j, 1, 1)
                row.append(button)
            self.buttons.append(row)
        
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 70, 91, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("JOGO DA VELHA")
        
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(640, 490, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setText("REINICIAR")
        self.pushButton_10.clicked.connect(self.reset_game)  # Conectar botão reiniciar
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo da Velha"))

    def make_move(self, x, y):
        if not self.board[x * 3 + y] and self.current_player:  # Verifica se a célula está vazia
            self.board[x * 3 + y] = self.current_player
            self.buttons[x][y].setText(self.current_player)
            if self.check_winner():
                self.lineEdit.setText(f"{self.current_player} ganhou!")
                self.current_player = None  # Desabilita mais movimentos
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for row in self.buttons:
            for button in row:
                button.setText("")
        self.lineEdit.setText("JOGO DA VELHA")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)              # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
