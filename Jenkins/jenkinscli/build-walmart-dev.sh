echo "Triggering the Jobs"
java -jar jenkins-cli.jar -s http://13.235.24.16:8080/ -auth manoj:11afdb0218bfacafb4878c63318bb6278e build walmart-dev
