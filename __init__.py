# ---------------------------------------------------------------- # 
# Hi there! I hope you’re enjoying this tool.
# If you have any concerns or feedback about the tool,
# Please feel free to contact me via email.
#
# vanthekhoi@gmail.com 
#
# Thank you :))
# ---------------------------------------------------------------- #


bl_info = {
    "name" : "K_Working_Tools",
    "author" : "khoivan",
    "description" : "Press Alt Shift W to open the tool in 3D viewport.\n If you have any feedback please contact me via vanthekhoi@gmail.com",
    "blender" : (4, 0, 0),
    "version" : (0, 0, 1),
    "location" : "3D View",
    "warning" : "",
    "category" : "Object",
}

try:
    from imp import reload
except:
    pass

import bpy
import os
import sys

# Find root path
TOOL_ROOT_PATH_WORKING = os.path.dirname(os.path.abspath(__file__))
TOOL_ROOT_PATH_WORKING = TOOL_ROOT_PATH_WORKING.replace("\\", "/")

print("---- K WORKING TOOLS LOADED ----")
print(TOOL_ROOT_PATH_WORKING)

sys.path.append(TOOL_ROOT_PATH_WORKING)

# Import - Main controller
import K_Working_Tools.K_MainController.Controller.K_MainController_UI as K_MainController_UI # type: ignore

# Import - Geometry diplay 
import K_Working_Tools.K_Geometry_Display.Controller.K_Geometry_Display_UI as K_Geometry_Display_UI # type: ignore
import K_Working_Tools.K_Geometry_Display.Functions.K_Geometry_Display_Action as K_Geometry_Display_Action # type: ignore

# Import - Cursor n origin
import K_Working_Tools.K_Cursor_N_Origin.Controller.K_Cursor_N_Origin_UI as K_Cursor_N_Origin_UI # type: ignore
import K_Working_Tools.K_Cursor_N_Origin.Functions.K_Cursor_N_Origin_Action as K_Cursor_N_Origin_Action # type: ignore

# Import - Transform
import K_Working_Tools.K_Transform.Controller.K_Transform_UI as K_Transform_UI # type: ignore
import K_Working_Tools.K_Transform.Functions.K_Transform_Action as K_Transform_Action # type: ignore

# Import - Vertex
import K_Working_Tools.K_Vertex.Controller.K_Vertex_UI as K_Vertex_UI # type: ignore
import K_Working_Tools.K_Vertex.Functions.K_Vertex_Action as K_Vertex_Action # type: ignore

# Import - Show Hide
# import K_Working_Tools.K_Show_Hide.Controller.K_Show_Hide_UI as K_Show_Hide_UI # type: ignore
# import K_Working_Tools.K_Show_Hide.Functions.K_Show_Hide_Action as K_Show_Hide_Action # type: ignore

# Import - Cleanup
import K_Working_Tools.K_Cleanup.Controller.K_Cleanup_UI as K_Cleanup_UI # type: ignore
import K_Working_Tools.K_Cleanup.Functions.K_Cleanup_Action as K_Cleanup_Action # type: ignore

# Import - Combine Detach
import K_Working_Tools.K_Combine_Detach.Controller.K_Combine_Detach_UI as K_Combine_Detach_UI # type: ignore
import K_Working_Tools.K_Combine_Detach.Functions.K_Combine_Detach_Action as K_Combine_Detach_Action # type: ignore

# Import - Validate
# import K_Working_Tools.K_Validate.Controller.K_Validate_UI as K_Validate_UI # type: ignore
# import K_Working_Tools.K_Validate.Functions.K_Validate_Action as K_Validate_Action # type: ignore

# Import - Switch Selection
import K_Working_Tools.K_Switch_Selection.Controller.K_Switch_Selection_UI as K_Switch_Selection_UI # type: ignore
import K_Working_Tools.K_Switch_Selection.Functions.K_Switch_Selection_Action as K_Switch_Selection_Action # type: ignore

# Import - Normal
import K_Working_Tools.K_Normal.Controller.K_Normal_UI as K_Normal_UI # type: ignore
import K_Working_Tools.K_Normal.Functions.K_Normal_Action as K_Normal_Action # type: ignore

# Import - Edge
# import K_Working_Tools.K_Edge.Controller.K_Edge_UI as K_Edge_UI # type: ignore
# import K_Working_Tools.K_Edge.Functions.K_Edge_Action as K_Edge_Action # type: ignore

# Import - Others
import K_Working_Tools.K_Global.K_Props as K_Props # type: ignore

global_addon_keymap = {}


def register_key_1():
    key_config = bpy.context.window_manager.keyconfigs.addon
    if key_config:
        key_map = key_config.keymaps.new(name="3D View", space_type="VIEW_3D")
        
        key_map_item = key_map.keymap_items.new("wm.call_menu_pie",
                            type= "W",
                            value= "PRESS",
                            repeat= True,
                            ctrl=False,
                            alt=True,
                            shift=True)
        
        key_map_item.properties.name = "KWT_MT_K_Working_Tools"
        global_addon_keymap['key_1'] = (key_map, key_map_item)
        print("Configurate key DONE !!")


def register():
    # Reload - Main controller
    reload(K_MainController_UI)

    # Reload - Geometry display
    reload(K_Geometry_Display_UI)
    reload(K_Geometry_Display_Action)

    # Reload - Cursor n origin
    reload(K_Cursor_N_Origin_UI)
    reload(K_Cursor_N_Origin_Action)

    # Reload - Transform
    reload(K_Transform_UI)
    reload(K_Transform_Action)

    # Reload - Vertex
    reload(K_Vertex_UI)
    reload(K_Vertex_Action)

    # Reload - Show Hide
    # reload(K_Show_Hide_UI)
    # reload(K_Show_Hide_Action)

    # Reload - Cleanup
    reload(K_Cleanup_UI)
    reload(K_Cleanup_Action)

    # Reload - Combine Detach
    reload(K_Combine_Detach_UI)
    reload(K_Combine_Detach_Action)

    # Reload - Validate
    # reload(K_Validate_UI)
    # reload(K_Validate_Action)

    # Reload - Switch Selection
    reload(K_Switch_Selection_UI)
    reload(K_Switch_Selection_Action)

    # Reload - Normal
    reload(K_Normal_UI)
    reload(K_Normal_Action)

    # Reload - Edge
    # reload(K_Edge_UI)
    # reload(K_Edge_Action)

    # Reload - Others
    reload(K_Props)

    # Register key
    register_key_1()

    # Register classs - Main controller
    bpy.utils.register_class(K_MainController_UI.KWT_MT_K_Working_Tools)

    # Register classs - Geometry display
    bpy.utils.register_class(K_Geometry_Display_UI.KWT_MT_K_Geometry_Display)
    bpy.utils.register_class(K_Geometry_Display_Action.KWT_OT_K_Geometry_Display)

    # Register classs - Cursor n origin
    bpy.utils.register_class(K_Cursor_N_Origin_UI.KWT_MT_K_Cursor_N_Origin)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Mesh_Snap)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Cursor_Snap)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Selected_Snap)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Selected_Snap)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Active_Snap)
    bpy.utils.register_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Center_Snap)

    # Register classs - Transform
    bpy.utils.register_class(K_Transform_UI.KWT_MT_K_Transform)
    bpy.utils.register_class(K_Transform_Action.KWT_OT_K_Transform)

    # Register classs - Vertex
    bpy.utils.register_class(K_Vertex_UI.KWT_MT_K_Vertex)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Addivision_Smooth_Vertices)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Snap_Vertex_To_Mesh)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Snap_Mesh_To_Vertex)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Snap_Vertex_To_Mesh_N_Merge)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Copy_Paste_Vertex)
    bpy.utils.register_class(K_Vertex_Action.KWT_OT_K_Merge_Vertices)

    # Register classs - Show Hide
    # bpy.utils.register_class(K_Show_Hide_UI.KWT_MT_K_Show_Hide)
    # bpy.utils.register_class(K_Show_Hide_Action.KWT_OT_K_Show_Hide)

    # Register classs - Cleanup
    bpy.utils.register_class(K_Cleanup_UI.KWT_MT_K_Cleanup)
    bpy.utils.register_class(K_Cleanup_Action.KWT_OT_K_Cleanup)

    # Register classs - Combine Detach
    bpy.utils.register_class(K_Combine_Detach_UI.KWT_MT_K_Combine_Detach)
    bpy.utils.register_class(K_Combine_Detach_Action.KWT_OT_K_Combine_Detach)

    # Register classs - Validate
    # bpy.utils.register_class(K_Validate_UI.KWT_MT_K_Validate)
    # bpy.utils.register_class(K_Validate_Action.KWT_OT_K_Validate)

    # Register classs - Switch Selection
    bpy.utils.register_class(K_Switch_Selection_UI.KWT_MT_K_Switch_Selection)
    bpy.utils.register_class(K_Switch_Selection_Action.KWT_OT_K_Switch_Selection)

    # Register classs - Normal
    bpy.utils.register_class(K_Normal_UI.KWT_MT_K_Normal)
    bpy.utils.register_class(K_Normal_Action.KWT_OT_K_Normal)

    # Register classs - Edge
    # bpy.utils.register_class(K_Edge_UI.KWT_MT_K_Edge)
    # bpy.utils.register_class(K_Edge_Action.KWT_OT_K_Edge)

    # Register classs - Others
    bpy.utils.register_class(K_Props.KWT_Propertise_Setup)


def unregister():
    # Un-Register key
    for key_map, key_map_item in global_addon_keymap.items():
        try:
            key_map.keymap_items.remove(key_map_item)
        except:
            pass

    global_addon_keymap.clear()

    # Un-Register classs - Main controller
    bpy.utils.unregister_class(K_MainController_UI.KWT_MT_K_Working_Tools)

    # Un-Register classs - Geometry display
    bpy.utils.unregister_class(K_Geometry_Display_UI.KWT_MT_K_Geometry_Display)
    bpy.utils.unregister_class(K_Geometry_Display_Action.KWT_OT_K_Geometry_Display)

    # Un-Register classs - Cursor n origin
    bpy.utils.unregister_class(K_Cursor_N_Origin_UI.KWT_MT_K_Cursor_N_Origin)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Mesh_Snap)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Cursor_Snap)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Origin_To_Selected_Snap)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Selected_Snap)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Active_Snap)
    bpy.utils.unregister_class(K_Cursor_N_Origin_Action.KWT_OT_K_Cursor_To_Center_Snap)

    # Un-Register classs - Transform
    bpy.utils.unregister_class(K_Transform_UI.KWT_MT_K_Transform)
    bpy.utils.unregister_class(K_Transform_Action.KWT_OT_K_Transform)

    # Un-Register classs - Vertex
    bpy.utils.unregister_class(K_Vertex_UI.KWT_MT_K_Vertex)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Addivision_Smooth_Vertices)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Snap_Vertex_To_Mesh)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Snap_Mesh_To_Vertex)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Snap_Vertex_To_Mesh_N_Merge)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Copy_Paste_Vertex)
    bpy.utils.unregister_class(K_Vertex_Action.KWT_OT_K_Merge_Vertices)

    #Un-Register classs - Show Hide
    # bpy.utils.unregister_class(K_Show_Hide_UI.KWT_MT_K_Show_Hide)
    # bpy.utils.unregister_class(K_Show_Hide_Action.KWT_OT_K_Show_Hide)

    # Un-Register classs - Cleanup
    bpy.utils.unregister_class(K_Cleanup_UI.KWT_MT_K_Cleanup)
    bpy.utils.unregister_class(K_Cleanup_Action.KWT_OT_K_Cleanup)

    # Un-Register classs - Combine Detach
    bpy.utils.unregister_class(K_Combine_Detach_UI.KWT_MT_K_Combine_Detach)
    bpy.utils.unregister_class(K_Combine_Detach_Action.KWT_OT_K_Combine_Detach)

    # Un-Register classs - Validate
    # bpy.utils.unregister_class(K_Validate_UI.KWT_MT_K_Validate)
    # bpy.utils.unregister_class(K_Validate_Action.KWT_OT_K_Validate)

    # Un-Register classs - Switch Selection
    bpy.utils.unregister_class(K_Switch_Selection_UI.KWT_MT_K_Switch_Selection)
    bpy.utils.unregister_class(K_Switch_Selection_Action.KWT_OT_K_Switch_Selection)

    # Un-Register classs - Normal
    bpy.utils.unregister_class(K_Normal_UI.KWT_MT_K_Normal)
    bpy.utils.unregister_class(K_Normal_Action.KWT_OT_K_Normal)

    # Un-Register classs - Edge
    # bpy.utils.unregister_class(K_Edge_UI.KWT_MT_K_Edge)
    # bpy.utils.unregister_class(K_Edge_Action.KWT_OT_K_Edge)

    # Un-Register classs - Others
    bpy.utils.unregister_class(K_Props.KWT_Propertise_Setup)