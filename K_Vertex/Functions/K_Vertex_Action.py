# ---------------------------------------------------------------- # 
# Hi there! I hope you’re enjoying this tool.
# If you have any concerns or feedback about the tool,
# Please feel free to contact me via email.
#
# vanthekhoi@gmail.com 
#
# Thank you :))
# ---------------------------------------------------------------- #


try:
    from imp import reload
except:
    pass

import bpy
from bpy.props import EnumProperty
from bpy.types import Operator

# Import
import K_Working_Tools.K_Vertex.Functions.K_Vertex_Utilities as K_Vertex_Utilities # type: ignore

# Reload
reload(K_Vertex_Utilities)

# # --- OPERATOR CLASS --- #
class KWT_OT_K_Snap_Vertex_To_Mesh(Operator):
    """Snap vertices selected to mesh"""
    bl_idname = "object.ot_snap_vertex_to_mesh"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('SNAP_VERTEX_TO_MESH', 'snap_vertex_to_mesh', 'snap_vertex_to_mesh')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'SNAP_VERTEX_TO_MESH':
            K_Vertex_Utilities.snap_vertex_to_mesh(threshold=5, is_reverted=False, is_merge=False)

        return {'FINISHED'}
    

class KWT_OT_K_Snap_Mesh_To_Vertex(Operator):
    """Snap mesh selected to vertex"""
    bl_idname = "object.ot_snap_mesh_to_vertex"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('SNAP_MESH_TO_VERTEX', 'snap_mesh_to_vertex', 'snap_mesh_to_vertex')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'SNAP_MESH_TO_VERTEX':
            K_Vertex_Utilities.snap_vertex_to_mesh(threshold=5, is_reverted=True, is_merge=False)

        return {'FINISHED'}
    

class KWT_OT_K_Snap_Vertex_To_Mesh_N_Merge(Operator):
    """Snap vertices selected to mesh and merge"""
    bl_idname = "object.ot_snap_vertex_to_mesh_n_merge"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('SNAP_VERTEX_TO_MESH_N_MERGE', 'snap_vertex_to_mesh_n_merge', 'snap_vertex_to_mesh_n_merge')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'SNAP_VERTEX_TO_MESH_N_MERGE':
            K_Vertex_Utilities.snap_vertex_to_mesh(threshold=5, is_reverted=False, is_merge=True)

        return {'FINISHED'}
    

class KWT_OT_K_Copy_Paste_Vertex(Operator):
    """Get/ Set vertex position"""
    bl_idname = "object.ot_copy_paste_vertex"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('COPY_VERTEX', 'copy_vetex', 'copy_vetex'),
        ('COPY_AVERAGE', 'copy_average', 'copy_average'),
        ('PASTE_VERTEX', 'paste_vertex', 'paste_vertex')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'COPY_VERTEX':
            K_Vertex_Utilities.copy_vertex()

        elif self.action == 'COPY_AVERAGE':
            K_Vertex_Utilities.copy_average_vertices()

        elif self.action == 'PASTE_VERTEX':
            K_Vertex_Utilities.paste_vertex()

        return {'FINISHED'}
    

class KWT_OT_K_Merge_Vertices(Operator):
    """Merge vertices"""
    bl_idname = "object.ot_merge_vertices"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('MERGE_CENTER', 'merge_center', 'merge_center'),
        ('MERGE_BY_DISTANCE', 'merge_by_distance', 'merge_by_distance')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'MERGE_CENTER':
            K_Vertex_Utilities.merge_verticies(mode='CENTER')

        elif self.action == 'MERGE_BY_DISTANCE':
            K_Vertex_Utilities.merge_verticies(mode='DISTANCE')

        return {'FINISHED'}
    

class KWT_OT_K_Addivision_Smooth_Vertices(Operator):
    """Add new vert and smooth normal"""
    bl_idname = "object.ot_addivision_smooth_vertices"
    bl_label = "K Vertex"

    action: EnumProperty(
    items=[
        ('ADD_SMOOTH_VERT', 'add_smooth_vert', 'add_smooth_vert')
        ]
    ) # type: ignore

    def execute(self, context):
        scene = context.scene

        if self.action == 'ADD_SMOOTH_VERT':
            K_Vertex_Utilities.subdivide_and_smooth_middle_vertices()

        return {'FINISHED'}