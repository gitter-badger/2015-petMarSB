BIBFILE=2015-petMarSB.bib

all: 2015-petMarSB.draft.pdf 2015-petMarSB.draft.rst

2015-petMarSB.draft.tex: 2015-petMarSB.draft.texw
	Pweave -f tex 2015-petMarSB.draft.texw -s ipython

2015-petMarSB.draft.rst: 2015-petMarSB.draft.tex
	pandoc $< -o $@

2015-petMarSB.draft.pdf: 2015-petMarSB.draft.tex
	rm -rf tex_out
	mkdir -p tex_out
	cd tex_out; ln -s ../$<
	cd tex_out; ln -s ../$(BIBFILE)
	cd tex_out; pdflatex $<; bibtex $<; pdflatex $<; pdflatex $<
	cp tex_out/$@ .

clean:
	rm -rf tex_out 2015-petMarSB.draft.pdf 2015-petMarSB.draft.tex
