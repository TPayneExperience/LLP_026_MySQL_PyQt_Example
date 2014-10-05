# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB_window.ui'
#
# Created: Sat Oct  4 20:21:38 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_TPayne_MySQL_Tool(object):
    def setupUi(self, TPayne_MySQL_Tool):
        TPayne_MySQL_Tool.setObjectName(_fromUtf8("TPayne_MySQL_Tool"))
        TPayne_MySQL_Tool.resize(457, 235)
        self.verticalLayout_2 = QtGui.QVBoxLayout(TPayne_MySQL_Tool)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(TPayne_MySQL_Tool)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(TPayne_MySQL_Tool)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.commitButton = QtGui.QPushButton(TPayne_MySQL_Tool)
        self.commitButton.setObjectName(_fromUtf8("commitButton"))
        self.horizontalLayout.addWidget(self.commitButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtGui.QTreeWidget(TPayne_MySQL_Tool)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TPayne_MySQL_Tool)
        QtCore.QMetaObject.connectSlotsByName(TPayne_MySQL_Tool)

    def retranslateUi(self, TPayne_MySQL_Tool):
        TPayne_MySQL_Tool.setWindowTitle(_translate("TPayne_MySQL_Tool", "TPayne\'s MySQL Message Storer", None))
        self.label.setText(_translate("TPayne_MySQL_Tool", "Super Fancy Title!", None))
        self.lineEdit.setText(_translate("TPayne_MySQL_Tool", "some text", None))
        self.commitButton.setText(_translate("TPayne_MySQL_Tool", "Commit!", None))
        self.treeWidget.headerItem().setText(0, _translate("TPayne_MySQL_Tool", "1", None))
        self.treeWidget.headerItem().setText(1, _translate("TPayne_MySQL_Tool", "New Column", None))
        self.treeWidget.headerItem().setText(2, _translate("TPayne_MySQL_Tool", "2", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("TPayne_MySQL_Tool", "test2", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("TPayne_MySQL_Tool", "test233", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("TPayne_MySQL_Tool", "asdf", None))
        self.treeWidget.topLevelItem(1).setText(2, _translate("TPayne_MySQL_Tool", "asdf", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

