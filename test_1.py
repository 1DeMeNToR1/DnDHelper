import sys
from PyQt5.QtWidgets import (QWidget, QListWidget, QVBoxLayout, QApplication)

LISTS = ("item1", "item2", "item3", "item4", "item5",)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.l = QListWidget()
        self.l.addItems(LISTS)

        self.l.itemClicked.connect(self.selectionChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.l)
        self.setLayout(vbox)
        #btn1.clicked.connect(self.buttonClicked)

    def selectionChanged(self, item):
        print("Вы кликнули: {}".format(item.text()))
        if item.text()=="item2": print("Делайте что-нибудь.")
        # ...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())