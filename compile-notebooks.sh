#!/bin/bash

rm report/final_report.ipynb 
python nbmerge.py report/header.ipynb divide-conquer/divide_and_conquer.ipynb greedy/greedy.ipynb dynamic-programming/dynamic_programming.ipynb run-files/question3.ipynb run-files/question4.ipynb run-files/question5.ipynb run-files/question6.ipynb run-files/question7.ipynb run-files/question8.ipynb report/references.ipynb > report/final_report.ipynb 