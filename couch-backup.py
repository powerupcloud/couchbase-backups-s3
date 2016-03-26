from __future__ import print_function
from datetime import datetime
from time import gmtime, strftime
import boto3
import time
import os
import gzip
import commands
import paramiko
import sys

DATE = time.strftime('%m%d%Y-%H%M%S')
Master_node="10.10.10.1"
port="8091"
DUMP_PATH='/tmp/'
username="Administrator"
password="'supersecret'"

BACKUPNAME =  DUMP_PATH + DATE

bucket='lambda-work-raju'        
s3 = boto3.client('s3')  

k = paramiko.RSAKey.from_private_key_file("/tmp/wgo.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())


command = "cd /opt/couch-cli/couchbase-cli/ && ./couchbase-cli server-list -c " + Master_node + ":8091" + " -u " + username + " -p " + password + "|" + "cut -f2 -d"'@'"" + "|" + "awk '{ print $1 }'" + ">" + "/tmp/nodelist.txt"
check = os.system(command)

print (check)
filename="/tmp/nodelist.txt"
with open(filename) as f:
    data = f.read().splitlines() 
    for datas in data:    	
    	host=datas
    	print (host)
    	print ("connecting to " + str(host))
    	c.connect(hostname=str(host), username="ubuntu", pkey=k)
    	print ("connected to"+host)
    	
    	scriptrun = [
    	"aws s3 cp  s3://couchbasebackups/master-couch.py /home/ubuntu/master-couch.py",
    	"cd /home/ubuntu/ && chmod 755 master-couch.py",
    	"python /home/ubuntu/master-couch.py"
        ]

    	for command in scriptrun:
    		print ("Executing {}".format(command))
    		stdin , stdout, stderr = c.exec_command(command)
        	print (stdout.read())
        	print (stderr.read())  
    	sys.exit()     	   
    c.close()
