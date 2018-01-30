#!/bin/bash

#########################################
#	Name: mat2ifw_Easy_enhanced.sh
#	Input file:  ./mat.txt
#	Output dir: ./ifw/
#	Script:   ./mat2ifw_Easy_enhanced.sh
# copy the original file to the Input
# dir, run the script mat2ifw_Easy_enhanced.sh,
# check the result under Out dir.
#########################################
filename="./mat.txt"
declare -a array

a=`cat $filename | awk -F "/" '{print $1}' | uniq`
array=($a)
srclist=$(cat $filename | sed '/./{s/^/  <component-filter name="&/g;s/$/&\"\ \/>/g}')

for i in ${a[*]}; do

	file="$i.xml"
	midlist=$(echo "${srclist}" | grep $i)
	dstlist="<rules>
<broadcast block=\"true\" log=\"false\">
"${midlist}"
</broadcast>
<service block=\"true\" log=\"false\">
"${midlist}"
</service>
<activity block=\"true\" log=\"false\">
"${midlist}"
</activity>
</rules>"
	echo "${dstlist}" > ./ifw/$file

done

