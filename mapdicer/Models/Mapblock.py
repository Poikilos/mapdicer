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
from MapDicer.MtCompat import *

class Mapblock(MapNode):
	def get_MapblockId(self):

	def set_MapblockId(self, value):

	MapblockId = property(fget=get_MapblockId, fset=set_MapblockId)

	# public string Name { get; set; }
	def __init__(self):
		""" <summary>
		 The primary key must be long (INT in SQLite is same as long) because it contains the hash
		 of the coordinates as the primary key. It is the key because the hash denotes a unique
		 combination of location, Layer, and Lod (See MtCompat.MapDatabase.getBlockAsInteger).
		 </summary>
		"""
		# <summary>
		# This is for getting infomation on how to place it, not for structure per se.
		# </summary>
		#, ForeignKey("LodId") // System.InvalidOperationException: 'The property 'LodId' cannot be configured as a navigation property. The property must be a valid entity type and the property should have a non-abstract getter and setter. For collection properties the type must implement ICollection<T> where T is a valid entity type.'
		# private EntityRef<Lod> _lod = new EntityRef<Lod>();
		# ^ See Bruniasty's answer on
		# https://stackoverflow.com/questions/29120917/how-to-add-a-relationship-between-tables-in-linq-to-db-model-class
		# <summary>
		# This is for organizing by stat, not for structure per se.
		# </summary>
		# <summary>
		# This is the structural (real) parent.
		# </summary>
		# <summary>
		# This is the default terrain for non-generated parts. It is visible through the transparent
		# parts of the map data, so only 24-bits of it is used.
		# </summary>
		# <summary>
		# This is the map data for this section of the map (this map block). Each color in the image
		# represents a terrain type.
		# </summary>
		# TODO: (future) -- this code is not validated
		# 
		# [Column("Data", TypeName = "BLOB")]
		# public byte[] Data { get; set; }
		# 
		self._errors = Queue[str]()

	def get_MapDicerPos(self):
		return MapDicerPos(self.MapblockId)

	MapDicerPos = property(fget=get_MapDicerPos)

	def GetLayer(self):
		return (MapDatabase.getIntegerAsBlock(self.MapblockId).Y % SettingModel.MaxLayerCount)

	def GetLodId(self):
		return (MapDatabase.getIntegerAsBlock(self.MapblockId).Y / SettingModel.MaxLayerCount)

	def get_LodId(self):

	def set_LodId(self, value):

	LodId = property(fget=get_LodId, fset=set_LodId)

	def get_Lod(self):

	def set_Lod(self, value):

	Lod = property(fget=get_Lod, fset=set_Lod)

	def get_LayerId(self):

	def set_LayerId(self, value):

	LayerId = property(fget=get_LayerId, fset=set_LayerId)

	def get_Layer(self):

	def set_Layer(self, value):

	Layer = property(fget=get_Layer, fset=set_Layer)

	def get_RegionId(self):

	def set_RegionId(self, value):

	RegionId = property(fget=get_RegionId, fset=set_RegionId)

	def get_Region(self):

	def set_Region(self, value):

	Region = property(fget=get_Region, fset=set_Region)

	def get_TerrainId(self):

	def set_TerrainId(self, value):

	TerrainId = property(fget=get_TerrainId, fset=set_TerrainId)

	def get_Terrain(self):

	def set_Terrain(self, value):

	Terrain = property(fget=get_Terrain, fset=set_Terrain)

	def get_Path(self):

	def set_Path(self, value):

	Path = property(fget=get_Path, fset=set_Path)

	def Insert(newEntry):
		""" <summary>
		 Insert at the location where x-z is the ground plane as per OpenGL.
		 </summary>
		 <param name="newEntry"></param>
		 <param name="x"></param>
		 <param name="z"></param>
		 <param name="generateId">generate the id; If false, ignore x and z (they are baked
		 into the MapblockId)</param>
		 <returns></returns>
		""" # , short x, short z, bool generateId)
		generateId = False
		error = ""
		newId = newEntry.MapblockId
		# Mapblock last = null;
		# 
		# MapDicerPos macroPos = new MapDicerPos
		# {
		# LodId = newEntry.LodId,
		# LayerId = newEntry.LayerId,
		# X = x,
		# Z = z,
		# };
		# 
		# 
		# if (generateId)
		# {
		# newId = macroPos.getSliceAsInteger();
		# }
		# 
		# 
		# if (generateId)
		# {
		# using (var context = new MapDicerContext())
		# {
		# context.Database.CreateIfNotExists();
		# var existing = (from entry in context.Mapblocks
		# // where entry.Id < 25
		# orderby entry.MapblockId descending // the Last method depends on ascending.
		# select entry).FirstOrDefault();
		# if (existing != null)
		# {
		# newId = (short)(existing.MapblockId + 1); // last = existing;
		# }
		# // else assume no entries (leave new entry at 0 if generateId)
		# }
		# }
		# 
		# 
		# newEntry.MapblockId = 0;
		# if (last != null)
		# newEntry.MapblockId = (short)(last.MapblockId + 1);
		# else
		# newEntry.MapblockId = 0; // Assumes the table is empty or not present.
		# 
		# There may be two inner exceptions such as
		# 1:
		# UpdateException: An error occurred while updating the entries. See the inner exception for details.
		# 2:
		# SQLiteException: constraint failed
		# UNIQUE constraint failed: Mapblock.MapblockId
		return error

	Insert = staticmethod(Insert)

	def HexQuad(v):
		return Convert.ToString(v, 16).PadLeft(4, '0')

	HexQuad = staticmethod(HexQuad)

	def GetImagePath(macroMapblockId, makeDirs):
		macroPos = MapDicerPos(macroMapblockId)
		return Mapblock.GetImagePath(macroPos, makeDirs)

	GetImagePath = staticmethod(GetImagePath)

	def GetImagePath(macroPos, makeDirs):
		sectorsPath = System.IO.Path.Combine(SettingController.DataPath, "mapblocks")
		yPath = System.IO.Path.Combine(sectorsPath, Mapblock.HexQuad(macroPos.Y))
		# Go into y first unlike sectors2 (since there are few layers), and with Quads for all 4 values.
		# (See
		# <https://git.minetest.org/minetest/minetest/src/branch/master/doc/world_format.txt#L221>).
		xPath = System.IO.Path.Combine(yPath, Mapblock.HexQuad(macroPos.X))
		zPath = System.IO.Path.Combine(xPath, Mapblock.HexQuad(macroPos.Z)) + SettingController.MapblockImageDotExt
		# return SettingController.ImportPath(null, "mapblocks", mapblockId.ToString(), makeDirs);
		if makeDirs:
			if not System.IO.Directory.Exists(yPath):
				System.IO.Directory.CreateDirectory(yPath)
			if not System.IO.Directory.Exists(xPath):
				System.IO.Directory.CreateDirectory(xPath)
		return zPath

	GetImagePath = staticmethod(GetImagePath)

	def GetImagePath(self, makeDirs):
		return Mapblock.GetImagePath(self.MapblockId, makeDirs)

	# 
	# /// <summary>
	# /// Update any fields that differ.
	# /// </summary>
	# /// <param name="entry">The new version of the entry with the matching Id</param>
	# /// <returns>True if ok</returns>
	# public static bool Update(Mapblock entry)
	# {
	# bool ok = false;
	# using (var context = new MapDicerContext())
	# {
	# context.Database.CreateIfNotExists();
	# // see https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/insert-update-and-delete-operations
	# var existing =
	# (from v in context.Mapblocks
	# where v.MapblockId == entry.MapblockId
	# select v).First();
	# existing.LayerId = entry.LayerId;
	# existing.LodId = entry.LodId;
	# existing.Path = entry.Path;
	# existing.RegionId = entry.RegionId;
	# existing.TerrainId = entry.TerrainId;
	# ok = context.SaveChanges() > 0;
	# }
	# return ok;
	# }
	# 
	def WhereLodIdEquals(matchLodId):
		try:
		except System.ArgumentException, ex:
			# 
			# string msg = String.Format("The database is missing {0}", context.Database.Log);
			# if (!errors.Contains(msg))
			# {
			# errors.Enqueue(msg);
			# }
			# 
			# MessageBox.Show(String.Format("context: {0}", context.Database.Exists())); # the Last method depends on ascending.
			msg = ex.Message
			if not self._errors.Contains(msg):
				self._errors.Enqueue(msg)
			return None
		finally:
		# 
		# catch (System.Data.SQLite.SQLiteException ex)
		# {
		# 
		# // SQLiteException: SQL logic error
		# // no such table: Lod
		# // ^ but that's just the inner exception. See below.
		# 
		# string msg = ex.Message;
		# if (!errors.Contains(msg))
		# {
		# errors.Enqueue(msg);
		# }
		# return null;
		# }
		# catch (System.Data.Entity.Core.EntityCommandExecutionException ex)
		# {
		# string msg = ex.Message;
		# if (!errors.Contains(msg))
		# {
		# errors.Enqueue(msg);
		# }
		# return null;
		# }
		# 
		return None

	WhereLodIdEquals = staticmethod(WhereLodIdEquals)

	def GetById(id):
		try:
		except System.ArgumentException, ex:
			# Don't use properties, only Db fields (fails regardless of name):
			# System.NotSupportedException: 'The specified type member 'Id' is not supported in LINQ to Entities. Only initializers, entity members, and entity navigation properties are supported.'
			# See
			# https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/insert-update-and-delete-operations
			# FirstOrDefault can handle null without throwing an exception.
			# Only use it when you do not need a record.
			msg = ex.Message
			if not self._errors.Contains(msg):
				self._errors.Enqueue(msg)
			return None
		finally:
		return None

	GetById = staticmethod(GetById)