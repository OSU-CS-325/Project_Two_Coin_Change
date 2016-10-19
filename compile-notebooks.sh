#!/bin/bash

rm report/final_report.ipynb 
python nbmerge.py report/header_page.ipynb > report/final_report.ipynb 
