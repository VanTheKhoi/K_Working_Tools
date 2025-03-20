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

class KWT_MT_K_Show_Hide(Menu):
    bl_idname = "KWT_MT_K_Show_Hide"
    bl_label = "K Show Hide"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        # Operator 
        layout.operator('object.ot_show_hide', 
            text='Isolate object', 
            emboss=True,
            depress=False,
            icon='VIS_SEL_11'
            ).action = 'ISOLATE_ON_OFF'
        

        layout.operator('object.ot_show_hide', 
            text='Isolate collection', 
            emboss=True,
            depress=False,
            icon='VIS_SEL_11'
            ).action = 'ISOLATE_COLLECTION_ON_OFF'