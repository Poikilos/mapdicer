# 
# * Created by SharpDevelop.
# * User: Jatlivecom
# * Date: 7/28/2022
# * Time: 6:58 AM
# *
# * To change this template use Tools | Options | Coding | Edit Standard Headers.
# 
from System import *
from System.Windows.Forms import *

class Program(object):
	""" <summary>
	 Class with program entry point.
	 </summary>
	"""
	def Main(args):
		# <summary>
		# Program entry point.
		# </summary>
		Application.EnableVisualStyles()
		Application.SetCompatibleTextRenderingDefault(False)
		Application.Run(MainForm())

	Main = staticmethod(Main)

Program.Main(None)