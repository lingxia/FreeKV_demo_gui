from PyQt4 import QtCore, QtGui
import sys, os

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,"../")
lib_path = main_path + "/lib/"
pic_path = main_path + "/pic/"
designer_path = main_path + "/designer_window/"
config_path = main_path +  "../" +"config/"

sys.path.append(lib_path)
sys.path.append(pic_path)
sys.path.append(designer_path)

from demoUi import Ui_demoUi
import platform_list
from get_local_config import Get_IDE_info
import win32api
from getconfig import Getconfig

config_file = config_path + "config.xml"
config = Getconfig(config_file)

class demoConfig(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.demoWin = Ui_demoUi()
        self.demoWin.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        
#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()
        
#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save_icon.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveConfig)
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveEvent)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/exit_icon.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File !")
        self.quitAct.whatsThis()
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),self.close)
               
#****************add Menus and Actions**************
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        

        
        self.initCombobox()
        
        self.connect(self.demoWin.buildCheckBox, QtCore.SIGNAL("stateChanged(int)"), self.selectBuild)
        self.connect(self.demoWin.runCheckBox, QtCore.SIGNAL("stateChanged(int)"),self.selectRun)
        self.connect(self.demoWin.ideComboBox, QtCore.SIGNAL("activated (int)"),self.initIde)
        
#***************some event with messagebox********        
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.warning(self, 'Warning', \
                                           'Are you sure to Quit ? Please make sure your Configurations had been Saved !',\
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def saveEvent(self):
        QtGui.QMessageBox.information(self,"Information",\
                                        "The Configuration File has been Saved Successfully !", QtGui.QMessageBox.Ok)            



#***************init of combo box******************
    def initCombobox(self):
        ide = platform_list.ide_list
        target = platform_list.target_list
        suite = platform_list.test_suite
        platform = platform_list.platform_list
        debugger = platform_list.debugger_list
        
        ide_len = len(ide)
        target_len = len(target)
        suite_len = len(suite)
        platform_len = len(platform)
        debugger_len = len(debugger) 
        
        for num in range(0,ide_len):
            self.demoWin.ideComboBox.addItem("")
            self.demoWin.ideComboBox.setItemText(num, ide[num])
        
        for num in range(0,target_len):
            self.demoWin.targetComboBox.addItem("")
            self.demoWin.targetComboBox.setItemText(num,target[num])
        
        for num in range(0,suite_len):
            self.demoWin.testsuiteComboBox.addItem("")
            self.demoWin.testsuiteComboBox.setItemText(num,suite[num])
            
        for num in range(0,platform_len):
            self.demoWin.platformComboBox.addItem("")
            self.demoWin.platformComboBox.setItemText(num,platform[num])
            
        for num in range(0,debugger_len):
            self.demoWin.debuggerComboBox.addItem("")
            self.demoWin.debuggerComboBox.setItemText(num,debugger[num])
            
    

#****************select test type: build or run*************
    def selectBuild(self):
        buildCheckStatus = self.demoWin.buildCheckBox.checkState()
        if buildCheckStatus == QtCore.Qt.Checked:
            config.setValue("build", "yes")
            config.setValue("run","no")
            config.setValue("build_and_run","no")
            config.setValue("app_info","yes")
            config.setValue("sync_enable","no")
            self.demoWin.runCheckBox.setCheckable(False)
            self.demoWin.demoTabWidget.setTabEnabled(2,False)            
        elif buildCheckStatus != QtCore.Qt.Checked:
            self.demoWin.runCheckBox.setCheckable(True)
            self.demoWin.demoTabWidget.setTabEnabled(2,True)

            
    def selectRun(self):
        runCheckStatus = self.demoWin.runCheckBox.checkState()
        if runCheckStatus == QtCore.Qt.Checked:
            config.setValue("build", "no")
            config.setValue("run","yes")
            config.setValue("build_and_run","no")
            config.setValue("build_lib","no")
            config.setValue("pre_configure", "no")
            config.setValue("sync_enable","no")
            self.demoWin.buildCheckBox.setCheckable(False)
            self.demoWin.demoTabWidget.setTabEnabled(1,False)
        elif runCheckStatus != QtCore.Qt.Checked:
            self.demoWin.buildCheckBox.setCheckable(True)
            self.demoWin.demoTabWidget.setTabEnabled(1,True) 
    
#************************ide init*********************
    def initIde(self):
            ideSelect = self.demoWin.ideComboBox.currentText()
            ide_info = Get_IDE_info()
            
            if ideSelect.__str__() == "uv4":
                ideSelected = "keil"
                ideList = ide_info[ideSelected]
            elif ideSelect.__str__() == "kds":
                self.demoWin.ideVersionComboBox.clear()
                self.demoWin.ideLineEdit.clear()
                return
            else:
                ideSelected = ideSelect.__str__()
                ideList = ide_info[ideSelected]
            
            ideLen = len(ideList)
            if ideLen == 0:
                self.demoWin.ideVersionComboBox.clear()
                self.demoWin.ideLineEdit.clear()
            elif ideLen !=0 :
                for num in range(0, ideLen):
                    self.demoWin.ideVersionComboBox.removeItem(num)
                    self.demoWin.ideVersionComboBox.addItem("")
                    self.demoWin.ideVersionComboBox.setItemText(num,ideList[num]["version"])
                
                ideIndex = self.demoWin.ideVersionComboBox.currentIndex()
                idePath = ideList[ideIndex]["path"]
                self.demoWin.ideLineEdit.setText(idePath)    
                    

#************************save build*******************
    def saveConfig(self):
        type = self.demoWin.testsuiteComboBox.currentText()
        config.setValue("test_type", type.__str__())
        
        app = self.demoWin.appLineEdit.text()
        if app != "":
            config.setValue("app", app.__str__())
        elif app == "":
            pass        
        
        currentPlatform = self.demoWin.platformComboBox.currentText()
        platform = currentPlatform.__str__()
        config.setValue("platform", platform)
        
        mingwDir = self.demoWin.mingwLineEdit.text()
        if mingwDir != "":
            mingwShrot = win32api.GetShortPathName(mingwDir.__str__())
            config.setValue("mingw", mingwShrot)
        elif mingwDir == "":
            pass
        
        buildCheckStatus = self.demoWin.buildCheckBox.checkState()
        runCheckStatus = self.demoWin.runCheckBox.checkState()
        if buildCheckStatus == QtCore.Qt.Checked:
            testDir = self.demoWin.testLineEdit.text()
            if testDir != "":
                config.setValue("psdk_demo_dir", testDir.__str__())
            elif testDir == "":
                pass
            
            buildLib = self.demoWin.libComboBox.currentText()
            config.setValue("build_lib", buildLib.__str__())
            
            project = self.demoWin.projectComboBox.currentText()
            config.setValue("pre_configure",project.__str__())
            
            target = self.demoWin.targetComboBox.currentText()
            config.setValue("target", target.__str__())
            
            ideSelect = self.demoWin.ideComboBox.currentText()
            config.setValue("IDE", ideSelect.__str__())
            
            ideDir = self.demoWin.ideLineEdit.text()
            ideDirShort = win32api.GetShortPathName(ideDir.__str__())
            config.setValue(ideSelect.__str__(), ideDirShort)
            
            ideVer = self.demoWin.ideVersionComboBox.currentText()
            config.setAttr(ideSelect.__str__(), "version", ideVer.__str__())
                    
                
            
            
        elif runCheckStatus == QtCore.Qt.Checked:
            debugger = self.demoWin.debuggerComboBox.currentText()
            config.setValue("debugger", debugger.__str__())
            debuggerDir = self.demoWin.debuggerLineEdit.text()
            if debuggerDir != "":
                debuggerShort = win32api.GetShortPathName(debuggerDir.__str__())
                config.setValue(debugger.__str__(), debuggerShort)
            elif debuggerDir == "":
                pass
            

            
            serialPort = self.demoWin.serialLineEdit.text()
            debugPort = self.demoWin.debugPortLineEdit.text()
            
            config.setAttr(platform, "serial_port", serialPort.__str__())
            config.setAttr(platform, "debug_port", debugPort.__str__())
            
            binaryDir = self.demoWin.binaryLineEdit.text()
            if binaryDir != "":
                binaryShort = win32api.GetShortPathName(binaryDir.__str__())
                config.setValue("binary", binaryShort)
            elif binaryDir == "":
                pass
        else:
            pass
    
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testWin = demoConfig()
    testWin.show()
    sys.exit(app.exec_())