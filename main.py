import random
import time


def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]


def save_array_to_file(arr, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(','.join(map(str, arr)))


def main():
    while True:
        try:
            size = int(input("Введите размер массива (больше 1): "))
            if size > 1:
                break
        except ValueError:
            pass
    
    original_array = generate_random_array(size)
    
    input_filename = "unsorted_array.txt"
    save_array_to_file(original_array, input_filename)
    print(f"Исходный массив сохранен в файл: {input_filename}")
    
    sorted_array = original_array.copy()
    
    start_time = time.time()
    quick_sort_inplace(sorted_array, 0, len(sorted_array) - 1)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    output_filename = "sorted_array.txt"
    save_array_to_file(sorted_array, output_filename)
    print(f"Отсортированный массив сохранен в файл: {output_filename}")
    
    print(f"Время сортировки: {execution_time:.6f} секунд")


if __name__ == "__main__":
    main()