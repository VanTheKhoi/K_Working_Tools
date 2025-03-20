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
import K_Working_Tools.K_Cleanup.Functions.K_Cleanup_Utilities as K_Cleanup_Utilities # type: ignore
import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore

# Reload
reload(K_Cleanup_Utilities)
reload(K_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Cleanup(Operator):
    """Cleanup tools"""
    bl_idname = "object.ot_cleanup"
    bl_label = "K Cleanup"

    action: EnumProperty(
        items=[
            ('CLEANUP_UNUSED_MATERIAL', 'cleanup_unused_material', 'cleanup_unused_material'),
            ('CLEANUP_UNUSED_DATA', 'cleanup_unused_data', 'cleanup_unused_data')
            ]
    ) # type: ignore


    def execute(self, context):
        scene = context.scene

        if self.action == 'CLEANUP_UNUSED_MATERIAL':
            K_Utilities.cleanup_unused_materials()
            self.report({'INFO'}, "Cleanup material DONE")

        elif self.action == 'CLEANUP_UNUSED_DATA':
            K_Utilities.cleanup_unused_data()
            self.report({'INFO'}, "Cleanup data DONE")

        return {'FINISHED'}
