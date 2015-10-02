"""

 ribNode.py
 
 ver. 1.0.0
 Author: Yuri Meshalkin (aka mesh) (yuri.meshalkin@gmail.com)

"""
import os, sys
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore

from core.node import Node
from core.nodeParam import NodeParam
from core.meCommon import *

from global_vars import app_global_vars, DEBUG_MODE
from core.node_global_vars import node_global_vars
#
# RIBNode
#
class RIBNode ( Node ) :
	#
	# __init__
	#
	def __init__ ( self, xml_node = None ) :
		#
		Node.__init__ ( self, xml_node )
		self.ribName = ''
	#
	# copy
	#
	def copy ( self ) :
		#
		if DEBUG_MODE : print '>> RIBNode( %s ).copy' % self.label
		newNode = RIBNode ()
		self.copySetup ( newNode )
		return newNode
	#
	# parseLocalVars
	#
	def parseLocalVars ( self, parsedStr, CodeOnly = False ) :
		#print '-> parseLocalVars in %s' % parsedStr
		resultStr = ''
		parserStart = 0
		parserPos = 0

		while parserPos != -1 :
			parserPos = parsedStr.find ( '$', parserStart )
			if parserPos != -1 :
				#
				if parserPos != 0 :
					resultStr += parsedStr [ parserStart : parserPos ]

				# check local variables
				if parsedStr [ ( parserPos + 1 ) : ( parserPos + 2 ) ] == '(' :
					globStart = parserPos + 2
					parserPos = parsedStr.find ( ')', globStart )
					local_var_name = parsedStr [ globStart : ( parserPos ) ]

					# print '-> found local var %s' % local_var_name

					param = self.getInputParamByName ( local_var_name )
					if param is not None :
						value = self.getInputParamValueByName ( local_var_name, CodeOnly )
						resultStr += value
					else :
						param = self.getOutputParamByName ( local_var_name )
						if param is not None :
							resultStr += param.getValueToStr ()
						else :
							print '!! local var %s is not defined !' % local_var_name
				else :
					# keep $ sign for otheer, non $(...) cases
					resultStr += '$'

			#print 'parserPos = %d parserStart = %d' % ( parserPos, parserStart )
			if parserPos != -1 :
				parserStart = parserPos + 1

		resultStr += parsedStr [ parserStart: ]
		
		if resultStr != '' :
			resultStr = self.getHeader () + resultStr
			
		return resultStr
	#
	# getInputParamValueByName
	#
	def getInputParamValueByName ( self, name, CodeOnly = False ) :
		#
		result = None
		srcNode = srcParam = None
		param = self.getInputParamByName ( name )
		( srcNode, srcParam ) = self.getLinkedSrcNode ( param )
		if srcNode is not None :
			srcNode.computeNode ( CodeOnly )
			#if self.computed_code is not None :
			#  self.computed_code += link.srcNode.computed_code

			if srcNode.type in [ 'rib', 'rib_code' ] :
				#result = '## start code from :' + link.srcNode.label
				result = srcNode.parseLocalVars ( srcNode.code, CodeOnly )
				#result += '## end code from :' + link.srcNode.label
			else :
				result = srcNode.parseGlobalVars ( srcParam.getValueToStr () )
		else :
			result = param.getValueToStr ()

		return result
	#
	# getHeader
	#
	def getHeader ( self ) :
		#
		ribHeader =  '#\n'
		ribHeader += '# %s\n' % ( self.getInstanceName () + '.rib' )
		ribHeader += '# Generated by meShaderEd ver.${version}\n' 
		ribHeader += '#\n\n'
		return ribHeader
	#
	# getComputedCode
	#
	def getComputedCode ( self, CodeOnly = False ) :
		#
		computedCode = ''
		
		self.execControlCode ()
		
		computedCode = self.parseLocalVars ( self.code, CodeOnly )
		computedCode = self.parseGlobalVars ( computedCode )
		
		return computedCode
	#
	# writeRIB
	#
	def writeRIB ( self, ribCode, ribName ) :
		#
		self.ribName = normPath ( ribName )
		f = open ( self.ribName, 'w+t' )
		f.write ( ribCode )
		f.close ()
	#
	# renderRIB
	#
	def renderRIB ( self ) :
		#
		#from meShaderEd import app_renderer
	
		renderer = app_global_vars [ 'RendererName' ]
		flags = app_global_vars [ 'RendererFlags' ]
		renderCmd = [ renderer ]
		if  flags != '' :  renderCmd.append ( flags )
		renderCmd.append ( self.ribName )

		print '>> RIBNode renderCmd = %s' %  ' '.join ( renderCmd )

		# call the process
		from core.meCommon import launchProcess

		launchProcess ( renderCmd )
	#
	# computeNode
	#
	def computeNode ( self, CodeOnly = False ) :
		#
		ribCode = self.getComputedCode ( CodeOnly )

		if ribCode != '' and not CodeOnly :
			
			ribName = os.path.join ( app_global_vars [ 'TempPath' ], self.getNodenetName () + '_' + self.getInstanceName () + '.rib' )
			self.writeRIB ( ribCode, ribName )
			self.renderRIB ()      

		return self.ribName
	

