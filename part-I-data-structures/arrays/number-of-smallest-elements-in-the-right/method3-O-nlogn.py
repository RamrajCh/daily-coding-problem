import bisect

def main(S):
    res = []
    seen = []
    
    for num in reversed(S):
        i = bisect.bisect_left(seen, num)
        res.append(i)
        bisect.insort(seen, num)
        
    print(list(reversed(res)))

if __name__ == "__main__":
    S= [ 3, 4, 9, 6, 1]
    main(S)