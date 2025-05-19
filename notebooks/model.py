import pandas as pd

# Read the dataset using the correct path
try:
    df = pd.read_csv("Data/Dataset .csv")
    print("Dataset loaded successfully!")
    print("Shape of the dataset:", df.shape)
    print("\nFirst few rows of the dataset:")
    print(df.head())
except Exception as e:
    print("Error reading the dataset:")
    print(e) 