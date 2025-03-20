# ---------------------------------------------------------------- # 
# Hi there! I hope you’re enjoying this tool.
# If you have any concerns or feedback about the tool,
# Please feel free to contact me via email.
#
# vanthekhoi@gmail.com 
#
# Thank you :))
# ---------------------------------------------------------------- #

import bpy 

def origin_to_mesh():
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')


def origin_to_cursor():
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')


def origin_to_selected():
        # Memorize original cursor pos
        # cursor_position = bpy.context.scene.cursor.location

        # Snap cursor to selected 
        bpy.ops.view3d.snap_cursor_to_selected()

        # Turn to object mode 
        bpy.ops.object.mode_set(mode = 'OBJECT')

        # Move origin to cursor
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

        # Turn back to edit mode
        bpy.ops.object.mode_set(mode = 'EDIT')

        # Move cursor back to original pos
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)


def cursor_to_selected():
     bpy.ops.view3d.snap_cursor_to_selected()


def cursor_to_active():
     bpy.ops.view3d.snap_cursor_to_active()


def cursor_to_center():
     bpy.ops.view3d.snap_cursor_to_center()
