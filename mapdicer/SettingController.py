from MapDicer.Models import *
from System import *
from System.Collections.Generic import *
from System.Data.SQLite import *
from System.IO import *
from System.Linq import *
from System.Text import *
from System.Text.RegularExpressions import *

class SettingController(object):
    def Start():
        if self._started:
            return
        self._started = True
        # The static constructor runs when the first instance is created or the first static member
        # is accessed (even if this method is empty).
        SettingController.InitializeDB()

    Start = staticmethod(Start)

    def InitializeDB():
        if self._loadedCS != SettingModel.SqlConnectionString:
            self._loadedCS = SettingModel.SqlConnectionString
            self._NewDB = True
            SettingController.EnsureTables()
            SettingController.EnsureSampleData()

    InitializeDB = staticmethod(InitializeDB)

    def get_DataPath(self):
        DbPath = SettingModel.DbFullPath
        fi = FileInfo(DbPath)
        DbNoExt = Path.GetFileNameWithoutExtension(DbPath)
        DbDirPath = fi.Directory.FullName
        DataDirName = DbNoExt + "_files"
        return Path.Combine(DbDirPath, DataDirName)

    DataPath = property(fget=get_DataPath)

    def get_MapblockImageDotExt(self):
        return ".png"

    MapblockImageDotExt = property(fget=get_MapblockImageDotExt)

    # <summary>
    # This must be 96 for WPF or WPF will scale the WriteableBitmap (See
    # <https://www.hanselman.com/blog/be-aware-of-dpi-with-image-pngs-in-wpf-images-scale-weird-or-are-blurry>)
    # </summary>
    def get_DpiForNonViewableData(self):
        return 96

    DpiForNonViewableData = property(fget=get_DpiForNonViewableData)

    def Import(path, category, id, overwrite):
        """ <summary>
         Import the file to DataPath in the given category as a subfolder.
         </summary>
         <param name="path">The original file to move</param>
         <param name="category">Use this subdirectory under DataPath.</param>
         <param name="id">The new filename, or null to retain filename (extension from path is
         <param name="overwrite">Overwrite any existing file (at return path--see returns).</param>
         <returns>The new path relative to DataPath, without a leading slash.</returns>
        """
        return SettingController.Import(path, category, id, overwrite, False, True)

    Import = staticmethod(Import)

    def Import(path, category, id, overwrite, dryRun, makeDirs):
        category = category.Replace('\\', '/')
        fileName = None
        if id != None:
            dotExt = Path.GetExtension(path)
            # Remove invalid file name characters:
            regex = String.Format("[{0}]", Regex.Escape(System.String(Path.GetInvalidFileNameChars())))
            removeInvalidChars = Regex(regex, RegexOptions.Singleline | RegexOptions.Compiled | RegexOptions.CultureInvariant)
            id = removeInvalidChars.Replace(id, "_")
            # ^ See Jan's answer on
            # <https://stackoverflow.com/questions/146134/how-to-remove-illegal-characters-from-path-and-filenames>
            fileName = id + dotExt
        else:
            if path != None:
                fileName = Path.GetFileName(path)
            elif not dryRun:
                raise ApplicationException("You cannot use a null path unless there is an id.")
        catPath = Path.Combine(self.DataPath, category)
        if makeDirs:
            if not Directory.Exists(self.DataPath):
                Directory.CreateDirectory(self.DataPath)
            if not Directory.Exists(catPath):
                Directory.CreateDirectory(catPath)
        # TODO: allow category to contain a slash
        relPath = Path.Combine(category, fileName)
        newPath = Path.Combine(self.DataPath, relPath)
        if not dryRun:
            File.Copy(path, newPath, overwrite)
        return relPath

    Import = staticmethod(Import)

    def GetImportRelPath(path, category, id, makeDirs):
        """ <summary>
         Get the path to which the file would be imported including the filename. See
         public static Import for documentation.
         </summary>
         <param name="path"></param>
         <param name="category"></param>
         <param name="id"></param>
         <param name="makeDirs"></param>
         <returns></returns>
        """
        return SettingController.Import(path, category, id, False, True, makeDirs)

    GetImportRelPath = staticmethod(GetImportRelPath)

    def GetImportFullPath(path, category, id, makeDirs):
        """ <summary>
         Get the path to which the file would be imported including the filename. See
         public static Import for documentation.
         </summary>
         <param name="path"></param>
         <param name="category"></param>
         <param name="id"></param>
         <param name="makeDirs"></param>
         <returns></returns>
        """
        return Path.Combine(self.DataPath, SettingController.Import(path, category, id, False, True, makeDirs))

    GetImportFullPath = staticmethod(GetImportFullPath)

    def __init__():
        self._started = False
        self._LayerWhenOnly1 = 0
        self._NewDB = True
        self._loadedCS = None
        self.Start()

    # Properties.Settings.Default.PropertyChanged += SettingModel.PropertyChangedCallback_Event;
    def TrySql(sql, sc):
        """ <summary>
         Try a sql command, otherwise return an exception.
         </summary>
         <param name="sql">SQLite-flavored SQL code</param>
         <param name="sc">The SQLiteConnection</param>
         <returns>Exception or null</returns>
        """
        try:
        except SQLiteException, ex:
            # probably already exists
            return ex
        finally:
        return None

    TrySql = staticmethod(TrySql)

    def IntParseOrDefault(text, defaultValue):
        ok = int.TryParse(text, )
        return result if ok else defaultValue

    IntParseOrDefault = staticmethod(IntParseOrDefault)

    def EnsureSampleData():
        layer = Layer()
        layer.LayerId = SettingController.LayerWhenOnly1
        layer.Name = "terrain"
        layer.Num = 0
        try:
            Layer.Insert(layer)
        except , :
        finally:

    EnsureSampleData = staticmethod(EnsureSampleData)

    # TODO: this assumes it was already added and the problem was a primary key constraint violation
    def EnsureTables():
        # SettingModel.SqlConnectionString = Properties.Settings.Default.DbConnectionString;
        if not File.Exists(SettingModel.DbFullPath):
            SQLiteConnection.CreateFile(SettingModel.DbFullPath)

    EnsureTables = staticmethod(EnsureTables)

    # For a description of the fields, see Models. # top should be null
    # + ", Data BLOB" // TODO: (future) Data
    def GenerateBlock(pos, regionId, terrainId):
        """ <summary>
         Generate the block, but do not save an image nor write the entry to the database.
         </summary>
         <param name="pos"></param>
         <param name="regionId"></param>
         <param name="terrainId"></param>
         <returns></returns>
        """
        path = None
        mapblock = Mapblock(MapblockId = pos.getSliceAsInteger(), LodId = pos.LodId, LayerId = pos.LayerId, RegionId = regionId, TerrainId = terrainId, Path = Mapblock.GetImagePath(pos, True))
        return mapblock

    GenerateBlock = staticmethod(GenerateBlock)
