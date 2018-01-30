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

function ct(){
temfile=$1

echo "<rules> \

	 <broadcast block=\"true\" log=\"false\"> \

	  </broadcast> \

	   <service block=\"true\" log=\"false\"> \

	    </service> \

	     <activity block=\"true\" log=\"false\"> \

	      </activity> \

	      </rules>" > $temfile
}

for i in ${a[*]}; do

file1="$i.xml"
file2="$i.tp2"
ct ./ifw/$file1

cat $filename | grep $i | sed '/./{s/^/  <component-filter name="&/g;s/$/&\"\ \/>/g}' > $file2
echo $file2 | sed -i "/log/r $file2" ./ifw/$file1


rm -rf $file2

done
