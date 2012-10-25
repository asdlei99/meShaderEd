#===============================================================================
# nodeCodeEditor.py
#
# ver. 1.0.0
# Author: Yuri Meshalkin (aka mesh) (yuri.meshalkin@gmail.com)
# 
# Dialog for managing node code
# 
#===============================================================================

import os, sys
from PyQt4 import QtCore, QtGui

from core.meCommon import *
from global_vars import app_global_vars

import gui.ui_settings as UI
from gui.codeSyntaxHighlighter import CodeSyntaxHighlighter

from ui_nodeCodeEditor import Ui_NodeCodeEditor
#
#
#
class NodeCodeEditor ( QtGui.QWidget ):
  #
  #
  def __init__ ( self, parent, editNodeCode = None ):
    QtGui.QDialog.__init__ ( self )
    
    self.editNodeCode = editNodeCode
     
    #self.debugPrint()
    self.buildGui()
  #
  #
  def buildGui ( self ) :
    # build the gui created with QtDesigner
    self.ui = Ui_NodeCodeEditor ( )
    self.ui.setupUi ( self )
    
  #
  #
  def setNodeCode ( self, editNodeCode, mode = 'SL' ) :
    self.editNodeCode = editNodeCode
    
    doc = QtGui.QTextDocument ()
    
    font = QtGui.QFont( 'Monospace' )
    font.setFixedPitch ( True )
    font.setPointSize ( UI.FONT_HEIGHT )

    
    codeSyntax = CodeSyntaxHighlighter ( doc, mode )
    
    self.ui.textEdit.setDocument ( doc )  
    self.ui.textEdit.setTabStopWidth ( UI.TAB_SIZE )
    self.ui.textEdit.setCurrentFont ( font )
    self.ui.textEdit.setLineWrapMode ( QtGui.QTextEdit.NoWrap )

    code = self.editNodeCode
    if self.editNodeCode is None : code = ''
    self.ui.textEdit.setPlainText ( code )
        
        
        
    
