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

class KWT_MT_K_Cleanup(Menu):
    bl_idname = "KWT_MT_K_Cleanup"
    bl_label = "K Cleanup"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout
        main_layout = layout.row()

        # Operator 
        first_column = main_layout.column(align=True)

        first_column.operator('object.ot_cleanup', 
            text='Clean unused materials', 
            emboss=True,
            depress=False,
            icon='BRUSH_DATA'
            ).action = 'CLEANUP_UNUSED_MATERIAL'
        
        first_column.operator('object.ot_cleanup', 
            text='Clean unused data', 
            emboss=True,
            depress=False,
            icon='BRUSH_DATA'
            ).action = 'CLEANUP_UNUSED_DATA'
        
        second_column = main_layout.column(align=True)

        second_column.operator('object.ot_transform', 
            text='All Transform', 
            emboss=True,
            depress=False,
            icon='OBJECT_ORIGIN'
            ).action = 'APPLY_ALL_TRANSFORM'
        
        second_column.operator('object.ot_transform', 
            text='Transform to Deltas', 
            emboss=True,
            depress=False,
            icon='OBJECT_ORIGIN'
            ).action = 'TRANSFORM_TO_DELTAS'
