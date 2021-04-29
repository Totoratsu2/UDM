# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogAgregarSocioCwvxNg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAgregarSocio(object):
    def setupUi(self, DialogAgregarSocio):
        if not DialogAgregarSocio.objectName():
            DialogAgregarSocio.setObjectName(u"DialogAgregarSocio")
        DialogAgregarSocio.resize(400, 121)
        self.verticalLayout = QVBoxLayout(DialogAgregarSocio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogAgregarSocio)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_nombre = QLabel(self.frame)
        self.lbl_nombre.setObjectName(u"lbl_nombre")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_nombre)

        self.lbl_telefono = QLabel(self.frame)
        self.lbl_telefono.setObjectName(u"lbl_telefono")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_telefono)

        self.lbl_cedula = QLabel(self.frame)
        self.lbl_cedula.setObjectName(u"lbl_cedula")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_cedula)

        self.lnedit_nombre = QLineEdit(self.frame)
        self.lnedit_nombre.setObjectName(u"lnedit_nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lnedit_nombre)

        self.lnedit_cedula = QLineEdit(self.frame)
        self.lnedit_cedula.setObjectName(u"lnedit_cedula")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lnedit_cedula)

        self.lnedit_telefono = QLineEdit(self.frame)
        self.lnedit_telefono.setObjectName(u"lnedit_telefono")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lnedit_telefono)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(DialogAgregarSocio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogAgregarSocio)
        self.buttonBox.accepted.connect(DialogAgregarSocio.accept)
        self.buttonBox.rejected.connect(DialogAgregarSocio.reject)

        QMetaObject.connectSlotsByName(DialogAgregarSocio)
    # setupUi

    def retranslateUi(self, DialogAgregarSocio):
        DialogAgregarSocio.setWindowTitle(QCoreApplication.translate("DialogAgregarSocio", u"Agregar Socio", None))
        self.lbl_nombre.setText(QCoreApplication.translate("DialogAgregarSocio", u"Nombre", None))
        self.lbl_telefono.setText(QCoreApplication.translate("DialogAgregarSocio", u"Telefono", None))
        self.lbl_cedula.setText(QCoreApplication.translate("DialogAgregarSocio", u"Cedula", None))
        self.lnedit_nombre.setPlaceholderText(QCoreApplication.translate("DialogAgregarSocio", u"Obligatorio", None))
        self.lnedit_cedula.setPlaceholderText(QCoreApplication.translate("DialogAgregarSocio", u"Obligatorio", None))
        self.lnedit_telefono.setPlaceholderText(QCoreApplication.translate("DialogAgregarSocio", u"Obligatorio", None))
    # retranslateUi

