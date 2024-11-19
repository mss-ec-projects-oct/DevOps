#!/bin/bash
echo "Funtion demo starts...."
greetfn
greetfn()
{
        echo "Hello Guys..."
        echo "GM/GA/GE"
        echo "Today date is: $(date)"
}
echo "Functions are very useful for reusing the code...."
echo "calling the function..."
greetfn
