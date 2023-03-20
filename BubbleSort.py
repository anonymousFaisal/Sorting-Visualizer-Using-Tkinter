import time


# Bubble sort Algorithm
def bubble_sort(data, drawData, timeTick):
    n = len(data)

    for i in range(n):
        isSorted = True
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                # Change colors when swapped
                drawData(data, ['#e0271d' if x == j else '#16c937' if x == j + 1 else '#010445' if x > n-i-1 else '#ADD8E6' for x in range(len(data))])
                time.sleep(timeTick)
    # Data After completion
    drawData(data, ['#010445' for x in range(len(data))])