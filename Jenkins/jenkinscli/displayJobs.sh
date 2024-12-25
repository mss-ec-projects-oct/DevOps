#!/bin/bash
source /home/ubuntu/jenkinscli/jenkinsdetails.properties
echo "Display the jobs"
echo "----------------"
java -jar jenkins-cli.jar -s $jenkinsurl -auth $jenkinsuser:$jenkinspassword list-jobs
