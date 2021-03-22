import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

Form, _ = uic.loadUiType('ui.ui')

id_name = []

class main_ui(QMainWindow, Form):
    def __init__(self):
        super(main_ui, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.characters_tab.setTabsClosable(True)
        self.characters_tab.tabCloseRequested.connect(self.delete_person)

        self.add_character.triggered.connect(lambda: self.create_character())
        self.load_character.triggered.connect(lambda: self.load_file_character())
        self.save_character.triggered.connect(lambda: self.save_all())
        #self.add_character.triggered.connect(lambda: self.save_one())

    @QtCore.pyqtSlot(int)
    def delete_person(self, tab_index):
        name_of_del_tab = self.characters_tab.tabText(tab_index)
        currentQWidget = self.characters_tab.widget(tab_index)
        currentQWidget.deleteLater()
        self.characters_tab.removeTab(tab_index)
        id_name.remove(name_of_del_tab)


    def create_character(self):
        text, ok = QInputDialog.getText(self, 'Создание персонажа', 'Введите имя героя:')
        self.text = QtWidgets.QWidget()
        self.text.setObjectName(text)
        id_name.append(text)


        self.characters_tab.addTab(self.text, text)

        name_of_labl = str(text) + "label"
        self.name_of_labl = QtWidgets.QLabel(self.text)
        self.name_of_labl.setGeometry(QtCore.QRect(370, 300, 171, 41))
        self.name_of_labl.setObjectName(name_of_labl)

        name_of_but = str(text) + "pushButton"
        name_of_but1 = str(text) + "pushButton"
        self.name_of_but = QtWidgets.QPushButton(self.text)
        self.name_of_but.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.name_of_but.setObjectName(name_of_but1)
        self.name_of_but.triggered.connect(lambda: print("1"))
        #fix this shit



    def load_file_character(self):
        file, __ = QFileDialog.getOpenFileName(self, 'Open file')
        print(file)
    def save_all(self):
        print("345")
    def save_one(self):
        print("456")



class Player():
    def __init__(self, name, strg, lovk, body, inta, mydr, charizma, classs, yroven, rasa, naviki_akrobatika, naviki_analiz, naviki_atletika, naviki_vnimatelnost,
                    naviki_vizivanie, naviki_vistyplenie, naviki_zapygivanie, naviki_history, naviki_lovk_ryk, naviki_magia, naviki_med, naviki_obman, naviki_priroda, naviki_pronicatelnost,
                    naviki_religia, naviki_skritnost, naviki_ybesjenie, naviki_yxod_za_jivotn, invent, url, invent2, url1, invent3, url3, naviki_spas_bros_sila, naviki_spas_bros_lovk, naviki_spas_bros_body, naviki_spas_bros_int, naviki_spas_bros_mydr, naviki_spas_bros_charisma):
        self.name = name
        self.strg = strg
        self.lovk = lovk
        self.body = body
        self.inta = inta
        self.mydr = mydr
        self.charizma = charizma
        self.classs = classs
        self.yroven = yroven
        self.rasa = rasa
        self.inventar = []

        self.naviki_akrobatika = naviki_akrobatika
        self.naviki_analiz = naviki_analiz
        self.naviki_atletika = naviki_atletika
        self.naviki_vnimatelnost = naviki_vnimatelnost
        self.naviki_vizivanie = naviki_vizivanie
        self.naviki_vistyplenie = naviki_vistyplenie
        self.naviki_zapygivanie = naviki_zapygivanie
        self.naviki_history = naviki_history
        self.naviki_lovk_ryk = naviki_lovk_ryk
        self.naviki_magia = naviki_magia
        self.naviki_med = naviki_med
        self.naviki_obman = naviki_obman
        self.naviki_priroda = naviki_priroda
        self.naviki_pronicatelnost = naviki_pronicatelnost
        self.naviki_religia = naviki_religia
        self.naviki_skritnost = naviki_skritnost
        self.naviki_ybesjenie = naviki_ybesjenie
        self.naviki_yxod_za_jivotn = naviki_yxod_za_jivotn
        self.invent = invent
        self.url = url
        self.invent2 = invent2
        self.url1 = url1
        self.invent3 = invent3
        self.url3 = url3

        self.naviki_spas_bros_sila = naviki_spas_bros_sila
        self.naviki_spas_bros_lovk = naviki_spas_bros_lovk
        self.naviki_spas_bros_body = naviki_spas_bros_body
        self.naviki_spas_bros_int = naviki_spas_bros_int
        self.naviki_spas_bros_mydr = naviki_spas_bros_mydr
        self.naviki_spas_bros_charisma = naviki_spas_bros_charisma


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui1 = main_ui()
    ui1.show()
    sys.exit(app.exec_())