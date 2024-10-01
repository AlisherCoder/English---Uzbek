from PyQt5.QtWidgets import *
from add_win import AddWin
from showlist_win import Showlistwin
from search_win import Searchwin

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,450)

        self.v_main_lay = QVBoxLayout()

        self.show_btn = QPushButton("Barcha lug'atlarni ko'rish", clicked = self.Showlist)
        self.add_btn = QPushButton("Lug'at qo'shish", clicked = self.Add)
        self.search_btn = QPushButton("Lug'at qidirish", clicked = self.Search)
        self.exit_btn = QPushButton("Exit", clicked = exit)

        self.v_main_lay.addWidget(self.show_btn)
        self.v_main_lay.addWidget(self.add_btn)
        self.v_main_lay.addWidget(self.search_btn)
        self.v_main_lay.addWidget(self.exit_btn)

        self.setLayout(self.v_main_lay)

    def Showlist(self):
        self.hide()
        self.showlist = Showlistwin(self)
        self.showlist.show()

    def Add(self):
        self.hide()
        self.addwin = AddWin(self)
        self.addwin.show()

    def Search(self):
        self.hide()
        self.searchwin = Searchwin(self)
        self.searchwin.show()


if __name__ == "__main__":
    app = QApplication([])
    win = MyWin()
    win.show()
    app.exec_()