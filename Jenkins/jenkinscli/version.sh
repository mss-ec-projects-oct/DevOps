#!/bin/bash
source /home/ubuntu/jenkinscli/jenkinsdetails.properties
echo "Displaying the Jenkins version"
echo "=============================="
java -jar jenkins-cli.jar -s $jenkinsurl -auth $jenkinsuser:$jenkinspassword version
