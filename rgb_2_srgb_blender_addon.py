bl_info = {
    "name": "RGB to sRGB conversion",
    "author": "FuWan",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Properties > Tool > Vertex Paint",
    "description": "Linear RGB color picker for vertex paint",
    "category": "Paint",
}

import bpy
from bpy.types import Operator

class MESH_OT_rgb_vertex_color_picker(Operator):
    """RGB 2 sRGB for Vertex Paint"""
    bl_idname = "mesh.rgb_2_srgb"
    bl_label = "Linear RGB Color Picker"
    bl_options = {'REGISTER', 'UNDO'}
    
    red: bpy.props.FloatProperty(
        name="Red",
        default=1.0,
        min=0.0,
        max=1.0,
        description="Red component (Linear RGB)"
    )
    
    green: bpy.props.FloatProperty(
        name="Green", 
        default=1.0,
        min=0.0,
        max=1.0,
        description="Green component (Linear RGB)"
    )
    
    blue: bpy.props.FloatProperty(
        name="Blue",
        default=1.0,
        min=0.0,
        max=1.0,
        description="Blue component (Linear RGB)"
    )
    
    def execute(self, context):
        if context.tool_settings.vertex_paint:
            brush = context.tool_settings.vertex_paint.brush
            if brush:
                brush.color = (self.red, self.green, self.blue)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        if context.tool_settings.vertex_paint:
            brush = context.tool_settings.vertex_paint.brush
            if brush:
                self.red = brush.color[0]
                self.green = brush.color[1] 
                self.blue = brush.color[2]
        
        return context.window_manager.invoke_props_dialog(self, width=350)
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Linear RGB Values:", icon='COLOR')
        layout.separator()
        
        col = layout.column(align=True)
        
        # Convert to sRGB for display
        srgb_rgb = linear_to_srgb((self.red, self.green, self.blue))
        
        # RGB sliders with sRGB values
        row = col.row(align=True)
        row.prop(self, "red", slider=True)
        row.label(text=f"sRGB: {srgb_rgb[0]:.3f}")
        
        row = col.row(align=True)
        row.prop(self, "green", slider=True)
        row.label(text=f"sRGB: {srgb_rgb[1]:.3f}")
        
        row = col.row(align=True)
        row.prop(self, "blue", slider=True)
        row.label(text=f"sRGB: {srgb_rgb[2]:.3f}")

def linear_to_srgb(color):
    """Convert linear RGB to sRGB"""
    def convert_component(c):
        if c <= 0.0031308:
            return 12.92 * c
        else:
            return 1.055 * pow(c, 1.0 / 2.4) - 0.055
    
    return [convert_component(c) for c in color[:3]]

class VIEW3D_PT_rgb_vertex_paint_panel(bpy.types.Panel):
    """RGB 2 sRGB Panel"""
    bl_label = "RGB to sRGB conversion"
    bl_idname = "VIEW3D_PT_rgb_2_sRGB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_context = "vertexpaint"
    
    @classmethod
    def poll(cls, context):
        return (context.mode == 'PAINT_VERTEX' and 
                context.tool_settings.vertex_paint)
    
    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.rgb_2_srgb", 
                       text="RGB to sRGB conversion", icon='COLOR')

def register():
    bpy.utils.register_class(MESH_OT_rgb_vertex_color_picker)
    bpy.utils.register_class(VIEW3D_PT_rgb_vertex_paint_panel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_rgb_vertex_paint_panel)
    bpy.utils.unregister_class(MESH_OT_rgb_vertex_color_picker)

if __name__ == "__main__":
    register()