#!/usr/bin/python
from sense_hat import SenseHat
import time

# Initialise Temperature and Humidity Sensors
sense = SenseHat()
sense.low_light = True
temp = sense.get_temperature()
humidity = sense.get_humidity()

# Colour Variables
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
cyan = (135, 206, 250) 
red = (255, 0, 0)
orange = (255, 165, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

# Define Pixel Colours
def low_humidity():
  W = white
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, O, W, O, O, W, O, O,
  O, O, W, O, O, W, O, O,
  O, O, W, O, O, W, O, O,
  O, O, O, O, O, O, O, O,
  O, W, O, O, O, O, W, O,
  O, O, W, W, W, W, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
  
def high_humidity():
  W = white
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, O, W, O, O, W, O, O,
  O, O, W, O, O, W, O, O,
  O, O, W, O, O, W, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, W, W, W, W, O, O,
  O, W, O, O, O, O, W, O,
  ]
  return logo
  
 
def hot_temp():
  W = white
  R = red
  V = orange
  Y = yellow
  O = nothing
  logo = [
  Y, O, O, O, O, O, O, Y,
  O, Y, V, V, V, V, Y, O,
  O, V, Y, Y, Y, Y, V, O,
  O, V, Y, Y, Y, Y, V, O,
  O, V, Y, Y, Y, Y, V, O,
  O, V, Y, Y, Y, Y, V, O,
  O, Y, V, V, V, V, Y, O,
  Y, O, O, O, O, O, O, Y,
  ]
  return logo
  
def cold_temp():
  C = cyan
  B = blue
  W = white
  O = nothing
  logo = [
  C, C, C, O, O, C, C, C,
  C, C, O, O, O, O, C, C,
  C, O, C, O, O, C, O, C,
  O, O, O, C, C, O, O, O,
  O, O, O, C, C, O, O, O,
  C, O, C, O, O, C, O, C,
  C, C, O, O, O, O, C, C,
  C, C, C, O, O, C, C, C,
  ]
  return logo
  
try:
	# Print onto Console
	print("Temp: %s C" % temp)
	print("Humidity: %s %%rH" % humidity)

	# Set LED matrix to scroll from right to left
	sense.set_rotation(180)        

	# If temp low
	if (sense.get_temperature() < 18) :
		images = [cold_temp]
		count = 0

		while True:
			sense.set_pixels(images[count % len(images)]())
			time.sleep(.75)
			count += 1
			# Wait 1 second
			time.sleep(1)


	# If temp high
	if (sense.get_temperature() > 18) :
		images = [hot_temp]
		count = 0

		while True:
			sense.set_pixels(images[count % len(images)]())
			time.sleep(.75)
			count += 1
			# Wait 1 second
			time.sleep(1
			
	# If humidity high
	if (sense.get_humidity() > 50) :
		images = [high_humidity]
		count = 0

		while True:
			sense.set_pixels(images[count % len(images)]())
			time.sleep(.75)
			count += 1
			# Wait 1 second
			time.sleep(1)
			
	# If humidity low
	if (sense.get_humidity() < 50) :
		images = [low_humidity]
		count = 0

		while True:
			sense.set_pixels(images[count % len(images)]())
			time.sleep(.75)
			count += 1
			# Wait 1 second
			time.sleep(1)

except KeyboardInterrupt:
# Clear LED matrix 
	sense.clear()      
