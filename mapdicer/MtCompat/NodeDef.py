# 
# Mtcompat
# Copyright(C) 2013 celeron55, Perttu Ahola<celeron55@gmail.com>; 2020 Jake "Poikilos" Gustafson
# 
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *

class ContentParamType(object):
	def __init__(self):

class ContentParamType2(object):
	def __init__(self):

	# Need 8-bit param2
	# Flowing liquid properties
	# Direction for chests and furnaces and such
	# Direction for signs, torches and such
	# Block level like FLOWINGLIQUID
	# 2D rotation for things like plants
	# Mesh options for plants
	# Index for palette
	# 3 bits of palette index, then facedir
	# 5 bits of palette index, then wallmounted
	# Glasslike framed drawtype internal liquid level, param2 values 0 to 63
class LiquidType(object):
	def __init__(self):

class NodeDef(object):
	pass
# TODO: Implement this if importing Nodes from Minetest Lua mods.
class INodeDefManager(object):
	def Get(self, node):
		pass