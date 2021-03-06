"""

 paramWidget.py

"""
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore, QtGui
from core.signal import Signal

from global_vars import app_global_vars, DEBUG_MODE, VALID_PARAM_TYPES, VALID_RSL_NODE_TYPES, VALID_RSL_PARAM_TYPES
import gui.ui_settings as UI

from paramLabel import ParamLabel

if not usePyQt5 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets
#
# ParamWidget general class for parameter widgets
#
class ParamWidget ( QtModule.QWidget ) :
	#
	# __init__
	#
	def __init__ ( self, param, gfxNode, ignoreSubtype = False ) :
		#
		QtModule.QWidget.__init__ ( self )
		#
		# Define signals for PyQt5
		#
		if usePySide or usePyQt5 :
			#
			self.nodeParamRemoved = Signal ()
			#
		self.param = param
		self.gfxNode = gfxNode
		self.ignoreSubtype = ignoreSubtype # if widget is used in NodeEditor, then ignoreSubtype = True

		self.buildGeneralGui ()
		self.buildGui ()
		self.ui.updateGui ( self.param.value )
		#self.connectSignals ()
		#self.connect( self.param, QtCore.SIGNAL( 'paramChanged(QObject)' ), self.onParamChanged )
		#if DEBUG_MODE : print ">> ParamWidget (%s.%s)  __init__" % ( self.gfxNode.node.label, self.param.label )
	#
	#  __del__
	#
	def __del__ ( self ) :
		#
		if DEBUG_MODE : print ( '>> ParamWidget( %s ).__del__ ' % self.param.name )
	#
	# connectSignals
	#
	def connectSignals ( self ) :
		#
		pass
	#
	# setEnabled
	#
	def setEnabled ( self, enabled = True ) :
		#
		for hl in self.param_vl.children () :
			for i in range ( hl.count () ) :
				obj = hl.itemAt ( i ).widget ()
				if obj is not None :
					obj.setEnabled ( enabled )
	#
	# onParamChanged
	#
	def onParamChanged ( self, param ) :
		#
		if DEBUG_MODE : print ( ">> ParamWidget( %s ).onParamChanged" % param.name )
		self.ui.disconnectSignals ( self )
		self.ui.updateGui ( self.param.value )
		self.ui.connectSignals ( self )
		#self.emit ( QtCore.SIGNAL( 'onParamChanged(QObject)' ), param )
	#
	# buildGeneralGui
	#
	def buildGeneralGui ( self ) :
		#if DEBUG_MODE : print ">> ParamWidget buildGeneralGui"
		
		self.label_vl = QtModule.QVBoxLayout ()
		self.label_vl.setSpacing ( UI.SPACING )
		self.label_vl.setContentsMargins ( 0, 0, 0, 0 )
		self.label_vl.setAlignment ( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft )
		
		
		self.hl = QtModule.QHBoxLayout ()
		self.hl.setSpacing ( UI.SPACING )
		self.hl.setContentsMargins ( 0, 0, 0, 0 )
		self.hl.setAlignment ( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft )
		
		# vertical layout for parametrs values (e.g. output links or matrix rows)
		self.param_vl = QtModule.QVBoxLayout ()
		self.param_vl.setSpacing ( UI.SPACING )
		self.param_vl.setContentsMargins ( 0, 0, 0, 0 )
		self.param_vl.setAlignment ( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft )
		#
		# add 'isShaderParam' check box only for RSL nodes
		#
		if self.gfxNode is not None :
			#
			# add "Use as Shader parameter" checkbox
			#
			#if ( self.gfxNode.node.type in VALID_RSL_NODE_TYPES ) and ( self.param.type in VALID_RSL_PARAM_TYPES ) and ( self.param.provider != 'attribute' ) :
			if ( self.gfxNode.node.format == 'rsl' ) and \
				( self.param.type in VALID_RSL_PARAM_TYPES ) and \
				( self.param.provider != 'attribute' ) :
				self.check = QtModule.QCheckBox ( self )
				self.check.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
				self.check.setMaximumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
				self.check.setToolTip ( 'Use as Shader parameter' )
				self.check.setChecked ( self.param.shaderParam )
				if  usePyQt4 :
					self.connect ( self.check, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onShaderParamChanged )
				else :
					self.check.stateChanged.connect ( self.onShaderParamChanged )
				self.hl.addWidget ( self.check )
			else :
				spacer = QtModule.QSpacerItem ( UI.LT_SPACE, UI.HEIGHT, QtModule.QSizePolicy.Minimum, QtModule.QSizePolicy.Minimum )
				self.hl.addItem ( spacer )
			#
			# add 'remove' button for removable parameters
			#
			if self.param.removable :
				self.removeButton = QtModule.QToolButton ( self )
				sizePolicy = QtModule.QSizePolicy ( QtModule.QSizePolicy.Fixed, QtModule.QSizePolicy.Fixed )
				sizePolicy.setHorizontalStretch ( 20 )
				sizePolicy.setVerticalStretch ( 20 )
				sizePolicy.setHeightForWidth ( self.removeButton.sizePolicy().hasHeightForWidth() )
				self.removeButton.setSizePolicy ( sizePolicy )
				self.removeButton.setMaximumSize ( QtCore.QSize ( 20, 20 ) )
				icon = QtGui.QIcon ()
				icon.addPixmap ( QtGui.QPixmap ( ':/edit_icons/resources/del_list.png' ), QtGui.QIcon.Normal, QtGui.QIcon.On )
				self.removeButton.setIcon ( icon )
				self.removeButton.setAutoRaise ( True )
				self.removeButton.setToolTip ( 'Remove parameter' )
				self.removeButton.setIconSize ( QtCore.QSize ( 16, 16 ) )
				self.removeButton.setObjectName ( 'removeButton' )
				self.hl.addWidget ( self.removeButton )
				if usePyQt4 :
					QtCore.QObject.connect ( self.removeButton, QtCore.SIGNAL ( 'clicked()' ), self.onRemoveItem )
				else :
					self.removeButton.clicked.connect ( self.onRemoveItem )

		self.label = ParamLabel ( self, self.param )
		
		self.helpMark = QtModule.QLabel ( self )
		palette = QtGui.QPalette ()
		palette.setColor ( QtGui.QPalette.WindowText, QtGui.QColor ( 0, 140, 0 ) )
		font1 = QtGui.QFont ()
		font1.setBold ( True )
		self.helpMark.setPalette ( palette )
		self.helpMark.setFont ( font1 )
		self.helpMark.setText ( '' )
		
		self.helpMark.setMinimumSize ( QtCore.QSize ( 6, UI.HEIGHT ) )
		self.helpMark.setMaximumSize ( QtCore.QSize ( 6, UI.HEIGHT ) )
		
		self.helpMark.setEnabled ( False )
		
		if self.param.help is not None and self.param.help != '' :
			self.label.setWhatsThis ( self.param.help )
			self.helpMark.setWhatsThis ( self.param.help )
			self.helpMark.setText ( '?' )
			self.helpMark.setEnabled ( True )
		
		self.label.setAlignment ( QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter )
		#self.label.setMinimumSize ( QtCore.QSize ( UI.LABEL_WIDTH, UI.HEIGHT ) )
		#self.label.setMaximumSize ( QtCore.QSize ( UI.LABEL_WIDTH, UI.HEIGHT ) )
		
		#self.vl.addWidget ( self.gui )
		self.hl.addWidget ( self.label )
		self.hl.addWidget ( self.helpMark )
		#self.hl.addLayout ( self.param_vl )
		#sp = QtModule.QSpacerItem ( 20, 20, QtModule.QSizePolicy.Expanding, QtModule.QSizePolicy.Minimum )
		
		self.label_vl.addLayout ( self.hl )
		sp_v = QtModule.QSpacerItem ( 0, 0, QtModule.QSizePolicy.Minimum, QtModule.QSizePolicy.Expanding )
		self.label_vl.addItem ( sp_v )
		
	#
	# onShaderParamChanged
	#
	def onShaderParamChanged ( self, value ) :
		#
		self.param.shaderParam = self.check.isChecked ()
		self.gfxNode.updateGfxNodeParams ( True )
	#
	# buildGui -- virtual method
	# should be overriden in inherited classes
	#
	def buildGui ( self ) :
		#
		pass
		#spacer = QtModule.QSpacerItem ( 20, 20, QtModule.QSizePolicy.Expanding, QtModule.QSizePolicy.Minimum )
		#self.hl.addItem ( spacer )
	#
	# onRemoveItem
	#
	def onRemoveItem ( self ) : 
		#
		if DEBUG_MODE : print '>> ParamWidget( %s ).onRemoveItem ' % self.param.name
		if usePyQt4 :   
			self.emit ( QtCore.SIGNAL ( 'nodeParamRemoved' ), self.param ) 
		else :
			self.nodeParamRemoved.emit ( self.param ) 

