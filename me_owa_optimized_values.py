from me_owa_optimal_solution import MeOWAOptimalSolution

def optimized_values_of_me_owa(data_instance_):
    # Generate range of values
    step = 0.01
    a_values = [i * step for i in range(int(1 / step) + 1)]
    b_values = [i * step for i in range(int(1 / step) + 1)]

    # Create all combinations of (a, b)
    combinations = [(a, b) for a in a_values for b in b_values]

    most_optimized_value = 10.0
    most_optimized_x = [None]
    optimized_range = [None]

    # Iterate through all combinations of (a1, b1) and (a2, b2)
    for alpha_pair in combinations:
        alpha_min = alpha_pair[0]
        alpha_max = alpha_pair[1]

        me_owa_vals = [alpha_min, alpha_max]
        # print(owa_vals)
        for index in range(len(me_owa_vals)):
            data_instance_[9+index] = me_owa_vals[index]

        # Compute the result using the function
        me_owa_result = MeOWAOptimalSolution(data_instance_)
        result, optimized_x = me_owa_result.solutions_for_combinations()
        result = round(result, 2)

        #If Inconsistent Solutions or max of optimal_x is below max of b_low
        if result == 0.0 or max(data_instance_[0]) > max(optimized_x):
            continue

        if result < most_optimized_value:
            most_optimized_value = result
            most_optimized_x = optimized_x
            optimized_range = [alpha_min, alpha_max]

    print(most_optimized_value, most_optimized_x, optimized_range)


# if __name__ == '__main__':
#     import sys
#     import time
#     from data import dataset
#
#     data_instances = dataset()
#
#     try:
#         indexes = list(map(int, input("Enter data number for which you want to optimize owa values\n").split()))
#         if (isinstance(indexes, int) and indexes >= 1) or len(indexes) > 1:
#             raise ValueError
#     except ValueError:
#         print("Not a Valid Number")
#         sys.exit()
#
#     data_instance = [data_instances[data_instance_index - 1] for data_instance_index in indexes]
#     data_instance[0][4] = False
#     print(f"{20 * '_*_'}")
#
#     # Start time
#     start_time = time.perf_counter()
#
#     # Function call
#     optimized_values_of_me_owa(data_instance[0])
#
#     # End time
#     end_time = time.perf_counter()
#
#     # Calculate runtime
#     runtime = end_time - start_time
#     print(f"Program runtime: {runtime:.6f} seconds")
