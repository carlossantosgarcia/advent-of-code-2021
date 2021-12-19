import numpy as np

def compute_gamma_epsilon(array):
    """ Computes the binary representation of gamma and epsilon"""
    final_gamma, final_epsilon = "", ""
    for idx in range(len(array[0])):
        ones = 0
        zeros = 0
        for binary in array:
            if binary[idx] == "1":
                ones += 1
            else:
                zeros += 1
        if ones>zeros:
            final_gamma += "1"
            final_epsilon += "0"
        else:
            final_gamma += "0"
            final_epsilon  += "1"
    return final_gamma, final_epsilon

def compute_rating(array, target):
    """Computes O2 or CO2 rating from the diagnostic report.

    Args:
        array (ndarray): Diagnostic report given as an input
        target (str): Wether O2 or CO2 rating is the target. Supports "CO2" or "O2".

    Returns:
        [str]: Returns binary representation of the wanted target rating
    """
    assert target in ['O2', 'CO2']
    final_array = array.copy()
    for idx in range(len(final_array[0])):
        counter_ones = [a[idx] for a in final_array].count('1')
        counter_zeros = [a[idx] for a in final_array].count('0')
        
        if counter_ones >= counter_zeros:
            O2_to_keep = 1
            CO2_to_keep = 0
        else : 
            O2_to_keep = 0
            CO2_to_keep = 1
        
        target_to_keep = O2_to_keep if target == "O2" else CO2_to_keep
        to_remove = []    
        for i,binary in enumerate(final_array):
            if int(binary[idx]) != target_to_keep:
                to_remove.append(binary)
        for i in to_remove:
            if len(final_array) > 1:
                final_array.remove(i)
    return final_array[0]

if __name__ == "__main__":
    # Loading the data
    test_data = [line.rstrip() for line in open("test_input.txt")]
    input_data = [line.rstrip() for line in open("input.txt")] 

    # Task 1
    # Gamma and epsilon are represented in binary
    test_gamma, test_epsilon = compute_gamma_epsilon(test_data)
    print(f'Test result: {int(test_gamma, 2)*int(test_epsilon, 2)}')
    gamma, epsilon = compute_gamma_epsilon(input_data)
    print(f'Input result: {int(gamma, 2)*int(epsilon, 2)}')

    # Task 2
    test_O2_rating = compute_rating(test_data, 'O2')
    test_CO2_rating = compute_rating(test_data, 'CO2')
    print(f'Test result: {int(test_O2_rating,2)*int(test_CO2_rating, 2)}')
    O2_rating = compute_rating(input_data, 'O2')
    CO2_rating = compute_rating(input_data, 'CO2')
    print(f'Input result: {int(O2_rating,2)*int(CO2_rating, 2)}')
