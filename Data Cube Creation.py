import pandas as pd
from cubes import Workspace

# Load the dataset
country_df = pd.read_csv('country-income.csv')

# Initialize the workspace
workspace = Workspace()

# Create a JSON schema for the data cube model
model = {
    "dimensions": [
        {"name": "region", "levels": [{"name": "region"}]},
        {"name": "age", "levels": [{"name": "age"}]},
        {"name": "online_shopper", "levels": [{"name": "online_shopper"}]}
    ],
    "measures": [
        {"name": "income", "aggregates": ["sum", "avg", "min", "max"]}
    ]
}

# Define the cube and load data
workspace.register_schema(model)
# Save the schema as a JSON file
with open('data_cube_model.json', 'w') as f:
    f.write(str(model))
cube = workspace.cube("country_income")
total_income = cube.aggregate(measures=["income"])
print(total_income)
region_results = cube.aggregate(drilldown=["region"], measures=["income"])
print(region_results)
online_shopper_results = cube.aggregate(drilldown=["online_shopper"], measures=["income"])
print(online_shopper_results)
age_40_50_results = cube.aggregate(drilldown=["age"], filters={"age": {"$gte": 40, "$lte": 50}}, measures=["income"])
print(age_40_50_results)
