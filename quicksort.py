def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]   
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements in the array "))
    for i in range(n):
        arr.append(int(input()))
    quickSort(arr, 0, n-1)
    print("Elements in the sorted order: ")
    for i in range(n):
        print(str(arr[i]),end=' '),
    print(' ')