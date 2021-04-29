# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowPrBeEs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_banner = QLabel(self.centralwidget)
        self.label_banner.setObjectName(u"label_banner")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_banner.sizePolicy().hasHeightForWidth())
        self.label_banner.setSizePolicy(sizePolicy)
        self.label_banner.setMinimumSize(QSize(0, 151))
        self.label_banner.setPixmap(QPixmap(u":/imgs/img/banner.jpg"))

        self.verticalLayout.addWidget(self.label_banner)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.pbtn_liquidar_natillera = QPushButton(self.groupBox)
        self.pbtn_liquidar_natillera.setObjectName(u"pbtn_liquidar_natillera")

        self.verticalLayout_5.addWidget(self.pbtn_liquidar_natillera)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.pbtn_empezar_rifa = QPushButton(self.groupBox_4)
        self.pbtn_empezar_rifa.setObjectName(u"pbtn_empezar_rifa")

        self.verticalLayout_6.addWidget(self.pbtn_empezar_rifa)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.frame_2)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listview_socios = QListView(self.groupBox_2)
        self.listview_socios.setObjectName(u"listview_socios")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listview_socios.sizePolicy().hasHeightForWidth())
        self.listview_socios.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.listview_socios)

        self.pbtn_agregar_aporte = QPushButton(self.groupBox_2)
        self.pbtn_agregar_aporte.setObjectName(u"pbtn_agregar_aporte")

        self.verticalLayout_3.addWidget(self.pbtn_agregar_aporte)

        self.pbtn_agregar_socio = QPushButton(self.groupBox_2)
        self.pbtn_agregar_socio.setObjectName(u"pbtn_agregar_socio")

        self.verticalLayout_3.addWidget(self.pbtn_agregar_socio)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listview_prestamos = QListView(self.groupBox_3)
        self.listview_prestamos.setObjectName(u"listview_prestamos")

        self.verticalLayout_4.addWidget(self.listview_prestamos)

        self.pbtn_pagar_prestamo = QPushButton(self.groupBox_3)
        self.pbtn_pagar_prestamo.setObjectName(u"pbtn_pagar_prestamo")

        self.verticalLayout_4.addWidget(self.pbtn_pagar_prestamo)

        self.pbtn_pedir_prestamo = QPushButton(self.groupBox_3)
        self.pbtn_pedir_prestamo.setObjectName(u"pbtn_pedir_prestamo")

        self.verticalLayout_4.addWidget(self.pbtn_pedir_prestamo)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Natillera", None))
        self.label_banner.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Natillera", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pbtn_liquidar_natillera.setText(QCoreApplication.translate("MainWindow", u"Liquidar Natillera", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Rifas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pbtn_empezar_rifa.setText(QCoreApplication.translate("MainWindow", u"Realizar rifa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Socios", None))
        self.pbtn_agregar_aporte.setText(QCoreApplication.translate("MainWindow", u"Agregar aporte", None))
        self.pbtn_agregar_socio.setText(QCoreApplication.translate("MainWindow", u"Agregar Socio", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Prestamos", None))
        self.pbtn_pagar_prestamo.setText(QCoreApplication.translate("MainWindow", u"Pagar prestamo", None))
        self.pbtn_pedir_prestamo.setText(QCoreApplication.translate("MainWindow", u"Pedir prestamo", None))
    # retranslateUi

