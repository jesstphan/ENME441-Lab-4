import cgi
import RPi.GPIO as GPIO

import cgitb
cgitb.enable()

ledPin1 = 19
ledPin2 = 20
ledPin3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

data = cgi.FieldStorage()
s1 = data.getvalue('slider1')

if ('LED Green' in data): 
  GPIO.output(ledPin1, 1)
elif ( 'LED Blue' in data):
  GPIO.output(ledPin2, 1)
elif ( 'LED White' in data):
  GPIO.output(ledPin3, 1)

with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))


print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>LED Control</title>')

print('<form action="/cgi-bin/LED_Control.py" method="POST">')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print(‘Brightness = %s' % s1)
print('</html>')

