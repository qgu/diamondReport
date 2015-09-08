#!/bin/bash

input_file=$1
output_file=$2

gs -q -dNOPAUSE -dBATCH -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite -sOutputFile=${output_file} ${input_file}

