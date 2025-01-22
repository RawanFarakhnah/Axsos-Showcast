#Insertion Sort 
#Refrence Video
#https://vimeo.com/707506539

#Devid your list to two sectiones {sorted,unsorted} and then 
#you have to take an element from unsorted section and add it
#to  the right place in sorted section 


myList = [3, 1, 5, 6, 7, 4, 8]

def insertion_sort(any_list):
    length = len(any_list) - 1
    for p1 in range(length):
        key = any_list[p1 + 1] #element to be palced 
        p2 = p1 #To start from end of sorted section
        # Shift elements of the sorted section to the right
        while p2 >= 0 and any_list[p2] > key:
            any_list[p2 + 1] = any_list[p2]
            p2 -= 1
        # Insert the key in the correct position
        any_list[p2 + 1] = key
    return any_list
        
print("Insertion Sort")
print(myList)
print(insertion_sort(myList))