import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
file_path = 'E:\\Code\\synthetic_survey_data_high_alpha.csv'
df = pd.read_csv(file_path)

# Independent variables
X = df[['item2', 'item3', 'item4', 'item5']]

# Dependent variable
y = df['item1']

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Get the coefficients and intercept of the model
coefficients = model.coef_
intercept = model.intercept_

# Display the coefficients and intercept
print('Coefficients:', coefficients)
print('Intercept:', intercept)

