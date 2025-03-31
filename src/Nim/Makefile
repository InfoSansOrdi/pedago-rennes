TRACES= nim_trace_ecrite.pdf
PREPS=  nim_prep_2017_BautistaBordais.pdf

RAPPORS=   
RAPPORTS+= 2023_AdamTimmerman 2023_RautureauHamon
RAPPORTS+= 2024_TroubleTanguyLegac

all: ${TRACES} ${PREPS} $(foreach rapport,${RAPPORTS},Rapports/${rapport}.html)

clean: 
	rm -f *.aux *.log *.html *.pdf *~

%.pdf: %.tex
	pdflatex $< -o $@
	
%.pdf: %.typ
	typst compile $< $@

%.html: %.md
	python ../../md-to-html.py $< $@
