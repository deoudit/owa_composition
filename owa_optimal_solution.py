from main.max_min_optimal_solution import MaxMinOptimalSolution


class OWAOptimalSolution(MaxMinOptimalSolution):
    def __init__(self, data_owa):
        super().__init__(data_owa)
        self.a_owa_min = data_owa[5]
        self.b_owa_min = data_owa[6]
        self.a_owa_max = data_owa[7]
        self.b_owa_max = data_owa[8]

    @staticmethod
    def calculate_owa_weights_linguistic(a_owa, b_owa, n):
        weights_linguistic = []
        # Calculate Q(r) for each i in weights_linguistic
        # n = self.m
        try:
            1 / (b_owa - a_owa)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!")
        for i in range(n+1):
            r = i/n
            if r < a_owa:
                weights_linguistic.append(0.0)
            elif a_owa <= r <= b_owa:
                weights_linguistic.append((r - a_owa) / (b_owa - a_owa))
            else:
                weights_linguistic.append(1.0)
        # Calculate weights
        weights_final = []
        for i in range(1, len(weights_linguistic)):
            weights_final.append(weights_linguistic[i] - weights_linguistic[i-1])
        return weights_final

    def calculate_max_x(self):
        weights = self.calculate_owa_weights_linguistic(self.a_owa_min, self.b_owa_min, self.m)
        x_hat = []
        for j in range(self.n):
            cap_i_bar = []
            for i in range(self.m):
                if self.a_matrix[i][j] > self.b_high[i]:
                    cap_i_bar.append(self.b_high[i])
            owa_val = 0
            if len(cap_i_bar) > 0:
                cap_i_bar.sort(reverse=True)
                for ind in range(len(cap_i_bar)):
                    owa_val += weights[ind] * cap_i_bar[ind]
                x_hat.append(owa_val)
            else:
                x_hat.append(1)
        # print(f"owa - {x_hat}")
        return x_hat

    def calculate_optimal_x(self, i_index_sets_star):
        weights = self.calculate_owa_weights_linguistic(self.a_owa_max, self.b_owa_max, self.m)
        x_optimal = []
        for index in i_index_sets_star:
            b_low_index = []
            for ind in i_index_sets_star[index]:
                if ind != 0:
                    b_low_index.append(self.b_low[ind-1])
                else:
                    b_low_index.append(0.0)
            b_low_index.sort(reverse=True)
            owa_val = 0.0
            for ind in range(len(b_low_index)):
                owa_val += weights[ind] * b_low_index[ind]
            x_optimal.append(round(owa_val, 2))
        return x_optimal
