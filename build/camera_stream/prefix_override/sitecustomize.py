import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jonathan0209/casper_robot/rob_ws/install/camera_stream'
