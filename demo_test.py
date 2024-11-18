"""
def dataset():
    return data_matrix

data_1 = [
        [.4, .4, .6, .5, .5, .6], [.6, .7, .8, .8, .7, .9], [.5, .6, .6, .8, .4, .7],
        [
            [.6, .5, .7, .8, .4, .5],
            [.7, .4, .9, .5, .8, .6],
            [.9, .7, .4, .6, .7, .8],
            [.6, .7, .8, .7, .6, .9],
            [.7, .6, .8, .9, .5, .6],
            [.8, .9, .6, .5, .7, .8]
        ], True, .0, .2
    ]

data_2 = [
        [.4, .6, .7, .7], [.6, .7, .8, .8], [.6, .7, .5, .2, .4],
        [
          [.5, .3, .7, .8, .3],
          [.7, .4, .9, .5, .8],
          [.8, .5, .4, .9, .7],
          [.9, .6, .5, .4, .9]
        ], False, .0, .2
]

data_matrix = [data_1, data_2]
"""

m = [(0.3, [0.6, 0.5, 0.5, 0.0, 0.5, 0.0]), (0.36, [0.6, 0.6, 0.0, 0.0, 0.5, 0.0])]
print(m[0][0], m[1][0])

# import itertools
#
# # Generate values from 0.0 to 1.0 with a step of 0.1
# values = [round(x, 2) for x in [i * 0.1 for i in range(11)]]
#
# # Generate all combinations of pairs (tuples)
# combinations = list(itertools.product(values, repeat=2))
#
# # Display the result
# print(len(combinations))

# import itertools
# import matplotlib.pyplot as plt
#
# # Define the function that takes four inputs
# def my_function(a1_, b1_, a2_, b2_):
#     # Example function: sum of products
#     return (a1_ * b1_) + (a2_ * b2_)
#
#
# # Generate values from 0.0 to 1.0 with a step of 0.1
# values = [round(x, 2) for x in [i * 0.1 for i in range(11)]]
#
# # Generate all possible pairs of values for (a1, b1) and (a2, b2)
# pairs = list(itertools.product(values, repeat=2))
#
# # Prepare lists to store the data for plotting
# a1_values = []
# b1_values = []
# a2_values = []
# b2_values = []
# results = []
#
# # Iterate through all combinations of (a1, b1) and (a2, b2)
# for (a1, b1), (a2, b2) in itertools.product(pairs, repeat=2):
#     # Compute the result using the function
#     result = my_function(a1, b1, a2, b2)
#
#     # Store the values
#     a1_values.append(a1)
#     b1_values.append(b1)
#     a2_values.append(a2)
#     b2_values.append(b2)
#     results.append(result)
#

# def optimal_2d_path(self):
#     j_matrix = self.calculate_j_index()
#     p_star = []
#     for j_set in j_matrix:
#         j_star = []
#         for index in j_set:
#             j_star.append(self.cost[index-1])
#         j_dash = min(j_star)
#         indices1 = [self.cost.index(j_dash)+1]
#         # index1 = [self.cost.index(j_dash) + 1]
#         # print("****")
#         # print(j_star)
#         j_star.remove(j_dash)
#         # j_star = list(filter(lambda a: a != j_dash, j_star))
#         # print(j_star)
#         # print("****")
#         j_double_dash = min(j_star)
#         indices2 = [self.cost.index(j_double_dash)+1]
#         # index2 = [self.cost.index(j_double_dash) + 1]
#         # p_star.append([index1, index2])
#         for index1 in indices1:
#             for index2 in indices2:
#                 p_star.append((index1, index2))
#     print(p_star)
#    return p_star