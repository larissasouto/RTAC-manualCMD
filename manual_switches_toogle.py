import gpiozero
import time

relay1 = gpiozero.OutputDevice(5)
relay2 = gpiozero.OutputDevice(6)
relay3 = gpiozero.OutputDevice(13)
relay4 = gpiozero.OutputDevice(16)
relay5 = gpiozero.OutputDevice(19)
relay6 = gpiozero.OutputDevice(20)
relay7 = gpiozero.OutputDevice(21)

def relayToogle():
  relay7.value = 1
  print("RELAY ON")
  time.sleep(5)
  relay7.value = 0
  print("RELAY OFF")
  time.sleep(5)


while True:
  relayToogle()