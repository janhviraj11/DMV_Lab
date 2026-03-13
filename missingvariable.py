import pandas as pd
from sklearn.impute import SimpleImputer


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, None, 30, None, 28],
    "Salary": [50000, 60000, None, 52000, None],
    "City": ["Mumbai", None, "Delhi", "Mumbai", "Delhi"]
}


df = pd.DataFrame(data)

print("Original Data:")
print(df)


print("\nMissing values in each column:")
print(df.isnull().sum())


num_imputer = SimpleImputer(strategy="mean")
df[["Age", "Salary"]] = num_imputer.fit_transform(df[["Age", "Salary"]])


cat_imputer = SimpleImputer(strategy="most_frequent")
df[["City"]] = cat_imputer.fit_transform(df[["City"]])

print("\nCleaned Data:")
print(df)