def main(S):
    product = 1
    for s in S:
        product *= s
    
    print([int(product/s) for s in S])
    

if __name__ == "__main__":
    S = [1,2,3,4,5]
    main(S)