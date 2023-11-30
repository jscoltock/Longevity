# longevity

# Life table data
#Period Life Table, 2020, as used in the 2023 Social Security Trustees Report
life_table = {
    'Male': {
        'Death probability': {
            0: 0.005837, 1: 0.00041, 2: 0.000254, 3: 0.000207, 4: 0.000167, 5: 0.000141, 6: 0.000123, 7: 0.000113, 8: 0.000108, 9: 0.000114,
            10: 0.000127, 11: 0.000146, 12: 0.000174, 13: 0.000228, 14: 0.000312, 15: 0.000435, 16: 0.000604, 17: 0.000814, 18: 0.001051, 19: 0.00125,
            20: 0.001398, 21: 0.001524, 22: 0.001612, 23: 0.001682, 24: 0.001747, 25: 0.001812, 26: 0.001884, 27: 0.001974, 28: 0.00207, 29: 0.002172,
            30: 0.002275, 31: 0.002368, 32: 0.002441, 33: 0.002517, 34: 0.00259, 35: 0.002673, 36: 0.002791, 37: 0.002923, 38: 0.003054, 39: 0.003207,
            40: 0.003333, 41: 0.003464, 42: 0.003587, 43: 0.003735, 44: 0.003911, 45: 0.004137, 46: 0.004452, 47: 0.004823, 48: 0.005214, 49: 0.005594,
            50: 0.005998, 51: 0.0065, 52: 0.007081, 53: 0.007711, 54: 0.008394, 55: 0.009109, 56: 0.009881, 57: 0.010687, 58: 0.011566, 59: 0.012497,
            60: 0.013485, 61: 0.014595, 62: 0.015702, 63: 0.016836, 64: 0.017908, 65: 0.018943, 66: 0.020103, 67: 0.021345, 68: 0.02275, 69: 0.024325,
            70: 0.026137, 71: 0.028125, 72: 0.030438, 73: 0.033249, 74: 0.036975, 75: 0.040633, 76: 0.04471, 77: 0.049152, 78: 0.054265, 79: 0.059658,
            80: 0.065568, 81: 0.07213, 82: 0.079691, 83: 0.088578, 84: 0.098388, 85: 0.109139, 86: 0.120765, 87: 0.133763, 88: 0.14837, 89: 0.164535,
            90: 0.182632, 91: 0.202773, 92: 0.223707, 93: 0.245124, 94: 0.266933, 95: 0.288602, 96: 0.309781, 97: 0.330099, 98: 0.349177, 99: 0.366635, 100: 0.384967
        }
    },
    'Female': {
        'Death probability': {
            0: 0.004907, 1: 0.000316, 2: 0.000196, 3: 0.00016, 4: 0.000129, 5: 0.000109, 6: 0.0001, 7: 0.000096, 8: 0.000092, 9: 0.000089,
            10: 0.000092, 11: 0.000104, 12: 0.000123, 13: 0.000145, 14: 0.000173, 15: 0.00021, 16: 0.000257, 17: 0.000314, 18: 0.000384, 19: 0.00044,
            20: 0.000485, 21: 0.000533, 22: 0.000574, 23: 0.000617, 24: 0.000655, 25: 0.0007, 26: 0.000743, 27: 0.000796, 28: 0.000851, 29: 0.000914,
            30: 0.000976, 31: 0.001041, 32: 0.001118, 33: 0.001186, 34: 0.001241, 35: 0.001306, 36: 0.001386, 37: 0.001472, 38: 0.001549, 39: 0.001637,
            40: 0.001735, 41: 0.00185, 42: 0.00195, 43: 0.002072, 44: 0.002217, 45: 0.002383, 46: 0.002573, 47: 0.002777, 48: 0.002984, 49: 0.00321,
            50: 0.003476, 51: 0.003793, 52: 0.004136, 53: 0.004495, 54: 0.00487, 55: 0.005261, 56: 0.005714, 57: 0.006227, 58: 0.006752, 59: 0.007327,
            60: 0.007926, 61: 0.008544, 62: 0.009173, 63: 0.009841, 64: 0.010529, 65: 0.011265, 66: 0.012069, 67: 0.012988, 68: 0.014032, 69: 0.015217,
            70: 0.016634, 71: 0.018294, 72: 0.020175, 73: 0.022321, 74: 0.02503, 75: 0.027715, 76: 0.030631, 77: 0.0339, 78: 0.037831, 79: 0.042249,
            80: 0.047148, 81: 0.052545, 82: 0.058685, 83: 0.065807, 84: 0.074052, 85: 0.083403, 86: 0.093798, 87: 0.104958, 88: 0.117435, 89: 0.13154,
            90: 0.146985, 91: 0.163592, 92: 0.181562, 93: 0.200724, 94: 0.219958, 95: 0.23946, 96: 0.258975, 97: 0.278225, 98: 0.296912, 99: 0.314727, 100: 0.33361
        }
    }
}

def calculate_survival_probability(life_table, age_from, age_to, gender):
    """
    Calculate the probability of survival based on a life table.

    :param life_table: A dictionary containing the life table data.
    :param age_from: The starting age.
    :param age_to: The ending age.
    :param gender: Gender ('Male' or 'Female').
    :return: The probability of survival from age_from to age_to.
    """
    # Initialize the probability of survival
    survival_probability = 1.0

    # Iterate over each year in the specified range
    for age in range(age_from, age_to):
        # Extract the death probability for the current age and gender
        death_probability = life_table[gender]['Death probability'].get(age, 0)

        # Update the survival probability
        survival_probability *= (1 - death_probability)

    return survival_probability

def estimate_age_at_given_survival_probability(life_table, age_from, gender, survival_probability_threshold):
    """
    Estimate the age at which the survival probability falls below a given threshold.

    :param life_table: A dictionary containing the life table data.
    :param age_from: The starting age.
    :param gender: Gender ('Male' or 'Female').
    :param survival_probability_threshold: The survival probability threshold (e.g., 0.10 for 10%).
    :return: The age at which the survival probability falls below the given threshold.
    """
    # Initialize the cumulative survival probability
    cumulative_survival_probability = 1.0

    # Iterate over each year starting from age_from
    for age in range(age_from, 101):  # Assuming the table goes up to age 100
        # Extract the death probability for the current age and gender
        death_probability = life_table[gender]['Death probability'].get(age, 0)

        # Update the cumulative survival probability
        cumulative_survival_probability *= (1 - death_probability)

        # Check if the cumulative survival probability falls below the threshold
        if cumulative_survival_probability < survival_probability_threshold:
            return age

    return 100  # Return 100 if the threshold is never reached

def probability_of_either_surviving(life_table, age_from_male, age_from_female, age_to):
    """
    Calculate the probability of either member of a couple surviving to a certain age.

    :param life_table: A dictionary containing the life table data.
    :param age_from_male: The current age of the male.
    :param age_from_female: The current age of the female.
    :param age_to: The target age to survive to.
    :return: Probability of at least one surviving to the specified age.
    """
    def calculate_survival_probability(age_from, gender):
        # Initialize the cumulative survival probability
        cumulative_survival_probability = 1.0

        # Iterate over each year starting from age_from
        for age in range(age_from, age_to):
            # Extract the death probability for the current age and gender
            death_probability = life_table[gender]['Death probability'].get(age, 0)

            # Update the cumulative survival probability
            cumulative_survival_probability *= (1 - death_probability)

        return cumulative_survival_probability

    # Calculate survival probabilities for each individual
    male_survival = calculate_survival_probability(age_from_male, 'Male')
    female_survival = calculate_survival_probability(age_from_female, 'Female')

    # Calculate the probability of both dying before the age
    both_die_before_age = (1 - male_survival) * (1 - female_survival)

    # Calculate the probability of at least one surviving
    at_least_one_survives = 1 - both_die_before_age

    return at_least_one_survives

# Example usage
# probability = probability_of_either_surviving(life_table, 73, 62, 95)
# print(f"Probability of at least one surviving to age 95: {probability:.2%}")


# # Example usage
estimated_age = estimate_age_at_given_survival_probability(life_table, 73, 'Male', 0.10)
print(f"Estimated age at which 73 year old male survival probability falls below 10%: {estimated_age}")

# estimated_age = estimate_age_at_given_survival_probability(life_table, 72, 'Male', 0.05)
# print(f"Estimated age at which Male survival probability falls below 5%: {estimated_age}")

# estimated_age = estimate_age_at_given_survival_probability(life_table, 72, 'Female', 0.10)
# print(f"Estimated age at which Female survival probability falls below 10%: {estimated_age}")

# estimated_age = estimate_age_at_given_survival_probability(life_table, 72, 'Female', 0.05)
# print(f"Estimated age at which Female survival probability falls below 5%: {estimated_age}")

# estimated_age = estimate_age_at_given_survival_probability(life_table, 72, 'Male', 0.90)
# print(f"Estimated age at which Male survival probability falls below 90%: {estimated_age}")

# estimated_age = estimate_age_at_given_survival_probability(life_table, 72, 'Male', 0.50)
# print(f"Estimated age at which Male survival probability falls below 50%: {estimated_age}")
 
# Example usage
probability = calculate_survival_probability(life_table, 73, 93, 'Male')
print(f"Probability of 73 year old male living to 93: {probability:.2%}")

# probability = calculate_survival_probability(life_table, 62, 95, 'Female')
# print(f"Probability of survival 62-95 Female: {probability:.2%}")

# probability = calculate_survival_probability(life_table, 73, 86, 'Male')
# print(f"Probability of survival 73-86 Male: {probability:.2%}")