import numpy as np
import pandas as pd

# Set a seed for reproducibility
np.random.seed(0)

# Generate data for 5 items on a Likert scale (1 to 5)
# Assuming these items are correlated as they measure the same construct
data = {
    'item1': np.random.choice(range(1, 6), 100),
    'item2': np.random.choice(range(1, 6), 100),
    'item3': np.random.choice(range(1, 6), 100),
    'item4': np.random.choice(range(1, 6), 100),
    'item5': np.random.choice(range(1, 6), 100)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Introduce some correlations between the items manually
df['item2'] += (df['item1'] - df['item2']).abs() * np.random.choice([-1, 1], 100) * 0.5
df['item3'] += (df['item1'] - df['item3']).abs() * np.random.choice([-1, 1], 100) * 0.5
df['item4'] += (df['item1'] - df['item4']).abs() * np.random.choice([-1, 1], 100) * 0.5
df['item5'] += (df['item1'] - df['item5']).abs() * np.random.choice([-1, 1], 100) * 0.5

# Ensure the data is within the Likert scale range after manipulation and round off to nearest integer
df = df.clip(1, 5).round(0)

# Save the DataFrame to a CSV file
df.to_csv('synthetic_survey_data.csv', index=False)

print(df.head())
# Item1: 您对工作环境的满意度如何？
# Item2: 您对与同事的关系满意度如何？
# Item3: 您对目前的工作岗位的满意度如何？
# Item4: 您对工作提供的个人成长机会的满意度如何？
# Item5: 您对您的工作薪酬和福利的满意度如何？