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
import K_Working_Tools.K_Normal.Functions.K_Normal_Utilities as K_Normal_Utilities # type: ignore

# Reload
reload(K_Normal_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Normal(Operator):
    """Normal tools"""
    bl_idname = "object.ot_normal"
    bl_label = "K Normal"

    action: EnumProperty(
        items=[
            ('RESET_VECTOR', 'reset_vector', 'reset_vector'),
            ('TOGGLE_VERTEX_NORMAL', 'toggle_vertex_normal', 'toggle_vertex_normal'),
            ('SET_NORMAL_FROM_FACE', 'set_normal_from_face', 'set_normal_from_face'),
            ('COPY_NORMAL', 'copy_normal', 'copy_normal'),
            ('PASTE_NORMAL', 'paste_normal', 'paste_normal'),
            ('COPY_FACE_NORMAL', 'copy_face_normal', 'copy_face_normal'),
            ('PASTE_VERTEX_FACE', 'paste_vertex_face', 'paste_vertex_face'),
            ('WEIGHTED_FACE_ANGLE', 'weighted_face_angle', 'weighted_face_angle'),
            ('WEIGHTED_FACE_AREA', 'weighted_face_area', 'weighted_face_area'),
            ('TRANSFER_NORMAL', 'transfer_normal', 'transfer_normal')
            ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene
        if self.action == 'RESET_VECTOR':
            K_Normal_Utilities.reset_vector()

        elif self.action == 'TOGGLE_VERTEX_NORMAL':
            K_Normal_Utilities.toggle_vertex_normal()

        elif self.action == 'SET_NORMAL_FROM_FACE':
            K_Normal_Utilities.normal_from_face()

        elif self.action == 'COPY_NORMAL':
            K_Normal_Utilities.copy_vertex_normal()

        elif self.action == 'PASTE_NORMAL':
            K_Normal_Utilities.paste_vertex_normal()

        elif self.action == 'COPY_FACE_NORMAL':
            K_Normal_Utilities.copy_faces_normal()

        elif self.action == 'PASTE_VERTEX_FACE':
            K_Normal_Utilities.paste_vertex_face_normal()

        elif self.action == 'TRANSFER_NORMAL':
            K_Normal_Utilities.transfer_normal()

        elif self.action == 'WEIGHTED_FACE_ANGLE':
            K_Normal_Utilities.weighted_normal(mode="ANGLE")

        elif self.action == 'WEIGHTED_FACE_AREA':
            K_Normal_Utilities.weighted_normal(mode="AREA")

        return{'FINISHED'}