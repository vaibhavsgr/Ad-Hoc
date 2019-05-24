import re

if __name__ == "__main__":
    print ("Enter the string")
    st = raw_input()
    print ("Enter the pattern to be searched in the string")
    pattern = raw_input()

    m = re.search(pattern, st)
    print m
