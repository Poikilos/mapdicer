# 
# * Created by SharpDevelop.
# * User: Jatlivecom
# * Date: 7/28/2022
# * Time: 8:53 AM
# *
# * To change this template use Tools | Options | Coding | Edit Standard Headers.
# 
class NewTerrainWindow(object):
	def __init__(self):
		# <summary>
		# Designer variable used to keep track of non-visual components.
		# </summary>
		self._components = None

	def Dispose(self, disposing):
		""" <summary>
		 Disposes resources used by the form.
		 </summary>
		 <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		"""
		if disposing:
			if self._components != None:
				self._components.Dispose()
		self.Dispose(disposing)

	def InitializeComponent(self):
		""" <summary>
		 This method is required for Windows Forms designer support.
		 Do not change the method contents inside the source code editor. The Forms designer might
		 not be able to load this method if it was changed manually.
		 </summary>
		"""
		# 
		# NewTerrainWindow
		# 
		self._AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		self._Text = "NewTerrainWindow"
		self._Name = "NewTerrainWindow"