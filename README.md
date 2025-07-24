In Blender vertex paint, the color picker is in sRGB space, which will lead to vertex color value not being the same when exported. This is because when exported, the color is converted to RGB.
Most game engine will read vertex color in RGB space, so we need to be precise with our values.
This addon simply add a tab which let us convert the color we want in RGB to the color picker sRGB space
