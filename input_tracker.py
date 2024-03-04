import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem 
from PyQt5.QtCore import QTimer
from GUI import Ui_MainWindow
import logging
import serial
import time
import numpy as np
import pyqtgraph as pg

'''
Standard Logging Levels:

DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
'''

logging.basicConfig(filename="results.log", level=logging.INFO, format='%(asctime)s - %(message)s')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Open the serial port
        self.serialInst = serial.Serial("COM4", 9600)
        self.counter = 0  # Initialize the counter variable for the time x-axis

        # Create a QTimer to read serial periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial)
        
        # Initialize data for plotting
        self.x_data = []
        self.y_data = []

        # Create a plot item
        self.plot_item = self.GraphWidget_Top.plot()

        # Start the timer
        self.timer.start(100) 

    def read_serial(self):
        if self.serialInst.in_waiting:
            # Read a line from the serial port
            packet = self.serialInst.readline()
            # Treat the line as the value itself
            value = packet.decode('utf-8').strip()
            try:
                value_int = int(value,2)
                current_time = time.strftime("%H:%M:%S", time.localtime(time.time()))
                # Append data to list
                self.counter += 1 
                self.x_data.append(self.counter)
                self.y_data.append(value_int)
                
                if value_int > 10 or value_int < -4:
                    logging.info(f"at {current_time} The following up-normality formed with temperature {value_int} *C.")
                    # Update the table
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    self.tableWidget.setItem(row_position, 0, QTableWidgetItem(current_time))
                    self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(value_int)))
                # Update the plot
                self.plot_item.setData(self.x_data, self.y_data)
                #if len(self.x_data) < 10:
                self.GraphWidget_Top.getViewBox().setXRange(max(self.x_data[0: self.counter+1]) - 10, max(self.x_data[0: self.counter +1 ]))
            except ValueError:
                print("Invalid value received from Arduino:", value)

    def closeEvent(self, event):
        # Close the serial port when the window is closed
        self.serialInst.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
