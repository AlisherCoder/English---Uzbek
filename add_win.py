from PyQt5.QtWidgets import *
from database import Mydb

class AddWin(QWidget):
    def __init__(self, Mainwin):
        super().__init__()
        self.mainwin = Mainwin
        self.mydb = Mydb()

        self.setFixedSize(300,450)

        self.v_main_lay = QVBoxLayout()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("English")

        self.uzb_edit = QLineEdit()
        self.uzb_edit.setPlaceholderText("Uzbek")
        self.uzb_edit.returnPressed.connect(self.Add)

        self.add_btn = QPushButton("Qo'shish", clicked = self.Add)
        self.back_btn = QPushButton("Orqaga", clicked = self.Back)

        self.v_main_lay.addWidget(self.eng_edit)
        self.v_main_lay.addWidget(self.uzb_edit)
        self.v_main_lay.addWidget(self.add_btn)
        self.v_main_lay.addWidget(self.back_btn)

        self.setLayout(self.v_main_lay)

    def Add(self):
        eng = self.eng_edit.text()
        uzb = self.uzb_edit.text()
        if eng and uzb:
            dub = self.mydb.insert(eng, uzb)
            if dub:
                QMessageBox.warning(self, "Xato", "Bunday so'z mavjud")
            else:
                QMessageBox.warning(self, "Accept", "So'z qo'shildi")
            self.eng_edit.clear()
            self.uzb_edit.clear()
        else:
            QMessageBox.warning(self, "Xato", "Iltimos barcha joyni to'ldiring!")

    def Back(self):
        self.hide()
        self.mainwin.show()

if __name__ == "__main__":
    app = QApplication([])
    win = AddWin()
    win.show()
    app.exec_()