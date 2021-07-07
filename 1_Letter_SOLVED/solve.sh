#! /bin/sh

file_name=5a0fad5699f75dee39434cc26587411b948e0574a545ef4157e5bf4700e9d62a

echo "solve.sh: Fetching file: $file_name" | cut -c -70
mkdir -p data
wget -N -q https://storage.googleapis.com/gctf-2018-attachments/$file_name -P data

echo "solve.sh: Unzipping"
unzip -d data -u data/$file_name > /dev/null

echo "solve.sh: Converting PDF to TXT"
pdftotext data/challenge.pdf data/challenge.txt

echo "solve.sh: Finding flag"
flag=$(grep -o "CTF{.*}" data/challenge.txt)

echo "Flag: $flag"
