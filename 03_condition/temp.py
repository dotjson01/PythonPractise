#  you're building a smart thermomet alert  system 
# if device_status = true 
#  and temperature  > 30 celsius warn : high temperature 
# else temp :normal 
#  device off : please turn on the device 

device_status =  True
temperature = 35
if device_status and temperature > 30 : print(f"High Temperature")
elif device_status and temperature < 30 : print(f"Normal Temperature")
else : print(f"Please turn on the device")