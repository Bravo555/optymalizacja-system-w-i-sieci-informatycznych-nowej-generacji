#/bin/sh

set -e

cat $1 | tail -n +2 | head -n -2 | sed '/[0-9];/d' | sed 's/-- //' | sed 's/\[weight=//' | sed 's/];//' | \

# swap end node and weight (in .edges weight is in the middle)
awk ' { t = $2; $2 = $3; $3 = t; print; } ' 
