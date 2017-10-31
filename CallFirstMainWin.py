# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import *
from UI.Lottery import *
from UI.UI_LatticePoint import *
from UI.UI_Maintenance import *
from UI.UI_Feedback import *
from UI.UI_MainWindow import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
