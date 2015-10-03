"""

 ribCodeNode.py

"""
from core.mePyQt import usePySide, usePyQt4, usePyQt5, QtCore

from core.node import Node
from core.nodeParam import NodeParam

from global_vars import app_global_vars, DEBUG_MODE
from core.node_global_vars import node_global_vars
#
# RIBCodeNode
#
class RIBCodeNode ( Node ) :
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
	def copy ( self ):
		#
		if DEBUG_MODE : print '>> RIBCodeNode( %s ).copy' % self.label
		newNode = RIBCodeNode ()
		self.copySetup ( newNode )
		return newNode
	#
	# getParamDeclaration
	#
	def getParamDeclaration ( self, param ) :
		#
		paramValueStr = param.getValueToStr ()
		if param.type == 'string' :
			paramValueStr = '"' + paramValueStr + '"'
		result = '"' + param.typeToStr () + ' ' + self.getParamName ( param ) + '" '
		result += '[ ' + paramValueStr + ' ]'
		return result
	#
	# getRiCallForShaderType
	#
	def getRiCallForShaderType ( self, shader_type ) :
		#
		result = ''
		shaderRiCall = {   'surface' : 'Surface' 
											,'displacement' : 'Displacement'
											,'light' : 'LightSource'
											,'volume' : 'Volume'
											,'shader' : 'Shader'
										}
		if shader_type in shaderRiCall.keys () :
			result = shaderRiCall [ shader_type ]
		return result
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

					#print '-> found local var %s' % local_var_name

					param = self.getInputParamByName ( local_var_name )
					if param is not None :
						value = self.getInputParamValueByName ( local_var_name, CodeOnly )
						resultStr += value
					else :
						param = self.getOutputParamByName ( local_var_name )
						if param is not None :
							resultStr += param.getValueToStr ()
						else :
							print '-> ERRPR: local var %s is not defined !' % local_var_name
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
		param = self.getInputParamByName ( name )

		if self.isInputParamLinked ( param ) :
			link = self.inputLinks [ param ]
			#link.printInfo ()
			link.srcNode.computeNode ( CodeOnly )
			#if self.computed_code is not None :
			#  self.computed_code += link.srcNode.computed_code
			if link.srcNode.type in [ 'rib', 'rib_code' ] :
				#result = '## start code from :' + link.srcNode.label
				result = link.srcNode.parseLocalVars ( link.srcNode.code, CodeOnly )
				#result += '## end code from :' + link.srcNode.label
			else :
				result = link.srcNode.parseGlobalVars ( link.srcParam.getValueToStr () )
		else :
			result = param.getValueToStr ()
		
		return result
	#
	# getHeader
	#
	def getHeader ( self ) :
		#
		rslHeader =  '\n'
		rslHeader += '#\n'
		rslHeader += '# RIB node: %s (%s)\n' % ( self.label,  self.name )
		rslHeader += '#\n'
		return rslHeader
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
	# computeNode
	#
	def computeNode ( self, CodeOnly = False ) :
		#
		self.execControlCode ()
	

