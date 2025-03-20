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

import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore

# Reload
reload(K_Utilities)

def to_edge():
    all_meshes = K_Utilities.get_all_selected_meshes_in_scene()
    all_meshes = all_meshes[0] + all_meshes[1]

    for mesh in all_meshes:
        K_Utilities.convert_mesh_to_mode_input(mesh, 'EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')


def to_face():
    all_meshes = K_Utilities.get_all_selected_meshes_in_scene()
    all_meshes = all_meshes[0] + all_meshes[1]

    for mesh in all_meshes:
        K_Utilities.convert_mesh_to_mode_input(mesh, 'EDIT')
        bpy.ops.mesh.select_mode(type='FACE')


def to_vertex():
    all_meshes = K_Utilities.get_all_selected_meshes_in_scene()
    all_meshes = all_meshes[0] + all_meshes[1]
    
    for mesh in all_meshes:
        K_Utilities.convert_mesh_to_mode_input(mesh, 'EDIT')
        bpy.ops.mesh.select_mode(type='VERT')


def to_object():
    all_meshes = K_Utilities.get_all_selected_meshes_in_scene()
    all_meshes = all_meshes[0] + all_meshes[1]

    for mesh in all_meshes:
        K_Utilities.convert_mesh_to_mode_input(mesh, 'OBJECT')