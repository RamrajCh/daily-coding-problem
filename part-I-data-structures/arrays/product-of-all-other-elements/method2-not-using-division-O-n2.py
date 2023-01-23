def main(S):
    product = [1 for _ in range(len(S))]
    for i in range(len(S)):
        for j in range(i):
            product[i] *= S[j]
        for j in range(i+1,len(S)):
            product[i] *= S[j]
    
    print(product)

if __name__ == "__main__":
    S = [1,2,3,4,5]
    main(S)