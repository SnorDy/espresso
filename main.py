import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from main_gui import Ui_MainWindow
from addEditCoffeeForm import Ui_Form


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.func)
        self.con = sqlite3.connect('data/coffee.sqlite3')
        self.cur = self.con.cursor()
        sorts = list(map(lambda x: x[0], self.cur.execute('SELECT sort_title FROM coffee').fetchall()))
        self.comboBox.addItems(sorts)
        self.comboBox.setEditable(True)
        self.add_btn.clicked.connect(self.add_func)
        self.change_btn.clicked.connect(self.change_func)

    def add_func(self):
        self.add_form = AddEditForm(0)
        self.add_form.show()

    def change_func(self):
        if self.comboBox.currentText() not in list(
                map(lambda x: x[0], self.cur.execute('SELECT sort_title FROM coffee').fetchall())):
            self.error.setText('Ошибка! Такого названия нет в списке!')
        else:
            self.add_form = AddEditForm(1)
            self.add_form.show()

    def func(self):
        if self.comboBox.currentText() not in list(
                map(lambda x: x[0], self.cur.execute('SELECT sort_title FROM coffee').fetchall())):
            self.error.setText('Ошибка! Такого названия нет в списке!')
        else:
            self.error.setText('')
            req = self.cur.execute(f'SELECT * FROM coffee WHERE sort_title="{self.comboBox.currentText()}"').fetchone()
            self.id.setText(str(req[0]))
            self.sort_title.setText(req[1])
            self.degree_of_roasting.setText(req[2])
            self.ground_or_grains.setText(req[3])
            self.flavor_description.setText(req[4])
            self.price.setText(str(req[5]))
            self.volume_of_packaging.setText(str(req[6]))


class AddEditForm(Ui_Form, QMainWindow):
    def __init__(self, f):
        super().__init__()
        self.f = f
        self.title = ''
        self.con = sqlite3.connect('data/coffee.sqlite3')
        self.cur = self.con.cursor()
        self.setupUi(self)
        if f:
            self.title = ex.comboBox.currentText()
            req = self.cur.execute(f'SELECT * FROM coffee WHERE sort_title="{self.title}"').fetchone()
            self.sort_title.setText(req[1])
            self.degree_of_roasting.setText(req[2])
            self.ground_or_grains.setText(req[3])
            self.flavor_description.setText(req[4])
            self.price.setText(str(req[5]))
            self.volume_of_packaging.setText(str(req[6]))
        self.btn.clicked.connect(self.save)

    def save(self):
        global ex
        ex.close()
        sort_title = self.sort_title.text()
        deg = self.degree_of_roasting.text()
        gog = self.ground_or_grains.text()
        desc = self.flavor_description.text()
        price = self.price.text()
        vop = self.volume_of_packaging.text()
        print(sort_title)
        if self.f:
            self.cur.execute(
                f'''UPDATE coffee SET sort_title="{sort_title}",degree_of_roasting="{deg}",
                ground_or_grains="{gog}",flavor_description="{desc}",price="{price}",
                volume_of_packaging="{vop}" WHERE sort_title="{self.title}"''')
        else:
            self.cur.execute(
                f'''INSERT INTO coffee(sort_title,degree_of_roasting,ground_or_grains,
                flavor_description,price,volume_of_packaging) VALUES("{sort_title}","{deg}","{gog}","{desc}","{price}","{vop}" )''')
        self.con.commit()
        self.close()
        ex = Example()
        ex.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec())
