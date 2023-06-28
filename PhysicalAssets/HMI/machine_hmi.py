# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\machine_hmi.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory
from PyQt5.QtWidgets import QColorDialog, QTextEdit
import time
import traceback, sys
import os

parent_dir=os.getcwd()
#Machine Twin
class MachineTwin(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Machine Twin Thread started")
        sys.path.append(parent_dir+r"\Machine_Twin 1")
        import MT
        MT.receive()

#Application and Service Agent
class AppandSerAgent(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Application and Service Agent Thread started")
        sys.path.append(parent_dir+r"\Application and Service Agent")
        import AaS
        AaS.receive()

#Operation and Management Agent
class OperandMaintAgent(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Operation and Management Agent Thread started")
        sys.path.append(parent_dir+r"\Operation and Management Agent")
        import OaM
        OaM.receive()

#Notifier Agent
class NotifierManager(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Notifier Agent Thread start")
        sys.path.append(parent_dir+r"\notifieragent")
        import NM
        NM.receive()

#Establish Connection
class EstablishConnection(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Connection Establish Thread started")
        sys.path.append("C:\\Users\\ashut\\OneDrive\\Desktop\\MTP_Report\\Digital Twin 3.0\\Physical Assets\\HMI_1\\notifieragent")
        import socketdll

# Application and Service Custom Function Installation
class App_and_ser_function_install(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Application and Service Custom Function Installation Thread start")
        sys.path.append(parent_dir+r"\Application and Service Agent")
        import install_function_file_gui_AaS

# Operation and Management Agent Custom Function Installation
class Oper_and_Manag_function_install(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Operation and Management Agent Custom Function Installation Thread start")
        sys.path.append(parent_dir+r"\Operation and Management Agent")
        import install_function_file_gui_OaM 

# Notifier Agent Custom Function Installation
class NotifierManager_function_install(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Notifier Agent Custom Function Installation Thread start")
        sys.path.append(parent_dir+r"\notifieragent")
        import install_function_file_gui_nm

# Machine Twin Agent Custom Function Installation
class MachineTwin_function_install(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Machine Twin Agent Custom Function Installation Thread start")
        sys.path.append(parent_dir+r"\Machine_Twin 1")
        import install_function_file_gui_mt
        

# Application and Service Custom Function Delete
class App_and_ser_function_uninstall(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Application and Service Custom Function Unstallation Thread start")
        sys.path.append(parent_dir+r"\Application and Service Agent")
        import delete_function_file_gui_AaS

# Operation and Management Agent Custom Function Delete
class Oper_and_Manag_function_uninstall(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Operation and Management Agent Custom Function Unstallation Thread start")
        sys.path.append(parent_dir+r"\Operation and Management Agent")
        import delete_function_file_gui_OaM 

# Notifier Agent Custom Function Delete
class NotifierManager_function_uninstall(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Notifier Agent Custom Function Unstallation Thread start")
        sys.path.append(parent_dir+r"\notifieragent")
        import delete_function_file_gui_nm

# Machine Twin Agent Custom Function Delete
class MachineTwin_function_uninstall(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Machine Twin Agent Custom Function Unstallation Thread start")
        sys.path.append(parent_dir+r"\Machine_Twin 1")
        import delete_function_file_gui_mt

# Editing of Active Function File for Application and Service
class App_Serv_active_function(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Application and Service Agent Active Function Initialization Thread start")
        sys.path.append(parent_dir+r"\Application and Service Agent")
        import Active_Function_Edit_AaS

# Editing of Active Function File for Operation and Maintenance
class Oper_Main_active_function(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Operation and Maintenance Agent Active Function Initialization Thread start")
        sys.path.append(parent_dir+r"\Operation and Management Agent")
        import Active_Function_Edit_OaM

# Editing of Active Function File for Notifier Service
class Notifier_Service_active_function(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Notifier Service Agent Active Function Initialization Thread start")
        sys.path.append(parent_dir+r"\notifieragent")
        import Active_Function_Edit_nm

# Editing of Active Function File for Machine Twin
class Machine_Twin_active_function(QThread):
    '''
    Worker thread
    '''
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Machine Twin Agent Active Function Initialization Thread start")
        sys.path.append(parent_dir+r"\Machine_Twin 1")
        import Active_Function_Edit_mt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 550)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(144, 144, 144);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.App_and_service_agent = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.App_and_service_agent.setFont(font)
        self.App_and_service_agent.setStyleSheet("color: rgb(17, 17, 17);\n"
"background-color: rgb(255, 85, 255);")
        
        # Buttons

        # Activate Application and Service Agent
        self.App_and_service_agent.setObjectName("App_and_service_agent")
        # Mapping of Inventory Manager button to inventory_click function
        self.App_and_service_agent.clicked.connect(self.app_and_service_click)
        self.verticalLayout.addWidget(self.App_and_service_agent)
        self.Oper_and_Main_Agent = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Oper_and_Main_Agent.setFont(font)
        self.Oper_and_Main_Agent.setStyleSheet("color: rgb(7, 7, 7);\n"
"background-color: rgb(255, 255, 127);")

        # Activate Operation and Management Agent
        self.Oper_and_Main_Agent.setObjectName("Oper_and_Main_Agent")
        # Mapping of Order Manager button to order_click function
        self.Oper_and_Main_Agent.clicked.connect(self.Oper_and_Main_click)
        self.verticalLayout.addWidget(self.Oper_and_Main_Agent)
        self.Notifier = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Notifier.setFont(font)
        self.Notifier.setStyleSheet("color: rgb(21, 21, 21);\n"
"background-color: rgb(0, 255, 255);")

        # Activate Notifier Agent
        self.Notifier.setObjectName("Notifier")
        # Mapping of Notifier Agent button to notifier_click function
        self.Notifier.clicked.connect(self.notifier_click)
        self.verticalLayout.addWidget(self.Notifier)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.agent_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.agent_button.setFont(font)
        self.agent_button.setStyleSheet("background-color: rgb(0, 255, 127);")

        # Twin Agent Activation
        self.agent_button.setObjectName("agent_button")
        # Mapping of Twin Agent button to twin_click function
        self.agent_button.clicked.connect(self.machine_initialization)
        self.gridLayout.addWidget(self.agent_button, 2, 0, 1, 1)
        self.Socket_dll = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Socket_dll.setFont(font)
        self.Socket_dll.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Socket_dll.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Socket_dll.setAutoFillBackground(False)
        self.Socket_dll.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Socket_dll.setIconSize(QtCore.QSize(20, 40))

        # Establish Connection
        self.Socket_dll.setObjectName("Socket_dll")
        # Mapping of Socket.dll script to Establish Connection button
        self.Socket_dll.clicked.connect(self.socket_click)
        self.gridLayout.addWidget(self.Socket_dll, 1, 2, 1, 1)
        self.server_frame = QtWidgets.QFrame(self.centralwidget)
        self.server_frame.setAutoFillBackground(False)
        self.server_frame.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.server_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.server_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.server_frame.setLineWidth(1)
        self.server_frame.setObjectName("server_frame")
        self.layoutWidget = QtWidgets.QWidget(self.server_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 78, 341, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IP_address_machine_agent = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.IP_address_machine_agent.setFont(font)

        # Twin Agent IP Address
        self.IP_address_machine_agent.setObjectName("IP_address_machine_agent")
        self.horizontalLayout.addWidget(self.IP_address_machine_agent)
        self.lineEdit_server_ip = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_server_ip.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_server_ip.setObjectName("lineEdit_server_ip")
        self.horizontalLayout.addWidget(self.lineEdit_server_ip)
        self.layoutWidget1 = QtWidgets.QWidget(self.server_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 341, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Port_No_machine_agent = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Port_No_machine_agent.setFont(font)

        # Twin Agent Port Number
        self.Port_No_machine_agent.setObjectName("Port_No_machine_agent")
        self.horizontalLayout_2.addWidget(self.Port_No_machine_agent)
        self.lineEdit_server_port = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_server_port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_server_port.setObjectName("lineEdit_server_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_server_port)
        self.gridLayout.addWidget(self.server_frame, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(8, 8, 8);\n"
"border-color: rgb(6, 6, 6);\n"
"background-color: rgb(92, 190, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(50)
        self.label.setMidLineWidth(17)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.logs_window = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.logs_window.setFont(font)
        self.logs_window.setStyleSheet("color: rgb(4, 4, 4);\n"
"border-color: rgb(8, 8, 8);\n"
"background-color: rgb(255, 255, 255);")
        self.logs_window.setFrameShape(QtWidgets.QFrame.Box)
        self.logs_window.setLineWidth(2)
        self.logs_window.setMidLineWidth(2)

        #Logs Window
        self.logs_window.setObjectName("logs_window")
        self.gridLayout.addWidget(self.logs_window, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))


        # Menu Bar : Functinal Entities
        self.menubar.setObjectName("menubar")
        self.menuCustom_Function_Install = QtWidgets.QMenu(self.menubar)
        self.menuCustom_Function_Install.setObjectName("menuCustom_Function_Install")
        self.menuApplication_and_Service = QtWidgets.QMenu(self.menuCustom_Function_Install)
        self.menuApplication_and_Service.setObjectName("menuApplication_and_Service")
        self.menuOperation_and_Maintenance = QtWidgets.QMenu(self.menuCustom_Function_Install)
        self.menuOperation_and_Maintenance.setObjectName("menuOperation_and_Maintenance")
        self.menuNotifier = QtWidgets.QMenu(self.menuCustom_Function_Install)
        self.menuNotifier.setObjectName("menuNotifier")
        self.menuMachine_Twin = QtWidgets.QMenu(self.menuCustom_Function_Install)
        self.menuMachine_Twin.setObjectName("menuMachine_Twin")
        self.menuActive_Function_Initialization = QtWidgets.QMenu(self.menubar)
        self.menuActive_Function_Initialization.setObjectName("menuActive_Function_Initialization")
        #self.menuOpen_Editor = QtWidgets.QMenu(self.menubar)
        #self.menuOpen_Editor.setObjectName("menuOpen_Editor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApplication_and_Service = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionApplication_and_Service.setFont(font)
        self.actionApplication_and_Service.setObjectName("actionApplication_and_Service")
        self.actionO_M = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.actionO_M.setFont(font)
        self.actionO_M.setObjectName("actionO_M")
        self.Install = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Install.setFont(font)

        # Install

        
        self.Install.setObjectName("Install")
        self.actionInstall = QtWidgets.QAction(MainWindow)
        self.actionInstall.setObjectName("actionInstall")
        # Mapping of method to install button
        self.actionInstall.triggered.connect(self.Application_and_Service_Install)
        self.actionInstall_2 = QtWidgets.QAction(MainWindow)
        self.actionInstall_2.setObjectName("actionInstall_2")
        # Mapping of method to install button
        self.actionInstall_2.triggered.connect(self.Operation_and_Management_Install)
        self.actionInstall_3 = QtWidgets.QAction(MainWindow)
        self.actionInstall_3.setObjectName("actionInstall_3")
        # Mapping of method to install button
        self.actionInstall_3.triggered.connect(self.Notifier_Service_Install)
        self.actionInstall_4 = QtWidgets.QAction(MainWindow)
        self.actionInstall_4.setObjectName("actionInstall_4")

        # Mapping of method to install button
        self.actionInstall_4.triggered.connect(self.Machine_Twin_Install)

        # Delete

        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        # Mapping of method to delete button
        self.actionDelete.triggered.connect(self.Application_and_Service_UnInstall)
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_2.setObjectName("actionDelete_2")
        # Mapping of method to delete button
        self.actionDelete_2.triggered.connect(self.Operation_and_Management_UnInstall)
        self.actionDelete_3 = QtWidgets.QAction(MainWindow)
        self.actionDelete_3.setObjectName("actionDelete_3")
        # Mapping of method to delete button
        self.actionDelete_3.triggered.connect(self.Notifier_Service_UnInstall)
        self.actionDelete_4 = QtWidgets.QAction(MainWindow)
        self.actionDelete_4.setObjectName("actionDelete_4")

        # Mapping of method to delete button
        self.actionDelete_4.triggered.connect(self.Machine_Twin_UnInstall)

        
        
        #
        self.actionApp_Serv_active = QtWidgets.QAction(MainWindow)
        self.actionApp_Serv_active.setObjectName("actionApp_Serv_active")
        self.actionApp_Serv_active.triggered.connect(self.Application_and_Service_Active_Function)
        #
        self.actionOper_Main_active = QtWidgets.QAction(MainWindow)
        self.actionOper_Main_active.setObjectName("actionOper_Main_active")
        self.actionOper_Main_active.triggered.connect(self.Operation_and_management_Active_Function)
        #
        self.actionNotifier_Serv_active = QtWidgets.QAction(MainWindow)
        self.actionNotifier_Serv_active.setObjectName("actionNotifier_Serv_active")
        self.actionNotifier_Serv_active.triggered.connect(self.Notifier_Service_Active_Function)
        #
        self.actionMachine_Twin_active = QtWidgets.QAction(MainWindow)
        self.actionMachine_Twin_active.setObjectName("actionMachine_Twin_active")
        self.actionMachine_Twin_active.triggered.connect(self.Machine_Twin_Active_Function)
        #self.actionOpen = QtWidgets.QAction(MainWindow)
        #self.actionOpen.setObjectName("actionOpen")
        #self.actionOpen.triggered.connect(self.editor)
        self.menuApplication_and_Service.addAction(self.actionInstall)
        self.menuOperation_and_Maintenance.addAction(self.actionInstall_2)
        self.menuNotifier.addAction(self.actionInstall_3)
        self.menuMachine_Twin.addAction(self.actionInstall_4)
        self.menuApplication_and_Service.addAction(self.actionDelete)
        self.menuOperation_and_Maintenance.addAction(self.actionDelete_2)
        self.menuNotifier.addAction(self.actionDelete_3)
        self.menuMachine_Twin.addAction(self.actionDelete_4)
        self.menuCustom_Function_Install.addAction(self.menuApplication_and_Service.menuAction())
        self.menuCustom_Function_Install.addAction(self.menuOperation_and_Maintenance.menuAction())
        self.menuCustom_Function_Install.addAction(self.menuNotifier.menuAction())
        self.menuCustom_Function_Install.addAction(self.menuMachine_Twin.menuAction())
        self.menuActive_Function_Initialization.addAction(self.actionApp_Serv_active)
        self.menuActive_Function_Initialization.addAction(self.actionOper_Main_active)
        self.menuActive_Function_Initialization.addAction(self.actionNotifier_Serv_active)
        self.menuActive_Function_Initialization.addAction(self.actionMachine_Twin_active)
        #self.menuOpen_Editor.addAction(self.actionOpen)
        self.menubar.addAction(self.menuCustom_Function_Install.menuAction())
        self.menubar.addAction(self.menuActive_Function_Initialization.menuAction())
        #self.menubar.addAction(self.menuOpen_Editor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.App_and_service_agent.setText(_translate("MainWindow", "Activate Application and Service Agent"))
        self.Oper_and_Main_Agent.setText(_translate("MainWindow", "Activate Operation and Maintanance Agent"))
        self.Notifier.setText(_translate("MainWindow", "Activate Notifier"))
        self.agent_button.setText(_translate("MainWindow", "Activate Twin"))
        self.Socket_dll.setText(_translate("MainWindow", "Establish Connection"))
        self.IP_address_machine_agent.setText(_translate("MainWindow", "IP Address : "))
        self.Port_No_machine_agent.setText(_translate("MainWindow", "Port No. : "))
        self.label.setText(_translate("MainWindow", "Machine HMI"))
        self.logs_window.setText(_translate("MainWindow", "Logs Window"))
        self.menuCustom_Function_Install.setTitle(_translate("MainWindow", "Custom Function Install"))
        self.menuApplication_and_Service.setTitle(_translate("MainWindow", "Application and Service"))
        self.menuOperation_and_Maintenance.setTitle(_translate("MainWindow", "Operation and Maintenance"))
        self.menuNotifier.setTitle(_translate("MainWindow", "Notifier"))
        self.menuActive_Function_Initialization.setTitle(_translate("MainWindow", "Active Function Initialization"))
        #self.menuOpen_Editor.setTitle(_translate("MainWindow", "Open Editor"))
        self.menuMachine_Twin.setTitle(_translate("MainWindow", "Machine_Twin"))
        self.actionApplication_and_Service.setText(_translate("MainWindow", "Application and Service"))
        self.actionO_M.setText(_translate("MainWindow", "Operation and Maintenance"))
        self.Install.setText(_translate("MainWindow", "Install"))
        self.actionInstall.setText(_translate("MainWindow", "Install"))
        self.actionInstall_2.setText(_translate("MainWindow", "Install"))
        self.actionInstall_3.setText(_translate("MainWindow", "Install"))
        self.actionInstall_4.setText(_translate("MainWindow", "Install"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_3.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_4.setText(_translate("MainWindow", "Delete"))
        self.actionApp_Serv_active.setText(_translate("MainWindow", "Application and Service"))
        self.actionOper_Main_active.setText(_translate("MainWindow", "Operation and Maintenance"))
        self.actionNotifier_Serv_active.setText(_translate("MainWindow", "Notifier Service"))
        self.actionMachine_Twin_active.setText(_translate("MainWindow", "Machine Twin"))
        #self.actionOpen.setText(_translate("MainWindow", "Open"))
        

    # Methods to execute functionalities in interface
    def app_and_service_click(self):
        # Write the functionalities that need to be executed here after pressing establish connection button
        self.logs_window.setText("Activating Application and Service Agent")
        self.worker1 = AppandSerAgent()
        self.worker1.start()

    def machine_initialization(self):
        # Provide Server Port Number and IP Address here
        port=self.lineEdit_server_port.text()
        ip_add=self.lineEdit_server_ip.text()
        self.logs_window.setText("Port No. for Twin Activation is : "+port+" and IP Address is : "+ip_add)
        with open(r'hmi_ip.txt', 'w') as f:
            line1 = port+"\n"
            line2 = ip_add
            f.writelines([line1, line2])
        self.worker = MachineTwin()
        self.worker.start()
    
    def Oper_and_Main_click(self):
        # Write the functionalities that need to be executed here after pressing establish connection button
        self.logs_window.setText("Activating Operation and Management Agent")
        self.worker2 = OperandMaintAgent()
        self.worker2.start()

    def notifier_click(self):
        # Write the functionalities that need to be executed here after pressing establish connection button
        self.logs_window.setText("Activating Notifier Agent")
        self.worker3 = NotifierManager()
        self.worker3.start()

    def socket_click(self):
        # Write the functionalities that need to be executed here after pressing establish connection button
        self.logs_window.setText("Establishing Connection through Socket_DLL via Win OMM")
        self.worker4 = EstablishConnection()
        self.worker4.start()

    def Application_and_Service_Install(self):
        self.logs_window.setText("Install Button Triggered : Please call functions to install in App&Serv Agent")
        self.worker5 = App_and_ser_function_install()
        self.worker5.start()
        
    def Operation_and_Management_Install(self):
        self.logs_window.setText("Install Button Triggered : Please call functions to install in Oper&Manag Agent")
        self.worker6 = Oper_and_Manag_function_install()
        self.worker6.start()
           
    def Notifier_Service_Install(self):
        self.logs_window.setText("Install Button Triggered : Please call functions to install in Notifier Service Agent")
        self.worker7 = NotifierManager_function_install()
        self.worker7.start()
        

    def Machine_Twin_Install(self):
        self.logs_window.setText("Install Button Triggered : Please call functions to install in Machine Twin Agent")
        self.worker8 = MachineTwin_function_install()
        self.worker8.start()

    def Application_and_Service_UnInstall(self):
        self.logs_window.setText("Delete Button Triggered : Please enter function file name to uninstall in App&Serv Agent")
        self.worker9 = App_and_ser_function_uninstall()
        self.worker9.start()
        
    def Operation_and_Management_UnInstall(self):
        self.logs_window.setText("Delete Button Triggered : Please enter function file name to uninstall in Oper&Manag Agent")
        self.worker10 = Oper_and_Manag_function_uninstall()
        self.worker10.start()
           
    def Notifier_Service_UnInstall(self):
        self.logs_window.setText("Delete Button Triggered : Please enter function file name to uninstall in Notifier Service Agent")
        self.worker11 = NotifierManager_function_uninstall()
        self.worker11.start()
        

    def Machine_Twin_UnInstall(self):
        self.logs_window.setText("Delete Button Triggered : Please enter function file name to uninstall in Machine Twin Agent")
        self.worker12 = MachineTwin_function_uninstall()
        self.worker12.start()

    def Application_and_Service_Active_Function(self):
        self.logs_window.setText("Please update the Active Functions list with 1 to activate function on separete thread")
        self.worker13 = App_Serv_active_function()
        self.worker13.start()

    def Operation_and_management_Active_Function(self):
        self.logs_window.setText("Please update the Active Functions list with 1 to activate function on separete thread")
        self.worker14 = Oper_Main_active_function()
        self.worker14.start()

    def Notifier_Service_Active_Function(self):
        self.logs_window.setText("Please update the Active Functions list with 1 to activate function on separete thread")
        self.worker15 = Notifier_Service_active_function()
        self.worker15.start()

    def Machine_Twin_Active_Function(self):
        self.logs_window.setText("Please update the Active Functions list with 1 to activate function on separete thread")
        self.worker16 = Machine_Twin_active_function()
        self.worker16.start()
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())