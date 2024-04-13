#bubble sort

def bubble_sort(Array):
    n=len(Array)
    for i in range (n):
        for j in range(n-i-1):
            if Array[j]>Array[j+1]:
                Array[j],Array[j+1]=Array[j+1],Array[j]

Array=input().split()
bubble_sort(Array)
print(Array)
