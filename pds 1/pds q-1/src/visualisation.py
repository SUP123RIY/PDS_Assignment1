df = pd.DataFrame(data)

# Create a scatter plot for Height vs Weight
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Height', y='Weight', data=df, hue='Frailty', style='Frailty', s=100)

# Add title and labels
plt.title('Height vs Weight', fontsize=16)
plt.xlabel('Height (inches)', fontsize=14)
plt.ylabel('Weight (lbs)', fontsize=14)

# Save the scatter plot to the specified directory
plt.savefig(r"C:\Users\supri\Downloads\height_vs_weight.png")

# Display the plot
plt.show()


#2nd one 

# Create bar graph
plt.figure(figsize=(6, 4))
plt.bar(data['Weight'], data['Grip strength'], color='blue', alpha=0.7)
plt.title('Grip Strength vs Weight')
plt.xlabel('Weight')
plt.ylabel('Grip Strength')

# Save the plot to Colab's /content directory
plt.savefig("GripStrength_Weight_BarGraph.png")  # Save to Colab
plt.savefig(r"C:\Users\supri\Downloads\GripStrength_Weight_BarGraph.png")
# Display the plot
plt.show()


#3rd one

import numpy as np
# Select numeric columns for correlation
numeric_data = data.select_dtypes(include=[np.number])

# Correlation heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Add title
plt.title('Correlation Heatmap')

# Save the plot to Colab's /content directory
plt.savefig("correlation_heatmap.png")  # Save to Colab
plt.savefig(r"C:\Users\supri\Downloads\correlation_heatmap.png")

# Display the plot
plt.show()