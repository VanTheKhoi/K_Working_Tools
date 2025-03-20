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
import K_Working_Tools.K_Switch_Selection.Functions.K_Switch_Selection_Utilities as K_Switch_Selection_Utilities # type: ignore

# Reload
reload(K_Switch_Selection_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Switch_Selection(Operator):
    """Switch selection to Vertex/ Face/ Edge"""
    bl_idname = "object.ot_switch_selection"
    bl_label = "K Switch Selection"

    action: EnumProperty(
        items=[
            ('TO_EDGE', 'to_edge', 'to_edge'),
            ('TO_FACE', 'to_face', 'to_face'),
            ('TO_VERTEX', 'to_vertex', 'to_vertex'),
            ('TO_OBJECT', 'to_object', 'to_object')
            ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'TO_EDGE':
            K_Switch_Selection_Utilities.to_edge()

        elif self.action == 'TO_FACE':
            K_Switch_Selection_Utilities.to_face()

        elif self.action == 'TO_VERTEX':
            K_Switch_Selection_Utilities.to_vertex()

        elif self.action == 'TO_OBJECT':
            K_Switch_Selection_Utilities.to_object()

        return {'FINISHED'}