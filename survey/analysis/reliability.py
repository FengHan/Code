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

# Load your data
#在Windows系统中，文件路径通常使用反斜杠（\）而不是斜杠（/）。
# 所以你需要将路径中的斜杠替换为反斜杠，并确保如果路径中包含反斜杠，Python字符串应该将它们视为普通字符，而不是转义字符。
# 这可以通过在字符串前面加上 r 来实现，这样就会创建一个原始字符串。在你的情况下，路径应该是这样的：
df = pd.read_csv(r'E:\Code\synthetic_survey_data_high_alpha.csv')


# Calculate Cronbach's alpha
alpha = cronbach_alpha(df)
print(f"Cronbach's alpha: {alpha}")
