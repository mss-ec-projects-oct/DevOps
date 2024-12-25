#!/bin/bash
source = /home/ubuntu/jenkinscli/jenkinsdetails.properties
echo "Please pass the job name which you want to delete...."
read jobname

echo "Deleting the $jobname"
echo "======================"
java -jar jenkins-cli.jar -s $jenkinsurl -auth $jenkinsuser:$jenkinspassword delete-job $jobname
