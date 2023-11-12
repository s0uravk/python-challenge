# python-challenge
These python scripts perform financial analysis of PyBank and election results of PyPoll.

**PyBank**

![revenue-per-lead](https://github.com/s0uravk/python-challenge/assets/144293972/25166afc-a047-4041-82de-2b1f8fe597ec)

PyBank summarize the financial data and outputs essential parts of analysis such as number of oberservation, in this case months, and net profit/loss along with average change occured, greatest increase and greatest decrease in profits over those number of observations.

This script requires the input data file to be formatted in a specific order with months as first value and here profit/loss as second value seprated by a comma. it could be another delimiter instead of a commas but then script will require a minor change to perform the analysis.

Pypoll main.py file, upon execution, retrieves the data form budget_data.csv file, process it and showcase the results in terminal and also creates a result.txt file in analysis folder in PyBank folder.

**PyPoll**

![Vote_counting](https://github.com/s0uravk/python-challenge/assets/144293972/70d7eced-acf1-4204-b789-cb2add605c8c)

PyPoll outputs the results of an election with essential such as total votes as well as each candidate listed along with the number of votes they received and percentage of the votes. At the end, it also display the Winning candidate with number of votes and percentage.

This script requires the data being proccessed to be in a specific format with name of candidates as third value in a csv file  and listed as many times as total votes have been cast to them in each row on third place. 

PyBank main.py file, upon execution , retrieves the data form election_data.csv file, process it and showcase the results in terminal and also creates a result.txt file in analysis folder in PyPoll folder.
