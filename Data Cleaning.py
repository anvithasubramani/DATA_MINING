import pandas as pd

# Load the country-income dataset
country_df = pd.read_csv('country-income.csv')

# Display the first few rows of the dataset
country_df.head()
from sklearn.impute import SimpleImputer

# Impute missing values with the mean of each feature
imputer = SimpleImputer(strategy='mean')
country_df_imputed = pd.DataFrame(imputer.fit_transform(country_df), columns=country_df.columns)

# Display the dataset after imputation
country_df_imputed.head()
from sklearn.preprocessing import LabelEncoder

# Identify categorical columns (assuming they are of object type)
categorical_columns = country_df_imputed.select_dtypes(include=['object']).columns

# Apply LabelEncoder to each categorical column
label_encoder = LabelEncoder()
for col in categorical_columns:
    country_df_imputed[col] = label_encoder.fit_transform(country_df_imputed[col])

# Display the resulting dataset with categorical features encoded numerically
country_df_imputed.head()
