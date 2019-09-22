# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_25-02.41.51 157541
# Run by zhangjiayong on Sun Sep 22 16:18:54 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=338.666656494141, 
    height=207.680557250977)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(
    name='/home/zhangjiayong/workspace/abaqus/UNIUSER_CLA_KIN.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/zhangjiayong/workspace/abaqus/UNIUSER_CLA_KIN.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.superimposeOptions.setValues(
    visibleEdges=ALL)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=HIDDEN)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=SHADED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    elemLabels=ON, nodeLabels=ON)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=19, maxValue=31.8355, minValue=6.60465)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    numIntervals=24)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=LINE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=BANDED)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=ISOSURFACE)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourType=BANDED)
