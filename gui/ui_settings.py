#
# ui_settings.py
#
import sys
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore, QtGui

if  not usePyQt5 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets

CHECK_WIDTH = 20
SPACING = 4
VSPACING = 8
FIELD_WIDTH = 60
COMBO_WIDTH = 120
COMBO_HEIGHT = 22
FONT_HEIGHT = 10

if sys.platform == 'darwin' : 
  CHECK_WIDTH = 25
  SPACING = 2
  FIELD_WIDTH = 80
  COMBO_HEIGHT = 24
  FONT_HEIGHT = 12
  
BROWSE_WIDTH = 24
LABEL_WIDTH = 100
NODE_LABEL_WIDTH = 40
EDIT_WIDTH = 160
COLOR_WIDTH = 60

HEIGHT = 20
  
MAX = 16777215
LT_SPACE = CHECK_WIDTH
TAB_SIZE = 10

SWATCH_SIZE = 64
NODE_RADIUS = 10
CONNECTOR_RADIUS = 5

SHADOW_OFFSET = 4
SHADOW_OPACITY = 0.2

SP_MIN = QtModule.QSizePolicy.Minimum
SP_EXPAND = QtModule.QSizePolicy.Expanding

