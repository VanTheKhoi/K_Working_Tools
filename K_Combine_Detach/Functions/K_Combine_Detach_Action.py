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
import K_Working_Tools.K_Combine_Detach.Functions.K_Combine_Detach_Utilities as K_Combine_Detach_Utilities # type: ignore

# Reload
reload(K_Combine_Detach_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Combine_Detach(Operator):
    """Combine and Detach tools"""
    bl_idname = "object.ot_combine_detach"
    bl_label = "K Combine Detach"

    action: EnumProperty(
        items=[
            ('COMBINE_OBJECTS', 'combine_objects', 'combine_objects'),
            ('DUPLICATE_FACES_SELECTED', 'duplicate_faces_selected', 'duplicate_faces_selected'),
            ('DETACH_FACES_SELECTED', 'detach_faces_selected', 'detach_faces_selected'),
            ('DETACH_OBJECTS_WITHIN_MATERIAL', 'detach_objects_within_material', 'detach_objects_within_material')
            ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'COMBINE_OBJECTS':
            K_Combine_Detach_Utilities.combine_objects()

        elif self.action == 'DUPLICATE_FACES_SELECTED':
            K_Combine_Detach_Utilities.duplicate_selected_faces()

        elif self.action == 'DETACH_FACES_SELECTED':
            K_Combine_Detach_Utilities.detach_faces_selected()

        elif self.action == 'DETACH_OBJECTS_WITHIN_MATERIAL':
            K_Combine_Detach_Utilities.detach_object_within_material()

        return {'FINISHED'}