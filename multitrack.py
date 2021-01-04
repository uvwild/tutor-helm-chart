#!/usr/bin/env python3
##########################################
from __future__ import print_function
import os
import json
import sys
import subprocess

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


NAMESPACE = "helmtutor"
resources = [ "Deployments", "Pods" ]

def getConfig(res,ns):
    cmd = "kubectl -n {0} get {1}".format (ns,res)
    cmd += " | grep -v Running | grep -v NAME | awk \'{print $1}\'"
#   print("cmd: " + cmd)
    process = subprocess.run(cmd, shell=True, capture_output=subprocess.PIPE)
    Resources = process.stdout.decode().split()
#   [ print("pod: " + str(pod)) for pod in pods ]
    resList = []
    for r in Resources:
        descriptor = {}
        descriptor['ResourceName'] = r
        descriptor['Namespace'] = NAMESPACE
        resList.append(descriptor)
    return resList

def main(ns):
    conf = {}
    for res in resources:
        conf[res] = getConfig(res,ns)
    confString = json.dumps(conf, indent = 2)
    print (confString)

if __name__ == "__main__":
    ns = NAMESPACE
    if len(sys.argv) > 1:
        ns = sys.argv[1]
    eprint ("using namespace {}".format(ns))
    main(ns)
