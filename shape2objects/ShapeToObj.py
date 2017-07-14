############################################################
# Copyright (c) 2015 Uiler
# Released under the MIT license
# http://opensource.org/licenses/mit-license.php
#
import bpy

# location differ for morp_targets
offsetX = 3
offsetY = 0
offsetZ = 0
dstX = 0
dstY = 0
dstZ = 0
nmBasis = 'Basis'

srcObj = bpy.context.active_object
srcShapes = srcObj.data.shape_keys.key_blocks
morpObjs = []

# duplicate for morphing target
for key, value in srcShapes.items():

    if key == nmBasis:
        continue 

    dstX = dstX + offsetX
    dstY = dstY + offsetY
    dstZ = dstZ + offsetZ
    
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(dstX, dstY, dstZ)})
    morpObj = bpy.context.active_object
    morpObjs.append(morpObj)
    morpObj.name = key
    bpy.ops.object.shape_key_remove(all=True)
    bpy.ops.object.select_all(action='DESELECT')
    
    bpy.ops.object.select_pattern(pattern=srcObj.name)
    srcShapes.get(key).value = 1.0
    bpy.ops.object.select_pattern(pattern=morpObj.name)
    bpy.context.scene.objects.active = morpObj
    bpy.ops.object.join_shapes()
    for idx in range(2):
        morpObj.active_shape_key_index = 0
        bpy.ops.object.shape_key_remove(all=False)        
        
    srcShapes.get(key).value = 0.0
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_pattern(pattern=srcObj.name)
    bpy.context.scene.objects.active = srcObj

    