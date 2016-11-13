#!/bin/sh

dict_file="en-cs.txt"
tmp_file="sort.tmp"

cd `dirname $0`
LC_COLLATE=cs_CZ.utf8 sort -f -o $tmp_file $dict_file

if [ "$1" = "check" ]
then
    diff -u $tmp_file $dict_file
    result=$?
    rm $tmp_file
    exit $result
fi

mv $tmp_file $dict_file
