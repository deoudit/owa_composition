def optimized_values_of_yager_owa(data_instance_):
    # Generate values from 0.0 to 1.0 with a step of 0.1
    values = [round(x, 2) for x in [i * 0.1 for i in range(11)]]

    # Generate values from 0.0 to 1.0 with a step of 0.05
    # values = [round(x, 2) for x in [i * 0.05 for i in range(21)]]

    # Generate all possible pairs of values for (a1, b1) and (a2, b2)
    pairs = list(itertools.product(values, repeat=2))

    # Prepare lists to store the data for plotting
    a1_values = []
    b1_values = []
    a2_values = []
    b2_values = []
    results = []

    most_optimized_value = 10.0
    most_optimized_x = [None]
    optimized_range = [None]
    glb_disp1, glb_disp2 = 0.0, 0.0

    # max_disp1 = 0.0
    # disp_owa_vals1= []

    # For having most_optimized_x with most numbers of vals in optimized_x >= min(data_instance_[0])
    # most_optimized_x_counter = 0

    # Iterate through all combinations of (a1, b1) and (a2, b2)
    for (a1, b1), (a2, b2) in itertools.product(pairs, repeat=2):
        if b1 == 0.0 or b2 == 0.0 or a1 >= b1 or a2 >= b2:
            continue

        owa_vals = [a1, b1, a2, b2]
        # print(owa_vals)
        for index in range(len(owa_vals)):
            data_instance_[5+index] = owa_vals[index]

        # Compute the result using the function
        yager_owa_result = YagerOWAOptimalSolution(data_instance_)
        result, optimized_x = yager_owa_result.solutions_for_combinations()
        result = round(result, 2)

        # Debugging
        # if owa_vals == [.0, .2, .0, .2]:
        #     print(f"{10 * '-'}")
        #     print(result, optimized_x)
        #     print(f"{10 * '-'}")

        #If Inconsistent Solutions or max of optimal_x is below max of b_low
        if result == 0.0 or max(data_instance_[0]) > max(optimized_x):
            continue

        # Creating object without waking up the constructor for static method
        owa_weights = YagerOWAOptimalSolution.__new__(YagerOWAOptimalSolution)
        # Function Call for dispersion
        dispersion_1 = dispersion_weights(
            owa_weights.calculate_yager_owa_weights(a1, b1, len(data_instance_[3])))
        dispersion_2 = dispersion_weights(
            owa_weights.calculate_yager_owa_weights(a2, b2, len(data_instance_[3])))


        if result==0.3:
            print(optimized_x, owa_vals)

        # if dispersion_1 > max_disp1:
        #     max_disp1 = dispersion_1
        #     disp_owa_vals1 = [a1, b1]
        # optimized_x_counter = len([val for val in optimized_x if val >= min(data_instance_[0])])

        # Debugging
        # if result == 0.3:
        #     print(result, optimized_x, [a1, b1, a2, b2])
        #     print(f"{20*'*'}")

        # Print where dispersion values are 0.0
        # if dispersion_1 == 0.0 and dispersion_2 == 0.0 and result == 0.42:
        #     print("Dispersion zero {}".format([a1, b1, a2, b2]))

        #Update if better optimized value found
        if result < most_optimized_value:
            most_optimized_value = result
            most_optimized_x = optimized_x
            optimized_range = [a1, b1, a2, b2]
        # Update if high dispersion found if optimized values are equal
        elif result == most_optimized_value and dispersion_1 > glb_disp1 and dispersion_2 > glb_disp2 and sum(optimized_x) > sum(most_optimized_x):
            most_optimized_value = result
            most_optimized_x = optimized_x
            optimized_range = [a1, b1, a2, b2]
            glb_disp1 = dispersion_1
            glb_disp2 = dispersion_2
            # print(glb_disp1, glb_disp2)
            # almost same as dispersion "and optimized_x_counter >= most_optimized_x_counter" and
            # "and sum(optimized_x) > sum(most_optimized_x)"
            # most_optimized_x_counter = optimized_x_counter

        # Store the values
        a1_values.append(a1)
        b1_values.append(b1)
        a2_values.append(a2)
        b2_values.append(b2)
        results.append(result)

    # print(f"High dispersion co-ordinates are {disp_owa_vals1} with dispersion {max_disp1}")

    print(most_optimized_value, most_optimized_x, optimized_range)

    return a1_values, b1_values, a2_values, b2_values, results


def dispersion_weights(weights):
    dispersion = 0.0
    for weight in weights:
        if weight == 0.0:
            continue
        dispersion += weight *  math.log(weight)

    if dispersion == 0.0:
        return dispersion
    return -dispersion


if __name__ == '__main__':
    import sys
    import time
    import itertools
    import math
    from data import dataset
    from yager_owa_optimal_solution import YagerOWAOptimalSolution

    data_instances = dataset()

    try:
        indexes = list(map(int, input("Enter data number for which you want to optimize owa values\n").split()))
        if (isinstance(indexes, int) and indexes >= 1) or len(indexes) > 1:
            raise ValueError
    except ValueError:
        print("Not a Valid Number")
        sys.exit()

    data_instance = [data_instances[data_instance_index - 1] for data_instance_index in indexes]
    data_instance[0][4] = False
    print(f"{20 * '_*_'}")

    # Start time
    start_time = time.perf_counter()

    # Function call
    optimized_values_of_yager_owa(data_instance[0])

    # End time
    end_time = time.perf_counter()

    # Calculate runtime
    runtime = end_time - start_time
    print(f"Program runtime: {runtime:.6f} seconds")
