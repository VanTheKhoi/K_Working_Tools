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

def geometry_display_mode(mode=""):
    if mode == 'WIREFRAME':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'WIREFRAME'
        bpy.context.space_data.overlay.show_face_orientation = False

    elif mode == 'SOLID':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.overlay.show_face_orientation = False

    elif mode == 'FACEORIENTATION':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'SOLID'
        bpy.context.space_data.overlay.show_face_orientation = True

    elif mode == 'MATERIAL':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'MATERIAL'
        bpy.context.space_data.overlay.show_face_orientation = False

    elif mode == 'RENDERED':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'RENDERED'
        bpy.context.space_data.overlay.show_face_orientation = False

    elif mode == 'NORMAL':
        bpy.context.space_data.shading.light = 'STUDIO'
        bpy.context.space_data.shading.type = 'SOLID'
        
        bpy.context.space_data.shading.light = 'MATCAP'
        bpy.context.space_data.shading.studio_light = 'check_normal+y.exr'
        bpy.context.space_data.overlay.show_face_orientation = False
