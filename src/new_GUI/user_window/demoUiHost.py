from PyQt4 import QtCore, QtGui
import sys, os

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,"../")
lib_path = main_path + "/lib/"
pic_path = main_path + "/pic/"
designer_path = main_path + "/designer_window/"

sys.path.append(lib_path)
sys.path.append(pic_path)
sys.path.append(designer_path)

from demoUi import Ui_demoUi

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
#        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveBuild)
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
#        if self.tokenFlag == True and self.testsuiteFlag == True:
        QtGui.QMessageBox.information(self,"Information",\
                                        "The Configuration File has been Saved Successfully !", QtGui.QMessageBox.Ok)            


        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testWin = demoConfig()
    testWin.show()
    sys.exit(app.exec_())