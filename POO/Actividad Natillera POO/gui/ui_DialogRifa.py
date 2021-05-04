# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogRifabLWyOv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogRifa(object):
    def setupUi(self, DialogRifa):
        if not DialogRifa.objectName():
            DialogRifa.setObjectName(u"DialogRifa")
        DialogRifa.resize(400, 100)
        self.verticalLayout = QVBoxLayout(DialogRifa)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogRifa)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_boleto_ganador = QLabel(self.frame)
        self.lbl_boleto_ganador.setObjectName(u"lbl_boleto_ganador")

        self.verticalLayout_2.addWidget(self.lbl_boleto_ganador)

        self.lbl_socio_ganador = QLabel(self.frame)
        self.lbl_socio_ganador.setObjectName(u"lbl_socio_ganador")

        self.verticalLayout_2.addWidget(self.lbl_socio_ganador)

        self.lbl_valor_rifa = QLabel(self.frame)
        self.lbl_valor_rifa.setObjectName(u"lbl_valor_rifa")

        self.verticalLayout_2.addWidget(self.lbl_valor_rifa)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogRifa)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogRifa)
        self.buttonBox.accepted.connect(DialogRifa.accept)
        self.buttonBox.rejected.connect(DialogRifa.reject)

        QMetaObject.connectSlotsByName(DialogRifa)
    # setupUi

    def retranslateUi(self, DialogRifa):
        DialogRifa.setWindowTitle(QCoreApplication.translate("DialogRifa", u"Rifa", None))
        self.lbl_boleto_ganador.setText(QCoreApplication.translate("DialogRifa", u"Boleto ganador:", None))
        self.lbl_socio_ganador.setText(QCoreApplication.translate("DialogRifa", u"Socio ganador:", None))
        self.lbl_valor_rifa.setText(QCoreApplication.translate("DialogRifa", u"Valor del premio:", None))
    # retranslateUi

