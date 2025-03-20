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

class KWT_MT_K_Vertex(Menu):
    bl_idname = "KWT_MT_K_Vertex"
    bl_label = "K Vertex"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout

        main_column = layout.column()
        snap_box_layout = main_column.column()

        snap_box_layout.operator('object.ot_addivision_smooth_vertices', 
                text='Addivision Smooth', 
                emboss=True,
                depress=False,
                icon='MOD_NORMALEDIT'
                ).action = 'ADD_SMOOTH_VERT'

        snap_box_layout.operator('object.ot_snap_vertex_to_mesh', 
                    text='Vertices to Mesh', 
                    emboss=True,
                    depress=False,
                    icon='SNAP_ON'
                    ).action = 'SNAP_VERTEX_TO_MESH'

        snap_box_layout.operator('object.ot_snap_vertex_to_mesh_n_merge', 
                    text='Snap vertices and merge', 
                    emboss=True,
                    depress=False,
                    icon='SNAP_ON'
                    ).action = 'SNAP_VERTEX_TO_MESH_N_MERGE'
        
        main_column.operator('object.ot_copy_paste_vertex', 
                    text='Get vertex position', 
                    emboss=True,
                    depress=False,
                    icon='COPYDOWN'
                    ).action = 'COPY_VERTEX'
        
        main_column.operator('object.ot_copy_paste_vertex', 
                    text='Get vertices average', 
                    emboss=True,
                    depress=False,
                    icon='COPYDOWN'
                    ).action = 'COPY_AVERAGE'
                
        main_column.operator('object.ot_copy_paste_vertex', 
                    text='Set vertices', 
                    emboss=True,
                    depress=False,
                    icon='PASTEDOWN'
                    ).action = 'PASTE_VERTEX'
        
        main_column.operator('object.ot_merge_vertices', 
                    text='Merge center', 
                    emboss=True,
                    depress=False,
                    icon='AUTOMERGE_ON'
                    ).action = 'MERGE_CENTER'
        
        main_column.operator('object.ot_merge_vertices', 
                    text='Remove double', 
                    emboss=True,
                    depress=False,
                    icon='AUTOMERGE_ON'
                    ).action = 'MERGE_BY_DISTANCE'

