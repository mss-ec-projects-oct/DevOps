echo "1)Build the Job"
echo "2)Delete the Job"
echo "3)Display the Jenkins Version"
echo "4)Get the Job Configuration"
echo "Please pass the right option to do the jenkins task"

read option

case $option in
	1)bash Build.sh
		;;
	2)bash deletejob.sh
		;;
	3)bash version.sh
		;;
	4)bash get_the_jobconfigurations.sh
		;;
	*)echo "Please pass the correct option"
		;;
esac
