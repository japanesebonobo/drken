def mul(a, b): 
    return a * b

def main():
    for i in range(9):
        for j in range(9):
            for k in range(9):
                tmp = mul(i + 1, j + 1)
                tmp2 = 2 * (j + 1) * 10
                tmp3 = mul(i + 1, k + 1) * 10
                tmp4 = 2 * (k + 1) * 100
                result = tmp + tmp2
                if len(str(result)) ==3 and str(result)[1] == '3':
                    result += tmp3
                    result += tmp4
                    if len(str(result)) == 3 and str(result)[1] == '4':
                        print(f"{i + 1} , {j + 1} , {k + 1} , {result}")
                        return
                    
if __name__ == "__main__":
    main()
