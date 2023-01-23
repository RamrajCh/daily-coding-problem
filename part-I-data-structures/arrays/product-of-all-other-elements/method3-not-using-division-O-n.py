def main(S):
    prefix_product = [1 for _ in range(len(S))]
    for i in range(1, len(S)):
        prefix_product[i] = S[i-1] * prefix_product[i-1]

    suffix_product = [1 for _ in range(len(S))]
    for i in range(len(S)-2, -1, -1):
        suffix_product[i] = S[i+1] * suffix_product[i+1]

    product = [prefix_product[i]*suffix_product[i] for i in range(len(S))]
    print(product)
        

if __name__ == "__main__":
    S = [1,2,3,4,5]
    main(S)