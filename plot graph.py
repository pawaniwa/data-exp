import matplotlib.pyplot as plt

# Assuming the first unnamed column is an identifier and the second unnamed column contains the category descriptions
category_column = 'Unnamed: 1'
# The rest of the columns are assumed to be data points for the trends
data_columns = df.columns[2:]

# Set the category column as the index
df.set_index(category_column, inplace=True)

# Plot a bar chart
plt.figure(figsize=(14, 7))
# Plot each column
for column in data_columns:
    plt.bar(df.index, df[column], label=column)

plt.title('Trends by Category')
plt.xlabel('Category')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
