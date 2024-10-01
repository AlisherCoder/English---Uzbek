from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from database import Mydb

class Searchwin(QWidget):
    def __init__(self, Mainwin):
        super().__init__()
        self.mydb = Mydb()
        self.mainwin = Mainwin
        self.setFixedSize(300,450)

        self.v_main_lay = QVBoxLayout()

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Kerakli so'zni kiriting.")
        self.search_edit.setFixedHeight(30)
        self.search_edit.returnPressed.connect(self.Search)

        self.h_labels_lay = QHBoxLayout()
        self.eng_label = QLabel("Eng")
        self.uzb_label = QLabel("Uzb")
        self.h_labels_lay.addWidget(self.eng_label)
        self.h_labels_lay.addStretch()
        self.h_labels_lay.addWidget(self.uzb_label)

        self.qlist = QListWidget()
        # self.qlist.setFixedHeight(150)

        self.search_btn = QPushButton("Qidirish", clicked = self.Search)
        self.back_btn = QPushButton("Orqaga", clicked = self.Back)

        self.v_main_lay.addWidget(self.search_edit)
        self.v_main_lay.addLayout(self.h_labels_lay)
        self.v_main_lay.addWidget(self.qlist)
        self.v_main_lay.addWidget(self.search_btn)
        self.v_main_lay.addWidget(self.back_btn)

        self.setLayout(self.v_main_lay)

    def Back(self):
        self.hide()
        self.mainwin.show()

    def Search(self):
        key = self.search_edit.text()
        if key:
            words = self.mydb.get_bysearch(key)
            if words:
                for i in words:
                    item = f"{i[0].title()} ------------ {i[1].title()}"
                    widitem = QListWidgetItem(item)
                    widitem.setTextAlignment(Qt.AlignCenter)
                    self.qlist.clear()
                    self.qlist.addItem(widitem)
                    self.search_edit.clear()
            else:
                QMessageBox.warning(self, "Xabar", "Bunday so'z topilmadi")
        else:
            QMessageBox.warning(self, "Xato", "Bo'sh joyni to'ldiring!")


if __name__ == "__main__":
    app = QApplication([])
    win = Searchwin()
    win.show()
    app.exec_()