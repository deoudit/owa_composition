from itertools import islice


def dataset():
    start_line = 1
    lines_to_read = 2
    with open('raw_data.dat', 'r') as file:
        selected_lines = list(islice(file, start_line - 1, start_line - 1 + lines_to_read))
        num_data_instances = int(selected_lines[0])
        m_vector = list(map(int, selected_lines[1].split()))
        data_instances = []
        for instance_index, m_row in zip(range(num_data_instances), m_vector):
            file.seek(0)
            start_line += lines_to_read
            lines_to_read = 7 + m_row
            selected_lines = list(islice(file, start_line - 1, start_line - 1 + lines_to_read))
            selected_lines = [line.strip() for line in selected_lines]
            b_low = list(map(float, selected_lines[1].split()))
            b_high = list(map(float, selected_lines[2].split()))
            cost = list(map(float, selected_lines[3].split()))
            a_matrix = []
            for row in range(m_row):
                a_matrix.append(list(map(float, selected_lines[4+row].split())))
            flag = False if int(selected_lines[4+m_row]) == 0 else True
            a_min, b_min, a_max, b_max = map(float, selected_lines[5+m_row].split())
            alpha_min, alpha_max = map(float, selected_lines[6+m_row].split())
            data_instances.append([b_low, b_high, cost, a_matrix, flag, a_min, b_min, a_max, b_max, alpha_min, alpha_max])
        file.close()

    return data_instances
