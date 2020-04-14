#Convert Dictionery into Dataframe
#modules


emp_details={'Employee':{'Raju':{'id':'001','Department':'4th'}},'Charlie':{'id':'002','Department':'3rd'}}
print(emp_details)

import pandas
df=pandas.Dataframe(emp_details['Employee'])
print(df)