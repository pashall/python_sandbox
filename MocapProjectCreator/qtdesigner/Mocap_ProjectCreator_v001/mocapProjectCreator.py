
import sys
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

class Ui_MocapProjectCreator_form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    
    def setupUi(self, MocapProjectCreator_form):
        MocapProjectCreator_form.setObjectName(_fromUtf8("MocapProjectCreator_form"))
        MocapProjectCreator_form.resize(526, 473)
        self.gridLayout = QtGui.QGridLayout(MocapProjectCreator_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 22, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(MocapProjectCreator_form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 23, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(MocapProjectCreator_form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 23, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.label = QtGui.QLabel(MocapProjectCreator_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 16, 0, 1, 1)
        self.label_2 = QtGui.QLabel(MocapProjectCreator_form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 13, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(MocapProjectCreator_form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 15, 0, 1, 1)
        self.label_3 = QtGui.QLabel(MocapProjectCreator_form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 17, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(MocapProjectCreator_form)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 18, 0, 1, 1)
        self.projectname_line = QtGui.QLineEdit(MocapProjectCreator_form)
        self.projectname_line.setObjectName(_fromUtf8("projectname_line"))
        self.gridLayout.addWidget(self.projectname_line, 5, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 22, 0, 1, 1)
        self.label_4 = QtGui.QLabel(MocapProjectCreator_form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 20, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(MocapProjectCreator_form)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 21, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 19, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 15, 2, 1, 1)
        self.line = QtGui.QFrame(MocapProjectCreator_form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 9, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)

        self.retranslateUi(MocapProjectCreator_form)
        QtCore.QMetaObject.connectSlotsByName(MocapProjectCreator_form)

    def retranslateUi(self, MocapProjectCreator_form):
        MocapProjectCreator_form.setWindowTitle(_translate("MocapProjectCreator_form", "Mocap Project Creator 1.0", None))
        self.pushButton.setText(_translate("MocapProjectCreator_form", "Create", None))
        self.pushButton_2.setText(_translate("MocapProjectCreator_form", "Cancel", None))
        self.label.setText(_translate("MocapProjectCreator_form", "Project Name:", None))
        self.label_2.setText(_translate("MocapProjectCreator_form", "Performer 01 Name", None))
        self.label_3.setText(_translate("MocapProjectCreator_form", "Performer 02 Name", None))
        self.label_4.setText(_translate("MocapProjectCreator_form", "Performer 03 Name", None))
        
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MocapProjectCreator_form
    ex.show
    sys.exit(app.exec_())         

