#!/usr/bin/python3

try:
    from ncclient import manager as ma

except ImportError as i_err:
    print(i_err)

def main():
  '''using with for the connection to be to close automatically.'''
  #details
  with ma.connect(
    host="host1.woodydapogi.local",
    port=22,
    username="user1",
    password="password123",
    hostkey_verify=False,
    device_params={'name': 'csr'}) as m:
    
    #printing device's capabilities
    for dev in m.server_capabilities:
      print(dev)

main()
      
