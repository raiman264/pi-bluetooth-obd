import obd
import time
# import boto3
import threading

import os

logFilePattern = "/home/pi/log/odb_%s.txt"
# logFilePattern = "obd_%s.txt"
logFileName = ""

i = 0
logFileName = logFilePattern % i
while os.path.exists(logFileName):
  i += 1
  logFileName = logFilePattern % i



# fh.write("========= file start =========")

def logData(str):
  fh = open(logFileName, "a")
  fh.write("{}\n".format(str))
  fh.close()

# OBD setup
obd.logger.setLevel(obd.logging.DEBUG)

# Connect to OBDII adapter
# ports = obd.scan_serial()
connection = obd.OBD("/dev/rfcomm0")

# Scheduler 
def repeat():
  threading.Timer(10.0, repeat).start()
  speedCmd = connection.query(obd.commands.SPEED)
  speedVal = speedCmd.value
  # speedVal = str(speedCmd.value)

  fuelCmd = connection.query(obd.commands.FUEL_LEVEL)
  fuelVal = fuelCmd.value
  # fuelVal = str(fuelCmd.value)

  fuelStatCmd = connection.query(obd.commands.FUEL_STATUS)
  fuelStatVal = fuelStatCmd.value
  # fuelStatVal = str(fuelStatCmd.value)

  fuelRateCmd = connection.query(obd.commands.FUEL_RATE)
  fuelRateVal = fuelRateCmd.value
  # fuelRateVal = str(fuelRateCmd.value)

  rpmCmd = connection.query(obd.commands.RPM)
  rpmVal = rpmCmd.value
  # rpmVal = str(rpmCmd.value)

  throttleCmd = connection.query(obd.commands.THROTTLE_POS)
  throttleVal = throttleCmd.value
  # throttleVal = str(throttleCmd.value)

  airTempCmd = connection.query(obd.commands.AMBIANT_AIR_TEMP)
  airTempVal = airTempCmd.value
  # airTempVal = str(airTempCmd.value)
  
  oilTempCmd = connection.query(obd.commands.OIL_TEMP)
  oilTempVal = oilTempCmd.value
  # oilTempVal = str(oilTempCmd.value)

  # row = "ts:" + time.time() + ", speed: " + speedVal + ", fuel: " + fuelVal + ", fuelStat: " + fuelStatVal + ", fuelRate: " + fuelRateVal + ", rpm: " + rpmVal + ", throttlePos: " + throttleVal + ", airTemp: " + airTempVal + ", oilTemp: " + oilTempVal
  row = "ts: {}, speed: {}, fuel: {}, fuelStat: {}, fuelRate: {}, rpm: {}, throttlePos: {}, airTemp: {}, oilTemp: {}".format(
    time.time(),
    speedVal,
    fuelVal,
    fuelStatVal,
    fuelRateVal,
    rpmVal,
    throttleVal,
    airTempVal,
    oilTempVal
  )

  logData(row)
  print(row)

repeat()

