#!/bin/bash
mins=${1:=30}
while [ $mins -gt 0 ]
do
  echo $mins left...
  mins=$(( $mins - 1 ))
  sleep 60
done
echo Done
osascript -e 'display alert "Cong!" message "Take a break now"'
