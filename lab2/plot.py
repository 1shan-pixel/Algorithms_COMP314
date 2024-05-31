import quick_sort as quick 
import merge_sort as merge 
import random
import time
import matplotlib.pyplot as plt 

def generate_random_data(size):
    #returns list of random integers of size 'size'
  return [random.randint(1, 100) for _ in range(size)]

def measure_execution_time(sort_function, data):
  
  start_time = time.time()
  sort_function(data)
  end_time = time.time()

  return end_time - start_time

def main():
  # Define input sizes for plotting
  input_sizes = [1000, 2500, 5000, 10000, 15000,20000,30000]
  quick_sort_times = []
  merge_sort_times = []

  for size in input_sizes:
    # Generate random data
    data = generate_random_data(size)

    # Measure execution times for both algorithms
    quick_sort_time = measure_execution_time(quick.quick_sort, data.copy())
    merge_sort_time = measure_execution_time(merge.merge_sort, data.copy())

    quick_sort_times.append(quick_sort_time)
    merge_sort_times.append(merge_sort_time)

  # Plot the results
  plt.plot(input_sizes, quick_sort_times, label="quick Sort")
  plt.plot(input_sizes, merge_sort_times, label=" merge Sort")
  plt.xlabel("Input Size")
  plt.ylabel("Execution Time (seconds)")
  plt.title("Comparison of Sorting Algorithm Execution Times")
  plt.legend()
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()
