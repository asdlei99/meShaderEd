"""

 IntWidget.py

"""
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore, QtGui

import gui.ui_settings as UI 
from paramWidget import ParamWidget

if  not usePyQt5 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets
#
# IntWidget
#
class IntWidget ( ParamWidget ) :
	#
	# buildGui
	#
	def buildGui ( self ) :
		#
		if self.param.isArray () :
			self.ui = Ui_IntWidget_array ()
		else :
			if not self.ignoreSubtype :
				if self.param.subtype == 'selector' : 
					self.ui = Ui_IntWidget_selector ()
				elif self.param.subtype == 'switch' : 
					self.ui = Ui_IntWidget_switch ()
				elif self.param.subtype == 'slider' or self.param.subtype == 'vslider' : 
					self.ui = Ui_IntWidget_slider ()
				else:
					self.ui = Ui_IntWidget_field () 
			else :
				self.ui = Ui_IntWidget_field () 
		self.ui.setupUi ( self )
#
# Ui_IntWidget_field
#          
class Ui_IntWidget_field ( object ) :
	#
	# setupUi
	#
	def setupUi ( self, IntWidget ) :
		#
		hl = QtModule.QHBoxLayout ()
		self.widget = IntWidget
		
		self.intEdit = QtModule.QLineEdit ( IntWidget )
		
		self.intEdit.setMinimumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) )
		self.intEdit.setMaximumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) )
		spacer = QtModule.QSpacerItem ( 20, 20, QtModule.QSizePolicy.Expanding, QtModule.QSizePolicy.Minimum )
		
		hl.addWidget ( self.intEdit )
		hl.addItem ( spacer )
		self.widget.param_vl.addLayout ( hl )
		
		QtCore.QMetaObject.connectSlotsByName ( IntWidget )
		self.connectSignals ( IntWidget )
	#
	# connectSignals
	#
	def connectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.connect ( self.intEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
		else :
			self.intEdit.editingFinished.connect ( self.onIntEditEditingFinished )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.disconnect ( self.intEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
		else :
			self.intEdit.editingFinished.disconnect ( self.onIntEditEditingFinished )
	#
	#  onIntEditEditingFinished
	#
	def onIntEditEditingFinished ( self ) :
		#
		intStr = self.intEdit.text ()
		if usePyQt4 :
			intValue = intStr.toInt () [ 0 ] 
		else :
			intValue = int ( intStr )
		self.widget.param.setValue (  intValue )      
	#
	# updateGui
	def updateGui ( self, value ):
		#
		if usePyQt4 : 
			self.intEdit.setText ( QtCore.QString.number ( value ) )
		else :
			self.intEdit.setText ( str ( value ) )
#
# Ui_IntWidget_array
#          
class Ui_IntWidget_array ( object ) :
	#
	# setupUi
	#
	def setupUi ( self, IntWidget ) :
		#
		self.widget = IntWidget
		self.labels = []
		self.controls = []
		
		font = QtGui.QFont ()
		labelFontMetric = QtGui.QFontMetricsF ( font )
		label_wi = 0
		char_wi = labelFontMetric.width ( 'x' )
		array_size = self.widget.param.arraySize
		if array_size > 0 :
			label_wi =  char_wi * ( len ( str ( array_size - 1 ) ) + 2 ) # [0]
		
		for i in range ( self.widget.param.arraySize ) :
			self.labels.append ( QtModule.QLabel ( IntWidget ) )
			self.labels [ i ].setMinimumSize ( QtCore.QSize ( label_wi, UI.HEIGHT ) )
			self.labels [ i ].setMaximumSize ( QtCore.QSize ( label_wi, UI.HEIGHT ) )
			self.labels [ i ].setAlignment ( QtCore.Qt.AlignRight )
			self.labels [ i ].setText ( '[' + str ( i ) + ']' )

			self.controls.append ( QtModule.QLineEdit ( IntWidget ) )
			self.controls [ i ].setMinimumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) )
			self.controls [ i ].setMaximumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) )
			
			sp = QtModule.QSpacerItem ( 0, 0, UI.SP_EXPAND,  UI.SP_MIN )
			
			hl = QtModule.QHBoxLayout ()
			hl.addWidget ( self.labels [ i ] )
			hl.addWidget ( self.controls [ i ] )
			hl.addItem ( sp )
			self.widget.param_vl.addLayout ( hl )
		
		self.connectSignals ( IntWidget )
		QtCore.QMetaObject.connectSlotsByName ( IntWidget )
	#
	# connectSignals
	#
	def connectSignals ( self, IntWidget ) :
		#
		for i in range ( self.widget.param.arraySize ) :
			if usePyQt4 :
				IntWidget.connect ( self.controls [ i ], QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
			else :
				self.controls [ i ].editingFinished.connect ( self.onIntEditEditingFinished )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self, IntWidget ) :
		#
		for i in range ( self.widget.param.arraySize ) :
			if usePyQt4 :
				IntWidget.disconnect ( self.controls [ i ], QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
			else :
				self.controls [ i ].editingFinished.disconnect ( self.onIntEditEditingFinished )
	#
	#  onIntEditEditingFinished
	#
	def onIntEditEditingFinished ( self ) :
		#
		arrayValue = []

		for i in range ( self.widget.param.arraySize ) :
			intStr = self.controls [ i ].text ()
			if usePyQt4 :
				intValue = intStr.toInt () [ 0 ] 
			else :
				intValue = int ( intStr )
			arrayValue.append ( intValue )

		self.widget.param.setValue ( arrayValue )      
	#
	# updateGui
	#
	def updateGui ( self, value ):
		#
		for i in range ( self.widget.param.arraySize ) :
			if usePyQt4 : 
				self.controls [ i ].setText ( QtCore.QString.number ( value [ i ] ) )
			else :
				self.controls [ i ].setText ( str ( value [ i ] ) )
#
# Ui_IntWidget_switch
#          
class Ui_IntWidget_switch ( object ) :
	#
	# setupUi
	#
	def setupUi ( self, IntWidget ) :
		#
		hl = QtModule.QHBoxLayout ()
		self.widget = IntWidget
		
		self.checkBox = QtModule.QCheckBox ( IntWidget )
		
		self.checkBox.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) ) 
		self.checkBox.setMaximumSize ( QtCore.QSize ( UI.MAX, UI.HEIGHT ) )
		spacer = QtModule.QSpacerItem ( 20, 20, QtModule.QSizePolicy.Expanding, QtModule.QSizePolicy.Minimum )
		
		hl.addWidget ( self.checkBox )
		hl.addItem ( spacer )
		self.widget.param_vl.addLayout ( hl )
		
		QtCore.QMetaObject.connectSlotsByName ( IntWidget )
		self.connectSignals ( IntWidget )
	#
	# connectSignals
	#
	def connectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.connect ( self.checkBox, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onStateChanged )
		else :
			self.checkBox.stateChanged.connect ( self.onStateChanged )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.disconnect ( self.checkBox, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onStateChanged )
		else :
			self.checkBox.stateChanged.disconnect ( self.onStateChanged )
	# 
	# onStateChanged 
	#
	def onStateChanged ( self, value ) :
		#
		intValue = self.checkBox.isChecked ()    
		self.widget.param.setValue ( intValue )
	#
	# updateGui
	#
	def updateGui ( self, value ) : 
		#
		self.checkBox.setChecked ( value != 0 )  
#
# Ui_IntWidget_selector
#          
class Ui_IntWidget_selector ( object ) :
	#
	# setupUi
	#
	def setupUi ( self, IntWidget ) :
		#
		hl = QtModule.QHBoxLayout ()
		self.widget = IntWidget
		
		self.selector = QtModule.QComboBox ( IntWidget )
		self.selector.setEditable ( False )
		self.selector.setMinimumSize ( QtCore.QSize ( UI.COMBO_WIDTH, UI.COMBO_HEIGHT ) )
		self.selector.setMaximumSize ( QtCore.QSize ( UI.MAX, UI.COMBO_HEIGHT ) )
		
		rangeList = self.widget.param.getRangeValues ()
		
		for ( label, value ) in rangeList : self.selector.addItem ( label, int( value ) )
		
		spacer = QtModule.QSpacerItem ( UI.HEIGHT, UI.HEIGHT, QtModule.QSizePolicy.Expanding, QtModule.QSizePolicy.Minimum )
		
		hl.addWidget ( self.selector )
		hl.addItem ( spacer )
		self.widget.param_vl.addLayout ( hl )
		
		QtCore.QMetaObject.connectSlotsByName ( IntWidget )
		self.connectSignals ( IntWidget )
	#
	# connectSignals
	#
	def connectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.connect ( self.selector, QtCore.SIGNAL ( 'activated(int)' ), self.onCurrentIndexChanged )
		else :
			self.selector.activated.connect ( self.onCurrentIndexChanged ) 
	#
	# disconnectSignals
	#
	def disconnectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.disconnect ( self.selector, QtCore.SIGNAL ( 'activated(int)' ), self.onCurrentIndexChanged )
		else :
			self.selector.activated.disconnect ( self.onCurrentIndexChanged ) 
	#
	# onCurrentIndexChanged
	#
	def onCurrentIndexChanged ( self, idx ) :
		#
		if usePyQt4 :
			( intValue, ok ) = self.selector.itemData ( idx ).toInt ()
		else :
			intValue = self.selector.itemData ( idx )
		self.widget.param.setValue ( int ( intValue ) )
	#
	# updateGui
	#
	def updateGui ( self, setValue ) : 
		#
		currentIdx = -1
		i = 0
		rangeList = self.widget.param.getRangeValues ()
		for ( label, value ) in rangeList :
			if setValue == value : 
				currentIdx = i
				break
			i += 1
		self.selector.setCurrentIndex ( currentIdx )
#
# Ui_IntWidget_slider
#          
class Ui_IntWidget_slider ( object ) :
	#
	# setupUi
	#
	def setupUi ( self, IntWidget ) :
		#
		hl = QtModule.QHBoxLayout ()
		hl.setStretch ( 1, 1 )
		
		self.widget = IntWidget
		
		self.intEdit = QtGui.QLineEdit ( IntWidget )
		
		self.intEdit.setMinimumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) ) 
		self.intEdit.setMaximumSize ( QtCore.QSize ( UI.FIELD_WIDTH, UI.HEIGHT ) )
		
		self.slider = QtModule.QSlider ( QtCore.Qt.Horizontal, IntWidget )
		
		intMinVal = 0
		intMaxVal = 10
		intStep = 1
		
		rangeList = self.widget.param.getRangeValues ()
		
		if len ( rangeList ) :
			intMinVal = rangeList [ 0 ]
			intMaxVal = rangeList [ 1 ]
			intStep   = rangeList [ 2 ]
		
		if intStep == 0 : intStep = 1
		
		self.slider.setRange ( intMinVal, intMaxVal )
		self.slider.setSingleStep ( intStep )
		
		self.slider.setValue ( int ( self.widget.param.value ) )

		hl.addWidget ( self.intEdit )
		hl.addWidget ( self.slider )
		self.widget.param_vl.addLayout ( hl )
		
		QtCore.QMetaObject.connectSlotsByName ( IntWidget )
		self.connectSignals ( IntWidget )
	#
	# connectSignals
	#
	def connectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.connect ( self.intEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
			IntWidget.connect ( self.slider, QtCore.SIGNAL ( 'valueChanged(int)' ), self.onSliderValueChanged )
		else :
			self.intEdit.editingFinished.connect ( self.onIntEditEditingFinished )
			self.slider.valueChanged.connect ( self.onSliderValueChanged )
	#
	# disconnectSignals
	#
	def disconnectSignals ( self, IntWidget ) :
		#
		if usePyQt4 :
			IntWidget.disconnect ( self.intEdit, QtCore.SIGNAL ( 'editingFinished()' ), self.onIntEditEditingFinished )
			IntWidget.disconnect ( self.slider, QtCore.SIGNAL ( 'valueChanged(int)' ), self.onSliderValueChanged )
		else :
			self.intEdit.editingFinished.disconnect ( self.onIntEditEditingFinished )
			self.slider.valueChanged.disconnect ( self.onSliderValueChanged )
	#
	# onIntEditEditingFinished
	#
	def onIntEditEditingFinished ( self ) :
		#
		intStr = self.intEdit.text ()
		if usePyQt4 :
			intValue = intStr.toInt () [ 0 ] 
		else :
			intValue = int ( intStr )
		self.widget.param.setValue ( intValue )    
		self.slider.setValue ( intValue )
	#
	# onSliderValueChanged
	#
	def onSliderValueChanged ( self, value ) :
		#
		self.widget.param.setValue ( value )
		self.updateGui ( value) 
		#self.widget.param.paramChanged ()
	#
	# updateGui
	#
	def updateGui ( self, value ) :
		# 
		if usePyQt4 :
			self.intEdit.setText ( QtCore.QString.number ( value ) )
		else :
			self.intEdit.setText ( str ( value ) ) 
