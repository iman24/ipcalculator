#!/bin/python

# by Iman Nurjaman
# http://www.imanancin.com

import ipcalc
from re import match
from sys import exit, argv
from os import system


system('clear')
print('=== IP CALCULATOR V2.0 ===')

if len(argv) > 1:
 ip = argv[1].strip()
else:
 ip = input('Enter Ip with prefix: ')

x = match("^(\d{1,3}\.){3}\d{1,3}\/\d{,2}$", ip)

if x is None:
 print('IP Address not valid')
 exit()

ipc = ipcalc.Network(ip)
print('[*] {0:<10} {1}'.format('IP ', ': '+ip))
print('[*] {0:<10} {1}'.format('Network ',': '+str(ipc.network())))
print('[*] {0:<10} {1}'.format('Netmask ',': '+str(ipc.netmask())))
print('[*] {0:<10} {1}'.format('Broadcast ', ': '+str(ipc.broadcast())))
print('[*] {0:<10} {1}'.format('IP First ',': '+str(ipc.host_first())))
print('[*] {0:<10} {1}'.format('IP Last ',': '+str(ipc.host_last())))
print('[*] {0:<10} {1} hosts'.format('IP Valid ', ': '+str(ipc.size()-2)))

p = len(ipc)


print( ' --------------')
print( '|List valid IP |')
print( '|--------------|')
inc = 0
for x in ipc:
 inc += 1
 if inc > 5 and inc < p-5 and p > 10:
  continue
 if inc == p-5 and p > 10:
  print('|   .......    |')
 print('| ' + str(x) + ' |')

# 20
#12345......1617181920


print( ' --------------')
