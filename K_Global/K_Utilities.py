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
import bmesh


def get_all_selected_meshes_in_scene():
    """ Function to get all mesh in edit mode and object mode in scene 
    """
    # Data return
    meshes_object_mode = []
    meshes_edit_mode = []

    #Get all objects in scene 
    objects_in_scene = bpy.context.scene.objects

    # Now we define which object is MESH
    meshes_selected = [obj for obj in objects_in_scene if obj.type=="MESH"]

    for mesh in meshes_selected:
        # Get all meshes in OBJECT mode 
        if(mesh.mode == "OBJECT"):
            # We check if mesh was selected
            if mesh.select_get():
                meshes_object_mode.append(mesh)

        # Get all meshes in EDIT mode
        elif(mesh.mode == "EDIT"):
            meshes_edit_mode.append(mesh)

    # Cleanup list
    meshes_object_mode = list(dict.fromkeys(meshes_object_mode))
    meshes_edit_mode = list(dict.fromkeys(meshes_edit_mode))

    return [meshes_object_mode, meshes_edit_mode]


def get_all_vertices_coordinate(mesh_input, mode):
    return_list = {}
    mesh = mesh_input.data
    bm = bmesh.from_edit_mesh(mesh)
    # ob = bpy.context.active_object
    obMat = mesh_input.matrix_world
    
    for v in bm.verts:
        if(mode=="Selected"):
            if(v.select):
                return_list[str(v.index)] = obMat @ v.co
        else:
            return_list[str(v.index)] = obMat @ v.co
            v.select_set(False)

    return return_list


def select_mesh(mesh_input=None):
    ''' Set selection of mesh input
    
    '''

    if mesh_input:
        mesh_input.select_set(True)
        bpy.context.view_layer.objects.active = mesh_input
    

def convert_mesh_to_mode_input(mesh_input, mode_input):
    select_mesh(mesh_input)
    bpy.context.view_layer.objects.active = mesh_input
    bpy.ops.object.mode_set(mode=mode_input)


def cleanup_unused_materials():
    # Get all materials in the scene
    all_materials = bpy.data.materials
    
    # Dictionary to store all materials
    material_usage = {mat.name: False for mat in all_materials}
    
    # Iterate over all objects in the scene
    for obj in bpy.data.objects:
        # Check each material slot in the object
        for slot in obj.material_slots:
            material_slot = slot.material
            if material_slot:
                material_usage[material_slot.name] = True
                # print("Object material linked >>>>> ", slot.material.name, obj.name)
    
    # Remove material not usage
    material_ignore_list = ["Dots Stroke", "Material"]

    for material, is_used in material_usage.items():
        if not is_used and material not in material_ignore_list:
            bpy.data.materials.remove(bpy.data.materials.get(material))


def cleanup_unused_data():
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=False)


def convert_mesh_to_mode_input(mesh_input, mode_input):
    select_mesh(mesh_input=mesh_input)
    bpy.context.view_layer.objects.active = mesh_input
    bpy.ops.object.mode_set(mode=mode_input)


def cleanup_un_used_material_slot(obj):
    bpy.ops.mesh.select_all(action='DESELECT')
    material_slot = obj.material_slots
    convert_mesh_to_mode_input(obj, mode_input='EDIT')

    for index in material_slot:
        obj.active_material_index = index
        bpy.ops.object.material_slot_select()

        all_selected = get_all_selected_meshes_in_scene()
        edit_mode = all_selected[1]

        if not edit_mode:
            print("REMOVE >>>>> ", index)


def get_all_object_in_scene(type_input=""):
    ''' Get all objects in scene with type input
        type : MESH/ CAMERA/ LIGHT/....
    
    '''
    # Data return
    objects_type_return = []
    
    if type_input:
        #Get all objects in scene 
        objects_in_scene = bpy.context.scene.objects
        
        # Object return
        objects_type_return = [obj for obj in objects_in_scene if obj.type==type_input]

    return objects_type_return


def get_the_last_n_first_selection(selected_meshes):
    first_selection = None
    active_objects = bpy.context.active_object

    for mesh in selected_meshes:
        if(mesh.name_full == active_objects.name_full):
            first_selection = mesh
            break

    selected_meshes.pop(selected_meshes.index(first_selection))
    last_selection = selected_meshes[0]

    return [first_selection, last_selection]
