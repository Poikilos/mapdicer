from MapDicer.Models import *
from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *

class TerrainButton(System.Windows.Controls.Button):
    """ <summary>
     It must be a button to be a combo box Item.
     </summary>
    """
    # public const string newItemContent = "(Add New)";
    # inherits Text from Button
    def __init__(self, Content, R, G, B):
        self._R = R
        self._G = G
        self._B = B
        self._Content = Content
        self._Loaded += self.Terrain_Loaded

    def Terrain_Loaded(self, sender, e):
        if Content != SettingModel.NewIdStr:
