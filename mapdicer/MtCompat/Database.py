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

class Database(object):
	def beginSave(self):
		pass

	def endSave(self):
		pass

	def initialized(self):
		pass

	def unsigned_to_signed(i, max_positive):
		""" <summary>
		 Convert unsigned to signed.
		 See
		 https://git.minetest.org/minetest/minetest/src/branch/master/src/database.cpp
		 </summary>
		"""
		# originally 16-bit params and return
		if i < max_positive:
			return i
		return (i - (max_positive * 2))

	unsigned_to_signed = staticmethod(unsigned_to_signed)

	def pythonmodulo(i, mod):
		""" <summary>
		 "Modulo of a negative number does not work consistently in C"
		 See
		 https://git.minetest.org/minetest/minetest/src/branch/master/src/database.cpp
		 </summary>
		"""
		# ^ mod was originally 16-bit
		if i >= 0:
			return i % mod
		return mod - ((-i) % mod)

	pythonmodulo = staticmethod(pythonmodulo)

class MapDatabase(Database):
	def getBlockAsInteger(pos):
		""" <summary>
		 Convert a mapblock offset (1 per mapblock) to a unique Mapblock Id given 3D
		 Coordinates (this part is like Minetest and shouldn't be called directly except
		 for 3D voxel applications). For compatibility with Minetest position hashes, the unusual
		 type casting must remain.
		 See
		 https://git.minetest.org/minetest/minetest/src/branch/master/src/database.cpp
		 </summary>
		 <param name="p">A block offset in [x, z] format where y is zenith and 1 is the
		 size of a Mapblock in this Lod</param>
		 <returns>a primary key for the Mapblock at the given location</returns>
		"""
		return (pos.Z * 0x1000000 + pos.Y * 0x1000 + pos.X)

	getBlockAsInteger = staticmethod(getBlockAsInteger)

	def getIntegerAsBlock(i):
		""" <summary>
		 This is a hashing algorithm so for compatibility with Minetest it must stay intact
		 even though it does some things inside out.
		 See
		 https://git.minetest.org/minetest/minetest/src/branch/master/src/database.cpp#L59
		 </summary>
		 <param name="i"></param>
		 <returns></returns>
		"""
		# barring the "new" operator, fields must be assigned manually before use in C# structs.
		pos.X = MapDatabase.unsigned_to_signed(MapDatabase.pythonmodulo(i, 4096), 2048)
		i = (i - pos.X) / 4096
		pos.Y = MapDatabase.unsigned_to_signed(MapDatabase.pythonmodulo(i, 4096), 2048)
		i = (i - pos.Y) / 4096
		pos.Z = MapDatabase.unsigned_to_signed(MapDatabase.pythonmodulo(i, 4096), 2048)
		return pos

	getIntegerAsBlock = staticmethod(getIntegerAsBlock)

	def beginSave(self):
		raise NotImplementedException()

	def endSave(self):
		raise NotImplementedException()

	def initialized(self):
		raise NotImplementedException()