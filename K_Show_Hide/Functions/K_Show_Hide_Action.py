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
import K_Working_Tools.K_Show_Hide.Functions.K_Show_Hide_Utilities as K_Show_Hide_Utilities # type: ignore

# Reload
reload(K_Show_Hide_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Show_Hide(Operator):
    """Show hide tools"""
    bl_idname = "object.ot_show_hide"
    bl_label = "K Show Hide"

    action: EnumProperty(
        items=[
            ('ISOLATE_ON_OFF', 'isolate_on_off', 'isolate_on_off'),
            ('ISOLATE_COLLECTION_ON_OFF', 'isolate_collection_on_off', 'isolate_collection_on_off')
            ]
    ) # type: ignore


    def execute(self, context):
        scene = context.scene

        if self.action == 'ISOLATE_ON_OFF':
            K_Show_Hide_Utilities.isolate_on_off_object_level()

        elif self.action == 'ISOLATE_COLLECTION_ON_OFF':
            K_Show_Hide_Utilities.isolate_on_off_collection_level()

        return {'FINISHED'}

