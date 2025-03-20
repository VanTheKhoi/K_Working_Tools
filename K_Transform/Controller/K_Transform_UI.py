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

class KWT_MT_K_Transform(Menu):
    bl_idname = "KWT_MT_K_Transform"
    bl_label = "K Transform"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        main_column = layout.row(align=True)

        transform_layout = main_column.column()
        transform_layout.operator('object.ot_transform', 
                    text='Location', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'APPLY_LOCATION'
        
        transform_layout.operator('object.ot_transform', 
                    text='Rotation', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'APPLY_ROTATION'
        
        transform_layout.operator('object.ot_transform', 
                    text='Scale', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'APPLY_SCALE'
        
        transform_layout.operator('object.ot_transform', 
                    text='All Transform', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'APPLY_ALL_TRANSFORM'
        
        deltas_layout = main_column.column()
        deltas_layout.operator('object.ot_transform', 
                    text='Location to Deltas', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'LOCATION_TO_DELTAS'
        
        deltas_layout.operator('object.ot_transform', 
                    text='Rotation to Deltas', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'ROTATION_TO_DELTAS'
        
        deltas_layout.operator('object.ot_transform', 
                    text='Scale to Deltas', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'SCALE_TO_DELTAS'
        
        deltas_layout.operator('object.ot_transform', 
                    text='Transform to Deltas', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'TRANSFORM_TO_DELTAS'