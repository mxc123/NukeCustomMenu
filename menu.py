# -*- coding:utf-8 -*-
import nuke
import sys

from nukescripts import panels
def _connect():

    
    
    # sys.path.append(r"D:/timeLog/timeLog01/timeLog01/mainWindows")
    # import timeLogUI
    # reload(timeLogUI)
    # className = timeLogUI.MinWindows
    # import connectUI
	
    # reload(connectUI)
    
    # pane = nuke.getPaneFor('Properties.1')
    # panels.registerWidgetAsPanel('connectUI.MainView()', 'Test table panel', 'uk.co.thefoundry.connectUI.MainView()', True).addToPane(pane)
    #import createNodeAPI
	#reload(createNodeAPI)
	#nukeAPI=createNodeAPI.Nuke()
	#nukeAPI.createNode()
    import connectUI
	
    reload(connectUI)
    # className=connectUI.MainView()
    # pane = nuke.getPaneFor('Properties.1')
    # panels.registerWidgetAsPanel('className', 'TimeLog', 'uk.co.thefoundry.className', True).addToPane(pane)
	
    customUI=connectUI.MainView()
    customUI.exec_()
   
def mainUI():

    menubar = nuke.menu("Nuke");  
    m = menubar.addMenu(u"&My_Menu")  
    #m.addCommand("Transform/Reformat", "nuke.createNode('Reformat')", "^r")
    m.addCommand("Transform","_connect()")

#nuke.utils(mainUI)
mainUI()
