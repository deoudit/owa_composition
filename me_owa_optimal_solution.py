import math
from scipy.optimize import minimize
from yager_owa_optimal_solution import YagerOWAOptimalSolution


class MeOWAOptimalSolution(YagerOWAOptimalSolution):
    def __init__(self, data_me_owa):
        super().__init__(data_me_owa)
        self.alpha_min = data_me_owa[9]
        self.alpha_max = data_me_owa[10]

    @staticmethod
    def entropy_objective(w_vec):
        """Objective function: -sum(Wj * ln(Wj))."""
        return -sum(w * math.log(w) if w > 0 else 0 for w in w_vec)  # Avoid log(0)

    @staticmethod
    def constraint_alpha(w_vec, alpha, n):
        """Constraint: alpha = sum((n-j)/(n-1) * Wj)."""
        if n == 1:
            return sum(w_vec) - alpha  # Special case: If n=1, alpha must equal W[0].
        weights = [(n - j) / (n - 1) for j in range(1, n + 1)]
        # w_vec = [float(w) for w in w_vec]  # Ensure all elements in W are floats
        return sum(w * Wj for w, Wj in zip(weights, w_vec)) - alpha

    @staticmethod
    def constraint_sum(w):
        """Constraint: sum(Wj) = 1."""
        return sum(w) - 1

    @staticmethod
    def calculate_me_owa_weights(alpha, n):
        """Optimize Wj to maximize entropy under given constraints."""
        if n == 1:
            # Special case: Only one variable
            return [1.0]
            # if alpha == 1.0:
            #     return [1.0]  # Only solution is W[0] = 1
            # else:
            #     raise ValueError("No solution: alpha must be 1 when n = 1.")

        # Initial guess (uniform distribution)
        w0 = [1 / n] * n
        # print(alpha, n)

        # Constraint definitions
        sum_constraint = {"type": "eq", "fun": MeOWAOptimalSolution.constraint_sum}
        alpha_constraint = {"type": "eq", "fun": lambda w: MeOWAOptimalSolution.constraint_alpha(w, alpha, n)}

        # Combine constraints into a list
        constraints = [sum_constraint, alpha_constraint]

        # Bounds: 0 <= Wj <= 1
        bounds = [(0, 1) for _ in range(n)]

        # Solve the optimization problem
        result = minimize(
            fun=MeOWAOptimalSolution.entropy_objective,
            x0=w0,
            constraints=constraints,
            bounds=bounds,
            method="SLSQP"
        )

        if result.success:
            final_weight = result.x
            final_weight = [float(w) for w in final_weight]
            return final_weight  # Optimal W
        else:
            raise ValueError(f"Optimization failed: {result.message}")

    def calculate_max_x(self):
        # weights_min = self.calculate_owa_weights_linguistic(self.a_owa_min, self.b_owa_min, self.m)
        x_hat = []
        for j in range(self.n):
            cap_i_bar = []
            for i in range(self.m):
                if self.a_matrix[i][j] > self.b_high[i]:
                    cap_i_bar.append(self.b_high[i])
            owa_val = 0
            if len(cap_i_bar) > 0:
                cap_i_bar.sort(reverse=True)
                weights_min = self.calculate_me_owa_weights(self.alpha_min, len(cap_i_bar))
                for ind in range(len(cap_i_bar)):
                    owa_val += weights_min[ind] * cap_i_bar[ind]
                x_hat.append(owa_val)
            else:
                x_hat.append(1)
        # print(f"owa - {x_hat}")
        return x_hat

    def calculate_optimal_x(self, i_index_sets_star):
        # weights_max = self.calculate_owa_weights_linguistic(self.a_owa_max, self.b_owa_max, self.m)
        x_optimal = []
        for index in i_index_sets_star:
            b_low_index = []
            for ind in i_index_sets_star[index]:
                if ind != 0:
                    b_low_index.append(self.b_low[ind-1])
                else:
                    b_low_index.append(0.0)
            b_low_index.sort(reverse=True)
            weights_max = self.calculate_me_owa_weights(self.alpha_max, len(b_low_index))
            owa_val = 0.0
            for ind in range(len(b_low_index)):
                owa_val += weights_max[ind] * b_low_index[ind]
            x_optimal.append(round(owa_val, 2))
        return x_optimal
