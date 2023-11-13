import pandas as pd
import statsmodels.api as sm

# Load the data
df = pd.read_csv('E:\\Code\\synthetic_survey_data_high_alpha.csv')

# Independent variables (with a constant added for the intercept)
X = df[['item2', 'item3', 'item4', 'item5']]
X = sm.add_constant(X)

# Dependent variable
y = df['item1']

# Create the OLS model
model = sm.OLS(y, X)

# Fit the model
results = model.fit()

# Print out the summary which includes the p-values
print(results.summary())

# you should interpret the p-values as "< 0.001" when they are very small, instead of "0.000"