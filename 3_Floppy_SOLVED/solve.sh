#! /bin/sh

file_name=4e69382f661878c7da8f8b6b8bf73a20acd6f04ec253020100dfedbd5083bb39

echo "solve.sh: Fetching file: $file_name" | cut -c -70
mkdir -p data
wget -N -q https://storage.googleapis.com/gctf-2018-attachments/$file_name -P data

echo "solve.sh: Unzipping"
unzip -d data -u data/$file_name > /dev/null

#echo "solve.sh:  Inspect strings"
#strings data/foo.ico


if [ ! -f data/_foo.ico.extracted ]; then
	echo "solve.sh: Binwalking"
	binwalk -eq data/foo.ico data/ -C data/
fi

echo "solve.sh: Searching for flag pattern"
flag=$(grep "CTF{.*}" data/_foo.ico.extracted/driver.txt | sed -e 's/^\s*//')

echo "Flag: $flag"