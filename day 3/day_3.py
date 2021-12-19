import numpy as np

def compute_gamma_epsilon(array):
    """ Computes the binary representation of gamma and epsilon"""
    final_gamma, final_epsilon = "", ""
    for idx in range(len(array[0])):
        ones = 0
        zeros = 0
        for binary in input3:
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

def oxygen_rating(array):
    oxygen = array.copy()
    for idx in range(len(input3[0])):
        counter_ones = [a[idx] for a in oxygen].count('1')
        counter_zeros = [a[idx] for a in oxygen].count('0')
        
        if counter_ones >= counter_zeros:
            o2_to_keep = 1
            co2_to_keep = 0
        else counter_zeros > counter_ones:
            o2_to_keep = 0
            co2_to_keep = 1
        
        to_remove_o2 = []    
        for i,binary in enumerate(oxygen):
            if int(binary[idx]) != o2_to_keep:
                to_remove_o2.append(binary)
        for i in to_remove_o2:
            if len(oxygen) > 1:
                oxygen.remove(i)
    return oxygen[0]

def cO2_rating(array):
    cO2 = array.copy()
    for idx in range(len(input3[0])):
        counter_ones = [a[idx] for a in cO2].count('1')
        counter_zeros = [a[idx] for a in cO2].count('0')
        
        if counter_ones >= counter_zeros:
            o2_to_keep = 1
            co2_to_keep = 0
        else counter_zeros > counter_ones:
            o2_to_keep = 0
            co2_to_keep = 1

        to_remove_co2 = []    
        for j,binary in enumerate(cO2):
            if int(binary[idx]) != co2_to_keep:
                to_remove_co2.append(binary)
        for i in to_remove_co2:
            if len(cO2) > 1:
                cO2.remove(i)
    return cO2[0]

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
    test_O2_rating = oxygen_rating(test_data)
    test_CO2_rating = cO2_rating(test_data)
    print(f'Test result: {int(test_O2_rating,2)*int(test_CO2_rating, 2)}')
    O2_rating = oxygen_rating(input_data)
    CO2_rating = cO2_rating(input_data)
    print(f'Input result: {int(O2_rating,2)*int(CO2_rating, 2)}')
