#!/bin/bash

bubbleSort()
{
for ((i=0;i<=${#nums[@]};i++))
do
    for ((j=0;j<=${#nums[@]};j++))
    do
        if [ ${nums[$i]} -gt ${nums[$j]} ]
        then
            t=${nums[$i]}
            nums[$i]=${nums[$j]}
            nums[$j]=$t
        fi
    done
done
}

declare -a nums=(89 62 11 75 8 33 95 4)
echo ${nums[*]} #prints out all elems
bubbleSort
echo ${nums[*]} #prints out all elems
