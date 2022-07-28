from System import *
from System.Collections.Generic import *
from System.Linq import *
# using System.Text;
from System.Data.SQLite.Linq import *
from System.Data.Entity import *
from System.Data.Entity.ModelConfiguration.Conventions import *
from System.Data.SQLite import *
# See https://damienbod.com/2013/11/14/using-sqlite-with-net/
class MapDicerContext(DbContext):
	def __init__(self):
		pass
	# can't derive from sealed class System.Data.SQLite.SQLiteContext
	def get_Layers(self):

	def set_Layers(self, value):

	Layers = property(fget=get_Layers, fset=set_Layers)

	def get_Lods(self):

	def set_Lods(self, value):

	Lods = property(fget=get_Lods, fset=set_Lods)

	def get_Mapblocks(self):

	def set_Mapblocks(self, value):

	Mapblocks = property(fget=get_Mapblocks, fset=set_Mapblocks)

	def get_Regions(self):

	def set_Regions(self, value):

	Regions = property(fget=get_Regions, fset=set_Regions)

	def get_Terrains(self):

	def set_Terrains(self, value):

	Terrains = property(fget=get_Terrains, fset=set_Terrains)

	def __init__(self):
		pass
	# MessageBox.Show(String.Format("Connection string: {0}", SettingModel.SqlConnectionString));
	def OnModelCreating(self, modelBuilder):
		# Do not pluralize table names.
		modelBuilder.Conventions.Remove()
		self.OnModelCreating(modelBuilder)