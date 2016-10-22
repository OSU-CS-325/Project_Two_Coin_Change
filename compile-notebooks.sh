#!/bin/bash

rm report/final_report.ipynb 
python nbmerge.py report/header_page.ipynb divide-conquer/divide_and_conquer.ipynb greedy/greedy.ipynb dynamic-programming/dynamic_programming.ipynb > report/final_report.ipynb 
