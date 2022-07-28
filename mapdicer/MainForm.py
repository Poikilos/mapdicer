#
# * Created by SharpDevelop.
# * User: Jatlivecom
# * Date: 7/28/2022
# * Time: 6:58 AM
# *
# * To change this template use Tools | Options | Coding | Edit Standard Headers.
#
from System import *
from System.Collections.Generic import *
from System.Drawing import *
from System.Windows.Forms import *
# Added for SharpDevelop:
from System.Windows.Media.Imaging import * # PresentationCore.dll (provides WriteableBitmap)
from System.Windows.Media import * # PresentationCore.dll (provides Visual)
from System.Windows.Shapes import * # PresentationFramework.dll (provides Ellipse)
from MapDicer.Models import *
from System.Collections.ObjectModel import * # System.ObjectModel.dll (provides ObservableCollection)

class TouchEventArgs(EventArgs):
    pass

class MouseButtonEventArgs(EventArgs):
    pass

class DependencyPropertyChangedEventArgs(EventArgs):
    pass

class MainForm(Form):
    """ <summary>
     Description of MainForm.
     </summary>
    """ # TODO: draw more than one tile at once.
    def afterBrushSize(self):
        pass

    def afterSize(self, InitializeBrush):
        self._touchSize = Math.Max(self._Height / 800, 1) * 16
        self._terrainBrushSizeSlider.Minimum = 1
        self._terrainBrushSizeSlider.Maximum = self._touchSize * 8
        if InitializeBrush:
            MainWindow.brushColorShape.Width = self._touchSize * 2
        # Always set H since W changes elsewhere:
        MainWindow.brushColorShape.Height = MainWindow.brushColorShape.Width
        if InitializeBrush:
            self._terrainBrushSizeSlider.Value = MainWindow.brushColorShape.Width
        self.afterBrushSize()
        if self._mapViewer.Visibility == Visibility.Visible:
            self.UpdateMapViewerSize()

    # <summary>
    # Indexed by the micro-position
    # </summary>
    # private Dictionary<long, ImageSource> mbSources = new Dictionary<long, ImageSource>();
    # <summary>
    # Indexed by the macro position
    # </summary>
    # private System.Windows.Forms.Panel mapViewer; # Added for SharpDevelop (Add the Panel subclass manually so Forms designer doesn't break)
    def UpdateMapViewerSize(self):
        self._mapViewer.Height = self._ActualHeight - self._menuGrid.ActualHeight

    def __init__(self):
        self._touchSize = 16
        self._thisMP = None
        self._brushColorShape = Ellipse()
        self._prefillTerrainRed = 128
        self._prefillTerrainGreen = 128
        self._prefillTerrainBlue = 128
        self._suppressNewWindow = False
        self._touching = False
        self._InitStateNone = 0
        self._InitStateDb = 1
        self._InitStateFull = 2
        self._initState = 0
        self._viewModel = None
        self._mbVisuals = Dictionary[Int64, Visual]()
        self._mbWBs = Dictionary[Int64, WriteableBitmap]()
        #
        # The InitializeComponent() call is required for Windows Forms designer support.
        #
        self.InitializeComponent()
        # Added for SharpDevelop (Add the Panel subclass manually so Forms designer doesn't break)
        # this.mapViewer = new System.Windows.Forms.Panel();
        self._mapViewer = MapViewer()
        self._mainTLP.Controls.Add(self._mapViewer, 0, 1)
        self._mapViewer.Location = System.Drawing.Point(3, 69)
        self._mapViewer.Name = "mapViewer"
        self._mapViewer.Size = System.Drawing.Size(325, 190)
        self._mapViewer.TabIndex = 1
        self._viewModel = ViewModel()
        self._viewModel.Parent = self
        self._DataContext = self._viewModel
        self.afterSize(True)
        MainWindow.thisMP = self
        self.ShowSplash()
        try:
            self._terrainImage.Source = BitmapImage(Uri(System.IO.Path.Combine(System.Environment.CurrentDirectory, "Assets", "terrain.png")))
        except System.IO.FileNotFoundException, ex:
            Console.Error.WriteLine(ex.ToString())
        finally:

    def ShowSplash(self):
        try:
            self._image.Source = BitmapImage(Uri(System.IO.Path.Combine(System.Environment.CurrentDirectory, "Assets", "splash.png")))
            self._image.Visibility = Visibility.Visible
        except System.IO.FileNotFoundException, ex:
            Console.Error.WriteLine(ex.ToString())
        finally:

    def ReloadDatabase(self):
        self._initState = self._InitStateNone
        self._mapViewer.IsNewDatabase = True
        self.ShowSplash()
        self._viewModel.Lods.Clear()
        self._viewModel.Regions.Clear()
        self._viewModel.Mapblocks.Clear()
        self._viewModel.Terrains.Clear()
        self.StartLoadStateThread()

    def TerrainColorBtnClick(self, sender, e):
        pass

    # goToAddTerrain();
    def TerrainBtnClick(self, sender, e):
        if not self._suppressNewWindow:
            self.goToAddTerrain()

    def MainFormResize(self, sender, e):
        self.afterSize(True)

    def TerrainBrushSizeSliderScroll(self, sender, e):
        MainWindow.brushColorShape.Width = self._terrainBrushSizeSlider.Value
        self.afterSize(False)

    #
    # private void AddTerrain(Terrain terrain, double r, double g, double b)
    # {
    # }
    #
    #
    # private void AddTerrain(string name, double r, double g, double b)
    # {
    # MainWindow.brushColorShape.Fill = new SolidColorBrush(Color.FromArgb(255, (byte)r, (byte)g, (byte)b));
    # this.terrainCBx.Items.Add(new TerrainButton(name, r, g, b));
    # for (int i = 0; i < this.terrainCBx.Items.Count; i++)
    # {
    # if ((string)((TerrainButton)this.terrainCBx.Items[i]).Content == name)
    # {
    # this.terrainCBx.SelectedIndex = i;
    # break;
    # }
    # }
    # }
    #
    def GetTerrainImageSource(self, terrainId):
        terrain = Terrain.GetById(terrainId)
        return BitmapImage(Uri(System.IO.Path.Combine(SettingController.DataPath, terrain.Path)))

    def ShowTerrain(self, terrain):
        if (terrain != None):
            MainWindow.brushColorShape.Fill = SolidColorBrush(terrain.GetColor())
            self._terrainColorEllipse.Fill = MainWindow.brushColorShape.Fill
            try:
                self._terrainImage.Source = BitmapImage(Uri(System.IO.Path.Combine(SettingController.DataPath, terrain.Path)))
            except System.IO.FileNotFoundException, ex:
                MessageBox.Show(String.Format("{0} is missing or inaccessible.", terrain.Path), "File Error")
                try:
                    self._terrainImage.Source = BitmapImage(Uri(System.IO.Path.Combine(System.Environment.CurrentDirectory, "Assets", "terrain.png")))
                except System.IO.FileNotFoundException, innerEx:
                    Console.Error.WriteLine(innerEx.ToString())
                finally:
            finally:
        else:
            #
            # if (((TerrainButton)this.terrainCBx.SelectedItem).Content.Equals(SettingModel.NewIdStr)) {
            # try
            # {
            # if (!suppressNewWindow)
            # {
            # goToAddTerrain();
            # }
            # }
            # catch (System.ArgumentException ex)
            # {
            # // The system gave us the page, not the add terrain page.
            # }
            # }
            #
            try:
                self._terrainImage.Source = BitmapImage(Uri(System.IO.Path.Combine(System.Environment.CurrentDirectory, "Assets", "terrain.png")))
            except System.IO.FileNotFoundException, ex:
                Console.Error.WriteLine(ex.ToString())
            finally:

    def BrushTerrainCBxSelectedIndexChanged(self, sender, e):
        # deprecated: See terrainCB instead.
        self.ShowTerrain(self._terrainCBx.SelectedItem)

    def goToAddTerrain(self):
        # this.Frame.Navigate(typeof(NewTerrainPage), null);
        # ^ Don't do that, it generates a new page.
        dlg = NewTerrainWindow()
        dlg.prefill(self._prefillTerrainRed, self._prefillTerrainGreen, self._prefillTerrainBlue, 32, 1)
        # ^ widgets are null at this point apparently
        result = dlg.ShowDialog()
        self._prefillTerrainRed = dlg.Red
        self._prefillTerrainGreen = dlg.Green
        self._prefillTerrainBlue = dlg.Blue
        if result == True:
            # string textTrim = contentDialog.TerrainName;
            # string textTrim = contentDialog.Terrain.Name;
            # if (textTrim.Length > 0)
            if dlg.NewEntry != None:
                self._viewModel.Terrains.Add(dlg.NewEntry)
                self._terrainCBx.SelectedIndex = self._viewModel.Terrains.Count - 1
                # AddTerrain(dlg.Terrain, dlg.Red, dlg.Green, dlg.Blue);
                dlg.NewEntry = None
            else:
                MessageBox.Show("The New Terrain was not valid.")
        elif result == False:
        else:
            # MessageBox.Show("You cancelled adding the terrain.");
            MessageBox.Show("The result of the dialog was null.")

    def SettingsButtonClick(self, sender, e):
        # Custom context menu moved from settingsEditorSettingsMI_Click
        # for SharpDevelop (There was only one item anyway
        # --settingsLayersMI_Click event binding was commented and
        # the handler was empty):
        # this.settingsCM.IsOpen = true;
        dlg = EditorSettingsWindow()
        result = dlg.ShowDialog()
        if result == True:
            if SettingController.NewDB:
                self.ReloadDatabase()

    def DetailBtnClick(self, sender, e):
        SettingController.Start()
        dlg = LodWindow()
        result = dlg.ShowDialog()
        if result == True:
            # saved to database already in this case, so:
            if dlg.NewEntry != None:
                self._viewModel.Lods.Add(dlg.NewEntry)
                dlg.NewEntry = None
            if dlg.ChangedEntry != None:
                found = -1
                # foreach (Lod lod in this.viewModel.Lods)
                i = 0
                while i < self._viewModel.Lods.Count:
                    if self._viewModel.Lods[i].LodId == dlg.ChangedEntry.LodId:
                        # this.viewModel.Lods.Add(dlg.ChangedEntry);
                        # lod.Name = dlg.ChangedEntry.Name;
                        # dlg.ChangedEntry = null;
                        found = i
                        self._viewModel.Lods.RemoveAt(i)
                        break
                    i += 1
                if found > -1:
                    self._viewModel.Lods.Insert(found, dlg.ChangedEntry)
                    dlg.ChangedEntry = None
                if dlg.ChangedEntry != None:
                    MessageBox.Show("The changed entry wasn't in the list.")
                    dlg.ChangedEntry = None

    def Enable(self, enable):
        #Here update your label, button or any string related object.
        #Dispatcher.CurrentDispatcher.Invoke(DispatcherPriority.Background, new ThreadStart(delegate { }));
        Application.Current.Dispatcher.Invoke(DispatcherPriority.Background, ThreadStart())

    # skeletonImage.Visibility = enable ? Visibility.Hidden : Visibility.Visible; // hide skeleton when enabled
    def LoadLodsSafe(self, reloadIds):
        Application.Current.Dispatcher.Invoke(DispatcherPriority.Background, ThreadStart())
 # Make sure this doesn't run again.
    # The timer will fill in everything dependent upon selected Lod.
    def LoadState(self, o):
        self.ReloadState(o)

    def ReloadState(self, reloadIds):
        self.Enable(False)
        #Enable(false);
        # LodId // short
        # Name // string
        # ParentLodId // short
        # UnitsPerSample // long; calculated
        # SamplesPerMapblock // int
        # IsLeaf // bool; calculated&saved
        self.LoadLodsSafe(reloadIds)

    # Enable(true); // don't enable until InitStateFull
    def MainFormLoad(self, sender, e):
        ok = True
        if not Terrain.Test():
            ok = False
        if not ok:
            System.Windows.Application.Current.Shutdown()
        self.StartLoadStateThread()

    def StartLoadStateThread(self):
        th = Thread(LoadState)
        th.Start(True)
 # parameterized (true becomes the object param for LoadState)
    def dispatcherTimer_Tick(self, sender, e):
        msg = ""
        if self._viewModel.Terrains.Count > 0:
            self._terrainCBx.SelectedIndex = self._viewModel.Terrains.Count - 1
        else:
            msg += "There are no terrains yet. "
        if self._viewModel.Lods.Count > 0:
            self._lodCBx.SelectedIndex = self._viewModel.Lods.Count - 1
        else:
            msg += "There are no Levels of Detail yet. "
        #
        # if (this.viewModel.Regions.Count > 0)
        # this.regionCBx.SelectedIndex = this.viewModel.Regions.Count - 1;
        # else
        # msg += "There are no Regions in this level of detail yet. ";
        #
        # if (this.viewModel.Mapblocks.Count > 0)
        # this.mapblockCBx.SelectedIndex = this.viewModel.Mapblocks.Count - 1;
        # else
        # msg += "There are no Mapblocks in this level of detail yet. "; // region doesn't matter
        #
        if msg.Length > 0:
            MessageBox.Show(msg + " Try adding some using the corresponding picture button by the empty selection box.")
        dispatcherTimer.Stop()
        dispatcherTimer = None
        self._initState = self._InitStateFull
        self._image.Visibility = Visibility.Hidden
        self._image.Source = None
        self.Enable(True)

    def RegionBtnClick(self, sender, e):
        SettingController.Start()
        if self._viewModel.SelectedLod == None:
            MessageBox.Show("You must select a Level of Detail before adding or changing regions.")
            return
        dlg = RegionWindow(self._viewModel.SelectedLod.LodId)
        result = dlg.ShowDialog()
        if result == True:
            # saved to database already in this case, so:
            if dlg.NewEntry != None:
                self._viewModel.Regions.Add(dlg.NewEntry)
                dlg.NewEntry = None

    def MapblockBtnClick(self, sender, e):
        SettingController.Start()
        if self._viewModel.SelectedLod == None:
            MessageBox.Show("You must select a Level of Detail, Region and Terrain before adding or changing mapblocks.")
            return
        if self._viewModel.SelectedRegion == None:
            MessageBox.Show("You must select a Region and Terrain before adding or changing mapblocks.")
            return
        if self._viewModel.SelectedTerrain == None:
            MessageBox.Show("You must select a Terrain before adding or changing mapblocks.")
            return
        dlg = MapblockWindow(self._viewModel.SelectedLod.LodId, self._viewModel.SelectedRegion.RegionId, self._viewModel.SelectedTerrain.TerrainId)
        result = dlg.ShowDialog()
        if result == True:
            # saved to database already in this case, so:
            if dlg.NewEntry != None:
                self._viewModel.Mapblocks.Add(dlg.NewEntry)
                dlg.NewEntry = None

    # private Dictionary<long, BitmapImage> bitmapCache = new Dictionary<long, BitmapImage>();
    def LoadMapBlock(self, mapblock):
        pass

    # TODO: finish this
    def ClearLodDependents(self):
        self._viewModel.Regions.Clear()
        self._viewModel.Mapblocks.Clear()
        self._viewModel.SelectedRegion = None
        enumerator = mbVisuals.GetEnumerator()
        while enumerator.MoveNext():
            entry = enumerator.Current
            self._mapViewer.RemoveVisual(entry.Value)
        self._mbVisuals.Clear()
        self._mbWBs.Clear()

    def LoadLodDependents(self):
        if self._viewModel.SelectedLod != None:
            enumerator = Region.WhereLodIdEquals(self._viewModel.SelectedLod.LodId).GetEnumerator()
            while enumerator.MoveNext():
                entry = enumerator.Current
                self._viewModel.Regions.Add(entry)
            if self._viewModel.Regions.Count > 0:
                self._regionCBx.SelectedIndex = self._viewModel.Regions.Count - 1
            badMBs = List[Mapblock]()
            lod = self._viewModel.SelectedLod
            enumerator = Mapblock.WhereLodIdEquals(self._viewModel.SelectedLod.LodId).GetEnumerator()
            while enumerator.MoveNext():
                entry = enumerator.Current
                macroPos = MapDicerPos(entry.MapblockId)
                msg = String.Format("~ Trying +mapblock:{0},{1}", macroPos.X, macroPos.Y)
                Console.Error.WriteLine(msg)
                path = entry.GetImagePath(True)
                wb = None
                if not File.Exists(path):
                    badMBs.Add(entry)
                    Console.Error.WriteLine("  FAILED (missing image)")
                    wb = MapViewer.NewWriteableBitmap(lod)
                else:
                    bitmap = BitmapImage(Uri(path))
                    wb = WriteableBitmap(bitmap)
                self._mbWBs[entry.MapblockId] = wb
                srcRect = Int32Rect()
                srcRect.Width = 1
                srcRect.Height = 1
                childLod = Lod.GetChild(entry.LodId)
                parentLod = Lod.GetById(entry.LodId).Parent
                childSamplesPerMapblock = 1
                if childLod != None:
                    childSamplesPerMapblock = childLod.SamplesPerMapblock
                parentSamplesPerMapblock = 1
                if parentLod != None:
                    parentSamplesPerMapblock = parentLod.SamplesPerMapblock
                msg = String.Format("  > mapblock:{0},{1}", macroPos.X, macroPos.Y)
                Console.Error.WriteLine(msg)
                pixel = Array.CreateInstance(Byte, 4)
                width = wb.Width
                height = wb.Height
                y = 0
                while y < width:
                    srcRect.X = 0
                    x = 0
                    while x < height: # TODO: Improve this--this is usually correct though.
                        microPos = MapDicerPos(LodId = (macroPos.LodId - 1), LayerId = macroPos.LayerId, X = (macroPos.X * lod.SamplesPerMapblock + x), Z = (macroPos.Z * lod.SamplesPerMapblock + y))
                        # ^ The microPos must become a bigger number since it is in the on-screen tile size.
                        offsetX = macroPos.X * lod.SamplesPerMapblock
                        offsetY = macroPos.Z * lod.SamplesPerMapblock
                        imageX = microPos.X - offsetX
                        imageY = microPos.Z - offsetY
                        #
                        # msg = String.Format("  + mapblock:{0},{1} global:{2},{3} offset:{4},{5} relative:{6},{7}",
                        # macroPos.X, macroPos.Y, microPos.X, microPos.Y, offsetX, offsetY, imageX, imageY);
                        # Console.Error.WriteLine(msg);
                        #
                        try:
                            wb.CopyPixels(srcRect, pixel, 4, 0)
                        except System.ArgumentException, ex:
                            MessageBox.Show(String.Format("srcRect {0} was out of range in {1}x{2}.", srcRect, width, height))
                            y = height
                            break
                        finally:
                        if pixel[3] > 0:
                            tid = Terrain.IdFromColorRgb(pixel[2], pixel[1], pixel[0])
                            if self._mbVisuals.TryGetValue(microPos.getSliceAsInteger(), ):
                                self._mapViewer.RemoveVisual(visual)
                                self._mbVisuals.Remove(microPos.getSliceAsInteger())
                                Console.Error.WriteLine(String.Format("ERROR: Duplicate sub-id (micro-scale MapblockId) {0} for {1} in Mapblock {2} with {3} samples per mapblock", microPos.getSliceAsInteger(), microPos.Dump(), macroPos.Dump(), lod.SamplesPerMapblock))
                            relativeMVPoint = self._mapViewer.GetPxPos(microPos)
                            visual = self._mapViewer.Add(relativeMVPoint, self.GetTerrainImageSource(tid), Terrain.GetById(tid).PixPerSample)
                            self._mbVisuals.Add(microPos.getSliceAsInteger(), visual)
                        srcRect.X += 1
                        x += 1
                    srcRect.Y += 1
                    y += 1
                self._viewModel.Mapblocks.Add(entry)
                self.LoadMapBlock(entry)
            # TODO: remove each mapblock in badMBs (may not be necessary since image gets generated if missing)
            if self._viewModel.Mapblocks.Count > 0:
                self._regionCBx.SelectedIndex = self._viewModel.Mapblocks.Count - 1

    def LodCBxSelectedIndexChanged(self, sender, e):
        self.ClearLodDependents()
        self.LoadLodDependents()

    def TerrainCBxSelectedIndexChanged(self, sender, e):
        if self._viewModel.SelectedTerrain != None:
            self.ShowTerrain(self._viewModel.SelectedTerrain)
            color = Terrain.ColorFromId(self._viewModel.SelectedTerrain.TerrainId)
            self._prefillTerrainRed = color.R
            self._prefillTerrainGreen = color.G
            self._prefillTerrainBlue = color.B

    # TODO: (optional) Change the prefill values for new colors to avoid primary key
    # constraint violations in case the user doesn't change the color:
    #
    # if (prefillTerrainRed < 255)
    # prefillTerrainRed += 1;
    # else
    # prefillTerrainRed -= 1;
    # if (prefillTerrainGreen < 255)
    # prefillTerrainGreen += 1;
    # else
    # prefillTerrainGreen -= 1;
    # if (prefillTerrainBlue < 255)
    # prefillTerrainBlue += 1;
    # else
    # prefillTerrainBlue -= 1;
    #
    def mapViewer_IsVisibleChanged(self, sender, e):
        # TODO: bind this in WinForms (SharpDevelop branch)
        if self._mapViewer.Visibility == Visibility.Visible:
            self.UpdateMapViewerSize()

    def mapViewer_Interaction(self, relativeMVPoint):
        """ <summary>
         Handle touch or click on the mapViewer. Add new ids to the mapblock image. Create a new mapblock
         if one doesn't exist at the clicked location.
         </summary>
         <param name="point">The point must be relative to mapViewer.</param>
        """
        # TODO: bind this in WinForms (SharpDevelop branch) -- only bind callers, not this itself
        msg = ""
        if self._viewModel.SelectedLod == None:
            MessageBox.Show("You must select a level of detail to expand a region through drawing.")
            return
        if self._viewModel.SelectedRegion == None:
            MessageBox.Show(String.Format("You must select a region (a {0}) to expand it through drawing.", self._viewModel.SelectedLod.Name))
            return
        if self._viewModel.SelectedTerrain == None:
            MessageBox.Show("You must select a terrain to draw.")
            return
        region = self._viewModel.SelectedRegion
        lod = self._viewModel.SelectedLod
        terrain = self._viewModel.SelectedTerrain
        layerId = self._viewModel.SelectedLayerId
        subLodId = (lod.LodId + 1) # TODO improve this. This is usually correct though.
        microPos = self._mapViewer.GetWorldMapDicerPos(relativeMVPoint, subLodId, self._viewModel.SelectedLayerId)
        if not self._mapViewer.IsNewWrite(microPos):
            return
        self._mapViewer.MarkAsWritten(microPos)
        # ^ Mark as written before written to avoid retrying on the same drag.
        # If we are in a region such as a province,
        # we draw province pixels (each pixel is displayed as a map tile).
        # If the current lod doesn't have an image here, create one.
        # At this point in the code, microPos is the child location (image pixel coordinates for saving).
        # We need the number of the mapblock within the lod.
        macroPos = MapDicerPos(LodId = lod.LodId, LayerId = layerId, X = (microPos.X / lod.SamplesPerMapblock), Z = (microPos.Z / lod.SamplesPerMapblock))
        existing = Mapblock.GetById(macroPos.getSliceAsInteger())
        mapblock = existing
        if existing == None:
            mapblock = SettingController.GenerateBlock(macroPos, region.RegionId, terrain.TerrainId)
            newWB = MapViewer.NewWriteableBitmap(lod)
            self._mbWBs.Add(mapblock.MapblockId, newWB)
            # ^ If didn't load at startup and wasn't deleted, may already exist here from a previous
            # stroke: "System.ArgumentException: 'An item with the same key has already been added.'"
            error = Mapblock.Insert(mapblock)
            if error.Length > 0:
                msg = String.Format("The mapblock didn't load at startup, probably due to" + "missing \"{0}\". MapblockId:{1} GetSliceAsInteger:{2} error: {3}", mapblock.GetImagePath(True), mapblock.MapblockId, macroPos.getSliceAsInteger(), error)
                MessageBox.Show(msg)
        offsetX = macroPos.X * lod.SamplesPerMapblock
        offsetY = macroPos.Z * lod.SamplesPerMapblock
        imageX = microPos.X - offsetX
        imageY = microPos.Z - offsetY
        msg = String.Format("SetPixel on mapblock:{0},{1} global:{2},{3} offset:{4},{5} relative:{6},{7}", macroPos.X, macroPos.Y, microPos.X, microPos.Y, offsetX, offsetY, imageX, imageY)
        self._statusTB.Text = msg
        Console.Error.WriteLine(msg)
        if not self._mbWBs.ContainsKey(macroPos.getSliceAsInteger()):
            msg = String.Format("Error: Generated {0} but tried to use {1}", mapblock.MapblockId, macroPos.getSliceAsInteger())
            MessageBox.Show(msg)
            return
        wb = self._mbWBs[macroPos.getSliceAsInteger()]
        ByteMap.WritePixelTo(wb, imageX, imageY, terrain.GetColor())
        path = Mapblock.GetImagePath(macroPos.getSliceAsInteger(), True)
        Console.Error.WriteLine(String.Format("^ saving image {0}", path))
        ByteMap.SaveWriteableBitmap(path, wb)
        if self._mbVisuals.TryGetValue(microPos.getSliceAsInteger(), ):
            self._mapViewer.RemoveVisual(visual)
            self._mbVisuals.Remove(microPos.getSliceAsInteger())
        visual = self._mapViewer.Add(relativeMVPoint, self._terrainImage.Source, terrain.PixPerSample)
        self._mbVisuals.Add(microPos.getSliceAsInteger(), visual)

    def mapViewer_MouseLeftButtonDown(self, sender, e):
        self.mapViewer_Interaction(e.GetPosition(self._mapViewer))
        self._touching = True

    def mapViewer_TouchDown(self, sender, e):
        self.mapViewer_Interaction(e.GetTouchPoint(self._mapViewer).Position)
        self._touching = True

    def mapViewer_TouchUp(self, sender, e):
        self._touching = False

    def mapViewer_LostTouchCapture(self, sender, e):
        self._touching = False

    def mapViewer_TouchLeave(self, sender, e):
        self._touching = False

    def mapViewer_TouchMove(self, sender, e):
        if self._touching:
            self.mapViewer_Interaction(e.GetTouchPoint(self._mapViewer).Position)

    def mapViewer_DragOver(self, sender, e):
        self.mapViewer_Interaction(e.GetPosition(self._mapViewer))

    def mapViewer_MouseUp(self, sender, e):
        self._touching = False

    def mapViewer_MouseMove(self, sender, e):
        if self._touching:
            self.mapViewer_Interaction(e.GetPosition(self._mapViewer))

    def mapViewer_MouseLeave(self, sender, e):
        self._touching = False

class ViewModel(object):
    def get_Lods(self):

    def set_Lods(self, value):

    Lods = property(fget=get_Lods, fset=set_Lods)

    def get_Regions(self):

    def set_Regions(self, value):

    Regions = property(fget=get_Regions, fset=set_Regions)

    # ^ otherwise ambiguous with System.Drawing.Region
    def get_Mapblocks(self):

    def set_Mapblocks(self, value):

    Mapblocks = property(fget=get_Mapblocks, fset=set_Mapblocks)

    def get_Terrains(self):

    def set_Terrains(self, value):

    Terrains = property(fget=get_Terrains, fset=set_Terrains)

    def get_SelectedLayerId(self):
        return SettingController.LayerWhenOnly1

    SelectedLayerId = property(fget=get_SelectedLayerId)

    def __init__(self):
        self._Parent = None
        self.Lods = ObservableCollection[Lod]()
        self.Regions = ObservableCollection[Region]()
        self.Mapblocks = ObservableCollection[Mapblock]()
        self.Terrains = ObservableCollection[Terrain]()

    def get_SelectedLodId(self):
        return self._selectedLodId

    def set_SelectedLodId(self, value):
        self._selectedLodId = value

    SelectedLodId = property(fget=get_SelectedLodId, fset=set_SelectedLodId)

    def get_SelectedLod(self):
        return self._selectedLod

    def set_SelectedLod(self, value):
        self._selectedLod = value

    SelectedLod = property(fget=get_SelectedLod, fset=set_SelectedLod)

    def get_SelectedRegionId(self):
        return self._selectedRegionId

    def set_SelectedRegionId(self, value):
        self._selectedRegionId = value

    SelectedRegionId = property(fget=get_SelectedRegionId, fset=set_SelectedRegionId)

    def get_SelectedRegion(self):
        return self._selectedRegion

    def set_SelectedRegion(self, value):
        self._selectedRegion = value

    SelectedRegion = property(fget=get_SelectedRegion, fset=set_SelectedRegion)

    def get_SelectedMapblockId(self):
        return self._selectedMapblockId

    def set_SelectedMapblockId(self, value):
        self._selectedMapblockId = value

    SelectedMapblockId = property(fget=get_SelectedMapblockId, fset=set_SelectedMapblockId)

    def get_SelectedMapblock(self):
        return self._selectedMapblock

    def set_SelectedMapblock(self, value):
        self._selectedMapblock = value

    SelectedMapblock = property(fget=get_SelectedMapblock, fset=set_SelectedMapblock)

    def get_SelectedTerrainId(self):
        return self._selectedTerrainId

    def set_SelectedTerrainId(self, value):
        self._selectedTerrainId = value

    SelectedTerrainId = property(fget=get_SelectedTerrainId, fset=set_SelectedTerrainId)

    def get_SelectedTerrain(self):
        return self._selectedTerrain

    def set_SelectedTerrain(self, value):
        self._selectedTerrain = value

    SelectedTerrain = property(fget=get_SelectedTerrain, fset=set_SelectedTerrain)
