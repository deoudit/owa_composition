from itertools import product
# import random


class MaxMinOptimalSolution:
    def __init__(self, data_max_min):
        self.b_low = data_max_min[0]
        self.b_high = data_max_min[1]
        self.cost = data_max_min[2]
        self.a_matrix = data_max_min[3]
        self.m = len(data_max_min[3])
        self.n = len(data_max_min[3][0])
        self.flag = data_max_min[4]

    def calculate_max_x(self):
        x_hat = []
        for j in range(self.n):
            cap_i_bar = []
            for i in range(self.m):
                if self.a_matrix[i][j] > self.b_high[i]:
                    cap_i_bar.append(self.b_high[i])
            if len(cap_i_bar) > 0:
                x_hat.append(min(cap_i_bar))
            else:
                x_hat.append(1)
        return x_hat

    def calculate_j_index(self):
        x_hat = self.calculate_max_x()
        j_matrix = []
        for i in range(self.m):
            s = set()
            for j in range(self.n):
                if min(self.a_matrix[i][j], x_hat[j]) >= self.b_low[i]:
                    s.add(j+1)
            j_matrix.append(s)
        is_inconsistent = False
        for j_set in j_matrix:
            if len(j_set) < 2:
                is_inconsistent = True
        try:
            if is_inconsistent:
                raise ValueError("Inconsistent Equation: No Solution")
        except ValueError: # uncomment this to print ValueError(as e)
            pass
            # print(e) //uncomment to print error
        return j_matrix, is_inconsistent

    def optimal_2d_path(self):
        j_matrix, is_inconsistent = self.calculate_j_index()
        if is_inconsistent:
            return -1
        p_star_total = []
        for j_set in j_matrix:
            j_star = {}
            for index in j_set:
                j_star[index] = self.cost[index - 1]
            # Find the minimum value
            min_value = min(j_star.values())
            # Get all keys with the minimum value
            min_keys = [key for key, value in j_star.items() if value == min_value]
            if len(min_keys) > 1:
                p_star_total.append([[min_keys[0]], [min_keys[1]]])
            else:
                j_dash = min_keys[0]
                del j_star[min_keys[0]]
                # Find the minimum value
                min_value = min(j_star.values())
                # Get all keys with the minimum value
                min_keys = [key for key, value in j_star.items() if value == min_value]
                p_star_total.append([[j_dash], min_keys])
        # p_star_total = [[[4], [3, 1]], [[5], [3]], [[5], [1, 2]], [[5], [1]]]
        # Generate all possible pairs for each sub-array using product
        all_combinations = [list(product(*subarray)) for subarray in p_star_total]
        # Generate all possible combinations using product of all pairs
        all_possible_combinations = list(product(*all_combinations))
        # Use a set to collect unique combinations
        unique_combinations_p_star = list(set(all_possible_combinations))
        # print("Number of solutions are: {}".format(len(unique_combinations_p_star)))
        return unique_combinations_p_star

    # Controller
    def solutions_for_combinations(self):
        unique_combinations_p_star = self.optimal_2d_path()
        if unique_combinations_p_star == -1:
            return 0.0, [0]
        # if not self.flag:
        #     # Only one Solution
        #     p_star = unique_combinations_p_star[random.randint(0, len(unique_combinations_p_star) - 1)]
        #     i_index_sets_star = self.calculate_i_index_sets(p_star)
        #     x_optimal = self.calculate_optimal_x(i_index_sets_star)
        #     return self.calculate_optimal_value(x_optimal)
        # else:
        # All Solutions
        all_solution_matrix = []
        for p_star in unique_combinations_p_star:
            i_index_sets_star = self.calculate_i_index_sets(p_star)
            x_optimal = self.calculate_optimal_x(i_index_sets_star)
            all_solution_matrix.append(self.calculate_optimal_value(x_optimal))
        min_value = min(item[0] for item in all_solution_matrix)
        all_solution_matrix = [item for item in all_solution_matrix if item[0] == min_value]
        if len(all_solution_matrix) <= 1 or self.flag == False:
            return all_solution_matrix[0]
        else:
            return all_solution_matrix

    def calculate_i_index_sets(self, p_star):
        i_index_sets_star = {key: set() for key in range(1, self.n+1)}
        for index in range(len(p_star)):
            a, b = p_star[index]
            i_index_sets_star[a].add(index + 1)
            i_index_sets_star[b].add(index + 1)
        for ind in range(1, self.m+1):
            if len(i_index_sets_star[ind]) == 0:
                i_index_sets_star[ind].add(0)
        return i_index_sets_star

    def calculate_optimal_x(self, i_index_sets_star):
        x_optimal = []
        for index in i_index_sets_star:
            max_m = 0.0
            for ind in i_index_sets_star[index]:
                if self.b_low[ind-1] > max_m and ind != 0:
                    max_m = self.b_low[ind-1]
            x_optimal.append(round(max_m, 2))
        return x_optimal

    def calculate_optimal_value(self, x_optimal):
        max_val = 0
        for c, x in zip(self.cost, x_optimal):
            max_val = max(max_val, c * x)
        # print(x_optimal)
        # print(max_val)
        return round(max_val,2), x_optimal
