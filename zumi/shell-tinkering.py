#!/usr/bin/python3.5
from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.personailty import Personailty

LTHRESH=170
RTHRESH=150
FOREVER=100000.0

zumi = Zumi()
screen=Screen()

# screen.draw_text_center("test test test")
# screen.draw_text_center("[{}] [{}]".format(zumi.get_IR_data(0), zumi.get_IR_data(5)))
# screen.draw_text_center(int(zumi.read_z_angle()))

out = True # "out" and "back"
# turn = 1 # -1 -> turn right; +1 -> turn left

zumi.reset_gyro()
heading = int(zumi.read_z_angle()) # should be zero immediately after gyro reseto

# zumi.turn_left() if out else zumi.turn_right()

heading = 0

while True:
    zumi.forward_avoid_collision(40, FOREVER, None, LTHRESH, RTHRESH)
    zumi.turn_left() if out else zumi.turn_right()
    zumi.forward_avoid_collision(40, FOREVER, None, LTHRESH, RTHRESH)
    heading = int(zumi.read_z_angle())
    if heading in range(-120, -59): # turn around(, bright eyes) - outbound
        heading += 180
        zumi.turn(heading)
        out = not out
    elif heading in range(30, 61): # turn around(, bright eyes) - outbound
        heading += 180
        zumi.turn(heading)
        zumi.reset_gyro()
        out = not out
    else:
        break

zumi.angry()
screen.draw_text_center(
"""
help me!
i'm lost!
""")

