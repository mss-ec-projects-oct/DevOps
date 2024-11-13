#!/bin/bash
echo "switch case demo starts..."
case $1 in
        start)
                echo "You have typed start, congratulations....:)"
                echo "Thnak you......"
                ;;
        stop)
                echo "you have selected stop. looking agin to start ..:)"
                echo "Thank you......"
                ;;
        restart)
                echo "Good choice to restart....:)"
                echo "Thank you......"
                ;;
        *)
                echo "Please pass the correct argument..."
                echo "Usage: sh $0 start|stop|restart"
esac
echo "switch case demo over....."
