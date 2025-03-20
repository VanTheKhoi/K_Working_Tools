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
import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore

# Reload
reload(K_Utilities)


def is_in_user_perspective():
    is_correct = False
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            if area.spaces.active.local_view is not None:
                is_correct = True

    return is_correct
            

def isolate_on_off_object_level():
    all_selected = K_Utilities.get_all_selected_meshes_in_scene()
    object_selected = all_selected[0]

    if object_selected:
        bpy.ops.view3d.localview()


def isolate_on_off_collection_level():
    all_selected = K_Utilities.get_all_selected_meshes_in_scene()
    object_selected = all_selected[0]

    if object_selected:
        obj = object_selected[0]
        collections = obj.users_collection[0]
        bpy.context.view_layer.active_layer_collection = collections
        bpy.ops.outliner.collection_isolate()

