#!/bin/python3
import paramiko

user='manoj'
password='7726'
port=22
hostname='172.31.12.54'

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,username=user,password=password)

stdin,stdout,stderr=client.exec_command('ls l-')
print(stderr.read().decode())
client.close()

