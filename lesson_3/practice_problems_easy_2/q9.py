# Add entries for Marilyn and Spot to the dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

# ages |= additional_ages
ages.update(additional_ages)

print(ages)
# print(additional_ages)