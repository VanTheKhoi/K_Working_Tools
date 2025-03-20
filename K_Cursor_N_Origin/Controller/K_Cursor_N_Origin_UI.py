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

class KWT_MT_K_Cursor_N_Origin(Menu):
    bl_idname = "KWT_MT_K_Cursor_N_Origin"
    bl_label = "K Cursor N Origin"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        # Operator
        main_row = layout.row(align=True)

        origin_layout = main_row.column()
        origin_layout.operator('object.ot_origin_to_selected_snap', 
                    text='Origin to Selected', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'ORIGIN_TO_SELECTED'

        origin_layout.operator('object.ot_origin_to_mesh_snap', 
                    text='Origin to Mesh', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'ORIGIN_TO_MESH'
        
        origin_layout.operator('object.ot_origin_to_cursor_snap', 
                    text='Origin to Cursor', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_ORIGIN'
                    ).action = 'ORIGIN_TO_CURSOR'
        
        cursor_layout = main_row.column()
        cursor_layout.operator('object.ot_cursor_to_selected_snap', 
                    text='Cursor to Selected', 
                    emboss=True,
                    depress=False,
                    icon='CURSOR'
                    ).action = 'CURSOR_TO_SELECTED'
        
        cursor_layout.operator('object.ot_cursor_to_active_snap', 
                    text='Cursor to Active', 
                    emboss=True,
                    depress=False,
                    icon='CURSOR'
                    ).action = 'CURSOR_TO_ACTIVE'
        
        cursor_layout.operator('object.ot_cursor_to_center_snap', 
                    text='Cursor to Center', 
                    emboss=True,
                    depress=False,
                    icon='CURSOR'
                    ).action = 'CURSOR_TO_CENTER'