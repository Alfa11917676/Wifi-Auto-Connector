import os
import sys


savedNetworks= os.popen('netsh wlan show profiles').read()

print(savedNetworks)
available_profiles=os.popen('netsh wlan show networks').read()
print(available_profiles)
prefered_network=input("Enter the prefered nertwork: ")

resonseFeed=os.popen('netsh wlan disconnect').read()
print(resonseFeed)


if prefered_network not in savedNetworks:
	print("Chosen network"+prefered_network+" is not in system")
	print("Sorry for the inconvinience")
	sys.exit()
else:
	print("Chosen network"+prefered_network+" is in system")

while True:
	avial=os.popen('netsh wlan show networks')
	break
if prefered_network in avial:
	print ('Found')
	


print("-----------connecting----------------")
red=os.popen('netsh wlan connect name='+'"'+prefered_network+'"').read() 		
print(red)

