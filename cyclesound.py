from pyfirmata import Arduino, util
import time
board = Arduino('/dev/tty.usbserial-A700eldr')
#board.digital[13].write(1)
it = util.Iterator(board)
it.start()
treshVal = 0.2
lastVal = 0
maxVal = 0
minVal = 0
maxTime = 0

def multiplier(treshVal):
  return (treshVal / (1 - treshVal)) + 1
while True:
	board.analog[2].enable_reporting()
	a = board.analog[2].read()
	try:
		if a > 1:
			continue

		if a >= treshVal:
			lastVal = (a - treshVal) * multiplier(treshVal)
				
			#print "lastVal", lastVal

			if lastVal > maxVal:
				maxVal = lastVal
				maxTime = time.time()
				print ">>>>>>max", maxVal
				
	
			if lastVal <= 0.1:
				if maxTime > 0:
					print time.time() - maxTime
				maxTime = 0				
#print "<<<<<min", minVal

	except TypeError:
		pass
