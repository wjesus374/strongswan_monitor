#!/usr/bin/python
# -*- encoding: utf-8 -*-

import vici
import sys


sline = '========================================================================================================================================'
ssline = '----------------------------------------------------------------------------------------------------------------------------------------'
print(sline)
print('\t\t\t\t\tStrongswan Status v.1.0 - by. wjesus')

s = vici.Session()
#list_sas = s.list_conns()
list_sas = s.list_sas()

for info in list_sas:
	#print(info)
	print(sline)
	for conn in info:
		print("Nome: \t\t[%s]" %conn)
		#print(info[conn])
		for data in info[conn]:
			#print('Chave: [%s]' %data)
			#print('Valor: [%s]' %info[conn][data])
			if 'state' in data:
				print('Status: \t[%s]' %info[conn][data])

			if 'established' in data:
				print('Tempo: \t\t[%s] segundos' %info[conn][data])

			if 'remote-host' in data:
				print('Publico: \t[%s]' %info[conn][data])

			if 'local-id' in data:
				print('Local: \t\t[%s]' %info[conn][data])

			if 'child-sas' in data:
				print(ssline)
				for child in info[conn][data]:
					#print(child)
					#Child Info
					#print(info[conn][data][child])
					name = info[conn][data][child]['name']
					state = info[conn][data][child]['state']
					life_time = info[conn][data][child]['life-time']
					install_time = info[conn][data][child]['install-time']
					local_ts = info[conn][data][child]['local-ts']
					remote_ts = info[conn][data][child]['remote-ts']
					bytes_in = info[conn][data][child]['bytes-in']
					bytes_out = info[conn][data][child]['bytes-out']
					packets_in = info[conn][data][child]['packets-in']
					packets_out = info[conn][data][child]['packets-out']
					print('Name: [%s]\t | State: [%s]\t | Life Time: [%s]\t | Remote: [%s]\t | Local: [%s]\t' %(name,state,life_time,remote_ts[0],local_ts[0]))

					#print('Network: [%s]TX [%s]RX [%s]IN [%s]OUT' %(bytes_in,bytes_out,packets_in,packets_out))
print(sline)
