#! /bin/sh

file_name=7ad5a7d71a7ac5f5056bb95dd326603e77a38f25a76a1fb7f7e6461e7d27b6a3

echo "solve.sh: Fetching file: $file_name" | cut -c -70
mkdir -p data
wget -N -q https://storage.googleapis.com/gctf-2018-attachments/$file_name -P data

echo "solve.sh: Unzipping"
unzip -d data -u data/$file_name > /dev/null

# OCR sometimes confuses L's and I's on this image so tweak it
# for better results
echo "solve.sh: Resizing and sharpen image."
convert -resize 600% -unsharp 0x5 -density 300 data/OCR_is_cool.png data/resized.png

echo "solve.sh: Performing OCR using Tesseract.\n"
tesseract --dpi 300 data/resized.png data/data > /dev/null
echo ""

echo "solve.sh: Brute forcing text through Caesar ciphers"
flag=$(python ./caesar.py data/data.txt)
if [ -n "$flag" ]; then
	echo "Flag: $flag"
fi