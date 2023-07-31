import numpy as np


def calculate(list):
    # try:
    #     arr = np.array(list).reshape(3, 3)
    # except ValueError:
    #     return "List must contain nine numbers."
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)
    mean_ax_0 = np.mean(arr, axis=0).tolist()
    mean_ax_1 = np.mean(arr, axis=1).tolist()
    mean_flat = np.mean(arr).tolist()

    var_ax_0 = np.var(arr, axis=0).tolist()
    var_ax_1 = np.var(arr, axis=1).tolist()
    var_flat = np.var(arr).tolist()

    std_ax_0 = np.std(arr, axis=0).tolist()
    std_ax_1 = np.std(arr, axis=1).tolist()
    std_flat = np.std(arr).tolist()

    max_ax_0 = np.max(arr, axis=0).tolist()
    max_ax_1 = np.max(arr, axis=1).tolist()
    max_flat = np.max(arr).tolist()

    min_ax_0 = np.min(arr, axis=0).tolist()
    min_ax_1 = np.min(arr, axis=1).tolist()
    min_flat = np.min(arr).tolist()

    sum_ax_0 = np.sum(arr, axis=0).tolist()
    sum_ax_1 = np.sum(arr, axis=1).tolist()
    sum_flat = np.sum(arr).tolist()

    

    return {
        'mean': [mean_ax_0, mean_ax_1, mean_flat],
        'variance': [var_ax_0, var_ax_1, var_flat],
        'standard deviation': [std_ax_0, std_ax_1, std_flat],
        'max': [max_ax_0, max_ax_1, max_flat],
        'min': [min_ax_0, min_ax_1, min_flat],
        'sum': [sum_ax_0, sum_ax_1, sum_flat]
    }


print(calculate([0, 1, 2, 3, 4, 5, 6,]))
