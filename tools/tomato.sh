#!/bin/bash
log_file="/Users/genguo/.wgg/tm.log"
fmt="+%Y/%m/%d %H:%M:%S"
mins=$1
mins=${mins:=30}
echo "" | tee -a $log_file
echo -n Start $(date "$fmt") $mins | tee -a $log_file
echo "" # line break
while [ $mins -gt 0 ]
do
  echo $mins left...
  mins=$(( $mins - 1 ))
  sleep 60
done
#osascript -e 'display alert "Cong!" message "Take a break now"'
answer=$(osascript -e 'display dialog "Tomato: Time up! How the pomodoro went?" buttons {"Done", "Half", "Failed"} default button "Done"')
result=${answer#"button returned:"}
echo -n " Finished" $(date "$fmt") $result | tee -a $log_file
