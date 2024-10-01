from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from database import Mydb

class Showlistwin(QWidget):
    def __init__(self, Mainwin):
        super().__init__()
        self.mainwin = Mainwin
        self.mydb = Mydb()
        self.setFixedSize(300,450)

        self.v_main_lay = QVBoxLayout()
        self.h_labels_lay = QHBoxLayout()

        self.eng_label = QLabel("English")
        self.uzb_label = QLabel("Uzbek")

        self.h_labels_lay.addWidget(self.eng_label)
        self.h_labels_lay.addStretch()
        self.h_labels_lay.addWidget(self.uzb_label)

        self.qlist = QListWidget()

        self.back_btn = QPushButton("Orqaga", clicked = self.Back)

        self.v_main_lay.addLayout(self.h_labels_lay)
        self.v_main_lay.addWidget(self.qlist)
        self.v_main_lay.addWidget(self.back_btn)

        self.setLayout(self.v_main_lay)

        self.ShowWords()
    
    def ShowWords(self):
        words = self.mydb.get_words()
        if words:
            for i in words:
                item = f"{i[0].title()} ------------ {i[1].title()}"
                widitem = QListWidgetItem(item)
                widitem.setTextAlignment(Qt.AlignCenter)
                self.qlist.addItem(widitem)
        else:
            QMessageBox.warning(self, "Bo'sh", "Ro'yxat bo'sh")

    def Back(self):
        self.hide()
        self.mainwin.show()

if __name__ == "__main__":
    app = QApplication([])
    win = Showlistwin()
    win.show()
    app.exec_()