from fractions import gcd

def find_gcd(a):
    num1, num2 = a[0], a[1]

    m_gcd = gcd(num1, num2)
    print gcd
    
    for i in range(2,len(a)):
        m_gcd = gcd(m_gcd, a[i])
        
    print m_gcd
    return m_gcd


def minimum_deletion(a):
    """ a= [2,"""
    for item in a:
        a = [x for x in a if x != item]
        

if __name__ == "__main__":
    t = int(raw_input("Enter no of test cases "))
    for i in xrange (t):
        a = []
        n = int(raw_input("Enter the size of testcase "))
        print "Enter elements for testcase"
        for e in xrange (n):
            a.append(raw_input())

        a.sort()
        l_orig = len(a)
        m_gcd = find_gcd(a)
        
        if m_gcd == 1:
            print 0
        else:
            x = minimum_deletion(a)

        print a
