#  此文件是生成科隆巴赫数据大于0.8的一组数据，并保存在本地
# Item1: 您对工作环境的满意度如何？
# Item2: 您对与同事的关系满意度如何？
# Item3: 您对目前的工作岗位的满意度如何？
# Item4: 您对工作提供的个人成长机会的满意度如何？
# Item5: 您对您的工作薪酬和福利的满意度如何？
import numpy as np
import pandas as pd

# Function to calculate Cronbach's alpha for a given dataframe
def cronbach_alpha(df):
    # Calculate the number of items in the scale
    k = df.shape[1]
    
    # Calculate the variance for each item
    variances = df.var(axis=0)
    
    # Calculate the variance of the total scores
    total_variance = df.sum(axis=1).var(axis=0)
    
    # Calculate Cronbach's alpha
    alpha = (k / (k - 1)) * (1 - variances.sum() / total_variance)
    
    return alpha

# Set a seed for reproducibility
np.random.seed(0)

# Generate base scores for 100 participants that will be similar across all items
base_scores = np.random.normal(3, 1, 100)  # Normal distribution around the center of the Likert scale (3)

# Generate 5 Likert-scale items based on the base scores
# Since we want the items to be highly correlated, we'll make each item score close to the base score
data = {
    'item1': np.clip(base_scores + np.random.normal(0, 0.5, 100), 1, 5),
    'item2': np.clip(base_scores + np.random.normal(0, 0.5, 100), 1, 5),
    'item3': np.clip(base_scores + np.random.normal(0, 0.5, 100), 1, 5),
    'item4': np.clip(base_scores + np.random.normal(0, 0.5, 100), 1, 5),
    'item5': np.clip(base_scores + np.random.normal(0, 0.5, 100), 1, 5),
}

# Create a DataFrame and round the scores to the nearest integer to mimic Likert scale responses
df = pd.DataFrame(data).round().astype(int)

# Calculate Cronbach's alpha for the dataset
alpha = cronbach_alpha(df)
print(f"Cronbach's alpha: {alpha}")

# Specify the file path where you want to save the CSV on your local machine
file_path = 'E:\\Code\\synthetic_survey_data_high_alpha.csv'

# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"The data has been saved to {file_path}")
