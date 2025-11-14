from sklearn.datasets import load_wine
import pandas as pd

# Load the wine dataset
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = pd.Series(data.target)

# Display the first few rows of the dataset
df.head()
# Compute the frequency of each value of the categorical feature ('target')
categorical_feature = 'target'
frequency = df[categorical_feature].value_counts()
frequency
# Univariate summary (mean and standard deviation)
univariate_summary = df.describe().loc[['mean', 'std']]
univariate_summary
# Multivariate summary: correlation matrix
correlation_matrix = df.corr()
correlation_matrix
# Group by the categorical feature ('target') and compute the median for each numerical feature
grouped_median = df.groupby('target').median()
grouped_median
import matplotlib.pyplot as plt

# Find the pair of numerical features with the highest correlation
correlation_matrix = df.corr()
highly_corr_pair = correlation_matrix.unstack().idxmax()

# Create the scatter plot for the most highly correlated features
feature1, feature2 = highly_corr_pair
plt.scatter(df[feature1], df[feature2])
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.title(f"Scatter plot of {feature1} vs {feature2}")
plt.show()
