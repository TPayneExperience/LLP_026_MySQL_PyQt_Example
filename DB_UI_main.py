#!/usr/bin/python

from PyQt4 import QtCore, QtGui
import DB_manager, sys

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

class Ui_TPayne_MySQL_Tool(QtGui.QWidget):
    def __init__(self, database, tableName):
        QtGui.QWidget.__init__(self)
        self.dbu = DB_manager.DatabaseUtility(database, tableName)
        self.setupUi(self)
        self.UpdateTree()

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
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TPayne_MySQL_Tool)
        QtCore.QMetaObject.connectSlotsByName(TPayne_MySQL_Tool)

    def retranslateUi(self, TPayne_MySQL_Tool):
        TPayne_MySQL_Tool.setWindowTitle(_translate("TPayne_MySQL_Tool", "TPayne\'s MySQL Message Storer", None))
        self.label.setText(_translate("TPayne_MySQL_Tool", "Super Fancy Title!", None))
        self.commitButton.setText(_translate("TPayne_MySQL_Tool", "Commit!", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    @QtCore.pyqtSignature("on_commitButton_clicked()")
    def Commit(self):
        text = self.lineEdit.text()
        self.dbu.AddEntryToTable(text)
        self.UpdateTree()

    def UpdateTree(self):
        col = self.dbu.GetColumns()
        table = self.dbu.GetTable()
        
        for c in range(len(col)):
            self.treeWidget.headerItem().setText(c, col[c][0])
        
        self.treeWidget.clear()
        
        for item in range(len(table)):
            QtGui.QTreeWidgetItem(self.treeWidget)
            for value in range(len(table[item])):
                self.treeWidget.topLevelItem(item).setText(value, str(table[item][value]))
        

if __name__ == '__main__':

    db = 'myFirstDB'
    tableName = 'test8'
    
    app = QtGui.QApplication(sys.argv)
    ex = Ui_TPayne_MySQL_Tool(db, tableName)
    ex.show()
    x = app.exec_()

    sys.exit(x)
