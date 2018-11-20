# *_*coding:utf-8 *_*
class Nuke(object):
    def __init__(self):
        import nuke as nuke
        import sys as sys
        self._nuke=nuke
        self._sys=sys
        
    def createNode(self):
        self.read=self._nuke.createNode("Read")
        
# read=nuke.nodes.Read()
# path=read.knob("file").value()
# 
# path="D:/1.tif/CrystalCity01_0000.tif"
# 
# read.knob("file").setValue(path)
