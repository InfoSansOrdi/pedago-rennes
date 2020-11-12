# /usr/bin/sh

# Very crude script to generate a whole booklet of boards
# This should be redone in python, or even integrated in the main script

### Parameters
###
PAGEBACK="" # if empty, no page back is inserted (print one-sided, then)
PAGECOUNT=10

### Start of script
###
set -e 

if [ "x$PAGEBACK" != "x" ] ; then # Need a page back
  sed -e "s/P°/$PAGEBACK/g" ../human-puzzle/pageback.svg > tmp-back.svg
  inkscape --export-pdf=tmp-back.pdf tmp-back.svg
  pdf90 tmp-back.pdf
  mv tmp-back-rotated90.pdf tmp-back.pdf
fi

# Generate all pages
files=
for n in `seq $PAGECOUNT` ; do
  echo
  echo "Generate page $n"
  ./generate.py
  mv board.pdf board-$n.pdf
  files="$files board-$n.pdf"
  if [ "x$PAGEBACK" != "x" ] ; then
    files="$files tmp-back.pdf"
  fi
done

# Assemblate the pages and cleanup
set -x
pdfjoin --outfile boards.pdf $files
rm -f $files tmp-back.svg tmp-back.pdf
