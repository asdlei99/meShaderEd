#===============================================================================
# paramWidget.py
#===============================================================================

from PyQt4 import QtGui, QtCore

from global_vars import app_global_vars, DEBUG_MODE, VALID_PARAM_TYPES, INVALID_RSL_PARAM_TYPES

import gui.ui_settings as UI

#
# ParamWidget general class for parameter widgets
#
class ParamWidget ( QtGui.QWidget ) :
  #
  # __init__
  #
  def __init__ ( self, param, gfxNode, parent = None, ignoreSubtype = False ) :
    #
    #print ">> ParamWidget  __init__"
    super ( QtGui.QWidget, self ).__init__ ( None )
    self.param = param
    self.gfxNode = gfxNode
    self.ignoreSubtype = ignoreSubtype # if widget is used in NodeEditor, then ignoreSubtype = True

    self.buildGeneralGui ()
    self.buildGui ()
    self.ui.updateGui ( self.param.value )
    #self.connect( self.param, QtCore.SIGNAL( 'paramChanged(QObject)' ), self.onParamChanged )
  #
  #  __del__
  #
  def __del__ ( self ) :
    print '>> ParamWidget( %s ).__del__ ' % self.param.name
  #
  # onParamChanged
  #
  def onParamChanged ( self, param ) :
    #
    print ">> ParamWidget( %s ).onParamChanged" % param.name
    self.ui.disconnectSignals ( self )
    self.ui.updateGui ( self.param.value )
    self.ui.connectSignals ( self )
    #self.emit ( QtCore.SIGNAL( 'onParamChanged(QObject)' ), param )
  #
  # buildGeneralGui
  #
  def buildGeneralGui ( self ) :
    #print ">> ParamWidget buildGeneralGui"
    self.vl = QtGui.QVBoxLayout ( self )
    self.vl.setSpacing ( UI.SPACING )
    self.vl.setMargin ( 0 )
    self.vl.setAlignment ( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft )

    self.gui = QtGui.QWidget( self )

    self.hl = QtGui.QHBoxLayout ( self.gui )
    self.hl.setSpacing ( UI.SPACING )
    self.hl.setMargin ( 0 )
    self.hl.setAlignment ( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft )
    #
    # add 'isShaderParam' check box only for RSL nodes
    #
    if self.gfxNode is not None :
      if not self.gfxNode.node.type in INVALID_RSL_PARAM_TYPES :
        if self.param.provider != 'attribute' :
          self.check = QtGui.QCheckBox ( self )
          self.check.setMinimumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
          self.check.setMaximumSize ( QtCore.QSize ( UI.CHECK_WIDTH, UI.HEIGHT ) )
          self.check.setToolTip ( 'Use as Shader parameter' )

          self.check.setChecked ( self.param.shaderParam )
          self.connect ( self.check, QtCore.SIGNAL ( 'stateChanged(int)' ), self.onShaderParamChanged )

          self.hl.addWidget ( self.check )
        else :
          spacer = QtGui.QSpacerItem ( UI.LT_SPACE, UI.HEIGHT, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum )
          self.hl.addItem ( spacer )
      #
      # add 'remove' button for removable parameters
      #
      if self.param.removable :
        self.removeButton = QtGui.QToolButton ( self )
        sizePolicy = QtGui.QSizePolicy ( QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed )
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
        
        QtCore.QObject.connect ( self.removeButton, QtCore.SIGNAL ( 'clicked()' ), self.onRemoveItem )
        
        self.hl.addWidget ( self.removeButton )
    
    self.label = QtGui.QLabel ( self )
    font = QtGui.QFont ()
    font.setBold ( False )
    self.label.setFont ( font )
  
    #if self.param.type != 'control' :
    self.label.setText ( self.param.label )
  
    self.label.setMinimumSize ( QtCore.QSize ( UI.LABEL_WIDTH, UI.HEIGHT ) )
    self.label.setMaximumSize ( QtCore.QSize ( UI.LABEL_WIDTH, UI.HEIGHT ) )
    self.label.setAlignment ( QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter )
  
    self.hl.addWidget ( self.label )
    self.vl.addWidget ( self.gui )
  #
  # onShaderParamChanged
  #
  def onShaderParamChanged ( self, value ) :
    #
    self.param.shaderParam = self.check.isChecked ()
    self.gfxNode.updateInputParams ()
  #
  # buildGui
  #
  def buildGui ( self ) :
    #
    spacer = QtGui.QSpacerItem ( 20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum )
    self.hl.addItem ( spacer )
  #
  # onRemoveItem
  #
  def onRemoveItem ( self ) : 
    #
    print '>> ParamWidget( %s ).onRemoveItem ' % self.param.name   
    self.emit ( QtCore.SIGNAL ( 'nodeParamRemoved' ), self.param ) 

