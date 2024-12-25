#!/bin/bash
source = /home/ubuntu/jenkinscli/jenkinsdetails.properties
echo "Please pass the job name which you want to trigger"
read jobname

echo "Please pass the BranchName"
read Branch

echo "Please pass the Person Name"
read Name

echo "Triggering the JobName"
echo "======================"
java -jar jenkins-cli.jar -s $jenkinsurl -auth $jenkinsuser:$jenkinspassword build $jobname -p	BranchName=$Branch PersonName=$Name
