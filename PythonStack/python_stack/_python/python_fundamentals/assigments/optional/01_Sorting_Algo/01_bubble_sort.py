# Bubble Sort
#Refrence Video
#(https://vimeo.com/86277799)

myList = [3, 1, 5, 6, 7, 4, 8]

def bubble_sort(any_list):
    n = len(any_list)
    for p1 in range(n - 1):
       for p2 in range(n - 1 - p1):
          if any_list[p2] > any_list[p2 + 1]:
              any_list[p2], any_list[p2 + 1] = any_list[p2 + 1], any_list[p2]              
    return any_list

print("\nUsing Bubble Sort")
print("Original List:", myList)
print("Sorted List:", bubble_sort(myList))