# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui-py3qt5\src\ui\SWMM\frmEventsDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmEvents(object):
    def setupUi(self, frmEvents):
        frmEvents.setObjectName("frmEvents")
        frmEvents.resize(466, 352)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmEvents.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmEvents)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTop = QtWidgets.QLabel(self.centralWidget)
        self.lblTop.setObjectName("lblTop")
        self.verticalLayout.addWidget(self.lblTop)
        self.lblTop2 = QtWidgets.QLabel(self.centralWidget)
        self.lblTop2.setObjectName("lblTop2")
        self.verticalLayout.addWidget(self.lblTop2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(10)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gbxModify = QtWidgets.QGroupBox(self.centralWidget)
        self.gbxModify.setObjectName("gbxModify")
        self.gridLayout = QtWidgets.QGridLayout(self.gbxModify)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblStart_2 = QtWidgets.QLabel(self.gbxModify)
        self.lblStart_2.setMinimumSize(QtCore.QSize(70, 0))
        self.lblStart_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lblStart_2.setObjectName("lblStart_2")
        self.gridLayout.addWidget(self.lblStart_2, 1, 0, 1, 1)
        self.dedEnd = QtWidgets.QDateEdit(self.gbxModify)
        self.dedEnd.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dedEnd.setDate(QtCore.QDate(2002, 1, 1))
        self.dedEnd.setObjectName("dedEnd")
        self.gridLayout.addWidget(self.dedEnd, 0, 4, 1, 1)
        self.tmeEnd = QtWidgets.QTimeEdit(self.gbxModify)
        self.tmeEnd.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tmeEnd.setProperty("showGroupSeparator", False)
        self.tmeEnd.setObjectName("tmeEnd")
        self.gridLayout.addWidget(self.tmeEnd, 1, 4, 1, 1)
        self.lblStart_3 = QtWidgets.QLabel(self.gbxModify)
        self.lblStart_3.setMinimumSize(QtCore.QSize(70, 0))
        self.lblStart_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lblStart_3.setObjectName("lblStart_3")
        self.gridLayout.addWidget(self.lblStart_3, 0, 3, 1, 1)
        self.dedStart = QtWidgets.QDateEdit(self.gbxModify)
        self.dedStart.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dedStart.setDate(QtCore.QDate(2002, 1, 1))
        self.dedStart.setObjectName("dedStart")
        self.gridLayout.addWidget(self.dedStart, 0, 1, 1, 2)
        self.lblStart = QtWidgets.QLabel(self.gbxModify)
        self.lblStart.setMinimumSize(QtCore.QSize(70, 0))
        self.lblStart.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lblStart.setObjectName("lblStart")
        self.gridLayout.addWidget(self.lblStart, 0, 0, 1, 1)
        self.lblStart_4 = QtWidgets.QLabel(self.gbxModify)
        self.lblStart_4.setMinimumSize(QtCore.QSize(70, 0))
        self.lblStart_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lblStart_4.setObjectName("lblStart_4")
        self.gridLayout.addWidget(self.lblStart_4, 1, 3, 1, 1)
        self.tmeStart = QtWidgets.QTimeEdit(self.gbxModify)
        self.tmeStart.setMinimumSize(QtCore.QSize(50, 0))
        self.tmeStart.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tmeStart.setBaseSize(QtCore.QSize(0, 0))
        self.tmeStart.setProperty("showGroupSeparator", False)
        self.tmeStart.setObjectName("tmeStart")
        self.gridLayout.addWidget(self.tmeStart, 1, 1, 1, 2)
        self.btnAdd = QtWidgets.QPushButton(self.gbxModify)
        self.btnAdd.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 2, 1, 1, 1)
        self.btnReplace = QtWidgets.QPushButton(self.gbxModify)
        self.btnReplace.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnReplace.setObjectName("btnReplace")
        self.gridLayout.addWidget(self.btnReplace, 2, 2, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(self.gbxModify)
        self.btnDelete.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 2, 3, 1, 1)
        self.btnDeleteAll = QtWidgets.QPushButton(self.gbxModify)
        self.btnDeleteAll.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnDeleteAll.setObjectName("btnDeleteAll")
        self.gridLayout.addWidget(self.btnDeleteAll, 2, 4, 1, 1)
        self.verticalLayout.addWidget(self.gbxModify)
        self.fraButtons = QtWidgets.QFrame(self.centralWidget)
        self.fraButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraButtons.setObjectName("fraButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.fraButtons)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraButtons)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraButtons)
        frmEvents.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmEvents)
        QtCore.QMetaObject.connectSlotsByName(frmEvents)

    def retranslateUi(self, frmEvents):
        _translate = QtCore.QCoreApplication.translate
        frmEvents.setWindowTitle(_translate("frmEvents", "SWMM Events Editor"))
        self.lblTop.setText(_translate("frmEvents", "Use this form to restrict hydraulic analysis to particular time periods."))
        self.lblTop2.setText(_translate("frmEvents", "Hydraulics will remain constant outside of these periods."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmEvents", "Use"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmEvents", "Start Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("frmEvents", "Start Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("frmEvents", "End Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("frmEvents", "End Time"))
        self.gbxModify.setTitle(_translate("frmEvents", "Modify the Selected Event"))
        self.lblStart_2.setText(_translate("frmEvents", "Start Time"))
        self.dedEnd.setDisplayFormat(_translate("frmEvents", "MM/dd/yyyy"))
        self.tmeEnd.setDisplayFormat(_translate("frmEvents", "hh:mm"))
        self.lblStart_3.setText(_translate("frmEvents", "End Date"))
        self.dedStart.setDisplayFormat(_translate("frmEvents", "MM/dd/yyyy"))
        self.lblStart.setText(_translate("frmEvents", "Start Date"))
        self.lblStart_4.setText(_translate("frmEvents", "End Time"))
        self.tmeStart.setDisplayFormat(_translate("frmEvents", "hh:mm"))
        self.btnAdd.setText(_translate("frmEvents", "Add Event"))
        self.btnReplace.setText(_translate("frmEvents", "Replace Event"))
        self.btnDelete.setText(_translate("frmEvents", "Delete Event"))
        self.btnDeleteAll.setText(_translate("frmEvents", "Delete All"))
        self.cmdOK.setText(_translate("frmEvents", "OK"))
        self.cmdCancel.setText(_translate("frmEvents", "Cancel"))
