from MapDicer.Models import *
from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *
from System.Windows import *
from System.Windows.Controls import *
from System.Windows.Media import *
from System.Windows.Media.Imaging import *

class MapViewer(Panel):
	""" <summary>
	 This is a special panel that accepts images.
	 See http://windowspresentationfoundationinfo.blogspot.com/2014/07/wpf-visuals.html
	 for a tutorial on accepting visuals.
	 </summary>
	"""
	def __init__(self):
		""" <summary>
		 This is a special panel that accepts images.
		 See http://windowspresentationfoundationinfo.blogspot.com/2014/07/wpf-visuals.html
		 for a tutorial on accepting visuals.
		 </summary>
		"""
		self._zoomPPS = 32
		self._pan = Point(0, 0)
		self._lastDrawnPos = MapDicerPos()
		self._isNewDatabase = True
		# <summary>
		# The zoom is in terms of the number of pixels per sample.
		# </summary>
		self._visuals = List[Visual]()

	def get_IsNewDatabase(self):
		return self._isNewDatabase

	def set_IsNewDatabase(self, value):
		self._isNewDatabase = value

	IsNewDatabase = property(fget=get_IsNewDatabase, fset=set_IsNewDatabase)

	def get_LastDrawnPos(self):
		return self._lastDrawnPos

	LastDrawnPos = property(fget=get_LastDrawnPos)

	def get_ZoomPPS(self):
		return self._zoomPPS

	ZoomPPS = property(fget=get_ZoomPPS)

	def GetVisualChild(self, index):
		return self._visuals[index]

	def get_VisualChildrenCount(self):
		return self._visuals.Count

	VisualChildrenCount = property(fget=get_VisualChildrenCount)

	def AddVisual(self, visual):
		self._visuals.Add(visual)
		self.AddVisualChild(visual)
		self.AddLogicalChild(visual)

	def RemoveVisual(self, visual):
		self._visuals.Remove(visual)
		self.RemoveVisualChild(visual)
		self.RemoveLogicalChild(visual)

	def GetWorldPos(self, relativeMVPoint):
		return Point(X = Math.Floor((relativeMVPoint.X + self._pan.X) / self._zoomPPS), Y = Math.Floor((relativeMVPoint.Y + self._pan.Y) / self._zoomPPS))

	def GetMapDicerPos(self, worldPoint, lodId, layerId):
		return MapDicerPos(LodId = lodId, LayerId = layerId, X = worldPoint.X, Z = worldPoint.Y)
 # ground plane is X-Z as per OpenGL
	def GetWorldMapDicerPos(self, relativeMVPoint, lodId, layerId):
		return self.GetMapDicerPos(self.GetWorldPos(relativeMVPoint), lodId, layerId)

	def GetPxPos(self, worldPoint):
		""" <summary>
		 Get the pixel point of the top left corner of the tile relative to the MapViewer.
		 </summary>
		 <param name="worldPoint">A point containing the X and Z (as Y) from a MapDicerPos</param>
		 <returns></returns>
		"""
		return Point(X = worldPoint.X * self._zoomPPS + self._pan.X, Y = worldPoint.Y * self._zoomPPS + self._pan.Y)

	def GetPxPos(self, microPos):
		return self.GetPxPos(Point(microPos.X, microPos.Z))

	def DrawSquare(self, visual, relativeMVPoint, currentlySelected):
 #draw square from constants
	def IsNewWrite(self, microPos, markAsWritten):
		changed = False
		if microPos.X != self._lastDrawnPos.X:
			changed = True
		elif microPos.Z != self._lastDrawnPos.Z:
			changed = True
		elif microPos.LodId != self._lastDrawnPos.LodId:
			changed = True
		elif microPos.LayerId != self._lastDrawnPos.LayerId:
			changed = True
		if changed and markAsWritten:
			self.MarkAsWritten(microPos)
		return changed

	def IsNewWrite(self, microPos):
		if self._isNewDatabase:
			return True
		changed = False
		if microPos.X != self._lastDrawnPos.X:
			changed = True
		elif microPos.Z != self._lastDrawnPos.Z:
			changed = True
		elif microPos.LodId != self._lastDrawnPos.LodId:
			changed = True
		elif microPos.LayerId != self._lastDrawnPos.LayerId:
			changed = True
		return changed

	def MarkAsWritten(self, microPos):
		self._isNewDatabase = False
		self._lastDrawnPos.LodId = microPos.LodId
		self._lastDrawnPos.LayerId = microPos.LayerId
		self._lastDrawnPos.X = microPos.X
		self._lastDrawnPos.Z = microPos.Z

	def DrawImage(self, visual, imageSource, relativeMVPoint, currentlySelected, pps):
		""" <summary>
		 Draw the image and modify the visual so it is ready to add to the canvas.
		 </summary>
		 <param name="visual">visual to modify using the parameters</param>
		 <param name="imageSource">image to display</param>
		 <param name="relativeMVPoint">a point relative to the MapView instance</param>
		 <param name="currentlySelected">whether highlighted (reserved for future use)</param>
		 <param name="pps">The Pixels Per Sample determines how much of the image fits within on square.</param>
		"""

	# Location = relativeMVPoint,
	def Add(self, relativeMVPoint):
		worldPoint = self.GetWorldPos(relativeMVPoint)
		pointSampleTopLeft = self.GetPxPos(worldPoint)
		visual = DrawingVisual()
		self.DrawSquare(visual, pointSampleTopLeft, False)
		self.AddVisual(visual)

	def Add(self, relativeMVPoint, imageSource, pps):
		""" <summary>
		 Add the image at the given location, offset negatively if pps is less than image size.
		 </summary>
		 <param name="relativeMVPoint"></param>
		 <param name="imageSource"></param>
		 <param name="pps">PPS (Pixels Per Sample) is how many pixels fit within a square. If smaller
		 than the image, the image will go beyond the square.</param>
		 <returns></returns>
		"""
		worldPoint = self.GetWorldPos(relativeMVPoint)
		pointSampleTopLeft = self.GetPxPos(worldPoint)
		visual = DrawingVisual()
		self.DrawImage(visual, imageSource, pointSampleTopLeft, False, pps)
		self.AddVisual(visual)
		return visual

	def NewWriteableBitmap(lod):
		dpi = SettingController.DpiForNonViewableData
		width = lod.SamplesPerMapblock
		height = lod.SamplesPerMapblock
		wb = WriteableBitmap(width, height, dpi, dpi, PixelFormats.Bgra32, None)
		if (wb.PixelWidth != width) or (wb.PixelHeight != height):
			raise ApplicationException(String.Format("Tried to get {0}x{1} image and got {2}x{3}", width, height, wb.PixelWidth, wb.PixelHeight))
		return wb

	NewWriteableBitmap = staticmethod(NewWriteableBitmap)