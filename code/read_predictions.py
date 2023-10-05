import pandas as pd

# read the txt file as a pandas dataframe
df = pd.read_csv('c2.txt', sep='\t')

# calculate the mean of the "correct" column
mean_correct = df['correct'].mean()

# print the mean of the "correct" column
print(mean_correct)

print(f"Abstained {(df['predict'] < 0.).mean():.4f}")

# print count unique values in predict column
print(df['predict'].value_counts())