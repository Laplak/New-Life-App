# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowSample.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class WindowSample(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 500)
        self.mainButton = QtWidgets.QPushButton(Dialog)
        self.mainButton.setGeometry(QtCore.QRect(-2, 440, 105, 60))
        self.mainButton.setObjectName("mainButton")
        self.sourceOfIncomeButton = QtWidgets.QPushButton(Dialog)
        self.sourceOfIncomeButton.setGeometry(QtCore.QRect(98, 440, 105, 60))
        self.sourceOfIncomeButton.setObjectName("sourceOfIncomeButton")
        self.developmentButton = QtWidgets.QPushButton(Dialog)
        self.developmentButton.setGeometry(QtCore.QRect(198, 440, 105, 60))
        self.developmentButton.setObjectName("developmentButton")
        self.userLabel = QtWidgets.QLabel(Dialog)
        self.userLabel.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.userLabel.setObjectName("userLabel")
        self.moneyLabel = QtWidgets.QLabel(Dialog)
        self.moneyLabel.setGeometry(QtCore.QRect(172, 30, 120, 16))
        self.moneyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.moneyLabel.setObjectName("moneyLabel")
        self.healthLabel = QtWidgets.QLabel(Dialog)
        self.healthLabel.setGeometry(QtCore.QRect(180, 10, 112, 16))
        self.healthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.healthLabel.setObjectName("healthLabel")
        self.pictureLabel = QtWidgets.QLabel(Dialog)
        self.pictureLabel.setGeometry(QtCore.QRect(52, 90, 191, 171))
        font = QtGui.QFont()
        font.setPointSize(100)
        self.pictureLabel.setFont(font)
        self.pictureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pictureLabel.setObjectName("pictureLabel")
        self.energyLabel = QtWidgets.QLabel(Dialog)
        self.energyLabel.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.energyLabel.setObjectName("energyLabel")
        self.warningLabel = QtWidgets.QLabel(Dialog)
        self.warningLabel.setGeometry(QtCore.QRect(10, 60, 281, 16))
        self.warningLabel.setText("")
        self.warningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warningLabel.setObjectName("label_2")
        self.pictureLabel.raise_()
        self.mainButton.raise_()
        self.sourceOfIncomeButton.raise_()
        self.developmentButton.raise_()
        self.userLabel.raise_()
        self.moneyLabel.raise_()
        self.healthLabel.raise_()
        self.energyLabel.raise_()
        self.warningLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mainButton.setText(_translate("Dialog", "Главная"))
        self.sourceOfIncomeButton.setText(_translate("Dialog", "Источник\n"
                                                     "дохода"))
        self.developmentButton.setText(_translate("Dialog", "Развитие"))
        self.userLabel.setText(_translate("Dialog", "Олег, 34 года"))
        self.moneyLabel.setText(_translate("Dialog", "0$"))
        self.healthLabel.setText(_translate("Dialog", "Здоровье: 100"))
        self.pictureLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀯛</span></p></body></html>"))
        self.energyLabel.setText(_translate("Dialog", "<html><head/><body><p>Энергия: 20<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>"))
