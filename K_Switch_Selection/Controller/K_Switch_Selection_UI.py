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
from bpy.types import Menu

class KWT_MT_K_Switch_Selection(Menu):
    bl_idname = "KWT_MT_K_Switch_Selection"
    bl_label = "K Switch Selection"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        # Operator 
        layout.operator('object.ot_switch_selection', 
                    text='OBJECT', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_DATAMODE'
                    ).action = 'TO_OBJECT'
        
        layout.operator('object.ot_switch_selection', 
                    text='VERTEX', 
                    emboss=True,
                    depress=False,
                    icon='VERTEXSEL'
                    ).action = 'TO_VERTEX'
        
        layout.operator('object.ot_switch_selection', 
                    text='FACE', 
                    emboss=True,
                    depress=False,
                    icon='FACESEL'
                    ).action = 'TO_FACE'
        
        layout.operator('object.ot_switch_selection', 
                    text='EDGE', 
                    emboss=True,
                    depress=False,
                    icon='EDGESEL'
                    ).action = 'TO_EDGE'