# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/tmp/tmpCPhivc.ui'
#
# Created: Wed Jan 16 09:11:13 2013
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CurveStatsDialog(object):
    def setupUi(self, CurveStatsDialog):
        CurveStatsDialog.setObjectName("CurveStatsDialog")
        CurveStatsDialog.resize(723, 382)
        self.gridLayout_2 = QtGui.QGridLayout(CurveStatsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(CurveStatsDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minCB = QtGui.QCheckBox(self.groupBox)
        self.minCB.setObjectName("minCB")
        self.horizontalLayout.addWidget(self.minCB)
        self.minSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.minSB.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minSB.sizePolicy().hasHeightForWidth())
        self.minSB.setSizePolicy(sizePolicy)
        self.minSB.setDecimals(5)
        self.minSB.setObjectName("minSB")
        self.horizontalLayout.addWidget(self.minSB)
        self.minDTE = QtGui.QDateTimeEdit(self.groupBox)
        self.minDTE.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minDTE.sizePolicy().hasHeightForWidth())
        self.minDTE.setSizePolicy(sizePolicy)
        self.minDTE.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.minDTE.setObjectName("minDTE")
        self.horizontalLayout.addWidget(self.minDTE)
        self.selectMinPB = QtGui.QToolButton(self.groupBox)
        self.selectMinPB.setEnabled(True)
        self.selectMinPB.setObjectName("selectMinPB")
        self.horizontalLayout.addWidget(self.selectMinPB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.maxCB = QtGui.QCheckBox(self.groupBox)
        self.maxCB.setObjectName("maxCB")
        self.horizontalLayout_2.addWidget(self.maxCB)
        self.maxSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.maxSB.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSB.sizePolicy().hasHeightForWidth())
        self.maxSB.setSizePolicy(sizePolicy)
        self.maxSB.setDecimals(5)
        self.maxSB.setObjectName("maxSB")
        self.horizontalLayout_2.addWidget(self.maxSB)
        self.maxDTE = QtGui.QDateTimeEdit(self.groupBox)
        self.maxDTE.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxDTE.sizePolicy().hasHeightForWidth())
        self.maxDTE.setSizePolicy(sizePolicy)
        self.maxDTE.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.maxDTE.setObjectName("maxDTE")
        self.horizontalLayout_2.addWidget(self.maxDTE)
        self.selectMaxPB = QtGui.QToolButton(self.groupBox)
        self.selectMaxPB.setEnabled(True)
        self.selectMaxPB.setObjectName("selectMaxPB")
        self.horizontalLayout_2.addWidget(self.selectMaxPB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(CurveStatsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.npointsStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.npointsStatCB.setChecked(True)
        self.npointsStatCB.setObjectName("npointsStatCB")
        self.gridLayout.addWidget(self.npointsStatCB, 0, 0, 1, 1)
        self.minStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.minStatCB.setChecked(True)
        self.minStatCB.setObjectName("minStatCB")
        self.gridLayout.addWidget(self.minStatCB, 0, 1, 1, 1)
        self.stdStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.stdStatCB.setChecked(True)
        self.stdStatCB.setObjectName("stdStatCB")
        self.gridLayout.addWidget(self.stdStatCB, 0, 2, 1, 1)
        self.meanStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.meanStatCB.setChecked(True)
        self.meanStatCB.setObjectName("meanStatCB")
        self.gridLayout.addWidget(self.meanStatCB, 1, 0, 1, 1)
        self.maxStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.maxStatCB.setChecked(True)
        self.maxStatCB.setObjectName("maxStatCB")
        self.gridLayout.addWidget(self.maxStatCB, 1, 1, 1, 1)
        self.rmsStatCB = QtGui.QCheckBox(self.groupBox_2)
        self.rmsStatCB.setChecked(True)
        self.rmsStatCB.setObjectName("rmsStatCB")
        self.gridLayout.addWidget(self.rmsStatCB, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.statsTW = QtGui.QTableWidget(CurveStatsDialog)
        self.statsTW.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.statsTW.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.statsTW.setObjectName("statsTW")
        self.statsTW.setColumnCount(0)
        self.statsTW.setRowCount(0)
        self.gridLayout_2.addWidget(self.statsTW, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.calculatePB = QtGui.QPushButton(CurveStatsDialog)
        self.calculatePB.setObjectName("calculatePB")
        self.horizontalLayout_4.addWidget(self.calculatePB)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)

        self.retranslateUi(CurveStatsDialog)
        QtCore.QObject.connect(self.minCB, QtCore.SIGNAL("toggled(bool)"), self.minSB.setEnabled)
        QtCore.QObject.connect(self.minCB, QtCore.SIGNAL("toggled(bool)"), self.minDTE.setEnabled)
        QtCore.QObject.connect(self.maxCB, QtCore.SIGNAL("toggled(bool)"), self.maxSB.setEnabled)
        QtCore.QObject.connect(self.maxCB, QtCore.SIGNAL("toggled(bool)"), self.maxDTE.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(CurveStatsDialog)

    def retranslateUi(self, CurveStatsDialog):
        CurveStatsDialog.setWindowTitle(QtGui.QApplication.translate("CurveStatsDialog", "Curve Stats Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CurveStatsDialog", "X limits", None, QtGui.QApplication.UnicodeUTF8))
        self.minCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.minDTE.setDisplayFormat(QtGui.QApplication.translate("CurveStatsDialog", "yyyy-MM-ddThh:mm:ss.zzz", None, QtGui.QApplication.UnicodeUTF8))
        self.selectMinPB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "Select from plot", None, QtGui.QApplication.UnicodeUTF8))
        self.selectMinPB.setText(QtGui.QApplication.translate("CurveStatsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "max", None, QtGui.QApplication.UnicodeUTF8))
        self.maxDTE.setDisplayFormat(QtGui.QApplication.translate("CurveStatsDialog", "yyyy-MM-ddThh:mm:ss.zzz", None, QtGui.QApplication.UnicodeUTF8))
        self.selectMaxPB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "Select from plot", None, QtGui.QApplication.UnicodeUTF8))
        self.selectMaxPB.setText(QtGui.QApplication.translate("CurveStatsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CurveStatsDialog", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.npointsStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "Number of points considered for the statistical analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.npointsStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "#points", None, QtGui.QApplication.UnicodeUTF8))
        self.minStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "x and y values for the minimum of the curve in the considered range", None, QtGui.QApplication.UnicodeUTF8))
        self.minStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.stdStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "biased standard deviation:\n"
"std = sqrt(mean(abs(y - y.mean())**2))", None, QtGui.QApplication.UnicodeUTF8))
        self.stdStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "std", None, QtGui.QApplication.UnicodeUTF8))
        self.meanStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "arithmetic mean", None, QtGui.QApplication.UnicodeUTF8))
        self.meanStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.maxStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "x and y values for the maximum of the curve in the considered range", None, QtGui.QApplication.UnicodeUTF8))
        self.maxStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "max", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsStatCB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "Root Mean Square:\n"
"rms=sqrt(mean(y**2))", None, QtGui.QApplication.UnicodeUTF8))
        self.rmsStatCB.setText(QtGui.QApplication.translate("CurveStatsDialog", "rms", None, QtGui.QApplication.UnicodeUTF8))
        self.statsTW.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "select the curve names for which statistics will be calculated", None, QtGui.QApplication.UnicodeUTF8))
        self.calculatePB.setToolTip(QtGui.QApplication.translate("CurveStatsDialog", "(re) calculate statistics for the selected curves (or for all curves if None is selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.calculatePB.setText(QtGui.QApplication.translate("CurveStatsDialog", "(re)calculate", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CurveStatsDialog = QtGui.QDialog()
    ui = Ui_CurveStatsDialog()
    ui.setupUi(CurveStatsDialog)
    CurveStatsDialog.show()
    sys.exit(app.exec_())
