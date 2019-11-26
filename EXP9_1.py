import pandas as pd

data1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80, 95, 79]}
math = pd.DataFrame(data1, columns = ['Student', 'Math'])
data2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85, 81, 83]}
electronics = pd.DataFrame(data2, columns = ['Student', 'Electronics'])
data3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90, 79, 93]}
geas = pd.DataFrame(data3, columns = ['Student', 'GEAS'])
data4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93, 89, 88]}
esat = pd.DataFrame(data4, columns = ['Student', 'ESAT'])

merge = pd.merge(math, electronics, how='right', on='Student')
merge1 = pd.merge(merge, geas, how='right', on='Student')
merge2 = pd.merge(merge1, esat, how='right', on='Student')

merged = pd.melt(merge2, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
merged1 = merged.rename(columns = {'variable': 'Subjects', 'value': 'Grades'})
merged2 = merged1.sort_values('Student').reset_index().drop(columns = 'index')

print(merge2)
print(merged2)