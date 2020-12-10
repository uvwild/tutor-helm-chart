#!/usr/bin/env python3
##########################################
import os
import json
import sys
import subprocess

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")


NAMESPACE = "helmtutor"
resources = [ "Deployments", "Pods" ]

def getConfig(res):
	cmd = "kubectl -n {0} get {1}".format (NAMESPACE,res)
	cmd += " | grep -v Running | grep -v NAME | awk \'{print $1}\'"
#	print("cmd: " + cmd)
	process = subprocess.run(cmd, shell=True, capture_output=subprocess.PIPE)
	Resources = process.stdout.decode().split()
#	[ print("pod: " + str(pod)) for pod in pods ]
	resList = []
	for r in Resources:
		descriptor = {}
		descriptor['ResourceName'] = r
		descriptor['Namespace'] = NAMESPACE
		resList.append(descriptor)
	return resList

def main():
	conf = {}
	for res in resources:
		conf[res] = getConfig(res)
	confString = json.dumps(conf, indent = 2)
	print (confString)

if __name__ == "__main__":
	main()