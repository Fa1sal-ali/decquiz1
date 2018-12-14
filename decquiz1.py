import pandas as pd
lst1 = [] # Create an empty list
print("Enter 5 Numbers: ")
for i in range(5):
   lst1.append(eval(input()))
print('The numbers you entered are: ', lst1)
ps=pd.Series(lst1) # converting the list to a pandas series
print('The mean is: ', ps.mean())
print('The median is: ', ps.median())
print('The mode is: ', ps.mode()[0])
