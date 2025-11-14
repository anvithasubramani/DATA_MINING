from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Extract features and target
X = df.drop(columns=['target'])
y = df['target']

# Apply PCA without scaling the data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the scatterplot color-coded by the 'target' column
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title("PCA of Wine Dataset (without scaling)")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Target')
plt.show()
# Standardize the data before applying PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA again with standardized data
pca = PCA(n_components=2)
X_pca_scaled = pca.fit_transform(X_scaled)

# Plot the scatterplot color-coded by the 'target' column
plt.figure(figsize=(8, 6))
plt.scatter(X_pca_scaled[:, 0], X_pca_scaled[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title("PCA of Wine Dataset (after scaling)")
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Target')
plt.show()
