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
import K_Working_Tools.K_Transform.Functions.K_Transform_Utilities as K_Transform_Utilities # type: ignore

# Reload
reload(K_Transform_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Transform(Operator):
    """Apply Transform/ Deltas"""
    bl_idname = "object.ot_transform"
    bl_label = "K Transform"

    action: EnumProperty(
        items=[
            ('APPLY_LOCATION', 'apply_location', 'apply_location'),
            ('APPLY_ROTATION', 'apply_rotation', 'apply_rotation'),
            ('APPLY_SCALE', 'apply_scale', 'apply_scale'),
            ('APPLY_ALL_TRANSFORM', 'apply_all_transform', 'apply_all_transform'),
            ('LOCATION_TO_DELTAS', 'location_to_deltas', 'location_to_deltas'),
            ('ROTATION_TO_DELTAS', 'rotation_to_deltas', 'rotation_to_deltas'),
            ('SCALE_TO_DELTAS', 'scale_to_deltas', 'scale_to_deltas'),
            ('TRANSFORM_TO_DELTAS', 'transform_to_deltas', 'transform_to_deltas'),
            ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'APPLY_LOCATION':
            K_Transform_Utilities.apply_transform(is_location=True, 
                                                  is_rotation=False, 
                                                  is_scale=False)

        elif self.action == 'APPLY_ROTATION':
            K_Transform_Utilities.apply_transform(is_location=False, 
                                                is_rotation=True, 
                                                is_scale=False)

        elif self.action == 'APPLY_SCALE':
            K_Transform_Utilities.apply_transform(is_location=False, 
                                                is_rotation=False, 
                                                is_scale=True)

        elif self.action == 'APPLY_ALL_TRANSFORM':
            K_Transform_Utilities.apply_transform(is_location=True, 
                                                is_rotation=True, 
                                                is_scale=True)

        elif self.action == 'LOCATION_TO_DELTAS':
            K_Transform_Utilities.transform_to_deltas(is_location=True, 
                                                      is_rotation=False, 
                                                      is_scale=False)

        elif self.action == 'ROTATION_TO_DELTAS':
            K_Transform_Utilities.transform_to_deltas(is_location=False, 
                                                    is_rotation=True, 
                                                    is_scale=False)

        elif self.action == 'SCALE_TO_DELTAS':
            K_Transform_Utilities.transform_to_deltas(is_location=False, 
                                                    is_rotation=False, 
                                                    is_scale=True)

        elif self.action == 'TRANSFORM_TO_DELTAS':
            K_Transform_Utilities.transform_to_deltas(is_location=True, 
                                                    is_rotation=True, 
                                                    is_scale=True)
            
        return {'FINISHED'}