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

# Import 
import K_Working_Tools.K_Cursor_N_Origin.Functions.K_Cursor_N_Origin_Utilities as K_Cursor_N_Origin_Utilities # type: ignore
import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore

# Reload
reload(K_Cursor_N_Origin_Utilities)
reload(K_Utilities)


def combine_objects():
    bpy.ops.object.join()
    K_Cursor_N_Origin_Utilities.origin_to_mesh()


def detach_faces_selected():
    bpy.ops.mesh.separate(type='SELECTED')

    bpy.ops.object.mode_set(mode='OBJECT')

    new_object = bpy.context.view_layer.objects.active = bpy.context.selected_objects[-1]
    bpy.ops.object.select_all(action='DESELECT')
    new_object.select_set(True)

    # Set origin to detached 
    K_Cursor_N_Origin_Utilities.origin_to_mesh()


def duplicate_selected_faces():
    bpy.ops.mesh.duplicate()

    # Separate the duplicated faces into a new object
    bpy.ops.mesh.separate(type='SELECTED')

    bpy.ops.object.mode_set(mode='OBJECT')

    new_object = bpy.context.view_layer.objects.active = bpy.context.selected_objects[-1]
    bpy.ops.object.select_all(action='DESELECT')
    new_object.select_set(True)

    # Set origin to detached 
    K_Cursor_N_Origin_Utilities.origin_to_mesh()


def detach_object_within_material():
    # Get all selected in scene
    all_selected = K_Utilities.get_all_selected_meshes_in_scene()
    objects_selected = all_selected[0]

    for obj in objects_selected:
        bpy.ops.object.select_all(action='DESELECT')
        K_Utilities.select_mesh(obj)

        # Switch to face mode
        K_Utilities.convert_mesh_to_mode_input(obj, "EDIT")
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.separate(type='MATERIAL')
        bpy.ops.object.editmode_toggle()

        all_selected = K_Utilities.get_all_selected_meshes_in_scene()
        objs_selected = all_selected[0]

        # Set origin 
        for obj_selected in objs_selected:
            bpy.ops.object.select_all(action='DESELECT')
            obj_selected.select_set(True)
            K_Cursor_N_Origin_Utilities.origin_to_mesh()
        