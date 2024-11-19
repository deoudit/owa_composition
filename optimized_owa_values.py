def optimized_values_of_owa(data_instance_):
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

    # For having most_optimized_x with most numbers of vals in optimized_x >= min(data_instance_[0])
    # most_optimized_x_counter = 0

    # Iterate through all combinations of (a1, b1) and (a2, b2)
    for (a1, b1), (a2, b2) in itertools.product(pairs, repeat=2):
        if b1 == 0.0 or b2 == 0.0 or a1 == b1 or a2 == b2:
            continue

        owa_vals = [a1, b1, a2, b2]
        # print(owa_vals)
        for index in range(len(owa_vals)):
            data_instance_[5+index] = owa_vals[index]

        # Compute the result using the function
        owa_result = OWAOptimalSolution(data_instance_)
        result, optimized_x = owa_result.solutions_for_combinations()
        result = round(result, 2)

        # Debugging
        # if owa_vals == [.0, .2, .0, .2]:
        #     print(f"{10 * '-'}")
        #     print(result, optimized_x)
        #     print(f"{10 * '-'}")

        #If Inconsistent Solutions or max of optimal_x is below max of b_low
        if result == 0.0 or max(data_instance_[0]) > max(optimized_x):
            continue

        # Function Call for dispersion
        owa_weights = OWAOptimalSolution.__new__(OWAOptimalSolution)
        dispersion_1 = dispersion_weights(
            owa_weights.calculate_owa_weights_linguistic(a1, b1, len(data_instance_[3])))
        dispersion_2 = dispersion_weights(
            owa_weights.calculate_owa_weights_linguistic(a2, b2, len(data_instance_[3])))

        # optimized_x_counter = len([val for val in optimized_x if val >= min(data_instance_[0])])

        # Debugging
        # if result == 0.3:
        #     print(result, optimized_x, [a1, b1, a2, b2])
        #     print(f"{20*'*'}")

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
            # almost same as dispersion "and optimized_x_counter >= most_optimized_x_counter" and
            # "and sum(optimized_x) > sum(most_optimized_x)"
            # most_optimized_x_counter = optimized_x_counter

        # Store the values
        a1_values.append(a1)
        b1_values.append(b1)
        a2_values.append(a2)
        b2_values.append(b2)
        results.append(result)

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


def create_plot(a1_values, b1_values, a2_values, b2_values, results):
    # Create a 3D scatter plot
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(14, 7))

    # Plot for (a1, b1)
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(a1_values, b1_values, results, c='blue', alpha=0.6, label='(a1, b1)')
    ax1.set_xlabel('a1 Values')
    ax1.set_ylabel('b1 Values')
    ax1.set_zlabel('Function Result')
    ax1.set_title('Function Results for (a1, b1)')
    ax1.legend()

    # Plot for (a2, b2)
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.scatter(a2_values, b2_values, results, c='red', alpha=0.6, label='(a2, b2)')
    ax2.set_xlabel('a2 Values')
    ax2.set_ylabel('b2 Values')
    ax2.set_zlabel('Function Result')
    ax2.set_title('Function Results for (a2, b2)')
    ax2.legend()

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    import sys
    import time
    import itertools
    import math
    from data import dataset
    from owa_optimal_solution import OWAOptimalSolution

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
    optimized_values_of_owa(data_instance[0])

    # End time
    end_time = time.perf_counter()

    # Calculate runtime
    runtime = end_time - start_time
    print(f"Program runtime: {runtime:.6f} seconds")
