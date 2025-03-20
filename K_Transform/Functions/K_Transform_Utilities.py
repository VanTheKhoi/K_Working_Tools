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

def apply_transform(is_location=False, is_rotation=False, is_scale=False):
    bpy.ops.object.transform_apply(
                                location=is_location, 
                                rotation=is_rotation, 
                                scale=is_scale
                                )
    
def transform_to_deltas(is_location=False, is_rotation=False, is_scale=False):
    checkBox_checked = {
            "Location":is_location, 
            "Rotate":is_rotation, 
            "Scale":is_scale
            }

    # Define which mode should run
    deltas_mode = {}

    if checkBox_checked["Location"]:
        deltas_mode["LOC"] = "RUN"

    if checkBox_checked["Rotate"]:
        deltas_mode["ROT"] = "RUN"

    if checkBox_checked["Scale"]:
        deltas_mode["SCALE"] = "RUN"

    for mode_name, v in deltas_mode.items():
        bpy.ops.object.transforms_to_deltas(mode=mode_name)