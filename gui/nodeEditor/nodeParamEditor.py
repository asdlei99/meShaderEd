"""
 nodeParamEditor.py

 ver. 1.0.0
 
 Author: Yuri Meshalkin (aka mesh) (mesh@kpp.kiev.ua)

 Dialog for managing node parameters

"""
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore, QtGui
from core.signal import Signal

from core.meCommon import *
from global_vars import app_global_vars, DEBUG_MODE, VALID_PARAM_TYPES
from core.nodeParam import *

import gui.ui_settings as UI
from gui.params.StringWidget import StringWidget
from gui.params.FloatWidget import FloatWidget
from gui.params.IntWidget import IntWidget
from gui.params.ColorWidget import ColorWidget
from gui.params.NormalWidget import NormalWidget
from gui.params.PointWidget import PointWidget
from gui.params.VectorWidget import VectorWidget
from gui.params.MatrixWidget import MatrixWidget
from gui.params.TextWidget import TextWidget
from gui.params.ControlWidget import ControlWidget

from ui_nodeParamEditor import Ui_NodeParamEditor

if  not usePyQt5 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets
#
# NodeParamEditor
#
class NodeParamEditor ( QtModule.QWidget ) :
	#
	# __init__
	#
	def __init__ ( self, parent ) :
		#
		QtModule.QWidget.__init__ ( self, parent )
		#
		# Define signals for PyQt5
		#
		if usePySide or usePyQt5 :
			#
			self.changeParamName = Signal ()
			self.changeParamLabel = Signal ()
			self.changeParamIsShader = Signal ()
			self.changeParamType = Signal ()
			self.changeParamDetail = Signal ()
			self.changeParamProvider = Signal ()
			self.changeParamSubtype = Signal ()
			self.changeParamRange = Signal ()
			
			self.changeParamValue = Signal ()
			self.changeParamDefValue = Signal ()
		#
		self.param = None
		self.param_default = None
		self.paramWidgets = {	 'string'       : StringWidget
													,'image'        : StringWidget
													,'rib'          : StringWidget
													,'surface'      : StringWidget
													,'displacement' : StringWidget
													,'light'        : StringWidget
													,'volume'       : StringWidget
													,'float'        : FloatWidget
													,'int'          : IntWidget
													,'color'        : ColorWidget
													,'normal'       : NormalWidget
													,'transform'    : PointWidget
													,'point'        : PointWidget
													,'vector'       : VectorWidget
													,'matrix'       : MatrixWidget
													,'text'         : TextWidget
													,'control'      : ControlWidget
													,'shader'       : StringWidget
													,'geom'         : StringWidget
												}

		self.buildGui()
	#
	#
	def __delete__ ( self, obj ) :
		#
		print ( '* NodeParamEditor closed... %s' % str( obj ) )
	#
	# buildGui
	#
	def buildGui ( self ) :
		# build the gui created with QtDesigner
		self.ui = Ui_NodeParamEditor ( )
		self.ui.setupUi ( self )

		# correct UI sizes for some controls
		self.ui.check_enabled.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
		self.ui.check_enabled.setMaximumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
		
		self.ui.check_display.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
		self.ui.check_display.setMaximumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )

		self.ui.check_shader.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
		self.ui.check_shader.setMaximumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )

		for label in VALID_PARAM_TYPES : self.ui.type_comboBox.addItem ( label )
		
		self.ui.type_comboBox.setCurrentIndex ( -1 )
		self.ui.type_comboBox.setMinimumSize ( QtCore.QSize ( UI.COMBO_WIDTH, UI.COMBO_HEIGHT ) )
		self.ui.type_comboBox.setMaximumSize ( QtCore.QSize( UI.MAX, UI.COMBO_HEIGHT ) )

		# temporary disabled, until "how to do it gracefully" will be clear ...
		self.ui.type_comboBox.setEnabled ( False )

		for label in [ 'None', 'uniform', 'varying', ]  :
			self.ui.detail_comboBox.addItem ( label )
		self.ui.detail_comboBox.setCurrentIndex ( -1 )
		self.ui.detail_comboBox.setMinimumSize ( QtCore.QSize ( UI.COMBO_WIDTH, UI.COMBO_HEIGHT ) )
		self.ui.detail_comboBox.setMaximumSize ( QtCore.QSize( UI.MAX, UI.COMBO_HEIGHT ) )

		for label in [ 'None', 'internal', 'external', 'primitive', 'attribute' ]  :
			self.ui.provider_comboBox.addItem ( label )
		self.ui.provider_comboBox.setCurrentIndex ( -1 )
		self.ui.provider_comboBox.setMinimumSize ( QtCore.QSize ( UI.COMBO_WIDTH, UI.COMBO_HEIGHT ) )
		self.ui.provider_comboBox.setMaximumSize ( QtCore.QSize( UI.MAX, UI.COMBO_HEIGHT ) )

		for label in [ 'None', 'slider', 'switch', 'selector', 'file', 'button' ]  :
			self.ui.subtype_comboBox.addItem ( label )
		self.ui.subtype_comboBox.setCurrentIndex ( -1 )
		self.ui.subtype_comboBox.setMinimumSize ( QtCore.QSize ( UI.COMBO_WIDTH, UI.COMBO_HEIGHT ) )
		self.ui.subtype_comboBox.setMaximumSize ( QtCore.QSize( UI.MAX, UI.COMBO_HEIGHT ) )
	#
	# As paramWidet is monitoring a change of param.value only,
	# we need to cynchronize changing of param_default.value with param.default
	#
	def onParamDefValueChanged ( self, param ) :
		#
		if DEBUG_MODE : print ( '* onParamDefValueChanged' )
		self.param.default = self.param_default.value
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamDefValue' ), self.param )
		else :
			self.changeParamDefValue.emit ( self.param )
	#
	# onParamValueChanged
	#
	def onParamValueChanged ( self, param ) :
		#
		if DEBUG_MODE : print ( '* onParamValueChanged' )
		self.param.value = param.value
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamValue' ), self.param )
		else :
			self.changeParamValue.emit ( self.param )
	#
	# connectSignals
	#
	def connectSignals ( self ) :
		#
		if  usePyQt4 :
			self.connect ( self.param_default, QtCore.SIGNAL ( 'paramChangedSignal(QObject)' ), self.onParamDefValueChanged )
			self.connect ( self.param, QtCore.SIGNAL ( 'paramChangedSignal(QObject)' ), self.onParamValueChanged )
			
			self.connect ( self.ui.name_lineEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onEditParamName )
			self.connect ( self.ui.label_lineEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onEditParamLabel )
			self.connect ( self.ui.check_enabled, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamEnabled )
			self.connect ( self.ui.check_display, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamDisplay )
			self.connect ( self.ui.check_shader, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamShader )
			self.connect ( self.ui.type_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamType )
			self.connect ( self.ui.detail_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamDetail )
			self.connect ( self.ui.provider_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamProvider )
			self.connect ( self.ui.subtype_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamSubtype )
			self.connect ( self.ui.range_lineEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onEditParamRange )
			self.connect ( self.ui.descr_plainTextEdit, QtCore.SIGNAL ( 'textChanged()' ), self.onEditParamHelp )
		else :
			self.param_default.paramChangedSignal.connect ( self.onParamDefValueChanged )
			self.param.paramChangedSignal.connect ( self.onParamValueChanged )
			
			self.ui.name_lineEdit.editingFinished.connect ( self.onEditParamName )
			self.ui.label_lineEdit.editingFinished.connect ( self.onEditParamLabel )
			self.ui.check_enabled.stateChanged.connect ( self.onEditParamEnabled )
			self.ui.check_display.stateChanged.connect ( self.onEditParamDisplay )
			self.ui.check_shader.stateChanged.connect ( self.onEditParamShader )
			self.ui.type_comboBox.activated.connect ( self.onEditParamType )
			self.ui.detail_comboBox.activated.connect ( self.onEditParamDetail )
			self.ui.provider_comboBox.activated.connect ( self.onEditParamProvider )
			self.ui.subtype_comboBox.activated.connect ( self.onEditParamSubtype )
			self.ui.range_lineEdit.editingFinished.connect ( self.onEditParamRange )
			self.ui.descr_plainTextEdit.textChanged.connect ( self.onEditParamHelp )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self ) :
		#
		if  usePyQt4 :
			if self.param_default is not None :
				self.disconnect ( self.param_default, QtCore.SIGNAL ( 'paramChangedSignal(QObject)' ), self.onParamDefValueChanged )
			if self.param is not None :
				self.disconnect ( self.param, QtCore.SIGNAL ( 'paramChangedSignal(QObject)' ), self.onParamValueChanged )
				
				self.disconnect ( self.ui.name_lineEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onEditParamName )
				self.disconnect ( self.ui.label_lineEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onEditParamLabel )
				self.disconnect ( self.ui.check_enabled, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamEnabled )
				self.disconnect ( self.ui.check_display, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamDisplay )
				self.disconnect ( self.ui.check_shader, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onEditParamShader )
				self.disconnect ( self.ui.type_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamType )
				self.disconnect ( self.ui.detail_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamDetail )
				self.disconnect ( self.ui.provider_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamProvider )
				self.disconnect ( self.ui.subtype_comboBox, QtCore.SIGNAL ( 'activated(int)' ), self.onEditParamSubtype )
				self.disconnect ( self.ui.descr_plainTextEdit, QtCore.SIGNAL ( 'textChanged()' ), self.onEditParamHelp )
		else :
			if self.param_default is not None :
				self.param_default.paramChangedSignal.disconnect ( self.onParamDefValueChanged )
			if self.param is not None :
				self.param.paramChangedSignal.disconnect ( self.onParamValueChanged )
				
				self.ui.name_lineEdit.editingFinished.disconnect ( self.onEditParamName )
				self.ui.label_lineEdit.editingFinished.disconnect ( self.onEditParamLabel )
				self.ui.check_enabled.stateChanged.disconnect ( self.onEditParamEnabled )
				self.ui.check_display.stateChanged.disconnect ( self.onEditParamDisplay )
				self.ui.check_shader.stateChanged.disconnect ( self.onEditParamShader )
				self.ui.type_comboBox.activated.disconnect ( self.onEditParamType )
				self.ui.detail_comboBox.activated.disconnect ( self.onEditParamDetail )
				self.ui.provider_comboBox.activated.disconnect ( self.onEditParamProvider )
				self.ui.subtype_comboBox.activated.disconnect ( self.onEditParamSubtype )
				self.ui.range_lineEdit.editingFinished.disconnect ( self.onEditParamRange )
				self.ui.descr_plainTextEdit.textChanged.disconnect ( self.onEditParamHelp )
	#
	# reset
	#
	def reset ( self ) :
		#
		self.ui.name_lineEdit.setText ( '' )
		self.ui.label_lineEdit.setText ( '' )
		
		self.ui.check_enabled.setChecked ( True )
		self.ui.check_display.setChecked ( True )
		self.ui.check_shader.setChecked ( False )

		self.ui.type_comboBox.setCurrentIndex( -1 )
		self.ui.detail_comboBox.setCurrentIndex ( -1 )
		self.ui.provider_comboBox.setCurrentIndex ( -1 )
		self.ui.subtype_comboBox.setCurrentIndex ( -1 )
		self.ui.range_lineEdit.setText ( '' )

		doc = QtGui.QTextDocument ()
		doc.setPlainText ( '' )
		layout = QtModule.QPlainTextDocumentLayout ( doc )
		doc.setDocumentLayout ( layout )
		self.ui.descr_plainTextEdit.setDocument ( doc )
	#
	# Remove stackedWidget's layout every time,
	# when current parameter (or it's type) is changing
	#
	def removeValueWidget ( self ) :
		#
		while True :
			currentWidget = self.ui.value_stackedWidget.currentWidget ()
			if currentWidget is not None :
				#print '> removeWidget: %s' % str( currentWidget )
				self.ui.value_stackedWidget.removeWidget ( currentWidget )
			else :
				break
	#
	# setParam
	#
	def setParam ( self, param ) :
		#
		print ( '>> NodeParamEdiror.setParam ' )
		self.removeValueWidget ()
		self.disconnectSignals ()
		self.param = param
		
		if self.param is not None :
			#import copy
			print ( ':: param(%s).value = ' % param.label ), param.value
			self.param_default = self.param.copy () # duplicate param for default value editing
			self.param_default.value = copy.deepcopy ( param.default )
			if param.isArray () :
				self.param_default.spaceDefArray = copy.deepcopy ( param.spaceDefArray )

			self.ui.name_lineEdit.setText ( self.param.name )
			self.ui.label_lineEdit.setText ( self.param.label )
			
			self.ui.check_enabled.setChecked ( self.param.enabled )
			self.ui.check_display.setChecked ( self.param.display )
			self.ui.check_shader.setChecked ( self.param.shaderParam )

			self.ui.type_comboBox.setCurrentIndex ( self.ui.type_comboBox.findText ( self.param.type ) )
			self.ui.detail_comboBox.setCurrentIndex ( self.ui.detail_comboBox.findText ( self.param.detail ) )
			self.ui.provider_comboBox.setCurrentIndex ( self.ui.provider_comboBox.findText ( self.param.provider ) )
			self.ui.subtype_comboBox.setCurrentIndex ( self.ui.subtype_comboBox.findText ( self.param.subtype ) )
			self.ui.range_lineEdit.setText ( self.param.range )

			doc = QtGui.QTextDocument ()
			help_text = ''
			if self.param.help != None : help_text = self.param.help

			doc.setPlainText ( help_text )
			layout = QtModule.QPlainTextDocumentLayout ( doc )
			doc.setDocumentLayout( layout )

			self.ui.descr_plainTextEdit.setDocument ( doc )
			#
			# setup param values view
			#
			paramsLayout = QtModule.QGridLayout ()
			paramsLayout.setContentsMargins ( UI.SPACING, UI.SPACING, UI.SPACING, UI.SPACING )
			paramsLayout.setSizeConstraint ( QtModule.QLayout.SetNoConstraint )
			paramsLayout.setVerticalSpacing ( UI.VSPACING  )
			paramsLayout.setColumnStretch ( 1, 1 )
			paramsLayout.setRowStretch ( 2, 1 )
			
			frame = QtModule.QFrame ()
			frame.setLayout ( paramsLayout )

			if self.param.type in self.paramWidgets.keys () :
				print '>> Create %s param widget' % self.param.type

				# create paramWidget without GfxNode and ignoreSubtype = True
				self.ui.value_widget = apply ( self.paramWidgets [ self.param.type ], [ self.param, None, True ] )
				self.ui.value_widget.label.setText ( 'Current Value' )
				
				paramsLayout.addLayout ( self.ui.value_widget.label_vl, 0, 0, 1, 1 )
				paramsLayout.addLayout ( self.ui.value_widget.param_vl, 0, 1, 1, 1 )
				
				self.ui.def_value_widget = apply ( self.paramWidgets [ self.param_default.type ], [ self.param_default, None, True ] )
				self.ui.def_value_widget.label.setText ( 'Default Value' )

				paramsLayout.addLayout ( self.ui.def_value_widget.label_vl, 1, 0, 1, 1 )
				paramsLayout.addLayout ( self.ui.def_value_widget.param_vl, 1, 1, 1, 1 )
				
				spacer = QtModule.QSpacerItem ( 0, 0, UI.SP_MIN, UI.SP_EXPAND )
				paramsLayout.addItem ( spacer, 2, 0, 1, 1 ) 

			# build a scroll area
			scrollArea = QtModule.QScrollArea ()
			scrollArea.setWidgetResizable ( True )
			scrollArea.setWidget ( frame )
			
			self.ui.value_stackedWidget.addWidget ( scrollArea )
			
			self.connectSignals ()
		else :
			self.reset ()
	#
	# onEditParamName
	#
	def onEditParamName ( self ) :
		#
		# !!! ListWidget item for param also should be changed
		#
		oldName = self.param.name
		newName = str ( self.ui.name_lineEdit.text () ).strip ()
		if newName == '' :
			newName = oldName
			self.ui.name_lineEdit.setText ( newName )
		if newName != oldName :
			self.param.name = newName
			if  usePyQt4 :
				self.emit( QtCore.SIGNAL ( 'changeParamName' ), oldName, newName )
			else :
				self.changeParamName.emit ( oldName, newName )
	#
	# onEditParamLabel
	#
	def onEditParamLabel ( self ) :
		#
		oldName = self.param.label
		newName  = str ( self.ui.label_lineEdit.text () ).strip ()
		if newName == '' :
			newName = oldName
			self.ui.label_lineEdit.setText ( newName )
		if newName != oldName :
			self.param.label = newName
			if  usePyQt4 :
				self.emit ( QtCore.SIGNAL ( 'changeParamLabel' ), oldName, newName )
			else :
				self.changeParamLabel.emit ( oldName, newName )
	#
	# onEditParamEnabled
	#
	def onEditParamEnabled ( self, value ) : 
		#
		self.param.enabled = self.ui.check_enabled.isChecked ()
	#
	# onEditParamEnabled
	#
	def onEditParamDisplay ( self, value ) : 
		#
		self.param.display = self.ui.check_display.isChecked ()
	#
	# onEditParamShader
	#
	def onEditParamShader ( self, value )  : 
		#
		self.param.shaderParam = self.ui.check_shader.isChecked ()
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamIsShader' ), self.param )
		else :
			self.changeParamIsShader.emit ( self.param )
	#
	# onEditParamType
	#	
	def onEditParamType ( self, idx ) :
		#
		# !!! UI for param.value and param.default also should be changed
		#
		self.param.type = str ( self.ui.type_comboBox.itemText ( idx ) )
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamType' ), self.param )
		else :
			self.changeParamType.emit ( self.param )
	#
	# onEditParamDetail
	#	
	def onEditParamDetail ( self, idx ) :
		#
		self.param.detail = str ( self.ui.detail_comboBox.itemText ( idx ) )
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamDetail' ), self.param )
		else :
			self.changeParamDetail.emit ( self.param )
	#
	# onEditParamProvider
	#		
	def onEditParamProvider ( self, idx ) : 
		#
		self.param.provider = str ( self.ui.provider_comboBox.itemText ( idx ) )
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamProvider' ), self.param )
		else :
			self.changeParamProvider.emit ( self.param )
	#
	# onEditParamSubtype
	#		
	def onEditParamSubtype ( self, idx ) : 
		#
		self.param.subtype = str ( self.ui.subtype_comboBox.itemText ( idx ) )
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamSubtype' ), self.param )
		else :
			self.changeParamSubtype.emit ( self.param )
	#
	# onEditParamRange
	#		
	def onEditParamRange ( self ) : 
		#
		self.param.range = str ( self.ui.range_lineEdit.text () )
		if  usePyQt4 :
			self.emit ( QtCore.SIGNAL ( 'changeParamRange' ), self.param )
		else :
			self.changeParamRange.emit ( self.param )
	#
	# onEditParamHelp
	#			
	def onEditParamHelp ( self ) : 
		#
		self.param.help = str ( self.ui.descr_plainTextEdit.toPlainText () )
