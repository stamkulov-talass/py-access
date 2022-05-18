import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
#from test import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.item_list = ['item %s' % i for i in range(11)]                 
        self.model_1 = QtCore.QStringListModel(self)
        self.model_1.setStringList(self.item_list)
        self.listView_1 = QtWidgets.QListView(self)                                    
        self.listView_1.setModel(self.model_1)
        
        self.model =  QtGui.QStandardItemModel(self)
        self.methods = ['PyScripts', 'option 1', 'option 2', 'option 3']
        for method in self.methods:
            item = QtGui.QStandardItem(method)
            item.setData(method)
            self.model.appendRow(item)        
        self.listView_2 = QtWidgets.QListView()
        self.listView_2.setModel(self.model)
        
        self.textBrowser = QtWidgets.QTextBrowser()
        self.textBrowser.setText("PyScripts")
        
        grid = QtWidgets.QGridLayout(self.centralWidget)
        grid.addWidget(self.listView_1)
        grid.addWidget(self.listView_2)
        grid.addWidget(self.textBrowser)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec_())