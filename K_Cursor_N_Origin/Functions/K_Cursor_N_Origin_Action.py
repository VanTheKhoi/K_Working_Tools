# ---------------------------------------------------------------- # 
# Hi there! I hope you’re enjoying this tool.
# If you have any concerns or feedback about the tool,
# Please feel free to contact me via email.
#
# vanthekhoi@gmail.com 
#
# Thank you :))
# ---------------------------------------------------------------- #

try:
    from imp import reload
except:
    pass

import bpy
from bpy.props import EnumProperty
from bpy.types import Operator


# Import 
import K_Working_Tools.K_Cursor_N_Origin.Functions.K_Cursor_N_Origin_Utilities as K_Cursor_N_Origin_Utilities # type: ignore

# Reload
reload(K_Cursor_N_Origin_Utilities)

# # --- OPERATOR CLASS --- #

# -------------- Origin to Mesh ------------------ #
class KWT_OT_K_Origin_To_Mesh_Snap(Operator):
    """Snap ORIGIN to MESH selected"""
    bl_idname = "object.ot_origin_to_mesh_snap"
    bl_label = "K Origin To Mesh"

    action: EnumProperty(
        items=[
            ('ORIGIN_TO_MESH', 'origin_to_mesh', 'origin_to_mesh')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'ORIGIN_TO_MESH':
            K_Cursor_N_Origin_Utilities.origin_to_mesh()

        return {'FINISHED'}


# -------------- Origin to Cursor ------------------ #
class KWT_OT_K_Origin_To_Cursor_Snap(Operator):
    """Snap ORIGIN to CURSOR"""
    bl_idname = "object.ot_origin_to_cursor_snap"
    bl_label = "K Origin To Cursor"

    action: EnumProperty(
        items=[
            ('ORIGIN_TO_CURSOR', 'origin_to_cursor', 'origin_to_cursor')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'ORIGIN_TO_CURSOR':
            K_Cursor_N_Origin_Utilities.origin_to_cursor()

        return {'FINISHED'}


# -------------- Origin to Slected ------------------ #
class KWT_OT_K_Origin_To_Selected_Snap(Operator):
    """Snap ORIGIN to SELECTED (Vertex/ Edge/ Face/ ...)"""
    bl_idname = "object.ot_origin_to_selected_snap"
    bl_label = "K Origin To Selected"

    action: EnumProperty(
        items=[
            ('ORIGIN_TO_SELECTED', 'origin_to_selected', 'origin_to_selected')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'ORIGIN_TO_SELECTED':
            K_Cursor_N_Origin_Utilities.origin_to_selected()

        return {'FINISHED'}
    

# -------------- Cursor to Slected ------------------ #
class KWT_OT_K_Cursor_To_Selected_Snap(Operator):
    """Snap CURSOR to SELECTED (Vertex/ Edge/ Face/ ...)"""
    bl_idname = "object.ot_cursor_to_selected_snap"
    bl_label = "K Cursor To Selected"

    action: EnumProperty(
        items=[
            ('CURSOR_TO_SELECTED', 'cursor_to_selected', 'cursor_to_selected')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'CURSOR_TO_SELECTED':
            K_Cursor_N_Origin_Utilities.cursor_to_selected()

        return {'FINISHED'}


# -------------- Cursor to Active ------------------ #
class KWT_OT_K_Cursor_To_Active_Snap(Operator):
    """Snap CURSOR to ACTIVE"""
    bl_idname = "object.ot_cursor_to_active_snap"
    bl_label = "K Cursor To Active"

    action: EnumProperty(
        items=[
            ('CURSOR_TO_ACTIVE', 'cursor_to_active', 'cursor_to_active')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'CURSOR_TO_ACTIVE':
            K_Cursor_N_Origin_Utilities.cursor_to_active()

        return {'FINISHED'}
    

# -------------- Cursor to Center ------------------ #
class KWT_OT_K_Cursor_To_Center_Snap(Operator):
    """Snap CURSOR to ACTIVE"""
    bl_idname = "object.ot_cursor_to_center_snap"
    bl_label = "K Cursor To Center"

    action: EnumProperty(
        items=[
            ('CURSOR_TO_CENTER', 'cursor_to_center', 'cursor_to_center')
        ]
    )# type: ignore

    def execute(self, context):
        scene = context.scene
        
        if self.action == 'CURSOR_TO_CENTER':
            K_Cursor_N_Origin_Utilities.cursor_to_center()

        return {'FINISHED'}