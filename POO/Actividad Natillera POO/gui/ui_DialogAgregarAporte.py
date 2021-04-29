# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogAgregarAporteCOorpc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAgregarAporte(object):
    def setupUi(self, DialogAgregarAporte):
        if not DialogAgregarAporte.objectName():
            DialogAgregarAporte.setObjectName(u"DialogAgregarAporte")
        DialogAgregarAporte.resize(329, 69)
        self.verticalLayout = QVBoxLayout(DialogAgregarAporte)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogAgregarAporte)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_aporte = QLabel(self.frame)
        self.lbl_aporte.setObjectName(u"lbl_aporte")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_aporte)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogAgregarAporte)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogAgregarAporte)
        self.buttonBox.accepted.connect(DialogAgregarAporte.accept)
        self.buttonBox.rejected.connect(DialogAgregarAporte.reject)

        QMetaObject.connectSlotsByName(DialogAgregarAporte)
    # setupUi

    def retranslateUi(self, DialogAgregarAporte):
        DialogAgregarAporte.setWindowTitle(QCoreApplication.translate("DialogAgregarAporte", u"Agregar aporte", None))
        self.lbl_aporte.setText(QCoreApplication.translate("DialogAgregarAporte", u"Valor aporte", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("DialogAgregarAporte", u"Obligatorio", None))
    # retranslateUi

