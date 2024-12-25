echo "please pass the jobname which you want to create...."
read jobname

echo "creating the $jobname job"
echo "==========================="
java -jar jenkins-cli.jar -s http://13.126.70.209:8080/ -auth manoj:11afdb0218bfacafb4878c63318bb6278e create-job $jobname < walmart-dev.xml
