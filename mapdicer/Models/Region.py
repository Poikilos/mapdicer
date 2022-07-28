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

class Region(object):
	def __init__(self):
		# <summary>
		# The region name, such as the name of the contenent if Lod's name is continent.
		# </summary>
		# <summary>
		# This is the parent.
		# </summary>
		self._errors = Queue[str]()
		Mapblocks = List[Mapblock]()

	def get_Mapblocks(self):

	def set_Mapblocks(self, value):

	Mapblocks = property(fget=get_Mapblocks, fset=set_Mapblocks)

	def get_RegionId(self):

	def set_RegionId(self, value):

	RegionId = property(fget=get_RegionId, fset=set_RegionId)

	def get_Name(self):

	def set_Name(self, value):

	Name = property(fget=get_Name, fset=set_Name)

	def get_LodId(self):

	def set_LodId(self, value):

	LodId = property(fget=get_LodId, fset=set_LodId)

	def get_Lod(self):

	def set_Lod(self, value):

	Lod = property(fget=get_Lod, fset=set_Lod)

	def Insert(newEntry, generateId):
		error = ""
		last = None
		newId = 0
		if generateId:
		# where entry.Id < 25 # the Last method depends on ascending. # last = existing;
		# else assume no entries (leave new entry at 0 if generateId)
		# 
		# newEntry.RegionId = 0;
		# if (last != null)
		# newEntry.RegionId = (short)(last.RegionId + 1);
		# else
		# newEntry.RegionId = 0; // Assumes the table is empty or not present.
		# 
		# There may be two inner exceptions such as
		# 1:
		# UpdateException: An error occurred while updating the entries. See the inner exception for details.
		# 2:
		# SQLiteException: constraint failed
		# UNIQUE constraint failed: Region.RegionId
		return error

	Insert = staticmethod(Insert)
 # (*Linq to db*, 2020)
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