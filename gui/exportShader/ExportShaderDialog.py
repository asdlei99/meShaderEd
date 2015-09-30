"""
 ExportShaderDialog.py

 ver. 1.0.0
 Author: Yuri Meshalkin (aka mesh) (yuri.meshalkin@gmail.com)
 
 Dialog for export node as SL shader 

""" 
from core.mePyQt import QtCore, QtGui
from core.signal import Signal
#from PyQt4.QtCore import QVariant

from core.meCommon import *
from global_vars import app_global_vars, DEBUG_MODE

import gui.ui_settings as UI
from gui.ViewComputedCodeDialog import ViewComputedCodeDialog

from core.node import Node

from ui_exportShaderDialog import Ui_ExportShaderDialog

if QtCore.QT_VERSION < 0x50000 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets
#
# ExportShaderDialog
#
class ExportShaderDialog ( QtModule.QDialog ) :
	#
	# __init__
	#
	def __init__ ( self, node ) :
		#
		QtModule.QDialog.__init__ ( self )
		
		self.editNode = node
		self.computed_code = None

		self.buildGui ()
		
		# !!!!!
		# temporary disable NodeParamEditor param name field
		# because after param name changing, shader code also have to be changed 
		# !!!!!
		self.ui.param.ui.name_lineEdit.setEnabled ( False )
		
		self.connectSignals ()
		
		self.ui.btn_view.setDefault ( False )
		self.ui.chk_save_changes.setEnabled ( False ) # !!! temporary all changes to nodes are saved
	#
	# connectSignals
	#
	def connectSignals ( self ) :
		# QtCore.QObject
		if QtCore.QT_VERSION < 0x50000 :
			QtCore.QObject.connect ( self.ui.list_nodes, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onNodeChanged ) 
			QtCore.QObject.connect ( self.ui.list_inputs, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onInputParamChanged )
			QtCore.QObject.connect ( self.ui.list_outputs, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onOutputParamChanged )
			QtCore.QObject.connect ( self.ui.node, QtCore.SIGNAL ( 'changeNodeLabel' ), self.onRenameNodeLabel )
			
			QtCore.QObject.connect ( self.ui.param, QtCore.SIGNAL ( 'changeParamLabel' ), self.onParamChange )
			QtCore.QObject.connect ( self.ui.param, QtCore.SIGNAL ( 'changeParamIsShader' ), self.onParamChange )
			QtCore.QObject.connect ( self.ui.param, QtCore.SIGNAL ( 'changeParamDetail' ), self.onParamChange )
			QtCore.QObject.connect ( self.ui.param, QtCore.SIGNAL ( 'changeParamProvider' ), self.onParamChange )
			QtCore.QObject.connect ( self.ui.param, QtCore.SIGNAL ( 'changeParamValue' ), self.onParamChange )
		else :
			self.ui.list_nodes.itemSelectionChanged.connect ( self.onNodeChanged ) 
			self.ui.list_inputs.itemSelectionChanged.connect ( self.onInputParamChanged )
			self.ui.list_outputs.itemSelectionChanged.connect ( self.onOutputParamChanged )
			
			self.ui.node.changeNodeLabel.connect ( self.onRenameNodeLabel )
			self.ui.param.changeParamLabel.connect ( self.onParamChange )
			self.ui.param.changeParamIsShader.connect ( self.onParamChange )
			self.ui.param.changeParamDetail.connect ( self.onParamChange )
			self.ui.param.changeParamProvider.connect ( self.onParamChange )
			self.ui.param.changeParamValue.connect ( self.onParamChange )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self ) :
		#
		if QtCore.QT_VERSION < 0x50000 :
			QtCore.QObject.disconnect ( self.ui.list_nodes, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onNodeChanged )
			QtCore.QObject.disconnect ( self.ui.list_inputs, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onInputParamChanged )
			QtCore.QObject.disconnect ( self.ui.list_outputs, QtCore.SIGNAL ( 'itemSelectionChanged()' ), self.onOutputParamChanged )
			
			QtCore.QObject.disconnect ( self.ui.node, QtCore.SIGNAL ( 'changeNodeLabel' ), self.onRenameNodeLabel )
			QtCore.QObject.disconnect ( self.ui.param, QtCore.SIGNAL ( 'changeParamLabel' ), self.onParamChange )
			QtCore.QObject.disconnect ( self.ui.param, QtCore.SIGNAL ( 'changeParamIsShader' ), self.onParamChange )
			QtCore.QObject.disconnect ( self.ui.param, QtCore.SIGNAL ( 'changeParamDetail' ), self.onParamChange )
			QtCore.QObject.disconnect ( self.ui.param, QtCore.SIGNAL ( 'changeParamProvider' ), self.onParamChange ) 
			QtCore.QObject.disconnect ( self.ui.param, QtCore.SIGNAL ( 'changeParamValue' ), self.onParamChange )
		else :
			self.ui.list_nodes.itemSelectionChanged.disconnect ( self.onNodeChanged ) 
			self.ui.list_inputs.itemSelectionChanged.disconnect ( self.onInputParamChanged )
			self.ui.list_outputs.itemSelectionChanged.disconnect ( self.onOutputParamChanged )
			
			self.ui.node.changeNodeLabel.disconnect ( self.onRenameNodeLabel )
			self.ui.param.changeParamLabel.disconnect ( self.onParamChange )
			self.ui.param.changeParamIsShader.disconnect ( self.onParamChange )
			self.ui.param.changeParamDetail.disconnect ( self.onParamChange )
			self.ui.param.changeParamProvider.disconnect ( self.onParamChange )
			self.ui.param.changeParamValue.disconnect ( self.onParamChange )
	#
	# buildGui
	#
	def buildGui ( self ) :
		# build the gui created with QtDesigner
		self.ui = Ui_ExportShaderDialog ()
		self.ui.setupUi ( self ) 
		if self.editNode is not None :
			#
			self.setWindowTitle ( 'ExportShader: %s (%s)' % ( self.editNode.label, self.editNode.name ) ) 
			
			separator = QtModule.QListWidgetItem ( '---- exported shader ----' )
			separator.setFlags ( QtCore.Qt.NoItemFlags )
			self.ui.list_nodes.addItem ( separator )
			
			item = QtModule.QListWidgetItem ( self.editNode.label )
			node_var = QtCore.QVariant ( self.editNode )
			item.setData ( QtCore.Qt.UserRole + 1, node_var  )
			self.ui.list_nodes.addItem ( item )

			separator = QtModule.QListWidgetItem ( '---- connected nodes ----' )
			separator.setFlags ( QtCore.Qt.NoItemFlags )
			self.ui.list_nodes.addItem ( separator )

			#childrenList = []
			#childrenList = self.editNode.getChildrenList ( childrenList )
			self.computed_code = self.editNode.getComputedCode ( CodeOnly = True )
			print '*** (%s) children list: ' % self.editNode.label
			for node in self.editNode.visitedNodes : #childrenList :
				print '* (%s)' % node.label
				item = QtModule.QListWidgetItem ( node.label )
				item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( node ) )
				self.ui.list_nodes.addItem ( item )
	#
	# updateComputedParams
	#
	def updateComputedParams ( self ) :
		#
		self.ui.list_inputs.clear ()
		self.ui.list_outputs.clear ()
		self.computed_code = self.editNode.getComputedCode ( CodeOnly = True )
		# setup input params list
		for ( param, node ) in self.editNode.computedInputParamsList :
			item = QtModule.QListWidgetItem ( ( node.getParamDeclaration ( param )).rstrip ( ';\n' ) )
			item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
			item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
			self.ui.list_inputs.addItem ( item )
		# setup output params list
		for ( param, node ) in self.editNode.computedOutputParamsList :
			item = QtModule.QListWidgetItem ( ( 'output ' + node.getParamDeclaration ( param ) ).rstrip ( ';\n' ) )
			item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
			item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
			self.ui.list_outputs.addItem ( item )
	#
	# updateNodeParams
	#
	def updateNodeParams ( self, node ) :
		#
		self.ui.list_inputs.clear ()
		self.ui.list_outputs.clear ()
		
		linkedFont = QtGui.QFont ()
		linkedFont.setItalic ( True )
		linkedBrush = QtGui.QBrush ()
		linkedBrush.setColor ( QtCore.Qt.blue )
		# setup input params list
		for param in node.inputParams :
			item = QtModule.QListWidgetItem ( param.label )
			item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
			item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
			if node.isInputParamLinked ( param ) :
				item.setFont ( linkedFont )
				item.setForeground ( linkedBrush )
			self.ui.list_inputs.addItem ( item )
		# setup output params list
		for param in node.outputParams :
			item = QtModule.QListWidgetItem ( param.label )
			item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
			item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
			if node.isOutputParamLinked ( param ) :
				item.setFont ( linkedFont )
				item.setForeground ( linkedBrush )
			self.ui.list_outputs.addItem ( item )
	#
	# onNodeChanged
	#
	def onNodeChanged ( self ) :
		#  
		if DEBUG_MODE : print '>> ExportShaderDialog.onNodeChanged'
		self.disconnectSignals ()
		item = self.ui.list_nodes.currentItem ()
		if QtCore.QT_VERSION < 0x50000 : 
			node = item.data ( QtCore.Qt.UserRole + 1 ).toPyObject ()
		else :
			node = item.data ( QtCore.Qt.UserRole + 1 )
		print '* (%s) selected' % node.label
		self.ui.node.setNode ( node )
		self.ui.prop_tabWidget.setCurrentIndex ( 0 )

		if self.ui.list_nodes.currentRow () != 1 :
			self.updateNodeParams ( node )
			self.ui.list_inputs.clear ()
			self.ui.list_outputs.clear ()
			
			linkedFont = QtGui.QFont ()
			linkedFont.setItalic ( True )
			linkedBrush = QtGui.QBrush ()
			linkedBrush.setColor ( QtCore.Qt.blue )
			# setup input params list
			for param in node.inputParams :
				item = QtModule.QListWidgetItem ( param.label )
				item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
				item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
				if node.isInputParamLinked ( param ) :
					item.setFont ( linkedFont )
					item.setForeground ( linkedBrush )
				self.ui.list_inputs.addItem ( item )
			
			# setup output params list
			for param in node.outputParams :
				item = QtModule.QListWidgetItem ( param.label )
				item.setData ( QtCore.Qt.UserRole + 1, QtCore.QVariant ( param ) )
				item.setData ( QtCore.Qt.UserRole + 2, QtCore.QVariant ( node ) )
				if node.isOutputParamLinked ( param ) :
					item.setFont ( linkedFont )
					item.setForeground ( linkedBrush )
				self.ui.list_outputs.addItem ( item )
		else :
			self.updateComputedParams ()
			
		self.connectSignals ()
	#
	# onInputParamChanged
	#
	def onInputParamChanged ( self ) :
		#  
		if DEBUG_MODE : print '>> ExportShaderDialog.onInputParamChanged'
		item = self.ui.list_inputs.currentItem ()
		if QtCore.QT_VERSION < 0x50000 :  
			param = item.data ( QtCore.Qt.UserRole + 1 ).toPyObject ()
			node = item.data ( QtCore.Qt.UserRole + 2 ).toPyObject ()
		else :
			param = item.data ( QtCore.Qt.UserRole + 1 )
			node = item.data ( QtCore.Qt.UserRole + 2 )
		#print '* (%s) selected' % param.label
		self.ui.param.setParam ( param )
		self.ui.node.setNode ( node )
		self.ui.prop_tabWidget.setCurrentIndex ( 1 )
	#
	# onOutputParamChanged
	#
	def onOutputParamChanged ( self ) :
		#  
		if DEBUG_MODE : print '>> ExportShaderDialog.onOutputParamChanged'
		item = self.ui.list_outputs.currentItem ()
		if QtCore.QT_VERSION < 0x50000 : 
			param = item.data ( QtCore.Qt.UserRole + 1 ).toPyObject ()
			node = item.data ( QtCore.Qt.UserRole + 2 ).toPyObject ()
		else :
			param = item.data ( QtCore.Qt.UserRole + 1 )
			node = item.data ( QtCore.Qt.UserRole + 2 )
		#print '* (%s) selected' % self.param.label
		self.ui.param.setParam ( param )
		self.ui.node.setNode ( node )
		self.ui.prop_tabWidget.setCurrentIndex ( 1 )    
	#
	# updateGui
	#
	def updateGui ( self ) :
		#
		if self.editNode is not None :
			if DEBUG_MODE : print '>> ExportShaderDialog.updateGui'
			self.disconnectSignals ()
			self.connectSignals ()
	#
	# onRenameNodeLabel
	#
	def onRenameNodeLabel ( self, oldName, newName ) :
		#
		editNode = self.ui.node.editNode
		for i in range ( self.ui.list_nodes.count () ) :
			item = self.ui.list_nodes.item ( i )
			if QtCore.QT_VERSION < 0x50000 : 
				node = item.data ( QtCore.Qt.UserRole + 1 ).toPyObject ()
			else :
				node = item.data ( QtCore.Qt.UserRole + 1 )
			if node is not None and node == editNode :
				item.setText ( editNode.label )
		
		if self.ui.list_nodes.currentRow () == 1 :
			self.updateComputedParams ()
	#
	# onParamChange
	#
	def onParamChange ( self ) :
		#
		param = self.ui.param.param
		node = self.ui.node.editNode
		
		if self.ui.list_nodes.currentRow () == 1 :
			self.updateComputedParams ()
		else :
			self.updateNodeParams ( node )
	#
	# onViewCode
	#
	def onViewCode ( self ) : ViewComputedCodeDialog ( self.editNode ).exec_ ()
	#
	# onExport
	#
	def onExport ( self ) :
		#
		import os
		saveName = os.path.join ( app_global_vars [ 'ProjectSources' ], self.editNode.getInstanceName () + '.sl' )
		typeFilter = 'Shader source files *.sl;;All files *.*;;'
		if QtCore.QT_VERSION < 0x50000 :
			filename = str( QtModule.QFileDialog.getSaveFileName ( self, "Export shader code as", saveName, typeFilter ) )
		else :
			( filename, filter ) = QtModule.QFileDialog.getSaveFileName ( self, "Export shader code as", saveName, typeFilter )
		if filename != '' :
			if DEBUG_MODE : print '-> Export shader code as %s' % filename
			shaderCode = self.editNode.getComputedCode ()
			self.editNode.writeShader ( shaderCode, filename )
	#
	# Ignore default Enter press event
	#
	def keyPressEvent ( self, event  ) :
		#
		#if DEBUG_MODE : print '>> ExportShaderDialog.keyPressEvent'
		if  event.key () == QtCore.Qt.Key_Enter or event.key () == QtCore.Qt.Key_Return :
			event.ignore ()
		else:
			QtModule.QDialog.keyPressEvent ( self, event )
	#
	# accept
	#
	def accept ( self ) :
		#
		if DEBUG_MODE : print '>> ExportShaderDialog.accept'
		self.done ( QtModule.QDialog.Accepted )