import pandas as pd

# Load the dataset
shoesize_df = pd.read_csv('shoesize.csv')

# Check the actual columns
print(shoesize_df.columns)
print(shoesize_df.head())


# Display the first few rows of the dataset
shoesize_df.head()
import matplotlib.pyplot as plt

# Separate the data by gender
male_data = shoesize_df[shoesize_df['gender'] == 'M']
female_data = shoesize_df[shoesize_df['gender'] == 'F']

# Plot for male subjects
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(male_data['shoe_size'], male_data['height'])
plt.title("Male: Shoe Size vs Height")
plt.xlabel('Shoe Size')
plt.ylabel('Height')

# Plot for female subjects
plt.subplot(1, 2, 2)
plt.scatter(female_data['shoe_size'], female_data['height'])
plt.title("Female: Shoe Size vs Height")
plt.xlabel('Shoe Size')
plt.ylabel('Height')

plt.tight_layout()
plt.show()
from scipy.stats import pearsonr

# Compute Pearson's correlation for male subjects
male_corr, _ = pearsonr(male_data['shoe_size'], male_data['height'])

# Compute Pearson's correlation for female subjects
female_corr, _ = pearsonr(female_data['shoe_size'], female_data['height'])

male_corr, female_corr
