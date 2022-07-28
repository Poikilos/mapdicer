import clr

# 
# * Created by SharpDevelop.
# * User: Jatlivecom
# * Date: 7/28/2022
# * Time: 6:58 AM
# *
# * To change this template use Tools | Options | Coding | Edit Standard Headers.
# 
class MainForm(object):
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
		resources = System.ComponentModel.ComponentResourceManager(clr.GetClrType(MainForm))
		self._progressbar = System.Windows.Forms.ProgressBar()
		self._menuTLP = System.Windows.Forms.TableLayoutPanel()
		self._detailBtn = System.Windows.Forms.Button()
		self._regionBtn = System.Windows.Forms.Button()
		self._terrainBtn = System.Windows.Forms.Button()
		self._terrainColorBtn = System.Windows.Forms.Button()
		self._settingsButton = System.Windows.Forms.Button()
		self._lodCBx = System.Windows.Forms.ComboBox()
		self._regionCBx = System.Windows.Forms.ComboBox()
		self._terrainCBx = System.Windows.Forms.ComboBox()
		self._terrainBrushSizeSlider = System.Windows.Forms.TrackBar()
		self._mapblockBtn = System.Windows.Forms.Button()
		self._mainTLP = System.Windows.Forms.TableLayoutPanel()
		self._menuTLP.SuspendLayout()
		((self._terrainBrushSizeSlider)).BeginInit()
		self._mainTLP.SuspendLayout()
		self.SuspendLayout()
		# 
		# progressbar
		# 
		self._progressbar.Dock = System.Windows.Forms.DockStyle.Bottom
		self._progressbar.Location = System.Drawing.Point(0, 348)
		self._progressbar.Name = "progressbar"
		self._progressbar.Size = System.Drawing.Size(904, 23)
		self._progressbar.TabIndex = 1
		# 
		# menuTLP
		# 
		self._menuTLP.ColumnCount = 8
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 3.636364f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 27.27273f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 3.636364f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 27.27273f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 3.636364f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 27.27273f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 3.636364f))
		self._menuTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 3.636364f))
		self._menuTLP.Controls.Add(self._detailBtn, 0, 0)
		self._menuTLP.Controls.Add(self._regionBtn, 2, 0)
		self._menuTLP.Controls.Add(self._terrainBtn, 4, 0)
		self._menuTLP.Controls.Add(self._terrainColorBtn, 6, 0)
		self._menuTLP.Controls.Add(self._settingsButton, 7, 0)
		self._menuTLP.Controls.Add(self._lodCBx, 1, 0)
		self._menuTLP.Controls.Add(self._regionCBx, 3, 0)
		self._menuTLP.Controls.Add(self._terrainCBx, 5, 0)
		self._menuTLP.Controls.Add(self._terrainBrushSizeSlider, 1, 1)
		self._menuTLP.Controls.Add(self._mapblockBtn, 4, 1)
		self._menuTLP.Dock = System.Windows.Forms.DockStyle.Fill
		self._menuTLP.Location = System.Drawing.Point(3, 3)
		self._menuTLP.Name = "menuTLP"
		self._menuTLP.RowCount = 2
		self._menuTLP.RowStyles.Add(System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50f))
		self._menuTLP.RowStyles.Add(System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50f))
		self._menuTLP.Size = System.Drawing.Size(898, 60)
		self._menuTLP.TabIndex = 0
		# 
		# detailBtn
		# 
		self._detailBtn.Location = System.Drawing.Point(3, 3)
		self._detailBtn.Name = "detailBtn"
		self._detailBtn.Size = System.Drawing.Size(26, 23)
		self._detailBtn.TabIndex = 0
		self._detailBtn.UseVisualStyleBackColor = True
		self._detailBtn.Click += self._DetailBtnClick
		# 
		# regionBtn
		# 
		self._regionBtn.Location = System.Drawing.Point(279, 3)
		self._regionBtn.Name = "regionBtn"
		self._regionBtn.Size = System.Drawing.Size(26, 23)
		self._regionBtn.TabIndex = 1
		self._regionBtn.UseVisualStyleBackColor = True
		self._regionBtn.Click += self._RegionBtnClick
		# 
		# terrainBtn
		# 
		self._terrainBtn.Location = System.Drawing.Point(555, 3)
		self._terrainBtn.Name = "terrainBtn"
		self._terrainBtn.Size = System.Drawing.Size(26, 23)
		self._terrainBtn.TabIndex = 2
		self._terrainBtn.UseVisualStyleBackColor = True
		self._terrainBtn.Click += self._TerrainBtnClick
		# 
		# terrainColorBtn
		# 
		self._terrainColorBtn.ForeColor = System.Drawing.Color.Green
		self._terrainColorBtn.Location = System.Drawing.Point(831, 3)
		self._terrainColorBtn.Name = "terrainColorBtn"
		self._terrainColorBtn.Size = System.Drawing.Size(26, 23)
		self._terrainColorBtn.TabIndex = 3
		self._terrainColorBtn.Text = "●"
		self._terrainColorBtn.UseVisualStyleBackColor = True
		self._terrainColorBtn.Click += self._TerrainColorBtnClick
		# 
		# settingsButton
		# 
		self._settingsButton.Image = ((resources.GetObject("settingsButton.Image")))
		self._settingsButton.Location = System.Drawing.Point(863, 3)
		self._settingsButton.Name = "settingsButton"
		self._settingsButton.Size = System.Drawing.Size(32, 23)
		self._settingsButton.TabIndex = 4
		self._settingsButton.UseVisualStyleBackColor = True
		self._settingsButton.Click += self._SettingsButtonClick
		# 
		# lodCBx
		# 
		self._lodCBx.Dock = System.Windows.Forms.DockStyle.Top
		self._lodCBx.FormattingEnabled = True
		self._lodCBx.Location = System.Drawing.Point(35, 3)
		self._lodCBx.Name = "lodCBx"
		self._lodCBx.Size = System.Drawing.Size(238, 21)
		self._lodCBx.TabIndex = 5
		self._lodCBx.SelectedIndexChanged += self._LodCBxSelectedIndexChanged
		# 
		# regionCBx
		# 
		self._regionCBx.Dock = System.Windows.Forms.DockStyle.Top
		self._regionCBx.FormattingEnabled = True
		self._regionCBx.Location = System.Drawing.Point(311, 3)
		self._regionCBx.Name = "regionCBx"
		self._regionCBx.Size = System.Drawing.Size(238, 21)
		self._regionCBx.TabIndex = 6
		# 
		# terrainCBx
		# 
		self._terrainCBx.Dock = System.Windows.Forms.DockStyle.Top
		self._terrainCBx.FormattingEnabled = True
		self._terrainCBx.Location = System.Drawing.Point(587, 3)
		self._terrainCBx.Name = "terrainCBx"
		self._terrainCBx.Size = System.Drawing.Size(238, 21)
		self._terrainCBx.TabIndex = 7
		self._terrainCBx.SelectedIndexChanged += self._TerrainCBxSelectedIndexChanged
		# 
		# terrainBrushSizeSlider
		# 
		self._terrainBrushSizeSlider.Location = System.Drawing.Point(35, 33)
		self._terrainBrushSizeSlider.Name = "terrainBrushSizeSlider"
		self._terrainBrushSizeSlider.Size = System.Drawing.Size(104, 24)
		self._terrainBrushSizeSlider.TabIndex = 8
		self._terrainBrushSizeSlider.Scroll += self._TerrainBrushSizeSliderScroll
		# 
		# mapblockBtn
		# 
		self._mapblockBtn.Location = System.Drawing.Point(555, 33)
		self._mapblockBtn.Name = "mapblockBtn"
		self._mapblockBtn.Size = System.Drawing.Size(26, 23)
		self._mapblockBtn.TabIndex = 9
		self._mapblockBtn.UseVisualStyleBackColor = True
		self._mapblockBtn.Click += self._MapblockBtnClick
		# 
		# mainTLP
		# 
		self._mainTLP.ColumnCount = 1
		self._mainTLP.ColumnStyles.Add(System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50f))
		self._mainTLP.Controls.Add(self._menuTLP, 0, 0)
		self._mainTLP.Dock = System.Windows.Forms.DockStyle.Fill
		self._mainTLP.Location = System.Drawing.Point(0, 0)
		self._mainTLP.Name = "mainTLP"
		self._mainTLP.RowCount = 2
		self._mainTLP.RowStyles.Add(System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 19.12226f))
		self._mainTLP.RowStyles.Add(System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 80.87775f))
		self._mainTLP.Size = System.Drawing.Size(904, 348)
		self._mainTLP.TabIndex = 2
		# 
		# MainForm
		# 
		self._AutoScaleDimensions = System.Drawing.SizeF(6f, 13f)
		self._AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
		self._ClientSize = System.Drawing.Size(904, 371)
		self._Controls.Add(self._mainTLP)
		self._Controls.Add(self._progressbar)
		self._Name = "MainForm"
		self._Text = "MapDicer"
		self._Load += self._MainFormLoad
		self._Resize += self._MainFormResize
		self._menuTLP.ResumeLayout(False)
		self._menuTLP.PerformLayout()
		((self._terrainBrushSizeSlider)).EndInit()
		self._mainTLP.ResumeLayout(False)
		self.ResumeLayout(False)