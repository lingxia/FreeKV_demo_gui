# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUi.ui'
#
# Created: Fri Aug 29 10:07:41 2014
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
        demoUi.resize(392, 342)
        self.demoGroupBox = QtGui.QGroupBox(demoUi)
        self.demoGroupBox.setGeometry(QtCore.QRect(10, 120, 371, 211))
        self.demoGroupBox.setObjectName(_fromUtf8("demoGroupBox"))
        self.demoTabWidget = QtGui.QTabWidget(self.demoGroupBox)
        self.demoTabWidget.setGeometry(QtCore.QRect(10, 20, 351, 181))
        self.demoTabWidget.setObjectName(_fromUtf8("demoTabWidget"))
        self.basicTab = QtGui.QWidget()
        self.basicTab.setObjectName(_fromUtf8("basicTab"))
        self.testsuiteComboBox = QtGui.QComboBox(self.basicTab)
        self.testsuiteComboBox.setGeometry(QtCore.QRect(80, 10, 111, 22))
        self.testsuiteComboBox.setObjectName(_fromUtf8("testsuiteComboBox"))
        self.testsuiteLabel = QtGui.QLabel(self.basicTab)
        self.testsuiteLabel.setGeometry(QtCore.QRect(20, 11, 71, 21))
        self.testsuiteLabel.setObjectName(_fromUtf8("testsuiteLabel"))
        self.label = QtGui.QLabel(self.basicTab)
        self.label.setGeometry(QtCore.QRect(200, 10, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.appLineEdit = QtGui.QLineEdit(self.basicTab)
        self.appLineEdit.setGeometry(QtCore.QRect(250, 10, 81, 20))
        self.appLineEdit.setObjectName(_fromUtf8("appLineEdit"))
        self.platformLabel = QtGui.QLabel(self.basicTab)
        self.platformLabel.setGeometry(QtCore.QRect(20, 50, 54, 21))
        self.platformLabel.setObjectName(_fromUtf8("platformLabel"))
        self.platformComboBox = QtGui.QComboBox(self.basicTab)
        self.platformComboBox.setGeometry(QtCore.QRect(70, 50, 121, 22))
        self.platformComboBox.setObjectName(_fromUtf8("platformComboBox"))
        self.label_2 = QtGui.QLabel(self.basicTab)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 41, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.mingwLineEdit = QtGui.QLineEdit(self.basicTab)
        self.mingwLineEdit.setGeometry(QtCore.QRect(250, 50, 81, 20))
        self.mingwLineEdit.setObjectName(_fromUtf8("mingwLineEdit"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/config_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.demoTabWidget.addTab(self.basicTab, icon, _fromUtf8(""))
        self.buildTab = QtGui.QWidget()
        self.buildTab.setObjectName(_fromUtf8("buildTab"))
        self.testDirLabel = QtGui.QLabel(self.buildTab)
        self.testDirLabel.setGeometry(QtCore.QRect(20, 10, 54, 21))
        self.testDirLabel.setObjectName(_fromUtf8("testDirLabel"))
        self.testLineEdit = QtGui.QLineEdit(self.buildTab)
        self.testLineEdit.setGeometry(QtCore.QRect(70, 10, 101, 20))
        self.testLineEdit.setObjectName(_fromUtf8("testLineEdit"))
        self.projectLabel = QtGui.QLabel(self.buildTab)
        self.projectLabel.setGeometry(QtCore.QRect(20, 50, 101, 20))
        self.projectLabel.setObjectName(_fromUtf8("projectLabel"))
        self.projectComboBox = QtGui.QComboBox(self.buildTab)
        self.projectComboBox.setGeometry(QtCore.QRect(118, 50, 61, 22))
        self.projectComboBox.setObjectName(_fromUtf8("projectComboBox"))
        self.projectComboBox.addItem(_fromUtf8(""))
        self.projectComboBox.addItem(_fromUtf8(""))
        self.ideLabel = QtGui.QLabel(self.buildTab)
        self.ideLabel.setGeometry(QtCore.QRect(20, 90, 21, 20))
        self.ideLabel.setObjectName(_fromUtf8("ideLabel"))
        self.ideComboBox = QtGui.QComboBox(self.buildTab)
        self.ideComboBox.setGeometry(QtCore.QRect(50, 90, 69, 22))
        self.ideComboBox.setObjectName(_fromUtf8("ideComboBox"))
        self.ideLineEdit = QtGui.QLineEdit(self.buildTab)
        self.ideLineEdit.setGeometry(QtCore.QRect(130, 90, 151, 20))
        self.ideLineEdit.setObjectName(_fromUtf8("ideLineEdit"))
        self.targetComboBox = QtGui.QComboBox(self.buildTab)
        self.targetComboBox.setGeometry(QtCore.QRect(240, 50, 91, 22))
        self.targetComboBox.setObjectName(_fromUtf8("targetComboBox"))
        self.targetLabel = QtGui.QLabel(self.buildTab)
        self.targetLabel.setGeometry(QtCore.QRect(190, 50, 41, 21))
        self.targetLabel.setObjectName(_fromUtf8("targetLabel"))
        self.libComboBox = QtGui.QComboBox(self.buildTab)
        self.libComboBox.setGeometry(QtCore.QRect(240, 10, 91, 22))
        self.libComboBox.setObjectName(_fromUtf8("libComboBox"))
        self.libComboBox.addItem(_fromUtf8(""))
        self.libComboBox.addItem(_fromUtf8(""))
        self.libLabel = QtGui.QLabel(self.buildTab)
        self.libLabel.setGeometry(QtCore.QRect(180, 10, 61, 20))
        self.libLabel.setObjectName(_fromUtf8("libLabel"))
        self.versionLabel = QtGui.QLabel(self.buildTab)
        self.versionLabel.setGeometry(QtCore.QRect(130, 120, 51, 16))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.ideVersionComboBox = QtGui.QComboBox(self.buildTab)
        self.ideVersionComboBox.setGeometry(QtCore.QRect(50, 120, 69, 22))
        self.ideVersionComboBox.setEditable(True)
        self.ideVersionComboBox.setObjectName(_fromUtf8("ideVersionComboBox"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/build_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.demoTabWidget.addTab(self.buildTab, icon1, _fromUtf8(""))
        self.runTab = QtGui.QWidget()
        self.runTab.setObjectName(_fromUtf8("runTab"))
        self.debuggerLabel = QtGui.QLabel(self.runTab)
        self.debuggerLabel.setGeometry(QtCore.QRect(20, 10, 51, 21))
        self.debuggerLabel.setObjectName(_fromUtf8("debuggerLabel"))
        self.debuggerLineEdit = QtGui.QLineEdit(self.runTab)
        self.debuggerLineEdit.setGeometry(QtCore.QRect(150, 10, 171, 20))
        self.debuggerLineEdit.setObjectName(_fromUtf8("debuggerLineEdit"))
        self.debuggerComboBox = QtGui.QComboBox(self.runTab)
        self.debuggerComboBox.setGeometry(QtCore.QRect(70, 10, 69, 22))
        self.debuggerComboBox.setObjectName(_fromUtf8("debuggerComboBox"))
        self.serialLabel = QtGui.QLabel(self.runTab)
        self.serialLabel.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.serialLabel.setObjectName(_fromUtf8("serialLabel"))
        self.serialLineEdit = QtGui.QLineEdit(self.runTab)
        self.serialLineEdit.setGeometry(QtCore.QRect(90, 50, 61, 20))
        self.serialLineEdit.setObjectName(_fromUtf8("serialLineEdit"))
        self.debugPortLineEdit = QtGui.QLineEdit(self.runTab)
        self.debugPortLineEdit.setGeometry(QtCore.QRect(230, 50, 91, 20))
        self.debugPortLineEdit.setText(_fromUtf8(""))
        self.debugPortLineEdit.setObjectName(_fromUtf8("debugPortLineEdit"))
        self.debugPortLabel = QtGui.QLabel(self.runTab)
        self.debugPortLabel.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.debugPortLabel.setObjectName(_fromUtf8("debugPortLabel"))
        self.binaryLabel = QtGui.QLabel(self.runTab)
        self.binaryLabel.setGeometry(QtCore.QRect(20, 80, 41, 21))
        self.binaryLabel.setObjectName(_fromUtf8("binaryLabel"))
        self.binaryLineEdit = QtGui.QLineEdit(self.runTab)
        self.binaryLineEdit.setGeometry(QtCore.QRect(70, 80, 251, 20))
        self.binaryLineEdit.setObjectName(_fromUtf8("binaryLineEdit"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../pic/run_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.demoTabWidget.addTab(self.runTab, icon2, _fromUtf8(""))
        self.typeGroupBox = QtGui.QGroupBox(demoUi)
        self.typeGroupBox.setGeometry(QtCore.QRect(10, 60, 161, 51))
        self.typeGroupBox.setObjectName(_fromUtf8("typeGroupBox"))
        self.buildCheckBox = QtGui.QCheckBox(self.typeGroupBox)
        self.buildCheckBox.setGeometry(QtCore.QRect(20, 20, 51, 17))
        self.buildCheckBox.setCheckable(True)
        self.buildCheckBox.setChecked(False)
        self.buildCheckBox.setObjectName(_fromUtf8("buildCheckBox"))
        self.runCheckBox = QtGui.QCheckBox(self.typeGroupBox)
        self.runCheckBox.setGeometry(QtCore.QRect(90, 20, 41, 17))
        self.runCheckBox.setObjectName(_fromUtf8("runCheckBox"))

        self.retranslateUi(demoUi)
        self.demoTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(demoUi)

    def retranslateUi(self, demoUi):
        demoUi.setWindowTitle(_translate("demoUi", "FreeKV_demo Configuration", None))
        self.demoGroupBox.setTitle(_translate("demoUi", "FreeKV_demo Configuration", None))
        self.testsuiteLabel.setText(_translate("demoUi", "TestSuite", None))
        self.label.setText(_translate("demoUi", "App Name", None))
        self.platformLabel.setText(_translate("demoUi", "Platform", None))
        self.label_2.setText(_translate("demoUi", "MinGW", None))
        self.demoTabWidget.setTabText(self.demoTabWidget.indexOf(self.basicTab), _translate("demoUi", "Basic", None))
        self.testDirLabel.setText(_translate("demoUi", "Test Dir", None))
        self.projectLabel.setText(_translate("demoUi", "Generate Project", None))
        self.projectComboBox.setItemText(0, _translate("demoUi", "yes", None))
        self.projectComboBox.setItemText(1, _translate("demoUi", "no", None))
        self.ideLabel.setText(_translate("demoUi", "IDE", None))
        self.targetLabel.setText(_translate("demoUi", "Target", None))
        self.libComboBox.setItemText(0, _translate("demoUi", "yes", None))
        self.libComboBox.setItemText(1, _translate("demoUi", "no", None))
        self.libLabel.setText(_translate("demoUi", "Build Lib", None))
        self.versionLabel.setText(_translate("demoUi", "*version", None))
        self.demoTabWidget.setTabText(self.demoTabWidget.indexOf(self.buildTab), _translate("demoUi", "Build", None))
        self.debuggerLabel.setText(_translate("demoUi", "Debugger", None))
        self.serialLabel.setText(_translate("demoUi", "Serial Port", None))
        self.debugPortLabel.setText(_translate("demoUi", "Debug Port", None))
        self.binaryLabel.setText(_translate("demoUi", "Binary", None))
        self.demoTabWidget.setTabText(self.demoTabWidget.indexOf(self.runTab), _translate("demoUi", "Run", None))
        self.typeGroupBox.setTitle(_translate("demoUi", "Configuation Type", None))
        self.buildCheckBox.setText(_translate("demoUi", "Build", None))
        self.runCheckBox.setText(_translate("demoUi", "Run", None))

