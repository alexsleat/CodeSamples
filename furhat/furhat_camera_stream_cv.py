import zmq
import numpy as np
import cv2

# Address:
addr="192.168.0.110"
url = 'tcp://{}:3000'.format(addr)
            
# Setup the sockets
context = zmq.Context()

# Input camera feed from furhat using a SUB socket
insocket = context.socket(zmq.SUB)
insocket.setsockopt_string(zmq.SUBSCRIBE, '')
insocket.connect(url)
insocket.setsockopt(zmq.RCVHWM, 1)
insocket.setsockopt(zmq.CONFLATE, 1)  # Only read the last message to avoid lagging behind the stream.

# Create frame var
img = None

# Loop the stream data
while True:
    
	string = insocket.recv()
	filetypeval = string[0:3]

	# check if we have a JPEG image (starts with ffd8ff
	if filetypeval == b'\xff\xd8\xff':
		#print("jpg rcv")
		
		# Grab the frame from buffer
		buf = np.frombuffer(string,dtype=np.uint8)
		# cv frame as "img"
		img = cv2.imdecode(buf,flags=1)

	
		# Display frame
		cv2.imshow('Furhat Stream',img)
		k = cv2.waitKey(1)
		

		# When pressing esc the program stops.
		if k%256 == 27: 
			# ESC pressed
			print("Escape hit, closing...")
			break

