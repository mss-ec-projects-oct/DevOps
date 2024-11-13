#!/bin/bash
for i in $(cat hosts)
do
ping -c 1 $i >> pingresult
validation=$(echo $?)
if [ $validation -gt 1 ]; then
        echo "$i Host is not reachable"
else
        echo "$i Host is up"
fi
done
