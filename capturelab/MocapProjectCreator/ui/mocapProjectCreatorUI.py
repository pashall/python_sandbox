# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mocapProjectCreator.ui'
#
# Created: Fri Mar 20 15:25:18 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mocapProjectCreator(object):
    def setupUi(self, mocapProjectCreator):
        mocapProjectCreator.setObjectName(_fromUtf8("mocapProjectCreator"))
        mocapProjectCreator.resize(501, 500)
        self.gridLayout_2 = QtGui.QGridLayout(mocapProjectCreator)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.create_btn = QtGui.QPushButton(mocapProjectCreator)
        self.create_btn.setObjectName(_fromUtf8("create_btn"))
        self.horizontalLayout_6.addWidget(self.create_btn)
        self.cancel_btn = QtGui.QPushButton(mocapProjectCreator)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_6.addWidget(self.cancel_btn)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.projectName_label = QtGui.QLabel(mocapProjectCreator)
        self.projectName_label.setObjectName(_fromUtf8("projectName_label"))
        self.horizontalLayout.addWidget(self.projectName_label)
        self.projectName_lineEdit = QtGui.QLineEdit(mocapProjectCreator)
        self.projectName_lineEdit.setObjectName(_fromUtf8("projectName_lineEdit"))
        self.horizontalLayout.addWidget(self.projectName_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.line_2 = QtGui.QFrame(mocapProjectCreator)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.mocap_radBtn = QtGui.QRadioButton(mocapProjectCreator)
        self.mocap_radBtn.setObjectName(_fromUtf8("mocap_radBtn"))
        self.horizontalLayout_7.addWidget(self.mocap_radBtn)
        self.vcam_radBtn = QtGui.QRadioButton(mocapProjectCreator)
        self.vcam_radBtn.setObjectName(_fromUtf8("vcam_radBtn"))
        self.horizontalLayout_7.addWidget(self.vcam_radBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line = QtGui.QFrame(mocapProjectCreator)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.performer01_label = QtGui.QLabel(mocapProjectCreator)
        self.performer01_label.setObjectName(_fromUtf8("performer01_label"))
        self.horizontalLayout_2.addWidget(self.performer01_label)
        self.performer01_lineEdit = QtGui.QLineEdit(mocapProjectCreator)
        self.performer01_lineEdit.setObjectName(_fromUtf8("performer01_lineEdit"))
        self.horizontalLayout_2.addWidget(self.performer01_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.performer02_label = QtGui.QLabel(mocapProjectCreator)
        self.performer02_label.setObjectName(_fromUtf8("performer02_label"))
        self.horizontalLayout_3.addWidget(self.performer02_label)
        self.performer02_lineEdit = QtGui.QLineEdit(mocapProjectCreator)
        self.performer02_lineEdit.setObjectName(_fromUtf8("performer02_lineEdit"))
        self.horizontalLayout_3.addWidget(self.performer02_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.performer03_label = QtGui.QLabel(mocapProjectCreator)
        self.performer03_label.setObjectName(_fromUtf8("performer03_label"))
        self.horizontalLayout_4.addWidget(self.performer03_label)
        self.performer03_lineEdit = QtGui.QLineEdit(mocapProjectCreator)
        self.performer03_lineEdit.setObjectName(_fromUtf8("performer03_lineEdit"))
        self.horizontalLayout_4.addWidget(self.performer03_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.performer04_label = QtGui.QLabel(mocapProjectCreator)
        self.performer04_label.setObjectName(_fromUtf8("performer04_label"))
        self.horizontalLayout_5.addWidget(self.performer04_label)
        self.performer04_lineEdit = QtGui.QLineEdit(mocapProjectCreator)
        self.performer04_lineEdit.setObjectName(_fromUtf8("performer04_lineEdit"))
        self.horizontalLayout_5.addWidget(self.performer04_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(mocapProjectCreator)
        QtCore.QMetaObject.connectSlotsByName(mocapProjectCreator)

    def retranslateUi(self, mocapProjectCreator):
        mocapProjectCreator.setWindowTitle(_translate("mocapProjectCreator", "Dialog", None))
        self.create_btn.setText(_translate("mocapProjectCreator", "Create Project", None))
        self.cancel_btn.setText(_translate("mocapProjectCreator", "Cancel", None))
        self.projectName_label.setText(_translate("mocapProjectCreator", "Project Name:", None))
        self.mocap_radBtn.setText(_translate("mocapProjectCreator", "Mocap", None))
        self.vcam_radBtn.setText(_translate("mocapProjectCreator", "VCam", None))
        self.performer01_label.setText(_translate("mocapProjectCreator", "Performer 01 Name:", None))
        self.performer02_label.setText(_translate("mocapProjectCreator", "Performer 02 Name:", None))
        self.performer03_label.setText(_translate("mocapProjectCreator", "Performer 03 Name:", None))
        self.performer04_label.setText(_translate("mocapProjectCreator", "Performer 04 Name:", None))

