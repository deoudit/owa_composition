def best_optimized_values():
    import sys
    import time
    from data import dataset
    # from owa_optimized_values import optimized_values_of_owa
    # from yager_owa_optimized_values import optimized_values_of_yager_owa
    from owa_and_yager_owa_optimized_values import optimized_values_of_owa_and_yager
    from me_owa_optimized_values import optimized_values_of_me_owa
    from owa_optimal_solution import OWAOptimalSolution
    from yager_owa_optimal_solution import YagerOWAOptimalSolution

    data_instances = dataset()

    # Dispatch table to map user input to functions
    function_map = {
        "O": optimized_values_of_owa_and_yager,
        "Y": optimized_values_of_owa_and_yager,
        "M": optimized_values_of_me_owa
    }

    # Get user input
    user_input = input("Enter O(OWA), Y(Yager), or M(MeOWA): \n").strip().upper()

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

    # Call the appropriate function based on input
    if user_input in function_map:
        if user_input == 'O':
            function_map[user_input](data_instance[0], OWAOptimalSolution)
        elif user_input == 'Y':
            function_map[user_input](data_instance[0], YagerOWAOptimalSolution)
        else:
            function_map[user_input](data_instance[0])
        # print(result)
    else:
        print("Invalid input. Please choose O, Y, or M.")

    # End time
    end_time = time.perf_counter()

    # Calculate runtime
    runtime = end_time - start_time
    print(f"Program runtime: {runtime:.6f} seconds")

    return user_input

best_optimized_values()
