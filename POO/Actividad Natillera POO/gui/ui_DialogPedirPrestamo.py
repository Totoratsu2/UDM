# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogPedirPrestamoYvCoIG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogPedirPrestamo(object):
    def setupUi(self, DialogPedirPrestamo):
        if not DialogPedirPrestamo.objectName():
            DialogPedirPrestamo.setObjectName(u"DialogPedirPrestamo")
        DialogPedirPrestamo.resize(332, 69)
        self.verticalLayout = QVBoxLayout(DialogPedirPrestamo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogPedirPrestamo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_valor_prestamo = QLabel(self.frame)
        self.lbl_valor_prestamo.setObjectName(u"lbl_valor_prestamo")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_valor_prestamo)

        self.lnedit_prestamo = QLineEdit(self.frame)
        self.lnedit_prestamo.setObjectName(u"lnedit_prestamo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lnedit_prestamo)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogPedirPrestamo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogPedirPrestamo)
        self.buttonBox.accepted.connect(DialogPedirPrestamo.accept)
        self.buttonBox.rejected.connect(DialogPedirPrestamo.reject)

        QMetaObject.connectSlotsByName(DialogPedirPrestamo)
    # setupUi

    def retranslateUi(self, DialogPedirPrestamo):
        DialogPedirPrestamo.setWindowTitle(QCoreApplication.translate("DialogPedirPrestamo", u"Pedir prestamo", None))
        self.lbl_valor_prestamo.setText(QCoreApplication.translate("DialogPedirPrestamo", u"Valor prestamo", None))
        self.lnedit_prestamo.setPlaceholderText(QCoreApplication.translate("DialogPedirPrestamo", u"Obligatorio", None))
    # retranslateUi

