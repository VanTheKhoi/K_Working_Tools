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

class KWT_MT_K_Geometry_Display(Menu):
    bl_idname = "KWT_MT_K_Geometry_Display"
    bl_label = "K Geometry Display"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout
        main_layout = layout.row()

        # Operator 
        first_column = main_layout.column(align=True)

        first_column.operator('object.ot_switch_selection', 
                    text='OBJECT', 
                    emboss=True,
                    depress=False,
                    icon='OBJECT_DATAMODE'
                    ).action = 'TO_OBJECT'
        
        first_column.operator('object.ot_switch_selection', 
                    text='VERTEX', 
                    emboss=True,
                    depress=False,
                    icon='VERTEXSEL'
                    ).action = 'TO_VERTEX'
        
        first_column.operator('object.ot_switch_selection', 
                    text='FACE', 
                    emboss=True,
                    depress=False,
                    icon='FACESEL'
                    ).action = 'TO_FACE'
        
        first_column.operator('object.ot_switch_selection', 
                    text='EDGE', 
                    emboss=True,
                    depress=False,
                    icon='EDGESEL'
                    ).action = 'TO_EDGE'

        second_column = main_layout.column(align=True)

        second_column.operator('object.ot_geometry_display', 
                    text='SOLID', 
                    emboss=True,
                    depress=False,
                    icon='SHADING_SOLID'
                    ).action = 'SHOW_SOLID'
        
        second_column.operator('object.ot_geometry_display', 
                    text='MATERIAL', 
                    emboss=True,
                    depress=False,
                    icon='SHADING_TEXTURE'
                    ).action = 'SHOW_MATERIAL'
        
        second_column.operator('object.ot_geometry_display', 
                    text='RENDERED', 
                    emboss=True,
                    depress=False,
                    icon='SHADING_RENDERED'
                    ).action = 'SHOW_RENDERED'

        second_column.operator('object.ot_geometry_display', 
                            text='WIRE FRAME', 
                            emboss=True,
                            depress=False,
                            icon='SHADING_WIRE'
                            ).action = 'SHOW_WIRE_FRAME'
        
        second_column.operator('object.ot_geometry_display', 
                            text='FACE ORIENTATION', 
                            emboss=True,
                            depress=False,
                            icon='SEQUENCE_COLOR_05'
                            ).action = 'SHOW_FACE_ORIENTATION'
        
        second_column.operator('object.ot_geometry_display', 
                            text='NORMAL', 
                            emboss=True,
                            depress=False,
                            icon='EVENT_N'
                            ).action = 'SHOW_NORMAL'