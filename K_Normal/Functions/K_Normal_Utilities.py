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
import bmesh
import math
import mathutils

# Import 
import K_Working_Tools.K_Normal.Functions.K_Normal_Variables as K_Normal_Variables # type: ignore
import K_Working_Tools.K_Global.K_Utilities as K_Utilities # type: ignore

# Reload
reload(K_Normal_Variables)
reload(K_Utilities)

def reset_vector():
    bpy.ops.mesh.normals_tools(mode='RESET')


def get_average_normal_from_verts(verts_input, mesh_data):
    normals_vector = []
    average_normal_vector = [0,0,0]

    for vert in verts_input:
        # normals_vector += [matrix @ mesh_data.loops[vertex_face_loop.index].normal for vertex_face_loop in vert.link_loops]
        normals_vector += [mesh_data.loops[vertex_face_loop.index].normal for vertex_face_loop in vert.link_loops]

    # Calculate average
    array_lenght = len(normals_vector)

    for vector in normals_vector:
        average_normal_vector[0] += vector.x
        average_normal_vector[1] += vector.y
        average_normal_vector[2] += vector.z

    average_normal_vector[0] = average_normal_vector[0]/ array_lenght
    average_normal_vector[1] = average_normal_vector[1]/ array_lenght
    average_normal_vector[2] = average_normal_vector[2]/ array_lenght

    return mathutils.Vector((average_normal_vector[0], average_normal_vector[1], average_normal_vector[2])).normalized()


def copy_vertex_normal():
    # Cleanup cache
    K_Normal_Variables.copied_vector = None

    process_continue = True

    # Get active edit mesh
    active_mesh_edit = bpy.context.edit_object

    try:
        active_mesh_edit.update_from_editmode() 
    except:
        process_continue = False

    if process_continue:
        # matrix = active_mesh_edit.matrix_world
        mesh_data = active_mesh_edit.data

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass

        # Get bmMesh data
        bm = bmesh.from_edit_mesh(mesh_data)

        # Get selected vertex
        selected_vert = [v for v in bm.verts if v.select]   

        # Get selected face 
        selected_face = [f for f in bm.faces if f.select]

        # Copy face normal
        if selected_face:
            selected_face = selected_face[0]
            # normals_vector = matrix @ selected_face.normal
            normals_vector = selected_face.normal
            K_Normal_Variables.copied_vector = mathutils.Vector((normals_vector[0], normals_vector[1], normals_vector[2]))

        # Copy vertex normal
        elif selected_vert:
            if len(selected_vert) == 1:
                selected_vert = selected_vert[0]

                # normals_vector = [matrix @ mesh_data.loops[vertex_face_loop.index].normal for vertex_face_loop in selected_vert.link_loops]
                normals_vector = [mesh_data.loops[vertex_face_loop.index].normal for vertex_face_loop in selected_vert.link_loops]
                
                normals_vector = normals_vector[0]
                K_Normal_Variables.copied_vector = mathutils.Vector((normals_vector[0], normals_vector[1], normals_vector[2]))

            # Get average vector
            elif len(selected_vert) > 1:
                K_Normal_Variables.copied_vector = get_average_normal_from_verts(selected_vert, mesh_data)


def copy_faces_normal():
    # Cleanup cache 
    K_Normal_Variables.copied_faces_normal = {}

    process_continue = True

    # Get active edit mesh
    active_mesh_edit = bpy.context.edit_object

    try:
        active_mesh_edit.update_from_editmode()
    except:
        process_continue = False

    if process_continue:
        # matrix = active_mesh_edit.matrix_world
        mesh_data = active_mesh_edit.data

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass

        # Get bmMesh data
        bm = bmesh.from_edit_mesh(mesh_data)

        # Get face selected 
        selected_face = [f for f in bm.faces if f.select]

        if selected_face:
            # K_Normal_Variables.copied_faces_normal = {str(face.index):matrix @ face.normal for face in selected_face}
            K_Normal_Variables.copied_faces_normal = {str(face.index):face.normal for face in selected_face}
            

def paste_vertex_normal():
    vector_process = K_Normal_Variables.copied_vector
    process_continue = True
    
    # Get active edit mesh
    active_mesh_edit = bpy.context.edit_object

    try:
        active_mesh_edit.update_from_editmode()
    except:
        process_continue = False

    if process_continue:
        # matrix_world = active_mesh_edit.matrix_world
        mesh_data = active_mesh_edit.data

        bpy.ops.object.mode_set(mode = 'OBJECT') # normals_split_custom_set work on object mode

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass
        
        # Prepare needed data
        try:
            mesh_data.use_auto_smooth = True
        except:
            pass
        
        bm = bmesh.new()
        bm.from_mesh(mesh_data)
        bm.verts.ensure_lookup_table()

        loop_edit = {}
        # vector_process = matrix_world @ vector_process

        # Store loop need to update normal
        for v in bm.verts:
            if v.select:
                loop_update = {str(loop.index):vector_process for loop in v.link_loops 
                            if str(loop.index) not in loop_edit}
                
                loop_edit.update(loop_update)

        # Re-update normal 
        debug_loops = {}
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

            debug_loops[key] = normal_append # For debug

        mesh_data.normals_split_custom_set(normals_vector)
        bpy.ops.object.mode_set(mode="EDIT")

        # Cleanup
        try:
            mesh_data.free_normals_split() # For lower blender version
        except:
            pass

        bm.free()
        bmesh.update_edit_mesh(mesh_data)


def paste_vertex_face_normal():
    vertex_face_vector_process = K_Normal_Variables.copied_faces_normal
    process_continue = True
    # Get active edit mesh
    active_mesh_edit = bpy.context.edit_object

    try:
        active_mesh_edit.update_from_editmode()
    except:
        process_continue = False

    if process_continue:
        # matrix_world = active_mesh_edit.matrix_world
        mesh_data = active_mesh_edit.data

        bpy.ops.object.mode_set(mode = 'OBJECT') # normals_split_custom_set work on object mode

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass
        
        # Prepare needed data
        try:
            mesh_data.use_auto_smooth = True
        except:
            pass
        
        bm = bmesh.new()
        bm.from_mesh(mesh_data)
        bm.verts.ensure_lookup_table()

        loop_edit = {}
        face_selected = [f for f in bm.faces if f.select]

        # Store loop need to update normal
        for face in face_selected:
            face_loops_index = [f.index for f in face.loops]

            for vert in face.verts:
                vert_loops = vert.link_loops
                faces_connected = vert.link_faces
                
                # Get vector 
                vector_process = None
                for f in faces_connected:
                    if str(f.index) in vertex_face_vector_process:
                        vector_process = vertex_face_vector_process[str(f.index)]
                        break
                
                if vector_process:
                    for loop in vert_loops:
                        if loop.index in face_loops_index:
                            if str(loop.index) not in loop_edit:
                                loop_edit[str(loop.index)] = vector_process
        
        # Re-update normal 
        debug_loops = {}
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

            debug_loops[key] = normal_append # For debug

        mesh_data.normals_split_custom_set(normals_vector)
        bpy.ops.object.mode_set(mode="EDIT")

        # Cleanup
        try:
            mesh_data.free_normals_split() # For lower blender version
        except:
            pass

        bm.free()
        bmesh.update_edit_mesh(mesh_data)


def toggle_vertex_normal():
    if bpy.context.space_data.overlay.show_split_normals:
        bpy.context.space_data.overlay.show_split_normals = False
    else:
        bpy.context.space_data.overlay.show_split_normals = True


def weighted_normal(mode="ANGLE"):
    process_continue = True
    # Get active edit mesh
    active_mesh_edit = bpy.context.edit_object

    try:
        active_mesh_edit.update_from_editmode()
    except:
        process_continue = False

    if process_continue:
        # matrix_world = active_mesh_edit.matrix_world
        mesh_data = active_mesh_edit.data

        bpy.ops.object.mode_set(mode = 'OBJECT') # normals_split_custom_set work on object mode

        try:
            mesh_data.calc_normals_split() # For lower blender version
        except:
            pass
        
        # Prepare needed data
        try:
            mesh_data.use_auto_smooth = True
        except:
            pass
        
        bm = bmesh.new()
        bm.from_mesh(mesh_data)
        bm.verts.ensure_lookup_table()

        loop_edit = {}
        verts_selected = []
        face_selected = [f for f in bm.faces if f.select]

        if face_selected:
            for f in face_selected:
                verts_selected += [v for v in f.verts]

        else:
            verts_selected = [v for v in bm.verts if v.select]

        if verts_selected:
            for vert in verts_selected:
                loops_link = vert.link_loops
                normal_update = mathutils.Vector()
                
                # Calculate weighted normal
                if mode == "ANGLE":
                    for loop in loops_link:
                        normal_update += loop.calc_angle() * loop.face.normal

                elif mode == "AREA":
                    for loop in loops_link:
                        area = 0.5 * loop.face.calc_area()
                        normal_update += area * loop.face.normal

                normal_update.normalize()

                for loop in loops_link:
                    key = str(loop.index)
                    # loop_edit[key] = matrix_world @ normal_update
                    loop_edit[key] = normal_update

            # Re-update normal 
            debug_loops = {}
            normals_vector = []

            # Update vertex normal
            # for v in mesh_data.vertices:
            #     vert_normal = matrix_world @ v.normal
            #     normal_append = (vert_normal.x, vert_normal.y, vert_normal.z)
            #     key = str(v.index)
                
            #     if key in loop_edit:
            #         normal_append = loop_edit[key]
            #         normals_vector.append((normal_append.x, normal_append.y, normal_append.z))
                
            #     else:
            #         normals_vector.append(normal_append)

            #     debug_loops[key] = normal_append # For debug

            # mesh_data.normals_split_custom_set_from_vertices(normals_vector)

            # Update vertex face normal

            # Re-update normal 
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

                debug_loops[key] = normal_append # For debug

            mesh_data.normals_split_custom_set(normals_vector)
            bpy.ops.object.mode_set(mode="EDIT")

            # Cleanup
            try:
                mesh_data.free_normals_split() # For lower blender version
            except:
                pass

            bm.free()
            bmesh.update_edit_mesh(mesh_data)


def normal_from_face():
    bpy.ops.mesh.set_normals_from_faces()
