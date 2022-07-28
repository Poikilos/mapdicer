from System import *
from System.Collections.Generic import *
from System.ComponentModel.DataAnnotations import *
from System.ComponentModel.DataAnnotations.Schema import *
from System.Data.Entity import *
# using System.Data.Entity.ModelConfiguration.Conventions;
# using System.Data.Entity.Core.Mapping;
# using System.Data.Linq.Mapping;
from System.Data.SQLite import *
# using System.Data.SQLite.EF6;
# using System.Data.SQLite.Linq;
# using System.Data.Linq;
from System.Linq import * # orderby etc
from System.Windows import *
from System.Windows.Media import *

class Terrain(object):
	def __init__(self):
		self._SourceWorldmapOverworldTileset = 1
		# <summary>
		# The color on the map image denotes the terrain. Alpha is unused, so only 24 bits of this
		# int will ever be used.
		# </summary>
		# <summary>
		# Ground, water, mountains, trees, etc
		# </summary>
		# <summary>
		# Variant such as oak, pine, etc
		# </summary>
		# <summary>
		# The path of the single tile.
		# </summary>
		# <summary>
		# (Reserved for future use) The source of the image.
		# </summary>
		# <summary>
		# (Reserved for future use) If this was/is cropped from a tileset (denoted by SourceId in future
		# versions), this is the ID.
		# </summary>
		# <summary>
		# (Reserved for future use) JSON metadata (NodeDef, one per many instances).
		# </summary>
		# <summary>
		# Scale the graphic so this many pixels fits into the sample (this is for representing a terrain
		# graphically rather than by plain color).
		# </summary>
		self._errors = Queue[str]()

	def get_TerrainId(self):

	def set_TerrainId(self, value):

	TerrainId = property(fget=get_TerrainId, fset=set_TerrainId)

	def get_Name(self):

	def set_Name(self, value):

	Name = property(fget=get_Name, fset=set_Name)

	def get_Classification(self):

	def set_Classification(self, value):

	Classification = property(fget=get_Classification, fset=set_Classification)

	def get_Variant(self):

	def set_Variant(self, value):

	Variant = property(fget=get_Variant, fset=set_Variant)

	def get_Path(self):

	def set_Path(self, value):

	Path = property(fget=get_Path, fset=set_Path)

	def get_SourceId(self):

	def set_SourceId(self, value):

	SourceId = property(fget=get_SourceId, fset=set_SourceId)

	def get_TileIndex(self):

	def set_TileIndex(self, value):

	TileIndex = property(fget=get_TileIndex, fset=set_TileIndex)

	def get_JSON(self):

	def set_JSON(self, value):

	JSON = property(fget=get_JSON, fset=set_JSON)

	def get_PixPerSample(self):

	def set_PixPerSample(self, value):

	PixPerSample = property(fget=get_PixPerSample, fset=set_PixPerSample)

	def All():
		try:
		except System.ArgumentException, ex:
			# where entry.Id < 25
			msg = ex.Message
			if not self._errors.Contains(msg):
				self._errors.Enqueue(msg)
			return None
		finally:
		return None

	All = staticmethod(All)
 # (*Linq to db*, 2020)
	def Insert(newEntry):
		error = ""
		# There may be two inner exceptions such as
		# 1:
		# UpdateException: An error occurred while updating the entries. See the inner exception for details.
		# 2:
		# SQLiteException: constraint failed
		# UNIQUE constraint failed: Mapblock.MapblockId
		return error

	Insert = staticmethod(Insert)
 # (*Linq to db*, 2020)
	def GetColor(self):
		return Terrain.ColorFromId(self.TerrainId)

	def IntFromHexPair(hexPairStr):
		return Convert.ToInt32(hexPairStr, 16)

	IntFromHexPair = staticmethod(IntFromHexPair)

	def ByteFromHexPair(hexPairStr):
		return Terrain.IntFromHexPair(hexPairStr)

	ByteFromHexPair = staticmethod(ByteFromHexPair)

	def HexPair(v):
		return Convert.ToString(v, 16).PadLeft(2, '0')

	HexPair = staticmethod(HexPair)

	def Test():
		ok = True
		hexPairStr = "10"
		value = Terrain.IntFromHexPair(hexPairStr)
		testStr = Terrain.HexPair(value)
		if testStr != hexPairStr:
			ok = False
			MessageBox.Show(String.Format("Error: {0} made {1} which is really {2}", hexPairStr, value, testStr))
		v = 128
		hStr = Terrain.HexPair(v)
		testByte = Terrain.ByteFromHexPair(hStr)
		if testByte != v:
			ok = False
			MessageBox.Show(String.Format("Error: {0} made {1} which is really {2}", v, hStr, testByte))
		return ok

	Test = staticmethod(Test)

	def GetById(id):

	GetById = staticmethod(GetById)

	# orderby entry.TerrainId ascending
	def IdFromHexColorBgr(hexColor):
		""" <summary>
		 Convert the string such that blue FIRST (in BBRRGG) is the MOST significant byte.
		 Get the color as a Terrain primary key integer. The order is BGR so blue is most significant
		 to immitate life (blue is a higher intensity by frequency).
		 The ID only reaches the value of a 24-bit number.
		 </summary>
		 <param name="hexColor"></param>
		 <returns></returns>
		"""
		if hexColor.Length != 6:
			raise ApplicationException("The hex color must be 6 characters.")
		return (Terrain.IntFromHexPair(hexColor.Substring(0, 2)) * 65536 + Terrain.IntFromHexPair(hexColor.Substring(2, 2)) * 256 + Terrain.ByteFromHexPair(hexColor.Substring(4, 2)))

	IdFromHexColorBgr = staticmethod(IdFromHexColorBgr)

	def IdFromColorRgb(r, g, b):
		return b * 65536 + g * 256 + r

	IdFromColorRgb = staticmethod(IdFromColorRgb)

	def IdFromHexColorRgb(hexColor):
		""" <summary>
		 Convert the string such that red FIRST (in RRGGBB) is the LEAST significant byte.
		 </summary>
		 <param name="hexColor"></param>
		 <returns></returns>
		"""
		if hexColor.Length != 6:
			raise ApplicationException("The hex color must be 6 characters.")
		return (Terrain.IntFromHexPair(hexColor.Substring(4, 2)) * 65536 + Terrain.IntFromHexPair(hexColor.Substring(2, 2)) * 256 + Terrain.ByteFromHexPair(hexColor.Substring(0, 2)))

	IdFromHexColorRgb = staticmethod(IdFromHexColorRgb)

	def HexBgrFromColor(r, g, b):
		return Terrain.HexPair(b) + Terrain.HexPair(g) + Terrain.HexPair(r)

	HexBgrFromColor = staticmethod(HexBgrFromColor)

	def HexRgbFromColor(r, g, b):
		return Terrain.HexPair(r) + Terrain.HexPair(g) + Terrain.HexPair(b)

	HexRgbFromColor = staticmethod(HexRgbFromColor)

	def ColorFromHexColorRgb(hexColor):
		if hexColor.Length != 6:
			raise ApplicationException("The hex color must be 6 characters.")
		r = Terrain.ByteFromHexPair(hexColor.Substring(0, 2))
		g = Terrain.ByteFromHexPair(hexColor.Substring(2, 2))
		b = Terrain.ByteFromHexPair(hexColor.Substring(4, 2))
		return Color.FromArgb(255, r, g, b)

	ColorFromHexColorRgb = staticmethod(ColorFromHexColorRgb)

	def ColorFromHexColorBgr(hexColor):
		if hexColor.Length != 6:
			raise ApplicationException("The hex color must be 6 characters.")
		b = Terrain.ByteFromHexPair(hexColor.Substring(0, 2))
		g = Terrain.ByteFromHexPair(hexColor.Substring(2, 2))
		r = Terrain.ByteFromHexPair(hexColor.Substring(4, 2))
		return Color.FromArgb(255, r, g, b)

	ColorFromHexColorBgr = staticmethod(ColorFromHexColorBgr)

	def ColorFromId(id):
		# A byte overflow will occur on blue if the id is out of range.
		return Color.FromArgb(255, (id & 0xFF), ((id >> 8) & 0xFF), (id >> 16))

	ColorFromId = staticmethod(ColorFromId)