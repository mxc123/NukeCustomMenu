# *_*coding:utf-8 *_*
import os
import sys
import json

from PySide import QtGui,QtCore
from PySide.QtCore import *
class MainViewdatas(object):
    def __init__(self,mainview,parent=None):
        self.mainview=mainview
        import createNodeAPI
        reload(createNodeAPI)
        self._nuke = createNodeAPI.Nuke()

        
    # def cacheBtn(self):
    #     cachePath=QtGui.QFileDialog.getSaveFileName()
    #     self.cachePath=list(cachePath)[0]
    #     self.mainview.cacheOutlineEdit.setText(self.cachePath)

    # def senceOutBtn(self):
    #     path=QtGui.QFileDialog.getSaveFileName()
    #     self.senceOutPath=list(path)[0]
    #     self.mainview.senceOutlineEdit.setText(self.senceOutPath)
        
    # def senceInBtn(self):
    #     path=QtGui.QFileDialog.getOpenFileName()

    #     self.pathText=list(path)[0]
        
    #     self.mainview.senceIntlineEdit.setText(self.pathText)
    # def setTreeWidgetItem(self):
    #     dict_all=self._maya.outObjectAttribute()
    #     for key in dict_all.keys():
    #         setText=QtGui.QTreeWidgetItem(self.mainview.treeWidget)
    #         num=0
    #         listKeys=dict_all[key].keys()[::-1]
    #         for keyTow in listKeys:
    #             setText.setText(num,str(dict_all[key][keyTow]))
    #             num+=1

    # def selectGeo(self):
    #     self.geoNameList=[]
       
    #     items=self.mainview.treeWidget.selectedItems()
    #     for ii in items:
    #         self.geoNameList.append(ii.text(0))


    #     return tuple(self.geoNameList)
       
    # def okBtn(self):
    #     if self.mainview.checkBox.isChecked()==True:

    #         self._maya.exportmaterail((self.geoNameList),str(self.cachePath))
    #         self._maya.writeJson()
    #     else:
    #         self._maya.exportmaterail((self.geoNameList),str(self.cachePath))
    #         self._maya.writeJson()
    #         self._maya.fileSave(str(self.senceOutPath))

    #         self._maya.openFile(str(self.pathText))
    #         self._maya.readJson()
    #         self._maya.importmateril()
        
        
    def okBtn(self):
        self._nuke.createNode()

    def canBtn(self):
        self.mainview.close()


class MainView(QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainView,self).__init__(parent)


        self._mainUi()

    def _mainUi(self):
        self.treeWidget=QtGui.QTreeWidget()
        self.treeWidget.setMinimumSize(200,200)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)


        self.treeWidget.setHeaderLabels(["Assets","cache","hair","material"])
        self.checkBox=QtGui.QCheckBox("cache only")
        horizeSpace=QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)


        cacheOutlabel=QtGui.QLabel("cache output path")
        cachespacerItem=QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.cacheOutlineEdit=QtGui.QLineEdit()
        self.cacheOutBtn=QtGui.QPushButton("set")

        senceOutlabel=QtGui.QLabel("scene output path")
        senceOutspacerItem = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.senceOutlineEdit=QtGui.QLineEdit()
        self.senceOutBtn=QtGui.QPushButton("set")

        senceIntlabel=QtGui.QLabel("sence input path")
        senceIntspacerItem = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.senceIntlineEdit=QtGui.QLineEdit()
        self.senceIntBtn=QtGui.QPushButton("load")



        self.fBtn=QtGui.QPushButton(u"确定")
        self.cancleBtn=QtGui.QPushButton(u"取消")
##########################################signal 连接#############################################

        self._mainviewdatas=MainViewdatas(self)
        #self._mainviewdatas.setTreeWidgetItem()
        #self.treeWidget.itemClicked.connect(self._mainviewdatas.selectGeo)
        # self.cacheOutBtn.clicked.connect(self._mainviewdatas.cacheBtn)
        # self.senceOutBtn.clicked.connect(self._mainviewdatas.senceOutBtn)
        # self.senceIntBtn.clicked.connect(self._mainviewdatas.senceInBtn)
        self.cancleBtn.clicked.connect(self._mainviewdatas.canBtn)
        self.fBtn.clicked.connect(self._mainviewdatas.okBtn)



        self.chakeBoxHlayout=QtGui.QHBoxLayout()
        self.chakeBoxHlayout.addWidget(self.checkBox)
        self.chakeBoxHlayout.addItem(horizeSpace)

        self.cacheOutspaceHlayout=QtGui.QHBoxLayout()
        self.cacheOutspaceHlayout.addWidget(cacheOutlabel)
        self.cacheOutspaceHlayout.addItem(cachespacerItem)

        self.cachOutHlayout=QtGui.QHBoxLayout()

        self.cachOutHlayout.addWidget(self.cacheOutlineEdit)
        self.cachOutHlayout.addWidget(self.cacheOutBtn)

        self.sceneOutspacerHlayout=QtGui.QHBoxLayout()
        self.sceneOutspacerHlayout.addWidget(senceOutlabel)
        self.sceneOutspacerHlayout.addItem(senceOutspacerItem)

        self.senceOutHlayout=QtGui.QHBoxLayout()

        self.senceOutHlayout.addWidget(self.senceOutlineEdit)
        self.senceOutHlayout.addWidget(self.senceOutBtn)

        self.sceneIntspaceHlayout=QtGui.QHBoxLayout()
        self.sceneIntspaceHlayout.addWidget(senceIntlabel)
        self.sceneIntspaceHlayout.addItem(senceIntspacerItem)

        self.scenIntHlayout=QtGui.QHBoxLayout()

        self.scenIntHlayout.addWidget(self.senceIntlineEdit)
        self.scenIntHlayout.addWidget(self.senceIntBtn)




        self.HBtnlayout=QtGui.QHBoxLayout()
        self.HBtnlayout.addWidget(self.fBtn)
        self.HBtnlayout.addWidget(self.cancleBtn)



        self.Hlayout=QtGui.QHBoxLayout()
        self.Hlayout.addWidget(self.treeWidget)
        self.mainlayout = QtGui.QVBoxLayout()
        self.mainlayout.addLayout(self.Hlayout)
        self.mainlayout.addLayout(self.chakeBoxHlayout)
        self.mainlayout.addLayout(self.cacheOutspaceHlayout)

        self.mainlayout.addLayout(self.cachOutHlayout)
        self.mainlayout.addLayout(self.sceneOutspacerHlayout)

        self.mainlayout.addLayout(self.senceOutHlayout)
        self.mainlayout.addLayout(self.sceneIntspaceHlayout)
        self.mainlayout.addLayout(self.scenIntHlayout)


        self.mainlayout.addLayout(self.HBtnlayout)

        self.setLayout(self.mainlayout)
