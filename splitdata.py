import pandas as pd

# Read the falling patterns dataset
falling_patterns = pd.read_csv('data/falling_patterns.csv')

# Add a column for the type (0 for falling patterns)
falling_patterns['type'] = 0

# Read the rising patterns dataset
rising_patterns = pd.read_csv('data/rising_patterns.csv')

# Add a column for the type (1 for rising patterns)
rising_patterns['type'] = 1

# Concatenate the falling and rising patterns into a single dataset
combined_patterns = pd.concat([falling_patterns, rising_patterns])

# Reset the index of the combined dataset
combined_patterns = combined_patterns.reset_index(drop=True)

# Save the transformed data to a new file
combined_patterns.to_csv('data/combined_patterns.csv', index=False)

