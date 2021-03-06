"""

	intNodeParam.py

"""
import re

from core.nodeParam import NodeParam
from global_vars import app_global_vars, DEBUG_MODE
from core.meCommon import parseGlobalVars
#
# IntNodeParam
#
class IntNodeParam ( NodeParam ) :
	#
	# __init__
	#
	def __init__ ( self, xml_param = None, isRibParam = False  ) :
		#
		NodeParam.__init__ ( self, xml_param, isRibParam )
		self.type = 'int'
	#
	# encodedTypeStr
	#
	def encodedTypeStr ( self ) : return 'i'
	#
	# copy
	#
	def copy ( self ) :
		#
		newParam = IntNodeParam ()
		self.copySetup ( newParam )
		return newParam
	#
	# valueFromStr
	#
	def valueFromStr ( self, strValue ) :
		#
		if not self.isArray () :
			value = 0
			if strValue != '' :
				try: value = int ( strValue )
				except: raise Exception ( 'Cannot parse integer value for parameter %s' % ( self.name ) )
		else :
			value = []
			s = re.findall ( r'[+-]?[\d\.]+', strValue )
			f = map ( int, s )
			value = f
		return value
	#
	# valueToStr
	#
	def valueToStr ( self, value ) : 
		#
		if not self.isArray () :
			strValue = '%d' % value
		else :
			strValue = '[' + ''.join ( '%d' % f + ',' for f in value [: - 1] ) + '%d' % value [ - 1] + ']'
		return strValue
	#
	# getValueToRIB
	#
	def getValueToRIB ( self, value ) :
		#
		if not self.isArray () :
			strValue = '%d' % value
		else :
			strValue = '[' + ''.join ( '%d' % f + ' ' for f in value [: - 1] ) + '%d' % value [ - 1] + ']'
		return strValue
	#
	# getRangeValues
	#
	# if subtype == selector then return list of (label,value) pairs
	# It's supposed, that range is defined as "value1:value2:value3"
	# or "label1=value1:label2=value2:label3=value3:"
	#
	def getRangeValues ( self ) :
		#
		rangeList = []
		i = 0
		if self.range != '' :
			#
			# get range for selector
			#
			if self.subtype == 'selector' :
				tmp_list = str ( self.range ).split ( ':' )
				for s in tmp_list :
					pair = s.split ( '=' )
					if len ( pair ) > 1 :
						label = pair [0]
						value = int ( pair [1] )
					else :
						label = s
						value = int ( i )
					i += 1
					rangeList.append ( ( parseGlobalVars ( label ), value ) )
			#
			# get range for slider
			#
			elif self.subtype == 'slider' or self.subtype == 'vslider' :
				tmp_list = str ( self.range ).split ()
				for i in range ( 0, 3 ) :
					value = 0
					if i < len ( tmp_list ) :
						value = int ( tmp_list [ i ] )
					rangeList.append ( value )

		return rangeList
