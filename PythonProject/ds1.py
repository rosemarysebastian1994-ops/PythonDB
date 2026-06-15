import pandas as pd

d = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 0, 1, 2]}
df = pd.DataFrame(data=d)
print(df)

print(df.head())
print(df['b'].mean())

count_column = df.shape[1]
print(count_column)

count_row = df.shape[0]
print(count_row)

average_pulse_max = max(d['c'])
print(average_pulse_max)

average_pulse_min = min(d['c'])
print(average_pulse_min)


