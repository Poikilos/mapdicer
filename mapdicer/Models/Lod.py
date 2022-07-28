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
from System.Linq import * # orderby etc

class Lod(object):
	def get_Mapblocks(self):

	def set_Mapblocks(self, value):

	Mapblocks = property(fget=get_Mapblocks, fset=set_Mapblocks)

	def get_Regions(self):

	def set_Regions(self, value):

	Regions = property(fget=get_Regions, fset=set_Regions)

	def __init__(self):
		# 
		# public void populateMapblocks()
		# {
		# Mapblocks = new List<Mapblock>();
		# }
		# 
		# <summary>
		# The name of this level of detail, such as World or Continent
		# </summary>
		# <summary>
		# The unique parent LOD in the LOD chain
		# </summary>
		# <summary>
		# This is how many pixels are in the square image. The region may contain more than
		# one Mapblock.
		# </summary> # <summary>
		# The statistic is only for display purposes.
		# This stored for caching purposes (to prevent having to traverse to the leaf).
		# </summary>
		# <summary>
		# Whether this is the leaf. You cannot enter a leaf. A leaf is a Node.
		# </summary> # var db = new ...())
		# See
		# https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/insert-update-and-delete-operations
		# FirstOrDefault can handle null without throwing an exception.
		# Only use it when you do not need a record.
		# return null;
		self._errors = Queue[str]()
		self.Mapblocks = List[Mapblock]()
		self.Regions = List[Region]()

	def get_LodId(self):

	def set_LodId(self, value):

	LodId = property(fget=get_LodId, fset=set_LodId)

	def get_Name(self):

	def set_Name(self, value):

	Name = property(fget=get_Name, fset=set_Name)

	def get_ParentLodId(self):

	def set_ParentLodId(self, value):

	ParentLodId = property(fget=get_ParentLodId, fset=set_ParentLodId)

	def get_Parent(self):

	def set_Parent(self, value):

	Parent = property(fget=get_Parent, fset=set_Parent)

	def get_SamplesPerMapblock(self):

	def set_SamplesPerMapblock(self, value):

	SamplesPerMapblock = property(fget=get_SamplesPerMapblock, fset=set_SamplesPerMapblock)

	def get_Child(self):
		return Lod.GetChild(self.LodId)

	Child = property(fget=get_Child)

	def GetNewId():
		return (Lod.LastId() + 1)

	GetNewId = staticmethod(GetNewId)

	def GetIsLeaf(entry):
		return (Lod.GetChild(entry.LodId) == None)

	GetIsLeaf = staticmethod(GetIsLeaf)

	def GetChild(parent):

	GetChild = staticmethod(GetChild)

	def All():
		try:
		except System.ArgumentException, ex:
			# 
			# string msg = String.Format("The database is missing {0}", context.Database.Log);
			# if (!errors.Contains(msg))
			# {
			# errors.Enqueue(msg);
			# }
			# 
			# MessageBox.Show(String.Format("context: {0}", context.Database.Exists()));
			# where entry.Id < 25 # the Last method depends on ascending.
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

	All = staticmethod(All)
 # (*Linq to db*, 2020)
	def Last():

	Last = staticmethod(Last)

	# 
	# string msg = String.Format("The database is missing {0}", context.Database.Log);
	# if (!errors.Contains(msg))
	# {
	# errors.Enqueue(msg);
	# }
	# 
	# where entry.Id < 25 # the Last method depends on ascending.
	def LastId():
		result = -1
		existing = Lod.Last()
		if existing != None:
			result = existing.LodId
		return result

	LastId = staticmethod(LastId)

	def GetById(id):

	GetById = staticmethod(GetById)

	def Insert(newEntry, generateId):
		error = ""
		last = None
		newId = 0
		if generateId:
		# where entry.Id < 25 # the Last method depends on ascending. # last = existing;
		# else assume no entries (leave new entry at 0 if generateId)
		# 
		# newEntry.LodId = 0;
		# if (last != null)
		# newEntry.LodId = (short)(last.LodId + 1);
		# else
		# newEntry.LodId = 0; // Assumes the table is empty or not present.
		# 
		# There may be two inner exceptions such as
		# 1:
		# UpdateException: An error occurred while updating the entries. See the inner exception for details.
		# 2:
		# SQLiteException: constraint failed
		# UNIQUE constraint failed: Lod.LodId
		return error

	Insert = staticmethod(Insert)
 # (*Linq to db*, 2020)
	def Update(entry):
		""" <summary>
		 Update any fields that differ.
		 </summary>
		 <param name="entry">The new version of the lod with the matching LodId</param>
		 <returns>True if ok</returns>
		"""
		ok = False
		# see https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/insert-update-and-delete-operations
		return ok

	Update = staticmethod(Update)

	def Delete(entry):
		ok = False
		return ok

	Delete = staticmethod(Delete)