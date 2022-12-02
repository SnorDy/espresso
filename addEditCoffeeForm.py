from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 359)
        Form.setStyleSheet("background-color:rgb(60, 60, 60)")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(350, 20, 141, 31))
        self.btn.setStyleSheet("border:none;\n"
                               "background-color:rgb(78, 208, 255);\n"
                               "font: 12pt \"Yu Gothic UI Semilight\";")
        self.btn.setObjectName("btn")
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
        self.label_4.setGeometry(QtCore.QRect(10, 180, 131, 20))
        self.label_4.setStyleSheet("color:white;\n"
                                   "font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 131, 20))
        self.label_5.setStyleSheet("color:white;\n"
                                   "font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 151, 20))
        self.label_6.setStyleSheet("color:white;\n"
                                   "font: 12pt \"Yu Gothic UI Semilight\";")
        self.label_6.setObjectName("label_6")
        self.sort_title = QtWidgets.QLineEdit(self.centralwidget)
        self.sort_title.setGeometry(QtCore.QRect(160, 20, 181, 31))
        self.sort_title.setStyleSheet("background-color:white;\n"
                                      "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                      "border:none;")
        self.sort_title.setObjectName("sort_title")
        self.degree_of_roasting = QtWidgets.QLineEdit(self.centralwidget)
        self.degree_of_roasting.setGeometry(QtCore.QRect(160, 70, 331, 31))
        self.degree_of_roasting.setStyleSheet("background-color:white;\n"
                                              "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                              "border:none;")
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.ground_or_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.ground_or_grains.setGeometry(QtCore.QRect(160, 120, 331, 31))
        self.ground_or_grains.setStyleSheet("background-color:white;\n"
                                            "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                            "border:none;")
        self.ground_or_grains.setObjectName("ground_or_grains")
        self.flavor_description = QtWidgets.QLineEdit(self.centralwidget)
        self.flavor_description.setGeometry(QtCore.QRect(160, 170, 331, 31))
        self.flavor_description.setStyleSheet("background-color:white;\n"
                                              "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                              "border:none;")
        self.flavor_description.setObjectName("flavor_description")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(160, 220, 331, 31))
        self.price.setStyleSheet("background-color:white;\n"
                                 "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                 "border:none;")
        self.price.setObjectName("price")
        self.volume_of_packaging = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_of_packaging.setGeometry(QtCore.QRect(160, 270, 331, 31))
        self.volume_of_packaging.setStyleSheet("background-color:white;\n"
                                               "font: 12pt \"Yu Gothic UI Semilight\";\n"
                                               "border:none;")
        self.volume_of_packaging.setObjectName("volume_of_packaging")
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 21))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Редактирование записи"))
        self.btn.setText(_translate("Form", "Сохранить"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("Form", "Описание вукуса"))
        self.label_5.setText(_translate("Form", "Цена в руб."))
        self.label_6.setText(_translate("Form", "Объём упаковки (г)"))
