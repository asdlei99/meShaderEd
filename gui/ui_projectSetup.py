# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\ui_projectSetup.ui'
#
# Created: Sun Jun 17 14:36:24 2012
#      by: PyQt4 UI code generator snapshot-4.9.2-fa0ccc58c397
#
# WARNING! All changes made in this file will be lost!

from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore, QtGui

if not usePyQt5 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets

try:
		_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
		_fromUtf8 = lambda s: s

class Ui_ProjectSetup(object):
		def setupUi(self, ProjectSetup):
				ProjectSetup.setObjectName(_fromUtf8("ProjectSetup"))
				ProjectSetup.resize(426, 342)
				sizePolicy = QtModule.QSizePolicy(QtModule.QSizePolicy.Preferred, QtModule.QSizePolicy.Minimum)
				sizePolicy.setHorizontalStretch(1)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(ProjectSetup.sizePolicy().hasHeightForWidth())
				ProjectSetup.setSizePolicy(sizePolicy)
				ProjectSetup.setMinimumSize(QtCore.QSize(0, 0))
				ProjectSetup.setMaximumSize(QtCore.QSize(16777215, 16777215))
				ProjectSetup.setSizeGripEnabled(False)
				self.verticalLayout_3 = QtModule.QVBoxLayout(ProjectSetup)
				self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
				self.grp_project = QtModule.QGroupBox(ProjectSetup)
				sizePolicy = QtModule.QSizePolicy(QtModule.QSizePolicy.Preferred, QtModule.QSizePolicy.Fixed)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(self.grp_project.sizePolicy().hasHeightForWidth())
				self.grp_project.setSizePolicy(sizePolicy)
				self.grp_project.setMinimumSize(QtCore.QSize(0, 0))
				self.grp_project.setMaximumSize(QtCore.QSize(16777215, 16777215))
				self.grp_project.setObjectName(_fromUtf8("grp_project"))
				self.verticalLayout = QtModule.QVBoxLayout(self.grp_project)
				self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
				self.hl_project = QtModule.QHBoxLayout()
				self.hl_project.setObjectName(_fromUtf8("hl_project"))
				self.label_project = QtModule.QLabel(self.grp_project)
				self.label_project.setMinimumSize(QtCore.QSize(80, 0))
				self.label_project.setMaximumSize(QtCore.QSize(80, 16777215))
				self.label_project.setObjectName(_fromUtf8("label_project"))
				self.hl_project.addWidget(self.label_project)
				self.lineEdit_project = QtModule.QLineEdit(self.grp_project)
				self.lineEdit_project.setObjectName(_fromUtf8("lineEdit_project"))
				self.hl_project.addWidget(self.lineEdit_project)
				self.btn_project_dir = QtModule.QToolButton(self.grp_project)
				self.btn_project_dir.setObjectName(_fromUtf8("btn_project_dir"))
				self.hl_project.addWidget(self.btn_project_dir)
				self.hl_project.setStretch(1, 1)
				self.verticalLayout.addLayout(self.hl_project)
				self.verticalLayout_3.addWidget(self.grp_project)
				self.grp_shaders = QtModule.QGroupBox(ProjectSetup)
				sizePolicy = QtModule.QSizePolicy(QtModule.QSizePolicy.Preferred, QtModule.QSizePolicy.Fixed)
				sizePolicy.setHorizontalStretch(0)
				sizePolicy.setVerticalStretch(0)
				sizePolicy.setHeightForWidth(self.grp_shaders.sizePolicy().hasHeightForWidth())
				self.grp_shaders.setSizePolicy(sizePolicy)
				self.grp_shaders.setMinimumSize(QtCore.QSize(0, 0))
				self.grp_shaders.setMaximumSize(QtCore.QSize(16777215, 16777215))
				self.grp_shaders.setObjectName(_fromUtf8("grp_shaders"))
				self.verticalLayout_2 = QtModule.QVBoxLayout(self.grp_shaders)
				self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
				self.hl_shaders = QtModule.QHBoxLayout()
				self.hl_shaders.setObjectName(_fromUtf8("hl_shaders"))
				self.label_shaders = QtModule.QLabel(self.grp_shaders)
				self.label_shaders.setMinimumSize(QtCore.QSize(80, 0))
				self.label_shaders.setMaximumSize(QtCore.QSize(80, 16777215))
				self.label_shaders.setObjectName(_fromUtf8("label_shaders"))
				self.hl_shaders.addWidget(self.label_shaders)
				self.lineEdit_shaders = QtModule.QLineEdit(self.grp_shaders)
				self.lineEdit_shaders.setObjectName(_fromUtf8("lineEdit_shaders"))
				self.hl_shaders.addWidget(self.lineEdit_shaders)
				self.btn_shaders_dir = QtModule.QToolButton(self.grp_shaders)
				self.btn_shaders_dir.setObjectName(_fromUtf8("btn_shaders_dir"))
				self.hl_shaders.addWidget(self.btn_shaders_dir)
				self.verticalLayout_2.addLayout(self.hl_shaders)
				self.hl_network = QtModule.QHBoxLayout()
				self.hl_network.setObjectName(_fromUtf8("hl_network"))
				self.label_network = QtModule.QLabel(self.grp_shaders)
				self.label_network.setMinimumSize(QtCore.QSize(80, 0))
				self.label_network.setMaximumSize(QtCore.QSize(80, 16777215))
				self.label_network.setObjectName(_fromUtf8("label_network"))
				self.hl_network.addWidget(self.label_network)
				self.lineEdit_network = QtModule.QLineEdit(self.grp_shaders)
				self.lineEdit_network.setObjectName(_fromUtf8("lineEdit_network"))
				self.hl_network.addWidget(self.lineEdit_network)
				self.btn_network_dir = QtModule.QToolButton(self.grp_shaders)
				self.btn_network_dir.setObjectName(_fromUtf8("btn_network_dir"))
				self.hl_network.addWidget(self.btn_network_dir)
				self.verticalLayout_2.addLayout(self.hl_network)
				self.hl_sources = QtModule.QHBoxLayout()
				self.hl_sources.setObjectName(_fromUtf8("hl_sources"))
				self.label_sources = QtModule.QLabel(self.grp_shaders)
				self.label_sources.setMinimumSize(QtCore.QSize(80, 0))
				self.label_sources.setMaximumSize(QtCore.QSize(80, 16777215))
				self.label_sources.setObjectName(_fromUtf8("label_sources"))
				self.hl_sources.addWidget(self.label_sources)
				self.lineEdit_sources = QtModule.QLineEdit(self.grp_shaders)
				self.lineEdit_sources.setObjectName(_fromUtf8("lineEdit_sources"))
				self.hl_sources.addWidget(self.lineEdit_sources)
				self.btn_sources_dir = QtModule.QToolButton(self.grp_shaders)
				self.btn_sources_dir.setObjectName(_fromUtf8("btn_sources_dir"))
				self.hl_sources.addWidget(self.btn_sources_dir)
				self.verticalLayout_2.addLayout(self.hl_sources)
				self.hl_textures = QtModule.QHBoxLayout()
				self.hl_textures.setObjectName(_fromUtf8("hl_textures"))
				self.label_textures = QtModule.QLabel(self.grp_shaders)
				self.label_textures.setMinimumSize(QtCore.QSize(80, 0))
				self.label_textures.setMaximumSize(QtCore.QSize(80, 16777215))
				self.label_textures.setObjectName(_fromUtf8("label_textures"))
				self.hl_textures.addWidget(self.label_textures)
				self.lineEdit_textures = QtModule.QLineEdit(self.grp_shaders)
				self.lineEdit_textures.setObjectName(_fromUtf8("lineEdit_textures"))
				self.hl_textures.addWidget(self.lineEdit_textures)
				self.btn_textures_dir = QtModule.QToolButton(self.grp_shaders)
				self.btn_textures_dir.setObjectName(_fromUtf8("btn_textures_dir"))
				self.hl_textures.addWidget(self.btn_textures_dir)
				self.verticalLayout_2.addLayout(self.hl_textures)
				self.verticalLayout_3.addWidget(self.grp_shaders)
				spacerItem = QtModule.QSpacerItem(20, 20, QtModule.QSizePolicy.Minimum, QtModule.QSizePolicy.Expanding)
				self.verticalLayout_3.addItem(spacerItem)
				self.buttonBox = QtModule.QDialogButtonBox(ProjectSetup)
				self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
				self.buttonBox.setStandardButtons(QtModule.QDialogButtonBox.Cancel|QtModule.QDialogButtonBox.Ok)
				self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
				self.verticalLayout_3.addWidget(self.buttonBox)

				self.retranslateUi(ProjectSetup)
				if usePyQt4 :
					QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ProjectSetup.accept)
					QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProjectSetup.reject)
					QtCore.QObject.connect(self.btn_project_dir, QtCore.SIGNAL(_fromUtf8("clicked()")), ProjectSetup.onBrowseProjectDir)
					QtCore.QObject.connect(self.btn_network_dir, QtCore.SIGNAL(_fromUtf8("clicked()")), ProjectSetup.onBrowseNetworksDir)
					QtCore.QObject.connect(self.btn_shaders_dir, QtCore.SIGNAL(_fromUtf8("clicked()")), ProjectSetup.onBrowseShadersDir)
					QtCore.QObject.connect(self.btn_sources_dir, QtCore.SIGNAL(_fromUtf8("clicked()")), ProjectSetup.onBrowseSourcesDir)
					QtCore.QObject.connect(self.btn_textures_dir, QtCore.SIGNAL(_fromUtf8("clicked()")), ProjectSetup.onBrowseTexturesDir)
				else :
					self.buttonBox.accepted.connect( ProjectSetup.accept)
					self.buttonBox.rejected.connect( ProjectSetup.reject)
					self.btn_project_dir.clicked.connect( ProjectSetup.onBrowseProjectDir)
					self.btn_network_dir.clicked.connect( ProjectSetup.onBrowseNetworksDir)
					self.btn_shaders_dir.clicked.connect( ProjectSetup.onBrowseShadersDir)
					self.btn_sources_dir.clicked.connect( ProjectSetup.onBrowseSourcesDir)
					self.btn_textures_dir.clicked.connect( ProjectSetup.onBrowseTexturesDir)
					
				QtCore.QMetaObject.connectSlotsByName(ProjectSetup)

		def retranslateUi(self, ProjectSetup):
			ProjectSetup.setWindowTitle(QtModule.QApplication.translate("ProjectSetup", "Project Setup", None))
			self.grp_project.setTitle(QtModule.QApplication.translate("ProjectSetup", "Project", None))
			self.label_project.setText(QtModule.QApplication.translate("ProjectSetup", "Root", None))
			self.btn_project_dir.setText(QtModule.QApplication.translate("ProjectSetup", "...", None))
			self.grp_shaders.setTitle(QtModule.QApplication.translate("ProjectSetup", "Resources", None))
			self.label_shaders.setText(QtModule.QApplication.translate("ProjectSetup", "Shaders", None))
			self.btn_shaders_dir.setText(QtModule.QApplication.translate("ProjectSetup", "...", None))
			self.label_network.setText(QtModule.QApplication.translate("ProjectSetup", "Networks", None))
			self.btn_network_dir.setText(QtModule.QApplication.translate("ProjectSetup", "...", None))
			self.label_sources.setText(QtModule.QApplication.translate("ProjectSetup", "Sources", None))
			self.btn_sources_dir.setText(QtModule.QApplication.translate("ProjectSetup", "...", None))
			self.label_textures.setText(QtModule.QApplication.translate("ProjectSetup", "Textures", None))
			self.btn_textures_dir.setText(QtModule.QApplication.translate("ProjectSetup", "...", None))

