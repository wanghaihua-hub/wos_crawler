# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_crawler.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonJournal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJournal.setEnabled(False)
        self.pushButtonJournal.setGeometry(QtCore.QRect(360, 30, 99, 28))
        self.pushButtonJournal.setObjectName("pushButtonJournal")
        self.pushButtonStartCrawler = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartCrawler.setEnabled(False)
        self.pushButtonStartCrawler.setGeometry(QtCore.QRect(180, 190, 99, 28))
        self.pushButtonStartCrawler.setObjectName("pushButtonStartCrawler")
        self.pushButtonJournalOutputPath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJournalOutputPath.setEnabled(True)
        self.pushButtonJournalOutputPath.setGeometry(QtCore.QRect(360, 140, 99, 28))
        self.pushButtonJournalOutputPath.setObjectName("pushButtonJournalOutputPath")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 11, 331, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonJournal = QtWidgets.QRadioButton(self.widget)
        self.radioButtonJournal.setObjectName("radioButtonJournal")
        self.verticalLayout.addWidget(self.radioButtonJournal)
        self.lineEditJournal = QtWidgets.QLineEdit(self.widget)
        self.lineEditJournal.setEnabled(False)
        self.lineEditJournal.setReadOnly(False)
        self.lineEditJournal.setObjectName("lineEditJournal")
        self.verticalLayout.addWidget(self.lineEditJournal)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonQuery = QtWidgets.QRadioButton(self.widget)
        self.radioButtonQuery.setChecked(True)
        self.radioButtonQuery.setObjectName("radioButtonQuery")
        self.verticalLayout_2.addWidget(self.radioButtonQuery)
        self.lineEditQuery = QtWidgets.QLineEdit(self.widget)
        self.lineEditQuery.setObjectName("lineEditQuery")
        self.verticalLayout_2.addWidget(self.lineEditQuery)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelOutputPath = QtWidgets.QLabel(self.widget)
        self.labelOutputPath.setObjectName("labelOutputPath")
        self.verticalLayout_4.addWidget(self.labelOutputPath)
        self.lineEditOutputPath = QtWidgets.QLineEdit(self.widget)
        self.lineEditOutputPath.setObjectName("lineEditOutputPath")
        self.verticalLayout_4.addWidget(self.lineEditOutputPath)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWeb_of_Science = QtWidgets.QAction(MainWindow)
        self.actionWeb_of_Science.setObjectName("actionWeb_of_Science")
        self.actionCNKI = QtWidgets.QAction(MainWindow)
        self.actionCNKI.setObjectName("actionCNKI")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web of Science Crawler"))
        self.pushButtonJournal.setText(_translate("MainWindow", "选择期刊列表"))
        self.pushButtonStartCrawler.setText(_translate("MainWindow", "开始爬取"))
        self.pushButtonJournalOutputPath.setText(_translate("MainWindow", "选择保存路径"))
        self.radioButtonJournal.setText(_translate("MainWindow", "期刊列表爬取"))
        self.radioButtonQuery.setText(_translate("MainWindow", "高级检索式爬取"))
        self.labelOutputPath.setText(_translate("MainWindow", "保存路径"))
        self.actionWeb_of_Science.setText(_translate("MainWindow", "Web of Science"))
        self.actionCNKI.setText(_translate("MainWindow", "CNKI"))
