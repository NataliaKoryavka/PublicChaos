# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25

@author: Егор
"""

import Ngl
import Nio
import numpy

file = Nio.open_file("file")

value = file.variables["value"]
x = file.variables["x"]
y = file.variables["y"]

value = value[0,0,:,:]
x = x[:]
y = y[:]

#  Создаём рабочую станцию.

rlist = Ngl.Resources()
rlist.wkColorMap = 'posneg_1'
wks_type = "ps"
wks = Ngl.open_wks(wks_type,"contours",rlist)

resources = Ngl.Resources()

resources.sfXArray = x[:]
resources.sfYArray = y[:]

map = Ngl.contour_map(wks,concentration[:,:],resources)

resources.cnFillOn             = True
resources.cnFillDrawOrder       = "Predraw" 
resources.cnLineLabelsOn        = False
