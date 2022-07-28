from System import *
from System.Collections.Generic import *
# using System.Linq;
from System.Text import *
from System.Data.SQLite import *

class SettingModel(object):
    def get_DbFullPath(self):
        return System.IO.Path.GetFullPath(Properties.Settings.Default.DbFile)

    DbFullPath = property(fget=get_DbFullPath)

    def get_SqlConnectionString(self):
        oldConnectionString = Properties.Settings.Default.DbConnectionString
        if oldConnectionString.Trim().Length == 0:
            conString = SQLiteConnectionStringBuilder()
            fullPath = self.DbFullPath
            conString.DataSource = fullPath
            # conString.ToFullPath = true; // not available
            # conString.FullUri = (new System.Uri(fullPath)).AbsoluteUri;
            # conString.Version = 3;
            conString.ForeignKeys = True # not available
            conString.Flags |= SQLiteConnectionFlags.HidePassword # Flags not available
            # conString.Flags |= SQLiteConnectionFlags.LogAll;
            # conString.Flags |= SQLiteConnectionFlags.UseConnectionPool;
            # conString.Flags |= SQLiteConnectionFlags.UseConnectionTypes;
            # conString.Pooling = true;
            # conString.Source = ":memory:";
            # conString.MaxPageCount = ;
            # maxI = conString.ProgressOps;
            # conString.PageSize = ;
            # conString.Password = ;
            # conString.VfsName = ;
            conString.Add("ProviderName", "SQLite") # not supported by EntityFrameworkCore
            # ^ linq2db.SQLite (<https://github.com/linq2db/examples/blob/master/SQLite/GetStarted/LinqToDB.Templates/CopyMe.SQLite.tt.txt>)
            conString.Add("Database", "MapDicer")
            Properties.Settings.Default.DbConnectionString = conString.ConnectionString
            Properties.Settings.Default.Save()
        return Properties.Settings.Default.DbConnectionString

    SqlConnectionString = property(fget=get_SqlConnectionString)

    # <summary>
    # Get the number of layers per level of detail (also determines y skip to next LOD).
    # Y is the height axis to match Minetest (each realm is MaxLayerCount apart here).
    # </summary>
    def get_MaxLayerCount(self):
        return self._maxLayerCount

    MaxLayerCount = property(fget=get_MaxLayerCount)

    def __init__():
        self._NewIdStr = "(New)"
        self._maxLayerCount = 128
