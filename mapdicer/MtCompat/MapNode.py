#
# Mtcompat
# Copyright(C) 2013 celeron55, Perttu Ahola<celeron55@gmail.com>; 2020 Jake "Poikilos" Gustafson
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
from MapDicer.Models import *
from System import *
from System.Collections.Generic import *
from System.Linq import *
from System.Text import *
from content_t import *

class LightBank(object):
    def __init__(self):

#
# Simple rotation enum.
#
class Rotation(object):
    def __init__(self):

class MapNode(object):
    def __init__(self):
        #
        # Naming scheme:
        # - Material = irrlicht's Material class
        # - Content = (content_t) content of a node
        # - Tile = TileSpec at some side of a node of some content type
        #
        #
        # The maximum node ID that can be registered by mods. This must
        # be significantly lower than the maximum content_t value, so that
        # there is enough room for dummy node IDs, which are created when
        # a MapBlock containing unknown node names is loaded from disk.
        #
        self._MaxRegisteredContent = 0x7fffu
        #
        # A solid walkable node with the texture unknown_node.png.
        #
        # For example, used on the client to display unregistered node IDs
        # (instead of expanding the vector of node definitions each time
        # such a node is received).
        #
        self._ContentUnknown = 125
        #
        # The common material through which the player can walk and which
        # is transparent to light
        #
        self._ContentAir = 126
        #
        # Ignored node.
        #
        # Unloaded chunks are considered to consist of this. Several other
        # methods return this when an error occurs. Also, during
        # map generation this means the node has not been set yet.
        #
        # Doesn't create faces with anything and is considered being
        # out-of-map in the game map.
        #
        self._ContentIgnore = 127
        self._LiquidLevelMask = 0x07
        self._LiquidFlowDownMask = 0x08
        #public static uint LIQUID_LEVEL_MASK 0x3f // better finite water
        #public static uint LIQUID_FLOW_DOWN_MASK 0x40 // not used when finite water
        # maximum amount of liquid in a block
        self._LiquidLevelMax = self._LiquidLevelMask
        self._LiquidInfinityMask = 0x80 #0b10000000
        # mask for leveled nodebox param2
        self._LeveledMask = 0x7F
        self._LeveledMax = self._LeveledMask

    def LiquidLevelSource():
        return (self._LiquidLevelMax + 1)

    LiquidLevelSource = staticmethod(LiquidLevelSource)

    def GetLevel(self, nodemgr):
        return 255

class LiquidMapNode(MapNode):
    def __init__(self):

    def getParam2(self):
        return self._param2

    def GetLevel(self, nodemgr):
        f = nodemgr.Get(self)
        if f.liquid_type == LiquidType.Source:
            return self.LiquidLevelSource()
        if f.param_type_2 == ContentParamType2.FlowingLiquid:
            return (self.getParam2() & MapNode.LiquidLevelMask)
        if f.liquid_type == LiquidType.Flowing: # can remove if all param_type_2 setted
            return (self.getParam2() & MapNode.LiquidLevelMask)
        if f.param_type_2 == ContentParamType2.Leveled:
            level = (self.getParam2() & MapNode.LeveledMask)
            if level != 0:
                return level
        if f.leveled > MapNode.LeveledMax:
            return MapNode.LeveledMax
        return f.leveled
