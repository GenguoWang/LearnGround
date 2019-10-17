#!/bin/bash
a="a b c d"
for i in $a
do
  echo $i
done

IN="a;b;c;d"
arrIN=(${IN//;/ })
# This construction replaces all occurrences of ';' (the initial // means global replace) in the string IN with ' ' (a single space), then interprets the space-delimited string as an array (that's what the surrounding parentheses do).
echo ${arrIN[0]}
echo ${arrIN[1]}
echo ${arrIN[2]}
echo ${arrIN[3]}
