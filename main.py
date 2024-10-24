import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.orderButton.clicked.connect(self.kalkulator)
        self.show()
    def kalkulator(self):
        rozmiar = ""
        dodatki = ""
        if self.ui.smallPizza.isChecked() or self.ui.normalPizza.isChecked() or self.ui.bigPizza.isChecked():
        rozmiar = "wybiesz rozmiar pizzy"
        if self.ui.smallPizza.isChecked():
            rozmiar = "small pizza"
        if self.ui.bigPizza.isChecked():
            rozmiar = "big pizza"
        if self.ui.normalPizza.isChecked():
            rozmiar = "normall pizza"
        if self.ui.mushroomBox.isChecked():
            dodatki += " pieczarki"
        if self.ui.salamiBox.isChecked():
            dodatki += " salami"
        if self.ui.cheeseBox.isChecked():
            dodatki += " podwójny ser"
        if self.ui.pineapleBox.isChecked():
            dodatki += " pajnaple"
        if self.ui.mushroomBox.isChecked() or self.ui.salamiBox.isChecked() or self.ui.pineapleBox.isChecked():
         self.ui.resultLabel.setText(f'rozmiar pizzy to: {rozmiar} z dodatkami{dodatki}')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    sys.exit(app.exec())



