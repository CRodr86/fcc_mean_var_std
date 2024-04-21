import numpy as np

def calculate(num_list):
    if len(num_list) != 9:
        raise ValueError("List must contain nine numbers.")
    parsed_matrix = [num_list[:3], num_list[3:6], num_list[6:]]
    
    return {
        'mean': [np.mean(parsed_matrix, axis = 0).tolist(), np.mean(parsed_matrix, axis = 1).tolist(), np.mean(parsed_matrix)],
        'variance': [np.var(parsed_matrix, axis = 0).tolist(), np.var(parsed_matrix, axis = 1).tolist(), np.var(parsed_matrix)],
        'standard deviation': [np.std(parsed_matrix, axis = 0).tolist(), np.std(parsed_matrix, axis = 1).tolist(), np.std(parsed_matrix)],
        'max': [np.max(parsed_matrix, axis = 0).tolist(), np.max(parsed_matrix, axis = 1).tolist(), np.max(parsed_matrix)],
        'min': [np.min(parsed_matrix, axis = 0).tolist(), np.min(parsed_matrix, axis = 1).tolist(), np.min(parsed_matrix)],
        'sum': [np.sum(parsed_matrix, axis = 0).tolist(), np.sum(parsed_matrix, axis = 1).tolist(), np.sum(parsed_matrix)]
    }

print(calculate([0,1,2,3,4,5,6,7,8]))