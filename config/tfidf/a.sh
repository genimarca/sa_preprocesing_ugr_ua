#!/bin/bash


#Un solo argumento de entrada


files=$(ls -1 ./*.txt)
for fileName in $files
do
	newName=${fileName/binary/tfidf}
	mv $fileName $newName
done
