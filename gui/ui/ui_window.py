# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 549)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 110, 229, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(810, 180, 121, 21))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 220, 291, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 180, 67, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 300, 111, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(640, 220, 260, 260))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 110, 151, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget_3)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(40)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 160, 111, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 150, 111, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 180, 131, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(760, 180, 134, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_manuals = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manuals.setGeometry(QtCore.QRect(810, 110, 89, 31))
        self.btn_manuals.setObjectName("btn_manuals")
        self.btn_crop_face = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crop_face.setGeometry(QtCore.QRect(60, 390, 111, 25))
        self.btn_crop_face.setObjectName("btn_crop_face")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 330, 109, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 270, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 450, 109, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.btn_capture = QtWidgets.QPushButton(self.centralwidget)
        self.btn_capture.setGeometry(QtCore.QRect(60, 330, 111, 25))
        self.btn_capture.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_capture.setObjectName("btn_capture")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionManuals = QtWidgets.QAction(MainWindow)
        self.actionManuals.setObjectName("actionManuals")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDraw_Clear = QtWidgets.QAction(MainWindow)
        self.actionDraw_Clear.setObjectName("actionDraw_Clear")
        self.actionCrop_Face = QtWidgets.QAction(MainWindow)
        self.actionCrop_Face.setObjectName("actionCrop_Face")
        self.actionRandom = QtWidgets.QAction(MainWindow)
        self.actionRandom.setObjectName("actionRandom")
        self.actionFill = QtWidgets.QAction(MainWindow)
        self.actionFill.setObjectName("actionFill")
        self.actionOriginal_Output = QtWidgets.QAction(MainWindow)
        self.actionOriginal_Output.setObjectName("actionOriginal_Output")
        self.actioncapture = QtWidgets.QAction(MainWindow)
        self.actioncapture.setObjectName("actioncapture")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actioncapture)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuHelp.addAction(self.actionDraw_Clear)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionRandom)
        self.menuHelp.addAction(self.actionCrop_Face)
        self.menuHelp.addAction(self.actionFill)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionOriginal_Output)
        self.menuHelp_2.addAction(self.actionManuals)
        self.menuHelp_2.addSeparator()
        self.menuHelp_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pluralistic Image Completion"))
        self.label_3.setText(_translate("MainWindow", "Options:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "CelebA-HQ-center"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Paris-center"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ImageNet-center"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Places2-center"))
        self.comboBox.setItemText(5, _translate("MainWindow", "CelebA-HQ-random"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Paris-random"))
        self.comboBox.setItemText(7, _translate("MainWindow", "ImageNet-random"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Places2-random"))
        self.label.setText(_translate("MainWindow", "Pluralistic Image Completion"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Score:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Input:"))
        self.pushButton.setText(_translate("MainWindow", "load"))
        self.label_2.setText(_translate("MainWindow", "Bush Width:"))
        self.radioButton.setText(_translate("MainWindow", "free-form"))
        self.radioButton_2.setText(_translate("MainWindow", "rectangle"))
        self.pushButton_5.setText(_translate("MainWindow", "draw/clear"))
        self.pushButton_6.setText(_translate("MainWindow", "Original/Output"))
        self.btn_manuals.setText(_translate("MainWindow", "Manuals"))
        self.btn_crop_face.setText(_translate("MainWindow", "crop face"))
        self.pushButton_3.setText(_translate("MainWindow", "Fill -->"))
        self.pushButton_2.setText(_translate("MainWindow", "random"))
        self.pushButton_4.setText(_translate("MainWindow", "save"))
        self.btn_capture.setText(_translate("MainWindow", "capture"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Edit"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "&Help"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.actionManuals.setText(_translate("MainWindow", "&Manuals"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionDraw_Clear.setText(_translate("MainWindow", "&Draw/Clear"))
        self.actionCrop_Face.setText(_translate("MainWindow", "&Crop Face"))
        self.actionRandom.setText(_translate("MainWindow", "&Random"))
        self.actionFill.setText(_translate("MainWindow", "&Fill"))
        self.actionOriginal_Output.setText(_translate("MainWindow", "&Original/Output"))
        self.actioncapture.setText(_translate("MainWindow", "&Capture"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
