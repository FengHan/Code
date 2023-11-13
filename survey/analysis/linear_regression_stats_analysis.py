import statsmodels.api as sm
import pandas as pd

# Load the data
file_path = 'E:\\Code\\synthetic_survey_data_high_alpha.csv'
df = pd.read_csv(file_path)

# Independent variables (adding a constant for the intercept)
X = sm.add_constant(df[['item2', 'item3', 'item4', 'item5']])

# Dependent variable
y = df['item1']

# Create a model
model = sm.OLS(y, X)

# Fit the model
results = model.fit()

# Get a summary of the regression results, which includes p-values
print(results.summary())
