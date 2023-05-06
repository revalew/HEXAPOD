import dynamixel_sdk as dxl

# Initialize the Dynamixel SDK and set up a connection to the motor
port = "/dev/ttyUSB0"  # Replace with the port connected to the motor
#baudrate = 57600  # Replace with the baudrate used by the motor
baudrate = 1000000  # Replace with the baudrate used by the motor
protocol_version = 1.0  # Use 1.0 for Dynamixel AX-12A and MX-28 motors
motor_id = 15  # Replace with the ID of your motor

# Initialize a PacketHandler instance and connect to the serial port
packet_handler = dxl.PacketHandler(protocol_version)
port_handler = dxl.PortHandler(port)
port_handler.openPort()
port_handler.setBaudRate(baudrate)

# Read the CW Angle Limit and CCW Angle Limit registers of the motor
cw_angle_limit_addr = 6  # Address of the CW Angle Limit register
ccw_angle_limit_addr = 8  # Address of the CCW Angle Limit register
cw_angle_limit, cw_error = packet_handler.read2ByteTxRx(port_handler, motor_id, cw_angle_limit_addr)
ccw_angle_limit, ccw_error = packet_handler.read2ByteTxRx(port_handler, motor_id, ccw_angle_limit_addr)

# Print the angle limits
print("CW Angle Limit: {0}, CCW Angle Limit: {1}".format(cw_angle_limit, ccw_angle_limit))

