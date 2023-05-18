# detecting the OS
import sys

# standard ros2 functionality
import rclpy

# importing our new message type
from hexapod_controller_interfaces.msg import BodyIKCalculate

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


msg = """
This node takes keypresses from the keyboard and publishes them
as BodyIKCalculate messages.
Below is the list of keys used to change the values:
---------------------------
Translation:
    Q   W   E
    A   S   D

Rotation:
    U   I
    J   K
    M   ,

---------------------------
W / S : X translation
A / D : Y translation
Q / E : Z translation

U / I : X rotation
J / K : Y rotation
M / , : Z rotation

---------------------------

anything else : back to initial position

CTRL-C to quit
"""

moveBindings = {
    'w': (1, 0, 0),
    's': (-1, 0, 0),
    'd': (0, 1, 0),
    'a': (0, -1, 0),
    'q': (0, 0, 1),
    'e': (0, 0, -1),
}

rotationBindings = {
    'u': (1, 0, 0),
    'i': (-1, 0, 0),
    'j': (0, 1, 0),
    'k': (0, -1, 0),
    'm': (0, 0, 1),
    ',': (0, 0, -1),
}

# TODO !!!
limits = {
    # X axis translation limits
    'transXMin': 0,
    'transXMax': 0,
    # Y axis translation limits
    'transYMin': 0,
    'transYMax': 0,
    # Z axis translation limits
    'transZMin': 0,
    'transZMax': 0,

    # X axis rotation limits
    'rotXMin': 0,
    'rotXMax': 0,
    # Y axis rotation limits
    'rotYMin': 0,
    'rotYMax': 0,
    # Z axis rotation limits
    'rotZMin': 0,
    'rotZMax': 0,
}

def getKey(settings):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)


def restoreTerminalSettings(old_settings):
    if sys.platform == 'win32':
        return
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def positionToCalculate(transX, transY, transZ, rotX, rotY, rotZ):
    return 'currently:\n\ttransX: %s\n\ttransY: %s\n\ttransZ %s\n\trotX: %s\n\trotY: %s\n\trotZ: %s' % (transX, transY, transZ, rotX, rotY, rotZ)

def positionSubscriber(msg: BodyIKCalculate):
    # transX, transY, transZ, rotX, rotY, rotZ = msg
    transX = msg.position_of_the_body[0]
    transY = msg.position_of_the_body[1]
    transZ = msg.position_of_the_body[2]
    rotX = msg.position_of_the_body[3]
    rotY = msg.position_of_the_body[4]
    rotZ = msg.position_of_the_body[5]
    print(f'currently:\n\ttransX: {transX}\n\ttransY: {transY}\n\ttransZ {transZ}\n\trotX: {rotX}\n\trotY: {rotY}\n\trotZ: {rotZ}')
    # return f'currently:\n\ttransX: {transX}\n\ttransY: {transY}\n\ttransZ {transZ}\n\trotX: {rotX}\n\trotY: {rotY}\n\trotZ: {rotZ}'

def main():
    settings = saveTerminalSettings()

    rclpy.init()

    node = rclpy.create_node('teleop_keyboard_test')
    pub_ = node.create_publisher(BodyIKCalculate, "body_IK_calculations", 10)
    sub_ = node.create_subscription(BodyIKCalculate, "body_IK_calculations", positionSubscriber, 10)

    transX = 0
    transY = 0
    transZ = 0
    rotX = 0
    rotY = 0
    rotZ = 0
    status = 0

    try:
        print(msg)
        # print(positionToCalculate(transX, transY, transZ, rotX, rotY, rotZ))
        print("\n---------------------------\n")
        while True:
            key = getKey(settings)
            # print(positionToCalculate(transX, transY, transZ, rotX, rotY, rotZ))
            if (status == 14):
                print(msg)
            status = (status + 1)
            if key in moveBindings.keys():
                transX = transX + moveBindings[key][0]
                transY = transY + moveBindings[key][1]
                transZ = transZ + moveBindings[key][2]
            elif key in rotationBindings.keys():
                rotX = rotX + moveBindings[key][0]
                rotY = rotY + moveBindings[key][1]
                rotZ = rotZ + moveBindings[key][2]              
            else:
                transX = 0
                transY = 0
                transZ = 0
                rotX = 0
                rotY = 0
                rotZ = 0
                if (key == '\x03'):
                    break

            cmd = BodyIKCalculate()
            cmd.position_of_the_body[0] = transX
            cmd.position_of_the_body[1] = transY
            cmd.position_of_the_body[2] = transZ
            cmd.position_of_the_body[3] = rotX
            cmd.position_of_the_body[4] = rotY
            cmd.position_of_the_body[5] = rotZ
            pub_.publish(cmd)

    except Exception as e:
        print(e)

    finally:
        cmd = BodyIKCalculate()
        cmd.position_of_the_body[0] = 0
        cmd.position_of_the_body[1] = 0
        cmd.position_of_the_body[2] = 0
        cmd.position_of_the_body[3] = 0
        cmd.position_of_the_body[4] = 0
        cmd.position_of_the_body[5] = 0
        pub_.publish(cmd)

        restoreTerminalSettings(settings)


if __name__ == '__main__':
    main()