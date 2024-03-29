DEVICEDEBUGCAMERA   = 'rtsp://admin:cctv1234@192.168.1.101:554/h264Preview_01_main'
DEVICESTGCAMERA     = 'rtsp://admin:cctv1234@192.168.1.101:554/h264Preview_01_main'
TIME                = 1
IMG_PATH            = './image/'
TIMESLEEPTHREAD     = 0.1

YOLO_SCALE          = 0.00392
YOLO_IMGSIZE        = (416,416)
YOLO_CONFI          = 0.45
YOLO_WEIGHT         = './model/yolo-obj_last.weights'
YOLO_CFG            = './model/yolo-obj.cfg'

FULL_RESOURCE       = 100
FULL_RESOURCE_DISK  = 54.7
CONST_CPU           = 60.77      #Batas usage CPU jika lebih do something
CONST_RAM           = 40.42      #Batas usage RAM jika lebih do something
CONST_DISK          = 54.5      #Batas usage Disk jika lebih do something

MAX_RELAY_LIST      = 5
RELAIS_1_GPIO       = 17