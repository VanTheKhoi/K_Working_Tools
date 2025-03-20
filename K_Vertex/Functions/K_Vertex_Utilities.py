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

from mathutils import Vector

import bpy
import bmesh


# Import
import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore
import K_Working_Tools.K_Global.K_Variables as K_Variables # type: ignore
import K_Working_Tools.K_Normal.Functions.K_Normal_Utilities as K_Normal_Utilities # type: ignore
import K_Working_Tools.K_Normal.Functions.K_Normal_Variables as K_Normal_Variables # type: ignore
import K_Working_Tools.K_Switch_Selection.Functions.K_Switch_Selection_Utilities as K_Switch_Selection_Utilities # type: ignore

# Reload
reload(K_Utilities)
reload(K_Variables)
reload(K_Normal_Utilities)
reload(K_Normal_Variables)
reload(K_Switch_Selection_Utilities)


def snap_vertex_to_mesh(threshold=0.5, is_reverted=False, is_merge=False):
    is_smart_snap = True

    #Get all selected meshes in scene 
    objects_selected = K_Utilities.get_all_selected_meshes_in_scene()

    meshes_in_object_mode = objects_selected[0]
    meshes_in_edit_mode = objects_selected[1]

    # Check if more than 2 mesh in OBJECT mode -> WARNING USER
    if(len(meshes_in_object_mode)>1 or len(meshes_in_object_mode) == 0):
        # --- TODO -- #
        # Create popup system here
        return 0
    
    # Check if nothing selected in edit mode
    elif(meshes_in_edit_mode == []):
        # --- TODO -- #
        # Create popup system here
        return 0
    
    selected_vertices_reverted = {}
    vertices_coor_dict_object_mode_mesh = {}

    for mesh_edit_mode in meshes_in_edit_mode:
        # Get all vertices selected of TARGET mesh
        mesh_edit_mode_name = mesh_edit_mode.name_full

        # Process for snap vertices to object
        # Get all vertices coordinates of SOURCE mesh
        mesh_object_mode = meshes_in_object_mode[0]
        K_Utilities.convert_mesh_to_mode_input(mesh_object_mode, "EDIT")
        vertices_coor_dict_object_mode_mesh = K_Utilities.get_all_vertices_coordinate(mesh_object_mode, "None")
        revert_coor_dict = {}

        if is_reverted:
            for k,vectors in vertices_coor_dict_object_mode_mesh.items():
                string_converted = "".join(str(v)+";" for v in vectors)[:-1]
                revert_coor_dict[string_converted] = k

        # Get the bmesh data of TARGET mesh
        mesh_edit = mesh_edit_mode.data
        bm = bmesh.from_edit_mesh(mesh_edit)
        dict_vertex_index_process = {}
        dict_distance = {}
        vector_distance = {}
        source_vertices_tracking = {}
        vector_move_list = []
        ob_mat = mesh_edit_mode.matrix_world
        
        selected_vertices = []

        # Compare selected vertices with all vertices from object we want to snap 
        # And find the shortest distance
        for v in bm.verts:
            if(v.select):
                index = v.index

                if(mesh_edit_mode_name not in selected_vertices_reverted):
                    selected_vertices_reverted[mesh_edit_mode_name] = [index]
                else:
                    selected_vertices_reverted[mesh_edit_mode_name].append(index)
                
                selected_vertices.append(v)
                
                vector_vertex = ob_mat @ v.co

                # Put a Temp value for our dictionary
                dict_distance[str(index)] = [100000]
                for k, v_object in vertices_coor_dict_object_mode_mesh.items():
                    distance = (v_object - vector_vertex).length
                    v_object_str = "".join(str(v)+";" for v in v_object)[:-1]

                    if is_smart_snap:
                        vector_distance[v_object_str + str(index)] = distance

                    if(threshold == 0):
                        dict_vertex_index_process[str(distance)+str(index)] = v_object
                        dict_distance[str(index)].append(distance)
                        source_vertices_tracking[v_object_str] = k

                    elif(distance < threshold):
                        dict_vertex_index_process[str(distance)+str(index)] = v_object
                        dict_distance[str(index)].append(distance)
                        source_vertices_tracking[v_object_str] = k

        if (dict_vertex_index_process != {} and dict_distance != {}):
            # Deselect all vertices
            bpy.ops.mesh.select_all(action='DESELECT')
            vertex_ob_move_dict = {}
            vector_tracking = []

            # Process for move vertex
            for v in selected_vertices:
                index = v.index
                list_distance = dict_distance[str(index)]
                list_distance.pop(0) #Remove TEMP value
                list_distance = list(dict.fromkeys(list_distance))
                
                if list_distance != []:
                    min_distance = min(list_distance)
                    vector_object_will_move = dict_vertex_index_process[str(min_distance) + str(index)]
                    vector_str = "".join(str(v)+";" for v in vector_object_will_move)[:-1]

                    # Process for smart snap
                    if is_smart_snap:
                        if not vector_tracking:
                            vector_tracking.append(vector_str)
                        
                        elif vector_str not in vector_tracking:
                            vector_tracking.append(vector_str)
                        
                        else:
                            for v_str in vector_tracking:
                                distance_remove = vector_distance[v_str+str(index)]
                                index_distance_remove = list_distance.index(distance_remove)
                                list_distance.pop(index_distance_remove)

                            min_distance = min(list_distance)
                            vector_object_will_move = dict_vertex_index_process[str(min_distance) + str(index)]
                            vector_str = "".join(str(v)+";" for v in vector_object_will_move)[:-1]
                            vector_tracking.append(vector_str)

                    # Calculate the vector
                    vector_vertex = ob_mat @ v.co # Get the global

                    if not is_reverted:
                        v.select_set(True)
                        vector_move = vector_object_will_move - vector_vertex

                        # --- DEBUG --- #
                        # print(index)
                        # print(vector_vertex)
                        # print(vector_object_will_move)
                        # print(vector_move)

                        # Move vertex
                        bpy.ops.transform.translate(value=vector_move)

                        # Use this list for merger vertices function
                        vector_move_list.append(vector_object_will_move)
                        
                        # De-select after move
                        v.select_set(False)
                    else:
                        v.select_set(False)
                        string_converted = "".join(str(v)+";" for v in vector_object_will_move)[:-1]
                        vertex_ob_mode = revert_coor_dict[string_converted]
                        vector_move = vector_vertex - vector_object_will_move
                        
                        vertex_ob_move_dict[vertex_ob_mode] = vector_move
                        vector_move_list.append(vector_vertex)

            if is_reverted:
                # Get the bmesh data of SOURCE mesh
                mesh_ob = mesh_object_mode.data
                bm_source = bmesh.from_edit_mesh(mesh_ob)
                for v in bm_source.verts:
                    index = str(v.index)
                    if index in vertex_ob_move_dict:
                        vector_move = vertex_ob_move_dict[index]

                        v.select_set(True)
                        # Move vertex
                        bpy.ops.transform.translate(value=vector_move)
                        
                        # De-select after move
                        v.select_set(False)

    # revert selected 
    for mesh_edit_mode in meshes_in_edit_mode:
        K_Utilities.convert_mesh_to_mode_input(mesh_edit_mode, "OBJECT")
    
    # Merge snapped vertices
    if(is_merge):
        bpy.ops.object.join()
        joined_mesh = bpy.context.active_object
        K_Utilities.convert_mesh_to_mode_input(joined_mesh, "EDIT")
        all_vertices_coor = K_Utilities.get_all_vertices_coordinate(joined_mesh, "None")

        vector_vertices_process = [v_coor for k, v_coor in all_vertices_coor.items() if v_coor in vector_move_list]

        mesh_joined_data = joined_mesh.data
        bm_mesh_joined = bmesh.from_edit_mesh(mesh_joined_data)
        mesh_joined_matrix = joined_mesh.matrix_world

        for vector in bm_mesh_joined.verts:
            vector_vertex = mesh_joined_matrix @ vector.co # Get the global
            if vector_vertex in vector_vertices_process:
                vector.select_set(True)

        #Merge
        bpy.ops.mesh.remove_doubles()

        K_Utilities.convert_mesh_to_mode_input(joined_mesh, "OBJECT")
    

def copy_vertex():
    objects_selected = K_Utilities.get_all_selected_meshes_in_scene() #Get all selected meshes in scene 
    meshes_in_edit_mode = objects_selected[1]

    if(meshes_in_edit_mode == [] or len(meshes_in_edit_mode) > 1):
        # ---- TODO --- #
        return 0
    
    # Get all vertices selected of TARGET mesh
    mesh_edit_mode = meshes_in_edit_mode[0]
    
    # Process for copy vertex
    # Get the bmesh data of TARGET mesh
    mesh_edit = mesh_edit_mode.data
    bm = bmesh.from_edit_mesh(mesh_edit)
    ob_mat = mesh_edit_mode.matrix_world

    selected_vertices = [v for v in bm.verts if v.select]

    if(len(selected_vertices) > 1):
        # --- TODO --- #
        return 0

    for v in selected_vertices:
        vector_vertex = ob_mat @ v.co # Get the global
        K_Variables.vertex_copied = vector_vertex


def copy_average_vertices():
    objects_selected = K_Utilities.get_all_selected_meshes_in_scene() #Get all selected meshes in scene 
    meshes_in_edit_mode = objects_selected[1]

    if(meshes_in_edit_mode == [] or len(meshes_in_edit_mode) > 1):
        # --- TODO --- #
        return 0
    
    mesh_edit_mode = meshes_in_edit_mode[0]

    # Process for copy vertex
    # Get the bmesh data of mesh
    mesh_edit = mesh_edit_mode.data
    bm = bmesh.from_edit_mesh(mesh_edit)
    ob_mat = mesh_edit_mode.matrix_world

    # Get all vertices selected
    selected_vertices = [v for v in bm.verts if v.select]

    if(len(selected_vertices) < 2):
        # --- TODO --- #
        return 0

    vector_array = []

    for v in selected_vertices:
        vetex_vector = ob_mat @ v.co
        vector_array.append(vetex_vector)

    # Calculate the middle vector
    sum_vector = Vector((0.0, 0.0, 0.0))

    for vector in vector_array:
        sum_vector += vector

    average_vector = sum_vector/len(vector_array)
    K_Variables.vertex_copied = average_vector


def paste_vertex():
    objects_selected = K_Utilities.get_all_selected_meshes_in_scene() #Get all selected meshes in scene 
    meshes_in_edit_mode = objects_selected[1]

    if(meshes_in_edit_mode == [] or len(meshes_in_edit_mode) > 1):
        # --- TODO --- #
       return 0
    
    # Get all vertices selected
    mesh_edit_mode = meshes_in_edit_mode[0]

    # Process for paste vertex
    # Get the bmesh data of  mesh
    mesh_edit = mesh_edit_mode.data
    bm = bmesh.from_edit_mesh(mesh_edit)
    ob_mat = mesh_edit_mode.matrix_world

    for v in bm.verts:
        if(v.select):
            vector_vertex = ob_mat @ v.co
            vector_from_memory = K_Variables.vertex_copied

            if vector_from_memory:
                vector_move = vector_from_memory - vector_vertex

                # Move vertex
                v.select_set(True)
                bpy.ops.transform.translate(value=vector_move)

                # De-select after move
                v.select_set(False)


def merge_verticies(mode=''):
    if mode == 'CENTER':
        bpy.ops.mesh.merge(type='CENTER')

    elif mode == 'DISTANCE':
        bpy.ops.mesh.remove_doubles()


def subdivide_and_smooth_middle_vertices(is_smooth=True):
    all_selected = K_Utilities.get_all_selected_meshes_in_scene()
    selected_in_edit = all_selected[1][0]

    # Enter Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the BMesh of the object
    mesh = selected_in_edit.data
    bm = bmesh.from_edit_mesh(mesh)
    
    # Ensure BMesh layers are up-to-date
    bm.verts.ensure_lookup_table()
    bm.edges.ensure_lookup_table()

    try:
        mesh.calc_normals_split() # For lower blender version
    except:
        pass

    # Get Edges selected 
    edges_selected = [e for e in bm.edges if e.select]

    # Subdivide the edges (creates new vertices in the middle of the edges)
    return_values = bmesh.ops.subdivide_edges(bm, edges=edges_selected, cuts=1)

    # Deselect everything
    bpy.ops.mesh.select_all(action = 'DESELECT')

    # Select middle
    for v in return_values['geom_inner']:
        v.select = True

    # Update the mesh
    bmesh.update_edit_mesh(mesh)
    K_Switch_Selection_Utilities.to_vertex()

    # Update normal
    if is_smooth:
        # K_Normal_Utilities.paste_vertex_normal()

        # Get active edit mesh
        active_mesh_edit = bpy.context.edit_object

        mesh_data = active_mesh_edit.data

        bpy.ops.object.mode_set(mode = 'OBJECT')

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass
        
        # Prepare needed data
        try:
            mesh_data.use_auto_smooth = True
        except:
            pass
        
        new_bm = bmesh.new()
        new_bm.from_mesh(mesh_data)
        new_bm.verts.ensure_lookup_table()

        loop_edit = {}

        # Get selected vertex
        selected_vert = [v for v in new_bm.verts if v.select]   

        for v in selected_vert:
            list_verts = []
            v_index = v.index

            # Get verts from link edges
            link_edges = v.link_edges
            for e in link_edges:
                list_verts += [v for v in e.verts if v.index != v_index]
            
            # Calculate average normal
            average_normal = K_Normal_Utilities.get_average_normal_from_verts(list_verts, mesh_data)

            # Store loop need to update normal
            loop_update = {str(loop.index):average_normal for loop in v.link_loops 
                            if str(loop.index) not in loop_edit}
                
            loop_edit.update(loop_update)

        # Re-update normal 
        normals_vector = []

        for loop in mesh_data.loops:
            # loop_normal = matrix_world @ loop.normal
            loop_normal = loop.normal
            normal_append = (loop_normal.x, loop_normal.y, loop_normal.z)
            key = str(loop.index)
            
            if key in loop_edit:
                normal_append = loop_edit[key]
                normals_vector.append((normal_append.x, normal_append.y, normal_append.z))
            
            else:
                normals_vector.append(normal_append)

        mesh_data.normals_split_custom_set(normals_vector)
        bpy.ops.object.mode_set(mode="EDIT")

        # Cleanup
        try:
            mesh_data.free_normals_split() # For lower blender version
        except:
            pass

        new_bm.free()
        bmesh.update_edit_mesh(mesh_data)


