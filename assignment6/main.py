from fac_fib import factorial, fibonacci
from sort import bubble_sort, insertion_sort, quick_sort
from timeab import timeit
from student_abstract import HighSchoolStudent

def use_factorial_fibonacci():
    print("Factorial of 5:", factorial(5))  # Output: 120
    print("Fibonacci series of first 6 numbers:", fibonacci(6))  # Output: [0, 1, 1, 2, 3, 5]

@timeit
def use_sorting_algorithms():
    arr = [9, 3, 1, 4, 7, 8, 5, 2, 6]
    print("Original array:", arr)
    print("Bubble sort:", bubble_sort(arr.copy()))
    print("Insertion sort:", insertion_sort(arr.copy()))
    print("Quick sort:", quick_sort(arr.copy()))



def use_abstract_class():
    student = HighSchoolStudent()
    student.study()
    student.write_exams()
    student.attend_class()

if __name__ == "__main__":
    print("\n--- Factorial and Fibonacci ---")
    use_factorial_fibonacci()

    print("\n--- Sorting Algorithms and time ---")
    use_sorting_algorithms()


    print("\n--- Abstract Class Example ---")
    use_abstract_class()
