#!/bin/bash
IFS="
"
VM=$1
IP=$2
PORT=$3
VMX_DIR="${HOME}/Documents/Virtual Machines.localized/"
VMRUN="/Applications/VMware Fusion.app/Contents/Library/vmrun"
NCAT="/usr/local/bin/ncat"

RUNNING=`${VMRUN} list | grep "${VM}"`

if [[ -z "${RUNNING}" ]];then
	echo "[+] starting ${VMX}"
	${VMRUN} -T fusion start ${VMX_DIR}/${VM} nogui
fi

count=0
while !	${NCAT} $IP $PORT 
do
	sleep 5
	if [ $count > 10 ];then
		exit
	fi
done
