while True:
    light.set_pixel_color(0, light.rgb(255,165,0))
    pause(300)
    light.set_pixel_color(1, light.rgb(255,255,0))
    pause(300)
    light.set_pixel_color(2, light.rgb(0,255,0))
    pause(300)
    light.set_pixel_color(3, light.rgb(0,255,255))
    pause(300)
    light.set_pixel_color(4, light.rgb(0,165,255))
    pause(300)
    light.set_pixel_color(5, light.rgb(0,0,165))
    pause(300)
    light.set_pixel_color(6, light.rgb(0,0,255))
    pause(300)
    light.set_pixel_color(7, light.rgb(165,0,255))
    pause(300)
    light.set_pixel_color(8, light.rgb(255,0,255))
    pause(300)
    light.set_pixel_color(9, light.rgb(255,0,0))
    pause(300)
    light.clear()