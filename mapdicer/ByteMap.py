from System import *
from System.Collections.Generic import *
from System.IO import *
from System.Linq import *
from System.Text import *
from System.Windows import *
from System.Windows.Media import *
from System.Windows.Media.Imaging import *

class ByteMap(object):
	def __init__(self, width, height, bytesPerPixel, fill, color):
		self._pixels = None
		self._width = width
		self._height = height
		self._bytesPP = bytesPerPixel
		self._stride = width * bytesPerPixel
		self._totalBytes = self._stride * self._height
		self._pixels = Array.CreateInstance(Byte, self._totalBytes)
		if fill:
			self.Fill(color)

	def SetPixel(self, x, y, color):
		lineIndex = y * self._stride
		pxIndex = lineIndex + x * self._bytesPP
		self._pixels[pxIndex] = color.B
		self._pixels[pxIndex + 1] = color.G
		self._pixels[pxIndex + 2] = color.B
		self._pixels[pxIndex + 3] = color.A

	def Fill(self, color):
		lineIndex = 0
		b = color.B
		g = color.G
		r = color.R
		a = color.A
		y = 0
		while y < self._height:
			pxIndex = lineIndex
			x = 0
			while x < self._width:
				self._pixels[pxIndex] = b
				self._pixels[pxIndex + 1] = g
				self._pixels[pxIndex + 2] = r
				self._pixels[pxIndex + 3] = a
				pxIndex += self._bytesPP
				x += 1
			lineIndex += self._stride
			y += 1

	def WriteTo(self, wb):
		dstRect = Int32Rect(0, 0, self._width, self._height)
		wb.WritePixels(dstRect, self._pixels, self._stride, 0)

	def WriteTo(self, wb, dstRect):
		""" <summary>
		 Write all pixels to the destination.
		 </summary>
		 <param name="wb"></param>
		 <param name="dstRect"></param>
		"""
		wb.WritePixels(dstRect, self._pixels, self._stride, 0)

	def WritePixelTo(self, wb, x, y):
		dstRect = Int32Rect(x, y, 1, 1)
		lineIndex = y * self._stride
		pxIndex = lineIndex + x * self._bytesPP
		wb.WritePixels(dstRect, self._pixels, self._stride, pxIndex)

	def WritePixelTo(wb, x, y, color):
		# See
		# https://docs.microsoft.com/en-us/dotnet/api/system.windows.media.imaging.writeablebitmap.writepixels?view=net-5.0
		pixels = 
		rect = Int32Rect(x, y, 1, 1)
		pxIndex = 0
		stride = 4
		wb.WritePixels(rect, self._pixels, self._stride, pxIndex)

	WritePixelTo = staticmethod(WritePixelTo)

	def SaveWriteableBitmap(path, wb):
		# ^ Use a different name to prevent infinite recursion
		# Clone converts a WriteableBitmap if the target is an implemented type.
		ByteMap.Save(path, wb.Clone())

	SaveWriteableBitmap = staticmethod(SaveWriteableBitmap)

	def Save(path, source):
		""" <summary>
		 Save the bitmapsource as a png file.
		 Use SaveWriteableBitmap instead of sending a WriteableBitmap directly.
		 </summary>
		 <param name="path"></param>
		 <param name="source">Any bitmap source such as from a WriteableBitmap's overloaded Clone method.</param>
		 <returns></returns>
		"""
		if Path.GetExtension(path).ToLower() != SettingController.MapblockImageDotExt:
			raise ApplicationException(String.Format("The file {0} doesn't have the extension {1}.", path, SettingController.MapblockImageDotExt))
		error = ""
		if path != str.Empty:
			try:
			except System.IO.DirectoryNotFoundException, ex:
				error = String.Format("The directory was not ensured to exist: {0}", path)
			except System.IO.IOException, ex:
				# File is in use
				error = String.Format("{0}", ex.Message)
			finally:
		return error

	Save = staticmethod(Save)