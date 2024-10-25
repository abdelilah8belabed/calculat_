

import numpy as np
def calculat():
    numbers = []
    #for i in range(9):
     #   num = int(input(f'give me the {i+1} number ' ))
      #  numbers.append(num)
    def get_nuumbers():
        while True:
            numbers = input('enter nine numbers : ').split()
            numbers = [int(number) for number in numbers]
            if len(numbers) > 9:
                print('you give too many numbers  ')
            elif len(numbers) < 9:
                print('you need 9 numbers to get matrix of 3*3 ')
            else:
                print("now we can calculate the mean , variance , std , max , min")
                return numbers

    numbers = get_nuumbers()
    print(numbers)

    rows = [ numbers[i:i + 3] for i in range(0 , len(numbers),3)]

    arr = np.array(rows)
    print(arr)

    mean_axis0 = np.mean(arr, axis=0)
    mean_axis1 = np.mean(arr, axis=1)
    mean_flat = np.mean(arr)

    variance_axis0 = np.var(arr, axis=0)
    variance_axis1 = np.var(arr, axis=1)
    variance_flat = np.var(arr)

    std_dev_axis0 = np.std(arr, axis=0)
    std_dev_axis1 = np.std(arr, axis=1)
    std_dev_flat = np.std(arr)

    max_axis0 = np.max(arr, axis=0)
    max_axis1 = np.max(arr, axis=1)
    max_flat = np.max(arr)

    min_axis0 = np.min(arr, axis=0)
    min_axis1 = np.min(arr, axis=1)
    min_flat = np.min(arr)

    sum_axis0 = np.sum(arr, axis=0)
    sum_axis1 = np.sum(arr, axis=1)
    sum_flat = np.sum(arr)

    output = {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [variance_axis0, variance_axis1, variance_flat],
        'standard deviation': [std_dev_axis0, std_dev_axis1, std_dev_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }
    import pprint
    pprint.pprint(output)

calculat()
