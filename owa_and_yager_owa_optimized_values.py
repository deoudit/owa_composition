import math
import itertools


def optimized_values_of_owa_and_yager(data_instance_, class_name):
    # Generate values from 0.0 to 1.0 with a step of 0.1
    values = [round(x, 2) for x in [i * 0.1 for i in range(11)]]

    # Generate values from 0.0 to 1.0 with a step of 0.05
    # values = [round(x, 2) for x in [i * 0.05 for i in range(21)]]

    # Generate all possible pairs of values for (a1, b1) and (a2, b2)
    pairs = list(itertools.product(values, repeat=2))

    most_optimized_value = 10.0
    most_optimized_x = [None]
    optimized_range = [None]
    glb_disp1, glb_disp2 = 0.0, 0.0

    # Iterate through all combinations of (a1, b1) and (a2, b2)
    for (a1, b1), (a2, b2) in itertools.product(pairs, repeat=2):
        if b1 == 0.0 or b2 == 0.0 or a1 == b1 or a2 == b2:
            continue

        owa_vals = [a1, b1, a2, b2]
        # print(owa_vals)
        for index in range(len(owa_vals)):
            data_instance_[5+index] = owa_vals[index]

        # Compute the result using the function
        owa_result = class_name(data_instance_)
        result, optimized_x = owa_result.solutions_for_combinations()
        result = round(result, 2)

        #If Inconsistent Solutions or max of optimal_x is below max of b_low
        if result == 0.0 or max(data_instance_[0]) > max(optimized_x):
            continue

        # Creating object without waking up the constructor for static method
        owa_weights = class_name.__new__(class_name)
        # Function Call for dispersion
        dispersion_1 = dispersion_weights(
            owa_weights.calculate_owa_weights_linguistic(a1, b1, len(data_instance_[3])))
        dispersion_2 = dispersion_weights(
            owa_weights.calculate_owa_weights_linguistic(a2, b2, len(data_instance_[3])))

        #Update if better optimized value found
        if result < most_optimized_value:
            most_optimized_value = result
            most_optimized_x = optimized_x
            optimized_range = owa_vals

        # Update if high dispersion found if optimized values are equal
        elif result == most_optimized_value and dispersion_1 > glb_disp1 and dispersion_2 > glb_disp2 and sum(optimized_x) > sum(most_optimized_x):
            most_optimized_value = result
            most_optimized_x = optimized_x
            optimized_range = owa_vals
            glb_disp1 = dispersion_1
            glb_disp2 = dispersion_2

    print(most_optimized_value, most_optimized_x, optimized_range)


def dispersion_weights(weights):
    dispersion = 0.0
    for weight in weights:
        if weight == 0.0:
            continue
        dispersion += weight *  math.log(weight)

    if dispersion == 0.0:
        return dispersion
    return -dispersion
