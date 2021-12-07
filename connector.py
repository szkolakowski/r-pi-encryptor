import subprocess
import sys
import time
import os
from algorythms import encrypt as e
from algorythms import decrypt as d

class systemStart():
	# init class instance
	def __init__(self, t1, t2):
		self.user = subprocess.check_output('echo $SUDO_USER', shell=True).decode('utf-8')[:-1]
		self.system = subprocess.check_output(['uname','-o']).decode('utf-8')[:-1]
		self.nodename = subprocess.check_output(['uname','-n']).decode('utf-8')[:-1]
		self.k_release = subprocess.check_output(['uname','-r']).decode('utf-8')[:-1]
		self.k_version = subprocess.check_output(['uname','-v']).decode('utf-8')[:-1]
		self.netstat = len(subprocess.check_output(['netstat','|','grep','ESTABLISHED']).decode('utf-8')[:-1].split('\n'))
		self.devices = subprocess.check_output(['lsusb']).decode('utf-8')[:-1].split('\n')
		self.devices_init = len(self.devices)
		self.path = '/media/'+self.user+'/'
		self.usbs = os.listdir(self.path)
		self.usbs_init = len(self.usbs)
		self.ready = False
		self.t1 = t1
		self.t2 = t2

	# print system startup info
	def print(self):
		print('[SYSTEM START]')
		time.sleep(self.t1)
		print('user: ', self.user)
		time.sleep(self.t1)
		print('system: ', self.system)
		time.sleep(self.t1)
		print('nodename: ', self.nodename)
		time.sleep(self.t1)
		print('k_release: ', self.k_release)
		time.sleep(self.t1)
		print('k_version: ', self.k_version)
		time.sleep(self.t1)
		print('netstat: ', self.netstat, 'operations active')
		time.sleep(self.t1)
		print('devices: ', len(self.devices))
		for device in self.devices:
			print('\t'+device)
			time.sleep(self.t2)
		print('[CHANGE LOG]')

	# check if any devices were added / removed
	def checkChanges(self):
		devices_check = subprocess.check_output(['lsusb']).decode('utf-8')[:-1].split('\n')
		if len(devices_check) < self.devices_init:
			for device in self.devices:
				if device not in devices_check:
					print('\t-- REMOVED --')
					print('\t\t', device)
					self.devices_init -= 1
					self.devices.remove(device)
		if len(devices_check) > self.devices_init:
			for device in devices_check:
				if device not in self.devices:
					print('\t-- ADDED --')
					print('\t\t', device)
					self.devices_init += 1
					self.devices.append(device)

	# check if added device is ready to use
	def checkIfReady(self):
		usbs_check = os.listdir(self.path)
		if len(usbs_check) < self.usbs_init:
			for usb in self.usbs:
				if usb not in usbs_check:
					time.sleep(self.t1)
					print('\t\t> connection lost with "', usb, '"')
					self.usbs_init -= 1
					self.usbs.remove(usb)
		if len(usbs_check) > self.usbs_init:
			for usb in usbs_check:
				if usb not in self.usbs:
					print('\t\t> connection established with "', usb, '"')
					self.usbs_init += 1
					self.usbs.append(usb)
					encrytor = e.encryptor(self.path+usb, self.t1)
					encrytor.begin()

if __name__ == '__main__':
	system = systemStart(0.3, 0.1)
	system.print()
	while True:
		system.checkChanges()
		system.checkIfReady()