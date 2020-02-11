#!/bin/bash
fmt="+%Y/%m/%d %H:%M:%S"
mins=$1
mins=${mins:=30}
log_file=$2
log_file=${log_file:="/Users/genguo/.wgg/tm.log"}
echo "" | tee -a $log_file
echo -n Start $(date "$fmt") $mins | tee -a $log_file
echo "" # line break
while [ $mins -gt 0 ]
do
  echo $mins left...
  mins=$(( $mins - 1 ))
  read -t 60 OP
  case $OP in
    q)
      break
      ;;
    *)
      ;;
  esac
done
let "actual = $SECONDS / 60"
finish_date=$(date "$fmt")
echo Time Up, Actual Minutes: $actual
answer=$(osascript -e 'display dialog "Tomato: Time up! How the pomodoro went?" buttons {"Done", "Half", "Failed"} default button "Done"')
result=${answer#"button returned:"}
echo -n " Finished" $finish_date $result $actual | tee -a $log_file
echo "" # line break
