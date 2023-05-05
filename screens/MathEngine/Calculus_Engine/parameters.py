from .ui import *

Width = 1920
Height = 1080

# UI paraeter
panel = Panel(position = (Width-515, 15), w= 500, h= 150, color=(55, 55, 155), alpha=50)


# Text UI
functionText = TextUI("fx :", (panel.position[0] + 15, panel.position[1] + 15), (255, 255, 255), "topleft")
derivativeText = TextUI("dfx :", (panel.position[0] + 15, panel.position[1] + 35), (255, 255, 255), "topleft")
tangentAt = TextUI("tangent at :", (panel.position[0] + 15, panel.position[1] + 55), (255, 255, 255), "topleft")