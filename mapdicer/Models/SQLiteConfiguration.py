import clr

from System import *
from System.Collections.Generic import *
from System.Data.Entity import *
from System.Data.Entity.Core.Common import *
from System.Data.SQLite import *
from System.Data.SQLite.EF6 import *
# using System.Data.SQLite.Linq;
# ^ SQLiteProviderFactory can come from either System.Data.SQLite.EF6 or System.Data.SQLite.Linq.
from System.Linq import *
from System.Text import *
# See https://www.codeproject.com/Articles/1158937/SQLite-with-Csharp-Net-and-Entity-Framework?msg=5772111#xx5772111xx
# - This file must be in the same namespace as the DbContext and Models.
class SQLiteConfiguration(DbConfiguration):
	def __init__(self):
		self.SetProviderFactory("System.Data.SQLite", SQLiteFactory.Instance)
		self.SetProviderFactory("System.Data.SQLite.EF6", SQLiteProviderFactory.Instance)
		# SetProviderFactory("System.Data.SQLite.Linq", SQLiteProviderFactory.Instance);
		self.SetProviderServices("System.Data.SQLite", SQLiteProviderFactory.Instance.GetService(clr.GetClrType(DbProviderServices)))