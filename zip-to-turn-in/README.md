Project Two: Coin Change
===

### Instructions

* Unzip Project_Two_Submission.zip in an empty directory on FLIP  
* Navigate to that directory
* Type the following command:

```
tar -xvf cs325_Group12_ProjectTwo.tar.bz2
```

* You should see the following directories/files:

  * ./divide-conquer/changeslow.py   -Contains python code for the 'changeslow' algorithm
  * ./greedy/changegreedy.py  -Contains python code for the 'greedy' algorithm
  * ./dynamic-programming/changedp.py   -Contains python code for the 'dynamic programming' algorithm
  * ./run-files/projectTwo.py   -Contains python code to run inputs through algorithms and Also runs tests and experimental analysis (commented out)
  * ./Coin1.txt   -Contains input to test the algorithms with
  * ./Coin1change.txt   -Contains the observed output when passing in Coin1.txt to projectTwo.py
  * ./Amount.txt  -Contains more inputs to test algorithms against
  * ./Amountchange.txt  -Contains the output when passing in Amount.txt to projectTwo.py
* Navigate to the "run-files" directory
* Type the following command to run the code, replacing 'InputFile.txt' with your desired input file: 

```
python projectTwo.py [Input filename].txt
```
* You can then check the results from running the script in the newly created '[InputFile]change.txt' in the current directory, where 'InputFile' will match your input file name.
* NOTE: Change values greater than 25 will not be run due to extremely long run times. A message will be placed in the output file alerting you to this fact.
