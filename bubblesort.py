def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr
arr = [("ali", 160), ("jawad", 150), ("brahim", 170), ("mhamad", 140)]
sorted_arr = bubblesort(arr)
for i in sorted_arr:
    print("Name: " + i[0] + " Height: " + str(i[1]))
#O(n^2)