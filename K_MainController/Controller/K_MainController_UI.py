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

class KWT_MT_K_Working_Tools(Menu):
    bl_idname = "KWT_MT_K_Working_Tools"
    bl_label = "K Working Tools"

    def draw(self, context):
        # --------------------- Main layout -------------------- #
        scene = context.scene
        layout = self.layout
        pie_main_layout = layout.menu_pie()

        # ---------------- POSITION : LEFT --------------------- #
        # ------------------------------------------------------ #
        # ---------------- Geometry Display -------------------- #
        main_box_geometry_display = pie_main_layout.split().box()
        main_box_geometry_display.enabled = True
        main_box_geometry_display.alert = False
        main_box_geometry_display.scale_x = 1.1
        main_box_geometry_display.scale_y = 1.0

        main_column_geometry_display = main_box_geometry_display.column()
        main_column_geometry_display.menu("KWT_MT_K_Geometry_Display",text=r"Geometry Display", icon="MESH_UVSPHERE")

        # ---------------- POSITION : RIGHT --------------------- #
        # ------------------------------------------------------#
        # ---------------- Normal ------------------- #
        main_box_normals = pie_main_layout.split().box()
        main_box_normals.enabled = True
        main_box_normals.alert = False
        main_box_normals.scale_x = 1.1
        main_box_normals.scale_y = 1.0

        main_column_normals = main_box_normals.column(align=True)
        main_column_normals.menu("KWT_MT_K_Normal",text=r"Normals", icon="MOD_NORMALEDIT")

        # ---------------- POSITION : BOTTOM --------------------- #
        # ---------------------------------------------------- #
        # ---------------- Clean up ------------------- #
        main_box_cleanup = pie_main_layout.split().box()
        main_box_cleanup.enabled = True
        main_box_cleanup.alert = False
        main_box_cleanup.scale_x = 1.1
        main_box_cleanup.scale_y = 1.0

        main_column_cleanup = main_box_cleanup.column(align=True)
        main_column_cleanup.menu("KWT_MT_K_Cleanup",text=r"Cleanup", icon="BRUSH_DATA")

        # ---------------- POSITION : TOP --------------------- #
        # ---------------------------------------------------- #
        # ---------------- Combine Detach ------------------- #
        main_box_combine_detach = pie_main_layout.split().box()
        main_box_combine_detach.enabled = True
        main_box_combine_detach.alert = False
        main_box_combine_detach.scale_x = 1.1
        main_box_combine_detach.scale_y = 1.0

        main_column_combine_detach = main_box_combine_detach.column(align=True)
        main_column_combine_detach.menu("KWT_MT_K_Combine_Detach",text=r"Combine/ Detach", icon="MODIFIER")

        # ---------------- POSITION : TOP LEFT --------------------- #
        # ---------------------------------------------------- #
        # ---------------- Cursor n Origin ------------------- #
        main_box_cursor_n_origin = pie_main_layout.split().box()
        main_box_cursor_n_origin.enabled = True
        main_box_cursor_n_origin.alert = False
        main_box_cursor_n_origin.scale_x = 1.1
        main_box_cursor_n_origin.scale_y = 1.0

        main_column_cursor_n_origin = main_box_cursor_n_origin.column(align=True)
        main_column_cursor_n_origin.menu("KWT_MT_K_Cursor_N_Origin",text=r"Cursor/ Origin", icon="CURSOR")

        # ---------------- POSITION : TOP RIGHT --------------------- #
        # ---------------------------------------------------- #
        # ---------------- Vertex ------------------- #
        main_box_vertex = pie_main_layout.split().box()
        main_box_vertex.enabled = True
        main_box_vertex.alert = False
        main_box_vertex.scale_x = 1.1
        main_box_vertex.scale_y = 1.0

        main_column_vertex = main_box_vertex.column(align=True)
        main_column_vertex.menu("KWT_MT_K_Vertex",text=r"Vertex", icon="MODIFIER")