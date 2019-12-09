import pandas as pd
from datetime import datetime

data = pd.read_excel('Final.xlsx')
primeCustomerData = pd.read_excel('PrimeCustomerDetails.xlsx')
primeCustomer = primeCustomerData.iloc[0,0]
planDate = primeCustomerData.iloc[0,1]
customerCode = customerRanking['Customer Code'].tolist()
customerRank = customerRanking['Rank'].tolist()
data.insert(5,'Week_And_Year',str)
data.insert(9,'PrimeAndOtherCustomerRanks',int)
data.insert(10,'CustomerRanking',int)
