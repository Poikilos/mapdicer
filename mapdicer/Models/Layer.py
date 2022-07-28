from System import *
from System.Collections.Generic import *
from System.ComponentModel.DataAnnotations import *
from System.ComponentModel.DataAnnotations.Schema import *
from System.Data.Entity import *
# using System.Data.Entity.Core.Mapping;
from System.Data.SQLite import *
# using System.Data.SQLite.EF6;
# using System.Data.SQLite.Linq;
# using System.Data.Linq;
from System.Linq import * # orderby etc
from MapDicer.MtCompat import *

class Layer(MapNode):
    def get_LayerId(self):

    def set_LayerId(self, value):

    LayerId = property(fget=get_LayerId, fset=set_LayerId)

    def get_Num(self):

    def set_Num(self, value):

    Num = property(fget=get_Num, fset=set_Num)

    def get_Name(self):

    def set_Name(self, value):

    Name = property(fget=get_Name, fset=set_Name)

    def Insert(newEntry):
        ok = False
        return ok

    Insert = staticmethod(Insert)
