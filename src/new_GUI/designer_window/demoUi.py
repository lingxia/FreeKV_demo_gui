# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUi.ui'
#
# Created: Wed Aug 27 19:17:32 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_demoUi(object):
    def setupUi(self, demoUi):
        demoUi.setObjectName(_fromUtf8("demoUi"))
        demoUi.resize(531, 420)
        self.demoGroupBox = QtGui.QGroupBox(demoUi)
        self.demoGroupBox.setGeometry(QtCore.QRect(20, 90, 491, 311))
        self.demoGroupBox.setObjectName(_fromUtf8("demoGroupBox"))
        self.demoTabWidget = QtGui.QTabWidget(self.demoGroupBox)
        self.demoTabWidget.setGeometry(QtCore.QRect(10, 50, 471, 251))
        self.demoTabWidget.setObjectName(_fromUtf8("demoTabWidget"))
        self.buildTab = QtGui.QWidget()
        self.buildTab.setObjectName(_fromUtf8("buildTab"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/build_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.demoTabWidget.addTab(self.buildTab, icon, _fromUtf8(""))
        self.runTab = QtGui.QWidget()
        self.runTab.setObjectName(_fromUtf8("runTab"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/run_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.demoTabWidget.addTab(self.runTab, icon1, _fromUtf8(""))
        self.runCheckBox = QtGui.QCheckBox(self.demoGroupBox)
        self.runCheckBox.setGeometry(QtCore.QRect(170, 30, 41, 17))
        self.runCheckBox.setObjectName(_fromUtf8("runCheckBox"))
        self.buildCheckBox = QtGui.QCheckBox(self.demoGroupBox)
        self.buildCheckBox.setGeometry(QtCore.QRect(230, 30, 41, 17))
        self.buildCheckBox.setObjectName(_fromUtf8("buildCheckBox"))
        self.typeGroupBox = QtGui.QGroupBox(demoUi)
        self.typeGroupBox.setGeometry(QtCore.QRect(290, 10, 91, 31))
        self.typeGroupBox.setObjectName(_fromUtf8("typeGroupBox"))

        self.retranslateUi(demoUi)
        self.demoTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(demoUi)

    def retranslateUi(self, demoUi):
        demoUi.setWindowTitle(_translate("demoUi", "FreeKV_demo Configuration", None))
        self.demoGroupBox.setTitle(_translate("demoUi", "FreeKV_demo Configuration", None))
        self.demoTabWidget.setTabText(self.demoTabWidget.indexOf(self.buildTab), _translate("demoUi", "Build", None))
        self.demoTabWidget.setTabText(self.demoTabWidget.indexOf(self.runTab), _translate("demoUi", "Run", None))
        self.runCheckBox.setText(_translate("demoUi", "Run", None))
        self.buildCheckBox.setText(_translate("demoUi", "Build", None))
        self.typeGroupBox.setTitle(_translate("demoUi", "Configuation Type", None))

