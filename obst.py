import

function generateTrees(elem, elem_freq):
    



if __name__ == "main":
    n = raw_input(int(print("Enter no of elements")))
    elem = []
    elem_freq = []
    print ("Enter {} elements for the array".(n))
    for i in xrange(n):
        elem.append(int(raw_input()))
    print ("Enter the frequency of each element")
    for i in xrange(n):
        elem_freq.append(int(raw_input()))


    optCost(elem, elem_freq, n)
