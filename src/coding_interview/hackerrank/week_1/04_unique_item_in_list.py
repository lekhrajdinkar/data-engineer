

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    tracker :dict = {}
    for i in a:
        tracker[i] = 1 if i not in tracker else tracker[i]+1
    print(tracker)

    for key in tracker.keys():
        if tracker[key] == 1:
            return key

if __name__ == '__main__':
    result = lonelyinteger(list([1,1,2,2,3]))
    print(result)

