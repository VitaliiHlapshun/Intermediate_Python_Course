numbers = [21,5,98,160,4]

def bubble(numb):
    top = len(numb) - 1
    sorted = False
    while (not sorted):
        sorted = True
        for x in range(0, top):
            if numb[x] > numb[x+1]:
                swap = numb[x]
                numb[x] = numb[x+1]
                numb[x+1] = swap
                sorted = False
    else:
        print(numb)

bubble(numbers)
