import streamlit as st
# Import your longevity script here if it's in a different file
from longevity import calculate_survival_probability, estimate_age_at_given_survival_probability, probability_of_either_surviving

# Streamlit app title
st.title('Life Expectancy and Survival Probability Calculator')

# Sidebar for input parameters
st.sidebar.header('User Input Parameters')

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

# Function to get user input
def user_input_features():
    current_age = st.sidebar.slider('Current Age', 0, 100, 25)
    target_age = st.sidebar.slider('Target Age', 0, 100, 75)
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    survival_probability = st.sidebar.slider('Survival Probability Threshold', 0.0, 1.0, 0.1)
    return current_age, target_age, gender, survival_probability

current_age, target_age, gender, survival_probability = user_input_features()

# Calculating survival probability
if st.button('Calculate Survival Probability'):
    survival_prob = calculate_survival_probability(life_table, current_age, target_age, gender)
    st.write(f'The survival probability from age {current_age} to {target_age} is {survival_prob:.2%}')

# Estimating age at given survival probability
if st.button('Estimate Age at Given Survival Probability'):
    estimated_age = estimate_age_at_given_survival_probability(life_table, current_age, gender, survival_probability)
    st.write(f'Estimated age at which survival probability falls below {survival_probability:.2%}: {estimated_age}')

# Probability of either surviving in a pair
# if st.button('Probability of Either in a Pair Surviving'):
#     male_age = st.sidebar.slider('Male Age', 0, 100, 25)
#     female_age = st.sidebar.slider('Female Age', 0, 100, 25)
#     either_survive_prob = probability_of_either_surviving(life_table, male_age, female_age, target_age)
#     st.write(f'Probability of at least one surviving to age {target_age}: {either_survive_prob:.2%}')
