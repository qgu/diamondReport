#!/bin/bash

latex report.tex
latex report.tex
dvips -P pdf report.dvi
ps2pdf report.ps

pdffonts report.pdf

echo "Embedding fonts into final output: paper.pdf"
./embedfonts.sh report.pdf paper.pdf

echo "Listing fonts in final output: paper.pdf"
pdffonts paper.pdf

