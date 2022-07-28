from MapDicer.Models import *
from MapDicer.MtCompat import *
from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *

class MapDicerPos(object):
	""" <summary>
	 This is a unique spatial position where y is an abstract computation from the Lod and
	 layer.
	 </summary>
	"""
	def __init__(self, mapBlockId):
		pos = MapDatabase.getIntegerAsBlock(mapBlockId)
		self._X = pos.X
		self._Z = pos.Z
		self._LodId = (pos.Y / SettingModel.MaxLayerCount)
		self._LayerId = (pos.Y % SettingModel.MaxLayerCount)

	def get_Y(self):
		return (self._LodId * SettingModel.MaxLayerCount + self._LayerId)

	def set_Y(self, value):
		self._LodId = (value / SettingModel.MaxLayerCount)
		self._LayerId = (value % SettingModel.MaxLayerCount)

	Y = property(fget=get_Y, fset=set_Y)

	def getSliceAsInteger(self):
		""" <summary>
		 Convert a mapblock offset (1 per mapblock) to a unique Mapblock Id given the
		 current level of detail and layer (z is computed from lod and layer, so this part
		 differs from Minetest. For compatibility with Minetest position hashes, the unusual
		 type casting must remain (This must match mtcompat/Database.getBlockAsInteger).
		 See
		 https://git.minetest.org/minetest/minetest/src/branch/master/src/database.cpp
		 </summary>
		 <param name="pos">A block offset in [x, z] format where y is zenith and 1 is the
		 size of a Mapblock in this Lod</param>
		 <param name="layer">A key for a layer entity such as that of "terrain" or
		 "elevation"</param>
		 <returns>a primary key for the Mapblock at the given location</returns>
		"""
		if self._LayerId >= SettingModel.MaxLayerCount:
			raise ApplicationException("The layer number cannot be >= MaxLayerCount")
		return (self._Z * 0x1000000 + self.Y * 0x1000 + self._X)

	def Dump(self):
		return String.Format("LodId={0,2},LayerId={1,2},X={2,2},Z={3,2}", self._LodId, self._LayerId, self._X, self._Z)