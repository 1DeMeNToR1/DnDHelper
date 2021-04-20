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
        #self.characters_tab.setStyleSheet("background: url(1.jpg);")


        self.characters_tab.setTabsClosable(True)
        self.characters_tab.tabCloseRequested.connect(self.delete_person)

        self.add_character.triggered.connect(lambda: self.create_character())
        self.load_character.triggered.connect(lambda: self.load_file_character())
        self.save_character.triggered.connect(lambda: self.save_all())
        #self.add_character.triggered.connect(lambda: self.save_one())
        self.add_mag_lvl0.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl0", self.list_mag_lvl0))
        self.add_mag_lvl1.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl1", self.list_mag_lvl1))
        self.add_mag_lvl2.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl2", self.list_mag_lvl2))
        self.add_mag_lvl3.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl3", self.list_mag_lvl3))
        self.add_mag_lvl4.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl4", self.list_mag_lvl4))
        self.add_mag_lvl5.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl5", self.list_mag_lvl5))
        self.add_mag_lvl6.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl6", self.list_mag_lvl6))
        self.add_mag_lvl7.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl7", self.list_mag_lvl7))
        self.add_mag_lvl8.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl8", self.list_mag_lvl8))
        self.add_mag_lvl9.clicked.connect(lambda: self.add_in_mag_list("add_mag_lvl9", self.list_mag_lvl9))

        self.list_mag_lvl0.clicked.connect(lambda: self.mag_list_clicked(self.list_mag_lvl0))
        self.list_mag_lvl1.clicked.connect(lambda: self.mag_list_clicked(self.list_mag_lvl1))
        self.list_mag_lvl1.clicked.connect(lambda: self.mag_list_clicked(self.list_mag_lvl2))

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

        #fix this shit



    def load_file_character(self):
        file, __ = QFileDialog.getOpenFileName(self, 'Open file')
        print(file)
    def save_all(self):
        print("345")


    """
    def save_one(self):
        print("456")
    
    add this late 
    """

    def mag_list_clicked(self, mag_lvl_list):
        item = mag_lvl_list.currentItem()
        print(item.text())

    def add_in_mag_list(self, mag_lvl_butt, mag_lvl_list):
        mag_lvl_list.insertItem(0, mag_lvl_butt)

        """
        item = self.mag_lvl_list.item(2)
        item.setText(mag_lvl_butt)
        """


class Player():
    def __init__(self, name, strg, lovk, body, inta, mydr, charizma, classs, yroven, rasa, naviki_akrobatika, naviki_analiz, naviki_atletika, naviki_vnimatelnost,
                    naviki_vizivanie, naviki_vistyplenie, naviki_zapygivanie, naviki_history, naviki_lovk_ryk, naviki_magia, naviki_med, naviki_obman, naviki_priroda, naviki_pronicatelnost,
                    naviki_religia, naviki_skritnost, naviki_ybesjenie, naviki_yxod_za_jivotn, naviki_spas_bros_sila, naviki_spas_bros_lovk, naviki_spas_bros_body, naviki_spas_bros_int, naviki_spas_bros_mydr, naviki_spas_bros_charisma,
                    zagovori, zaklinanie_lvl1, zaklinanie_lvl2, zaklinanie_lvl3, zaklinanie_lvl4, zaklinanie_lvl5, zaklinanie_lvl6, zaklinanie_lvl7, zaklinanie_lvl8, zaklinanie_lvl9):

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

        self.naviki_spas_bros_sila = naviki_spas_bros_sila
        self.naviki_spas_bros_lovk = naviki_spas_bros_lovk
        self.naviki_spas_bros_body = naviki_spas_bros_body
        self.naviki_spas_bros_int = naviki_spas_bros_int
        self.naviki_spas_bros_mydr = naviki_spas_bros_mydr
        self.naviki_spas_bros_charisma = naviki_spas_bros_charisma

        self.zagovori = zagovori
        self.zaklinanie_lvl1 = zaklinanie_lvl1
        self.zaklinanie_lvl2 = zaklinanie_lvl2
        self.zaklinanie_lvl3 = zaklinanie_lvl3
        self.zaklinanie_lvl4 = zaklinanie_lvl4
        self.zaklinanie_lvl5 = zaklinanie_lvl5
        self.zaklinanie_lvl6 = zaklinanie_lvl6
        self.zaklinanie_lvl7 = zaklinanie_lvl7
        self.zaklinanie_lvl8 = zaklinanie_lvl8
        self.zaklinanie_lvl9 = zaklinanie_lvl9

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui1 = main_ui()
    ui1.show()
    sys.exit(app.exec_())