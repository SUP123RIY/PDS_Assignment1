#1st one


import seaborn as sns
import matplotlib.pyplot as plt

# Box plot
sns.boxplot(x='gender', y='Percentage', data=df, palette='coolwarm')

# Display the plot
plt.show()

#2nd one


# Step 1: Count the number of occurrences for each type of lunch
lunchCount = df['lunch'].value_counts()

# Step 2: Create a bar graph
plt.figure(figsize=(6, 4))
plt.bar(lunchCount.index, lunchCount.values, color='green')

# Step 3: Add labels and title
plt.xlabel("Lunch Type")
plt.ylabel("Count")
plt.title("Types of Lunch Distribution")

# Step 4: Save the image to your local file manager
plt.savefig(r"C:\Users\supri\Downloads\lunchdistribution_bar.png")

# Step 5: Display the plot
plt.show()

#3rd one

import matplotlib.pyplot as plt

# Create the scatter plot
plt.plot(df['math score'], df['writing score'], marker='o', linestyle='none', color='blue')

# Add labels and title
plt.xlabel('Math Score')
plt.ylabel('Writing Score')
plt.title('Math vs Writing Scores')

# Option 1: Save to a different directory (e.g., current directory)
plt.savefig("mathvswriting.png")  # Saves in the current working directory

# Option 2: Save to a new valid folder
# Make sure this folder exists or change it to a valid one
plt.savefig(r"C:\Users\supri\Downloads\mathvswriting.png")

# Display the plot
plt.show()

#4th one

# Create a hexbin joint plot
ax = sns.jointplot(x='Percentage', y='reading score', data=df, kind='hex', cmap='Blues')

# Save the plot as a PNG file in Colab's /content directory
plt.savefig("Hexbin_Plot.png")

# Display the plot
plt.show()

plt.savefig(r"C:\Users\supri\Downloads\Hexbin_Plot.png")
plt.show()


#5th one

genders = df['gender'].unique()

# Create a figure with subplots
fig, axes = plt.subplots(nrows=1, ncols=len(genders), figsize=(15, 5), sharey=True)

# Iterate over each gender and plot
for ax, gender in zip(axes, genders):
    subset = df[df['gender'] == gender]
    sns.scatterplot(x='Percentage', y='reading score', data=subset, ax=ax)
    ax.set_title(f'{gender.capitalize()}')
    ax.set_xlabel('Percentage')
    ax.set_ylabel('Reading Score')

# Adjust layout
plt.tight_layout()

# Save the figure to Colab's /content directory
plt.savefig("FacetGrid_Scatterplot.png")

# Display the plot
plt.savefig(r"C:\Users\supri\Downloads\FacetGrid_Scatterplot.png")
plt.show()