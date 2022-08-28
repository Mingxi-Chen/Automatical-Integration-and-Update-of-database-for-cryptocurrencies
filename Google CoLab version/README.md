This *workflow* folder aims to  update weekly data to historical master database
Execution procedures:
1.	Run *ScratchNames.ipynb* to  obtain changes in Top 200 cryptocurrencies and save it in *latest* folder; and merge these names to *accumulative* folder
2.	Run * ScrtchNames.ipynb* to get data in  last week based on the crypto names in *accumulative* folder
3.	Run *merge_data.ipynb* to merge weekly data into master database

Accumulative Folder:
Sum of past ~Top 200 cryptocurrency names.

Latest Folder:
Latest Top 200 Cryptocurrency in last week.

Execution procedures in scratch5Days.ipynb:
1.set up environment 
2.import names from accumulative folder
3.scratch 7 days data
4.concat those dataframes

Issues:
(Done)1.title name [asses date (maybe can be removed: master database already existed)
			Or put if statement in that
(Done)2.sorting 
3.scheduler
