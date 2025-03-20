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

class KWT_MT_K_Combine_Detach(Menu):
    bl_idname = "KWT_MT_K_Combine_Detach"
    bl_label = "K Combine Detach"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        # Operator 
        layout.operator('object.ot_combine_detach', 
                    text='Combine', 
                    emboss=True,
                    depress=False,
                    icon='MODIFIER'
                    ).action = 'COMBINE_OBJECTS'
        
        layout.operator('object.ot_combine_detach', 
                    text='Duplicate faces', 
                    emboss=True,
                    depress=False,
                    icon='MODIFIER'
                    ).action = 'DUPLICATE_FACES_SELECTED'
        
        layout.operator('object.ot_combine_detach', 
                    text='Detach faces', 
                    emboss=True,
                    depress=False,
                    icon='MODIFIER'
                    ).action = 'DETACH_FACES_SELECTED'
        
        layout.operator('object.ot_combine_detach', 
                    text='Detach within material', 
                    emboss=True,
                    depress=False,
                    icon='MODIFIER'
                    ).action = 'DETACH_OBJECTS_WITHIN_MATERIAL'