############################################################
# Copyright (c) 2020 Uiler
# Released under the MIT license
# http://opensource.org/licenses/mit-license.php
#
import bpy

arm = bpy.context.active_object
dupb_suffix = "_IK"

bpy.ops.object.mode_set(mode="EDIT", toggle=False)

bMap = {}
for eb in bpy.context.selected_editable_bones:
    cb = arm.data.edit_bones.new(eb.name + dupb_suffix)
    cb.head = eb.head
    cb.tail = eb.tail
    cb.matrix = eb.matrix
    bMap[cb.name] = eb.name

bpy.ops.object.mode_set(mode="POSE", toggle=False)

for bn, ebn in bMap.items():
    pbone = arm.pose.bones[bn]
    con = pbone.constraints.new("COPY_TRANSFORMS")
    con.target = arm
    con.subtarget = ebn
