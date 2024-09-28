df.drop_duplicates(inplace=True)
df.fillna(method='ffill', inplace=True)  # Example of handling missing values

# Save cleaned data
df.to_csv('/content/StudentsPerformance.csv', index=False)