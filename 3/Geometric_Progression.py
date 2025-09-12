def geometricProgression(A, R, Z):
        result  = []

        while (A <= Z):
            result.append(A)

            if A > (Z // R):
                 break
            
            A *= R

        return result

if __name__ == "__main__":
    A = 2
    R = 3
    Z = 100
    print(geometricProgression(A, R, Z))