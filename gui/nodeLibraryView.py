"""

	nodeLibraryView.py

"""
from core.mePyQt import QtCore, QtGui

#from PyQt4.QtCore import QDir, QString, QModelIndex
#from PyQt4.QtGui  import QFileSystemModel
#from PyQt4.QtGui  import QFileIconProvider


from core.meCommon import *
from global_vars import app_global_vars

from ui_nodeLibraryView import Ui_nodeLibraryView

from core.node import Node
from core.nodeLibrary import NodeLibrary

if QtCore.QT_VERSION < 0x50000 :
	QtModule = QtGui
else :
	from core.mePyQt import QtWidgets
	QtModule = QtWidgets
	
#
# NodeLibraryView
#
class NodeLibraryView ( QtModule.QWidget ) :
	#
	# __init__
	#
	def __init__ ( self ) :
		#
		QtModule.QWidget.__init__ ( self )

		# This is always the same
		self.ui=Ui_nodeLibraryView () 
		self.ui.setupUi ( self )
		self.updateGui ()
	#
	# setLibrary
	#
	def setLibrary ( self, dirName ) : self.ui.nodeList.setLibrary ( dirName )
	#  
	# onReload
	#
	def onReload ( self ) : self.ui.nodeList.reloadLibrary ()  
	#   
	# updateGui
	#
	def updateGui ( self ) :
		#
		pass    
		#if ( self.nodesLib != '' ) :
			# self.ui.treeView.setupModel( self.nodesLib.model )
			
			#self.ui.treeView.reset ()
			#self.ui.treeView.setModel ( self.nodesLib.model ) 
			
			#self.ui.infoText.clear ()
			#self.ui.infoText.setText( "<i>Node:</i><br /><i>Author:</i><br />" )
			
		

 
