#! /bin/sh

echo "solve.sh: Finding flag"
flag=$(echo '!grep "CTF{" -r *'| ./connect.sh | grep -om 1 "CTF{.*}")

if [ -n "$flag" ]; then
	echo "Flag is: $flag"
else
	echo "Flag not found. Check connection."
fi