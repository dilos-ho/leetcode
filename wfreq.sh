#!/bin/bash

output="$(tr -s [:space:] \\n < words.txt | sort | uniq -c | sort -r)"
while read line
do
    num="${line:0:2}"
    word="${line:2}"
    res="${word+$word" "$num}"
    echo $res | tr -s [:space:]
done <<< "${output}"
