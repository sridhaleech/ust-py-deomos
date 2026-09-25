import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

print("Data:")
print(df)

# Statistics for numeric columns
print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMode:")
print(df.mode().iloc[0])