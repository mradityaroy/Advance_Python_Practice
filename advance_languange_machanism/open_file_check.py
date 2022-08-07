L = [10,20,30,40,50,60]

lst_iterator = L.__iter__()

while True:

    try:
        element = lst_iterator.__next__()
    except StopIteration:
        break
    print(element)
