# ---------------------------------------------------------------- # 
# Hi there! I hope you’re enjoying this tool.
# If you have any concerns or feedback about the tool,
# Please feel free to contact me via email.
#
# vanthekhoi@gmail.com 
#
# Thank you :))
# ---------------------------------------------------------------- #

''' This script store all Global Propertise variables

'''

try:
    from imp import reload
except:
    pass

import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )

from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )

# Store properties in the active scene
class KWT_Propertise_Setup(PropertyGroup):
    # --- Transform tools props --- #
    bpy.types.Scene.transform_bool = BoolProperty(
                                    name="Transform",
                                    description="Apply transform",
                                    default = False
                                    )
    
    bpy.types.Scene.rotate_bool = BoolProperty(
                                    name="Rotate",
                                    description="Apply rotate",
                                    default = False
                                    )
    
    bpy.types.Scene.scale_bool = BoolProperty(
                                name="Scale",
                                description="Apply scale",
                                default = False
                                )
    