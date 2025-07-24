## Context
In Blender vertex paint, the color picker is in sRGB space, which will lead to vertex color value not being the same when exported. This is because when exported, the color is converted to RGB.
Most game engine will read vertex color in RGB space, so we need to be precise with our values.
This addon simply add a tab which let us convert the color we want in RGB to the color picker sRGB space.

## Formula

linear RGB --> sRGB
If RGB ≤ 0.0031308:
    sRGB = 12.92 * RGB
Else:
    sRGB = 1.055 * (RGB)^(1/2.4) - 0.055

sRGB --> linear RGB
If sRGB ≤ 0.04045:
    RGB = sRGB / 12.92
Else:
    RGB = ((sRGB + 0.055) / 1.055) ^ 2.4
