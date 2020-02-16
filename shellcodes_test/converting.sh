#!/bin/bash
#輸出目錄內的所有ipynb轉成html存到html資料夾

mkdir html 2>/dev/null
jupyter nbconvert --to html *.ipynb 
mv *html html/