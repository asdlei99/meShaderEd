# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_nodeParamEditor.ui'
#
# Created: Wed Oct 03 14:19:58 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NodeParamEditor(object):
    def setupUi(self, NodeParamEditor):
        NodeParamEditor.setObjectName(_fromUtf8("NodeParamEditor"))
        NodeParamEditor.resize(714, 611)
        self.verticalLayout = QtGui.QVBoxLayout(NodeParamEditor)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.name_label = QtGui.QLabel(NodeParamEditor)
        self.name_label.setMinimumSize(QtCore.QSize(100, 0))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.horizontalLayout_2.addWidget(self.name_label)
        self.name_lineEdit = QtGui.QLineEdit(NodeParamEditor)
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.horizontalLayout_2.addWidget(self.name_lineEdit)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_label = QtGui.QLabel(NodeParamEditor)
        self.label_label.setMinimumSize(QtCore.QSize(100, 0))
        self.label_label.setObjectName(_fromUtf8("label_label"))
        self.horizontalLayout_3.addWidget(self.label_label)
        self.label_lineEdit = QtGui.QLineEdit(NodeParamEditor)
        self.label_lineEdit.setObjectName(_fromUtf8("label_lineEdit"))
        self.horizontalLayout_3.addWidget(self.label_lineEdit)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.display_label = QtGui.QLabel(NodeParamEditor)
        self.display_label.setMinimumSize(QtCore.QSize(100, 0))
        self.display_label.setObjectName(_fromUtf8("display_label"))
        self.horizontalLayout_5.addWidget(self.display_label)
        self.check_display = QtGui.QCheckBox(NodeParamEditor)
        self.check_display.setText(_fromUtf8(""))
        self.check_display.setObjectName(_fromUtf8("check_display"))
        self.horizontalLayout_5.addWidget(self.check_display)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.shader_label = QtGui.QLabel(NodeParamEditor)
        self.shader_label.setMinimumSize(QtCore.QSize(100, 0))
        self.shader_label.setObjectName(_fromUtf8("shader_label"))
        self.horizontalLayout_6.addWidget(self.shader_label)
        self.check_shader = QtGui.QCheckBox(NodeParamEditor)
        self.check_shader.setText(_fromUtf8(""))
        self.check_shader.setObjectName(_fromUtf8("check_shader"))
        self.horizontalLayout_6.addWidget(self.check_shader)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.type_label = QtGui.QLabel(NodeParamEditor)
        self.type_label.setMinimumSize(QtCore.QSize(100, 0))
        self.type_label.setObjectName(_fromUtf8("type_label"))
        self.horizontalLayout_7.addWidget(self.type_label)
        self.type_comboBox = QtGui.QComboBox(NodeParamEditor)
        self.type_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.type_comboBox.setObjectName(_fromUtf8("type_comboBox"))
        self.horizontalLayout_7.addWidget(self.type_comboBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.detail_label = QtGui.QLabel(NodeParamEditor)
        self.detail_label.setMinimumSize(QtCore.QSize(100, 0))
        self.detail_label.setObjectName(_fromUtf8("detail_label"))
        self.horizontalLayout_8.addWidget(self.detail_label)
        self.detail_comboBox = QtGui.QComboBox(NodeParamEditor)
        self.detail_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.detail_comboBox.setObjectName(_fromUtf8("detail_comboBox"))
        self.horizontalLayout_8.addWidget(self.detail_comboBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.provider_label_2 = QtGui.QLabel(NodeParamEditor)
        self.provider_label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.provider_label_2.setObjectName(_fromUtf8("provider_label_2"))
        self.horizontalLayout_11.addWidget(self.provider_label_2)
        self.provider_comboBox = QtGui.QComboBox(NodeParamEditor)
        self.provider_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.provider_comboBox.setObjectName(_fromUtf8("provider_comboBox"))
        self.horizontalLayout_11.addWidget(self.provider_comboBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.subtype_label = QtGui.QLabel(NodeParamEditor)
        self.subtype_label.setMinimumSize(QtCore.QSize(100, 0))
        self.subtype_label.setObjectName(_fromUtf8("subtype_label"))
        self.horizontalLayout_9.addWidget(self.subtype_label)
        self.subtype_comboBox = QtGui.QComboBox(NodeParamEditor)
        self.subtype_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.subtype_comboBox.setObjectName(_fromUtf8("subtype_comboBox"))
        self.horizontalLayout_9.addWidget(self.subtype_comboBox)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.range_label = QtGui.QLabel(NodeParamEditor)
        self.range_label.setMinimumSize(QtCore.QSize(100, 0))
        self.range_label.setObjectName(_fromUtf8("range_label"))
        self.horizontalLayout_10.addWidget(self.range_label)
        self.range_lineEdit = QtGui.QLineEdit(NodeParamEditor)
        self.range_lineEdit.setObjectName(_fromUtf8("range_lineEdit"))
        self.horizontalLayout_10.addWidget(self.range_lineEdit)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.value_stackedWidget = QtGui.QStackedWidget(NodeParamEditor)
        self.value_stackedWidget.setObjectName(_fromUtf8("value_stackedWidget"))
        self.value_stackedWidgetPage1 = QtGui.QWidget()
        self.value_stackedWidgetPage1.setObjectName(_fromUtf8("value_stackedWidgetPage1"))
        self.value_stackedWidget.addWidget(self.value_stackedWidgetPage1)
        self.verticalLayout.addWidget(self.value_stackedWidget)
        spacerItem6 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.descr_label = QtGui.QLabel(NodeParamEditor)
        self.descr_label.setMinimumSize(QtCore.QSize(100, 0))
        self.descr_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descr_label.setObjectName(_fromUtf8("descr_label"))
        self.horizontalLayout_4.addWidget(self.descr_label)
        self.descr_plainTextEdit = QtGui.QPlainTextEdit(NodeParamEditor)
        self.descr_plainTextEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.descr_plainTextEdit.setObjectName(_fromUtf8("descr_plainTextEdit"))
        self.horizontalLayout_4.addWidget(self.descr_plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(NodeParamEditor)
        QtCore.QMetaObject.connectSlotsByName(NodeParamEditor)

    def retranslateUi(self, NodeParamEditor):
        NodeParamEditor.setWindowTitle(QtGui.QApplication.translate("NodeParamEditor", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.display_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.shader_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Use in Shader", None, QtGui.QApplication.UnicodeUTF8))
        self.type_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.detail_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.provider_label_2.setText(QtGui.QApplication.translate("NodeParamEditor", "Provider", None, QtGui.QApplication.UnicodeUTF8))
        self.subtype_label.setText(QtGui.QApplication.translate("NodeParamEditor", "GUI Subtype", None, QtGui.QApplication.UnicodeUTF8))
        self.range_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.descr_label.setText(QtGui.QApplication.translate("NodeParamEditor", "Description", None, QtGui.QApplication.UnicodeUTF8))

