from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1201, 801)
                MainWindow.setMinimumSize(QtCore.QSize(1201, 801))
                MainWindow.setStyleSheet("background-color: #6c81cc;\n"
        "border-radius: 5px; \n"
        "\n"
        "background-color: #6c81cc;\n"
        "border: 1.2px solid #ffffff;\n"
        "border-style: outset;\n"
        "border-radius: 15px;\n"
        "\n"
        "\n"
        "")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setMinimumSize(QtCore.QSize(641, 300))
                self.centralwidget.setStyleSheet("border-radius: 5px; ")
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout()
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.groupbox.sizePolicy().hasHeightForWidth())
                self.groupbox.setSizePolicy(sizePolicy)
                self.groupbox.setStyleSheet("border: none;")
                self.groupbox.setObjectName("groupbox")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupbox)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem)
                self.Title = QtWidgets.QTextBrowser(self.groupbox)
                self.Title.setMinimumSize(QtCore.QSize(200, 51))
                self.Title.setMaximumSize(QtCore.QSize(341, 51))
                self.Title.setStyleSheet("border:none;\n"
        "color: white;")
                self.Title.setObjectName("Title")
                self.horizontalLayout_3.addWidget(self.Title)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_3.addItem(spacerItem1)
                self.verticalLayout_3.addWidget(self.groupbox)
                spacerItem2 = QtWidgets.QSpacerItem(19, 66, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout_3.addItem(spacerItem2)
                self.groupbox1 = QtWidgets.QGroupBox(self.centralwidget)
                self.groupbox1.setStyleSheet("")
                self.groupbox1.setObjectName("groupbox1")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupbox1)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                spacerItem3 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem3)
           
                spacerItem4 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem4)
                self.horizontalLayout_2.addLayout(self.verticalLayout)
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.groupbox2 = QtWidgets.QGroupBox(self.groupbox1)
                self.groupbox2.setStyleSheet("border:none;")
                self.groupbox2.setObjectName("groupbox2")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox2)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.Vert_ScrollBar_Top = QtWidgets.QScrollBar(self.groupbox2)
                self.Vert_ScrollBar_Top.setEnabled(False)
                self.Vert_ScrollBar_Top.setProperty("value", 50)
                self.Vert_ScrollBar_Top.setOrientation(QtCore.Qt.Vertical)
                self.Vert_ScrollBar_Top.setObjectName("Vert_ScrollBar_Top")
                self.horizontalLayout.addWidget(self.Vert_ScrollBar_Top)
                self.GraphWidget_Top = PlotWidget(self.groupbox2)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.GraphWidget_Top.sizePolicy().hasHeightForWidth())
                self.GraphWidget_Top.setSizePolicy(sizePolicy)
                self.GraphWidget_Top.setMinimumSize(QtCore.QSize(501, 222))
                self.GraphWidget_Top.setMaximumSize(QtCore.QSize(16777215, 941))
                self.GraphWidget_Top.setStyleSheet("border:none;")
                self.GraphWidget_Top.setObjectName("GraphWidget_Top")
                self.horizontalLayout.addWidget(self.GraphWidget_Top)
                self.verticalLayout_2.addWidget(self.groupbox2)
                self.Horiz_ScrollBar_Top = QtWidgets.QScrollBar(self.groupbox1)
                self.Horiz_ScrollBar_Top.setEnabled(False)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(1)
                sizePolicy.setVerticalStretch(1)
                sizePolicy.setHeightForWidth(self.Horiz_ScrollBar_Top.sizePolicy().hasHeightForWidth())
                self.Horiz_ScrollBar_Top.setSizePolicy(sizePolicy)
                self.Horiz_ScrollBar_Top.setOrientation(QtCore.Qt.Horizontal)
                self.Horiz_ScrollBar_Top.setObjectName("Horiz_ScrollBar_Top")
                self.verticalLayout_2.addWidget(self.Horiz_ScrollBar_Top)
                self.horizontalLayout_2.addLayout(self.verticalLayout_2)
                self.verticalLayout_3.addWidget(self.groupbox1)
                self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(255)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
                self.tableWidget.setSizePolicy(sizePolicy)
                # Resize columns to fit contents
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.setMinimumSize(QtCore.QSize(0, 200))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.tableWidget.setFont(font)
                self.tableWidget.setStyleSheet("border-radius: 5px solid black; ")
                self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
                self.tableWidget.setObjectName("tableWidget")
                self.tableWidget.setColumnCount(2)
                color = QColor('white')
                palette = self.tableWidget.palette()
                palette.setColor(self.tableWidget.foregroundRole(), color)
                self.tableWidget.setPalette(palette)
                self.tableWidget.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                item.setBackground(QtGui.QColor(85, 255, 255))
                self.tableWidget.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.tableWidget.setHorizontalHeaderItem(1, item)
        
                self.verticalLayout_3.addWidget(self.tableWidget)
                self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)
              

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Signal Viewer"))
                self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Live Signal Viewer</span></p></body></html>"))
       
                item = self.tableWidget.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Duration "))
                item = self.tableWidget.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "up-normal-Temp "))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
