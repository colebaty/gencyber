from zumi.zumi import Zumi
from zumi.util.screen import Screen
# from zumi.personailty import Personailty

LTHRESH=170
RTHRESH=150
FOREVER=100000.0

zumi = Zumi()
screen=Screen()

# screen.draw_text_center("test test test")
# screen.draw_text_center("[{}] [{}]".format(zumi.get_IR_data(0), zumi.get_IR_data(5)))
# screen.draw_text_center(int(zumi.read_z_angle()))

out = True # "out" and "back"

zumi.reset_gyro()
heading = int(zumi.read_z_angle()) # should be zero immediately after gyro reset
counter = 0

while True:
    zumi.forward_avoid_collision(40, FOREVER, None, LTHRESH, RTHRESH)
    
    zumi.turn_right() if out else zumi.turn_left()

    zumi.forward_avoid_collision(40, FOREVER, None, LTHRESH, RTHRESH)

    heading = int(zumi.read_z_angle()) - (counter * 360)
    print("counter: {} | heading: {}".format(counter, heading))
    counter += 1
    if heading in range(-120, -59): # turn around(, bright eyes) - outbound
        heading += 180 # TODO - does this need to be -= ?
        zumi.turn(heading)
        print("counter: {} | heading: {}".format(counter, heading))
        out = not out
    elif heading in range(-210, -149): # turn around(, bright eyes) - inbound
        heading = 0
        zumi.turn(heading)
        print("counter: {} | heading: {}".format(counter, heading))
        zumi.reset_drive()
        out = not out
    else:
        break

screen.draw_text_center("lost: {}".format(heading))

# zumi.angry()
# screen.draw_text_center(
# """
# help me!
# i'm lost!
# """)
