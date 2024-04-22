import insertion_sort as insertion
import selection_sort as selection 
import matplotlib.pyplot as plt 
import random
import time

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
  input_sizes = [100, 500, 1000, 5000, 10000]
  insertion_sort_times = []
  selection_sort_times = []

  for size in input_sizes:
    # Generate random data
    data = generate_random_data(size)

    # Measure execution times for both algorithms
    insertion_sort_time = measure_execution_time(insertion.insertion_sort, data.copy())
    selection_sort_time = measure_execution_time(selection.selection_sort, data.copy())

    insertion_sort_times.append(insertion_sort_time)
    selection_sort_times.append(selection_sort_time)

  # Plot the results
  plt.plot(input_sizes, insertion_sort_times, label="Insertion Sort")
  plt.plot(input_sizes, selection_sort_times, label=" Selection Sort")
  plt.xlabel("Input Size")
  plt.ylabel("Execution Time (seconds)")
  plt.title("Comparison of Sorting Algorithm Execution Times")
  plt.legend()
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()
