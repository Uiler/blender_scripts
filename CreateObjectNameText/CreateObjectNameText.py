############################################################
# Copyright (c) 2018 Uiler
# Released under the MIT license
# http://opensource.org/licenses/mit-license.php
#

import bpy
import math

# Offset distance from source objects.
offsetX = 0
offsetY = 0
offsetZ = 3

# Text object rotation. ex) Front view:rotX=90 rotY=rotZ=0 / Right view:rotX=rotZ=90 rotY=0
rotX = 90
rotY = 0
rotZ = 0

# Text data suffix. ex) Object name + <text_suffix>
text_suffix = "_name_text"

# Text format
text_size = 1.0 # Default is 1.0.
text_align_x = "CENTER" #  LEFT, CENTER , RIGHT , JUSTIFY , FLUSH, default LEFT

for obj in bpy.context.selected_objects:
    srcX = obj.location.x
    srcY = obj.location.y
    srcZ = obj.location.z
    
    textObjName = obj.name + text_suffix
    textDt = bpy.data.curves.new(textObjName, 'FONT')
    textDt.body = obj.name
    textDt.size = text_size
    textDt.align_x = text_align_x
    
    textObj = bpy.data.objects.new(textObjName, textDt)
    textObj.location.x = obj.location.x + offsetX
    textObj.location.y = obj.location.y + offsetY
    textObj.location.z = obj.location.z + offsetZ
    textObj.rotation_euler.x = math.radians(rotX)
    textObj.rotation_euler.y = math.radians(rotY)
    textObj.rotation_euler.z = math.radians(rotZ)
    
    bpy.context.scene.objects.link(textObj)
    