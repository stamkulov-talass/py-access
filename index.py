from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.Qt import *
from student import Student

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedHeight(600)
        MainWindow.setFixedWidth(900)
        MainWindow.setStyleSheet("background:rgb(47, 150, 171)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.frame.setStyleSheet("border: 4px solid \'#FFFFFF\';\n"
                                 "border-radius: 15px;\n"
                                 "margin: 10px;\n"
                                 "background: #FFFFFF")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 861, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setStyleSheet(                                    #"appearance: none;\n"
                                        "border: 0;\n"
                                        "border-radius: 15px;\n"
                                        "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
                                        "color: #FFFFFF;\n"
                                        "padding: 8px 16px;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(                                     #"appearance: none;\n"
                                        "border: 0;\n"
                                        "border-radius: 15px;\n"
                                        "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
                                        "color: #FFFFFF;\n"
                                        "padding: 8px 16px;\n"
                                        "font-size: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(                                    #"appearance: none;\n"
                                        "border: 0;\n"
                                        "border-radius: 15px;\n"
                                        "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
                                        "color: #FFFFFF;\n"
                                        "padding: 8px 16px;\n"
                                        "font-size: 16px;\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(                                      #"appearance: none;\n"
                                      "border: 0;\n"
                                      "border-radius: 15px;\n"
                                      "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 172, 235), stop:1 rgba(72,102,175));\n"
                                      "color: #FFFFFF;\n"
                                      "padding: 8px 16px;\n"
                                      "font-size: 16px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        
#        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget = QtWidgets.QTableView(self.frame)                # QTableView  !!!
        
        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 830, 351))
        self.tableWidget.setMinimumSize(QtCore.QSize(830, 351))
        self.tableWidget.setMaximumSize(QtCore.QSize(811, 351))
        self.tableWidget.setStyleSheet("border: 4px solid \'#2DACEB\';\n"
                                       "border-radius: 15px;\n"
                                       "margin: 10px;\n"
                                       "background: #FFFFFF")
        self.tableWidget.setObjectName("tableWidget")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Получить список студентов"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить студента"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить студента"))
        self.pushButton_4.setText(_translate("MainWindow", "Обновить данные студента"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog')

        self.id = QLineEdit()
        self.name = QLineEdit()
        self.group = QLineEdit()
        self.phone_number = QLineEdit()
        self.birth_date = QLineEdit()
        self.adress = QLineEdit()
        self.date_of_receipt = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow('id:', self.id)
        form_layout.addRow('name:', self.name)
        form_layout.addRow('group:', self.group)
        form_layout.addRow('phone_number:', self.phone_number)
        form_layout.addRow('birth_date:', self.birth_date)
        form_layout.addRow('adress:', self.adress)
        form_layout.addRow('date_of_receipt:', self.date_of_receipt)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.close) 
        self.pushButton_3.clicked.connect(self.add_row)
        self.pushButton_4.clicked.connect(self.update_row)
        self.pushButton_2.clicked.connect(self.delete_row)

        self.model = QtGui.QStandardItemModel(self)
        self.methods = Student.select().fetchall()
        for method in self.methods:
            item = QtGui.QStandardItem(str(method))
            item.setData(str(method))
            self.model.appendRow(item)
        self.tableWidget.setModel(self.model)

# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def add_row(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
            return  
        id = inputDialog.id.text()
        name = inputDialog.name.text()
        group = inputDialog.group.text()
        phone_number = inputDialog.phone_number.text()
        birth_date = inputDialog.birth_date.text()
        adress = inputDialog.adress.text()
        date_of_receipt = inputDialog.date_of_receipt.text()

        if not name or not id or not group or not phone_number or not birth_date or not adress or not date_of_receipt:
            msg = QMessageBox.information(self, 'Внимание', 'Заполните пожалуйста все поля.')
            return             
    
        Student.insert(id, name, group, phone_number, birth_date, adress, date_of_receipt)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    def update_row(self):
            inputDialog = Dialog()
            rez = inputDialog.exec()
            if not rez:
                msg = QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
                return  
            id = inputDialog.id.text()
            name = inputDialog.name.text()
            group = inputDialog.group.text()
            phone_number = inputDialog.phone_number.text()
            birth_date = inputDialog.birth_date.text()
            adress = inputDialog.adress.text()
            date_of_receipt = inputDialog.date_of_receipt.text()

            if not name or not id or not group or not phone_number or not birth_date or not adress or not date_of_receipt:
                msg = QMessageBox.information(self, 'Внимание', 'Заполните пожалуйста все поля.')
                return             
        
            Student.update(id, name, group, phone_number, birth_date, adress, date_of_receipt)

    def delete_row(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            msg = QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
            return  
        id = inputDialog.id.text()
        

        if not id:
            msg = QMessageBox.information(self, 'Внимание', 'Заполните пожалуйста все поля.')
            return             
    
        Student.delete(id)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())