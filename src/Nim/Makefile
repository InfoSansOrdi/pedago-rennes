TRACES= nim_trace_ecrite.pdf
PREPS=  nim_prep_2017_BautistaBordais.pdf
MATOS=materiel-SMN.pdf
IMG=materiel-SMN-300x.png

include ../Makefile.defs

materiel-SMN.pdf: materiel-SMN.svg
	rm -f tempfile.pdf ; rsvg-convert --format pdf1.5 -o tempfile.pdf materiel-SMN.svg
	pdfjam --outfile materiel-SMN.pdf --no-landscape --papersize '{210mm,297mm}' --nup 1x2 tempfile.pdf tempfile.pdf 
	
