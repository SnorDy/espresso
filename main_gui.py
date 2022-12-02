# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 443)
        MainWindow.setStyleSheet("background-color:rgb(60, 60, 60)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(360, 60, 151, 31))
        self.btn.setStyleSheet("border:none;\n"
"background-color:rgb(78, 208, 255);\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.btn.setObjectName("btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 20, 151, 31))
        self.comboBox.setStyleSheet("background-color:white;\n"
"border:none;\n"
"color:black;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.label.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 131, 20))
        self.label_2.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 141, 20))
        self.label_3.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 131, 20))
        self.label_4.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 131, 20))
        self.label_5.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 151, 20))
        self.label_6.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 340, 131, 20))
        self.label_7.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_7.setObjectName("label_7")
        self.sort_title = QtWidgets.QLineEdit(self.centralwidget)
        self.sort_title.setGeometry(QtCore.QRect(160, 20, 181, 31))
        self.sort_title.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.sort_title.setReadOnly(True)
        self.sort_title.setObjectName("sort_title")
        self.degree_of_roasting = QtWidgets.QLineEdit(self.centralwidget)
        self.degree_of_roasting.setGeometry(QtCore.QRect(160, 70, 181, 31))
        self.degree_of_roasting.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.degree_of_roasting.setReadOnly(True)
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.ground_or_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.ground_or_grains.setGeometry(QtCore.QRect(160, 120, 181, 31))
        self.ground_or_grains.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.ground_or_grains.setReadOnly(True)
        self.ground_or_grains.setObjectName("ground_or_grains")
        self.flavor_description = QtWidgets.QLineEdit(self.centralwidget)
        self.flavor_description.setGeometry(QtCore.QRect(160, 180, 331, 31))
        self.flavor_description.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.flavor_description.setReadOnly(True)
        self.flavor_description.setObjectName("flavor_description")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(160, 230, 331, 31))
        self.price.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.price.setReadOnly(True)
        self.price.setObjectName("price")
        self.volume_of_packaging = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_of_packaging.setGeometry(QtCore.QRect(160, 280, 331, 31))
        self.volume_of_packaging.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.volume_of_packaging.setReadOnly(True)
        self.volume_of_packaging.setObjectName("volume_of_packaging")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(160, 330, 331, 31))
        self.id.setStyleSheet("background-color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";\n"
"border:none;")
        self.id.setReadOnly(True)
        self.id.setObjectName("id")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(360, 100, 151, 31))
        self.add_btn.setStyleSheet("border:none;\n"
"background-color:rgb(78, 208, 255);\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.add_btn.setObjectName("add_btn")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(360, 140, 151, 31))
        self.change_btn.setStyleSheet("border:none;\n"
"background-color:rgb(78, 208, 255);\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.change_btn.setObjectName("change_btn")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(20, 380, 401, 21))
        self.error.setStyleSheet("color:white;\n"
"font: 12pt \"Yu Gothic UI Semilight\";")
        self.error.setText("")
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))
        self.btn.setText(_translate("MainWindow", "Запуск "))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("MainWindow", "Описание вукуса"))
        self.label_5.setText(_translate("MainWindow", "Цена в руб."))
        self.label_6.setText(_translate("MainWindow", "Объём упаковки (г)"))
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.add_btn.setText(_translate("MainWindow", "Добавить запись"))
        self.change_btn.setText(_translate("MainWindow", "Изменить запись"))
