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
import K_Working_Tools.K_Geometry_Display.Functions.K_Geometry_Display_Utilities as K_Geometry_Display_Utilities # type: ignore

# Reload
reload(K_Geometry_Display_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Geometry_Display(Operator):
    """Choose a display mode for the viewport"""
    bl_idname = "object.ot_geometry_display"
    bl_label = "K Geometry Display"

    action: EnumProperty(
        items=[
            ('SHOW_WIRE_FRAME', 'show_wire_frame', 'show_wire_frame'),
            ('SHOW_SOLID', 'show_solid', 'show_solid'),
            ('SHOW_FACE_ORIENTATION', 'show_face_orientaion', 'show_face_orientaion'),
            ('SHOW_MATERIAL', 'show_material', 'show_material'),
            ('SHOW_RENDERED', 'show_rendered', 'show_rendered'), 
            ('SHOW_NORMAL', 'show_normal', 'show_normal')
            ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'SHOW_WIRE_FRAME':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='WIREFRAME')

        elif self.action == 'SHOW_SOLID':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='SOLID')

        elif self.action == 'SHOW_FACE_ORIENTATION':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='FACEORIENTATION')

        elif self.action == 'SHOW_MATERIAL':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='MATERIAL')

        elif self.action == 'SHOW_RENDERED':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='RENDERED')

        elif self.action == 'SHOW_NORMAL':
            K_Geometry_Display_Utilities.geometry_display_mode(mode='NORMAL')


        return {'FINISHED'}