# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renameTool.ui'
#
# Created: Fri May 01 12:27:50 2015
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

class Ui_m_renameTool(object):
    def setupUi(self, m_renameTool):
        m_renameTool.setObjectName(_fromUtf8("m_renameTool"))
        m_renameTool.resize(895, 524)
        self.centralwidget = QtGui.QWidget(m_renameTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nodeName_txt = QtGui.QLineEdit(self.centralwidget)
        self.nodeName_txt.setObjectName(_fromUtf8("nodeName_txt"))
        self.horizontalLayout.addWidget(self.nodeName_txt)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(_fromUtf8("clear_btn"))
        self.horizontalLayout.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.rename_btn = QtGui.QPushButton(self.centralwidget)
        self.rename_btn.setObjectName(_fromUtf8("rename_btn"))
        self.verticalLayout.addWidget(self.rename_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        m_renameTool.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(m_renameTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        m_renameTool.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(m_renameTool)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        m_renameTool.setStatusBar(self.statusbar)

        self.retranslateUi(m_renameTool)
        QtCore.QMetaObject.connectSlotsByName(m_renameTool)

    def retranslateUi(self, m_renameTool):
        m_renameTool.setWindowTitle(_translate("m_renameTool", "Rename Tool", None))
        self.clear_btn.setText(_translate("m_renameTool", "Clear", None))
        self.rename_btn.setText(_translate("m_renameTool", "Rename selected node", None))

