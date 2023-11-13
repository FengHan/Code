import pandas as pd
from factor_analyzer import FactorAnalyzer

# Load the data
df = pd.read_csv('E:\\Code\\synthetic_survey_data_high_alpha.csv')

# Initialize factor analysis object and fit the model
fa = FactorAnalyzer(n_factors=1, rotation=None)
fa.fit(df)

# Get the factor loadings and communalities
loadings = fa.loadings_
communalities = fa.get_communalities()
uniquenesses = fa.get_uniquenesses()

# Calculate the explained variance and the eigenvalues
ev, v = fa.get_eigenvalues()

# Create the table
fa_results = pd.DataFrame({
    'Factor 1 Loadings': loadings[:, 0],
    'Communalities': communalities,
    'Uniquenesses': uniquenesses
}, index=['Item ' + str(i+1) for i in range(df.shape[1])])

# Add the eigenvalues and explained variance to the bottom of the DataFrame
additional_data = pd.DataFrame({
    'Factor 1 Loadings': ['Eigenvalue', 'Proportion Variance', 'Cumulative Variance'],
    'Communalities': [ev[0], ev[0]/sum(ev), ev[0]/sum(ev)],
    'Uniquenesses': ['', '', '']
}, index=['', '', ''])

fa_results = fa_results.append(additional_data)

# Save the DataFrame to an Excel file
excel_file_path = 'E:\\Code\\factor_analysis_table.xlsx'
fa_results.to_excel(excel_file_path, index=True)

# Print out the path to the saved file
print(f"The factor analysis results table has been saved to {excel_file_path}")
