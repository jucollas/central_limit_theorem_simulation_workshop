import numpy as np

def average(arr):
    return np.sum(arr)/len(arr)

def variance(arr):
    sumed = 0
    avg = average(arr)
    for i in range(len(arr)):
        sumed += (arr[i] - avg) ** 2   
    return (1/(len(arr) - 1)) * sumed  

def generate_numbers_normal(avg, var, size):
    return np.random.normal(avg, np.sqrt(var), size)
    




def main():
    len_sample = 35
    avg_expected = 5
    var_expected = 1.2
    random_numbers = generate_numbers_normal(avg_expected, var_expected, len_sample)
    
    print("Sample (len: %d, avg: %f, var: %f)" %(len_sample, avg_expected, var_expected))
    print(*random_numbers)
    
    print("\nCalculate:")
    avg = average(random_numbers)
    var = variance(random_numbers)
    
    print("avg: %f, error abs: %f" %(avg, abs(avg_expected - avg)))
    print("var: %f, error abs: %f" %(var, abs(var_expected - var)))


if __name__ == '__main__':
    main()
