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

class KWT_MT_K_Normal(Menu):
    bl_idname = "KWT_MT_K_Normal"
    bl_label = "K Normal"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        # Operator 
        layout.operator('object.ot_normal', 
                    text='Reset Vector', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'RESET_VECTOR'

        layout.operator('object.ot_normal', 
                    text='Show/Hide Normal', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'TOGGLE_VERTEX_NORMAL'
        
        layout.operator('object.ot_normal', 
                    text='Set From Faces', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'SET_NORMAL_FROM_FACE'

        layout.operator('object.ot_normal', 
                    text='Copy Vector', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'COPY_NORMAL'
        
        layout.operator('object.ot_normal', 
                    text='Paste Vector', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'PASTE_NORMAL'
        
        layout.operator('object.ot_normal', 
                    text='Copy Face Vector', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'COPY_FACE_NORMAL'
        
        layout.operator('object.ot_normal', 
                    text='Paste Face Vector', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'PASTE_VERTEX_FACE'
        
        layout.operator('object.ot_normal', 
                    text='Weighted Face Angle', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'WEIGHTED_FACE_ANGLE'
        
        layout.operator('object.ot_normal', 
                    text='Weighted Face Area', 
                    emboss=True,
                    depress=False,
                    icon='MOD_NORMALEDIT'
                    ).action = 'WEIGHTED_FACE_AREA'