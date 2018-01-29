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

echo "<rules>" >> $temfile
echo " <broadcast block="true" log="false">" >> $temfile
echo " </broadcast>" >> $temfile
echo " <service block="true" log="false">" >> $temfile
echo " </service>" >> $temfile
echo " <activity block="true" log="false">" >> $temfile
echo " </activity>" >> $temfile
echo "</rules>" >> $temfile
}

for i in ${a[*]}; do

file1="$i.tp1"
file2="$i.tp2"
file="$i.xml"
ct $file1
cat $filename | grep $i >> $file2

sed -i 's/^/  <component-filter name="&/g' $file2
sed -i 's/$/&" \/>/g' $file2

echo $file2 | sed -i "/log/r $file2" $file1

mv $file1 ./ifw/$file

rm -rf $file2

done
