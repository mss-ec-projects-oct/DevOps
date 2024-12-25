#!/bin/bash
source = /home/ubuntu/jenkinscli/jenkinsdetails.properties
echo "Please pass the job name which you want to get the configurations...."
read jobname

echo "Getting the $jobname job configurations"
echo "========================================="

java -jar jenkins-cli.jar -s $jenkinsurl -auth $jenkinsuser:$jenkinspassword get-job $jobname > $jobname.xml
