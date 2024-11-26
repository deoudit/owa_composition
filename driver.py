def driver_code():
    data_instances = dataset()

    user_input = input("DO you want to run the Simulator on some particular data? y or n\n")
    if user_input == 'y':
        indexes = list(map(int, input("Enter data numbers which you specifically want\n").split()))
        data_instances = [data_instances[data_instance - 1] for data_instance in indexes]
        print(f"{20 * '_*_'}")
    elif user_input == 'n':
        print(f"{20 * '_*_'}")
    else:
        print("Please enter y or n only.")
        sys.exit()

    # List to store objects
    max_min_vector = []
    owa_vector = []
    # me_owa_vector = []
    # yager_owa_vector = []

    # Start time
    start_time = time.perf_counter()

    # Loop to create multiple objects
    for data_instance in data_instances:
        max_min = MaxMinOptimalSolution(data_instance)
        max_min_vector.append(max_min)
        # yager_owa = YagerOWAOptimalSolution(data_instance)
        # yager_owa_vector.append(yager_owa)
        owa = OWAOptimalSolution(data_instance)
        owa_vector.append(owa)
        # me_owa = MeOWAOptimalSolution(data_instance)
        # me_owa_vector.append(me_owa)

    # Display all objects
    counter = 1
    # for max_min, owa, me_owa in zip(max_min_vector, owa_vector, me_owa_vector):
    for max_min, owa in zip(max_min_vector, owa_vector):
        print(f"Data_{counter}_Solutions")
        print(f"{20 * '-'}")
        print(f"Max_Min_Solution")
        print(max_min.solutions_for_combinations())
        # print(f"{30 * '-'}")
        # print(f"Yager_OWA_Solution")
        # print(yager_owa.solutions_for_combinations())
        print(f"{30 * '-'}")
        print(f"OWA_Solution")
        print(owa.solutions_for_combinations())
        # print(f"{30 * '-'}")
        # print(f"Me_OWA_Solution")
        # print(me_owa.solutions_for_combinations())
        # print(alpha, beta)
        print(f"{20 * '__'}")
        counter += 1
    print(f"{20 * '_*_'}")

    # End time
    end_time = time.perf_counter()

    # Calculate runtime
    runtime = end_time - start_time
    print(f"Program runtime: {runtime:.6f} seconds")


if __name__ == '__main__':
    import sys
    import time
    from max_min_optimal_solution import MaxMinOptimalSolution
    from owa_optimal_solution import OWAOptimalSolution
    # from main.yager_owa_optimal_solution import YagerOWAOptimalSolution
    # from me_owa_optimal_solution import MeOWAOptimalSolution
    from data import dataset

    driver_code()
