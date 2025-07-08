#801420902
import cmath
# Task 1: implementing horners rule 
def hornersRule(inputFile):
    # we read the input file and get coefficients of polynomial from it
    # the map function converts the string into float and then we convert it into complex
    # a is the list of coefficients
    with open(inputFile, 'r') as f:
        lines = f.readlines()
        a = []
        for line in lines:
            listCoef = list(map(float, line.strip().split()))
            if len(listCoef) == 2:  #
                a.append(complex(listCoef[0], listCoef[1]))
            else:  # Only real part is provided, imaginary part is 0
                a.append(complex(listCoef[0], 0.0))
    
    alen = len(a)  #It is the size of list of coefficients
    W = cmath.exp((2j * cmath.pi / alen))

#horners rule
    output = []
    for k in range(alen): 
        yk = a[-1]  #highest degree coeff first
        for j in range(alen - 2, -1, -1): 
            yk = yk * (W ** k) + a[j]  #summation ajWn^(kj) from 0 to n-1
        output.append(f"{yk.real:.3f} {yk.imag:.3f}")
    
    # Write the result to an output file
    outputFile = "Output_" + inputFile
    with open(outputFile, "w") as f:
        f.write('\n'.join(output))
    
    print(f"results written to {outputFile}")

# Task 2A: FFT
def paddingTwo(a): #we pad the input with 0s to nearest power of 2 so the fft gives more accurate output of the transforms
    nextTwo = 1
    while nextTwo < len(a):
        nextTwo *= 2
    return a + [0] * (nextTwo - len(a))

def FFT(a, n, sign):#as per pseudocode given in the description, we take in the coeffs, its size and sign
    if n == 1:
        return a #this is the base case
    elif sign == 1:
        Wn = cmath.exp( (2j * cmath.pi / n)) #for fft
    elif sign == -1: #it is used for inverse fft
        Wn = cmath.exp( (-2j * cmath.pi / n))

    W = 1
    aeven = a[0::2] #coefficients of even powers
    aodd = a[1::2] #coefficients of odd powers

    yeven = FFT(aeven, n // 2, sign) #it calls fft recursively on even parts
    yodd = FFT(aodd, n // 2, sign)# does the same for odd parts
    y = [0] * n #initializing the output array

    for k in range(n // 2):
        y[k] = yeven[k] + W * yodd[k]
        y[k + n // 2] = yeven[k] - W * yodd[k]
        W = W * Wn

    return y

def Task2A(inputFile): #pads the input and computes fft
    a = complexInput(inputFile)
    
    aPadded = paddingTwo(a)
    nPadded = len(aPadded)

    # Compute FFT
    result = FFT(aPadded, nPadded, 1) #sign is +ve for fft

    # Writing the output in file
    outputFile = "Task2A_Output_" + inputFile
    complexOutput(outputFile, result)
    
    print(f"results in {outputFile}")

# Task 2B: IFFT
def IFFT(a, n):
    
    result = FFT(a, n, -1)#call it with -1 for ifft
    
    # Normalize by dividing each element by n
    for i in range(len(result)):
        result[i] = result[i] / n
    
    return result

def Task2B(inputFile):#pads the input and computes  ifft
    a = complexInput(inputFile)

    aPadded = paddingTwo(a)
    nPadded = len(aPadded)

    result = IFFT(aPadded, nPadded)

    # Writing the output to a file
    outputFile = "Task2B_Output_" + inputFile
    complexOutput(outputFile, result)

    print(f"IFFT results written to {outputFile}")

# Task 3: Polynomial Multiplication
def multiPolynomial(a, b):
    #according to project description we need to multiply two ffts and then we take inverse fft of it
    #for fft, we pad the 2 polynomials first
    n = max(len(a), len(b))
    aPadded = paddingTwo(a + [0] * n)
    bPadded = paddingTwo(b + [0] * n)
    nPadded = len(aPadded)

    # Performing FFT on both padded polynomials
    Afft = FFT(aPadded, nPadded, sign=1)
    Bfft = FFT(bPadded, nPadded, sign=1)

    # Multiplying the FFTs
    Cfft = []
    for i in range(nPadded):
        Cfft.append(Afft[i] * Bfft[i])

    # Perform the inverse FFT
    result = IFFT(Cfft, nPadded)

    return result

def Task3(inputFile1, inputFile2):
    a = complexInput(inputFile1)
    b = complexInput(inputFile2)

    # Checking if both polynomials are non-empty
    if len(a) == 0 or len(b) == 0:
        raise ValueError("Error: Input polynomials cannot be empty.")
    
    # Multiplying the two polynomials
    result = multiPolynomial(a, b)

    # Output result to a file
    outputFile = f"Task3_Output_{inputFile1}_{inputFile2}"
    complexOutput(outputFile, result)

    print(f"result written to {outputFile}")

# input output for both real and imaginary bits
def complexInput(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 1:
                real = float(parts[0])
                result.append(complex(real, 0.0))
            elif len(parts) == 2:
                real = float(parts[0])
                imag = float(parts[1])
                result.append(complex(real, imag))
    return result

def complexOutput(filename, data):
    with open(filename, "w") as file:
        for r in data:
            file.write(f"{r.real:.3f} {r.imag:.3f}\n")


def main():
    
    print("Horners Rule\n")
    fname = input("Insert file\n")
    hornersRule(fname)

    print("FFT\n")
    fname = input("Insert file\n")
    Task2A(fname)

    print("IFFT\n")
    fname = input("Insert file\n ")
    Task2B(fname)

    print("Polynomial Multiplication\n")
    fname1 = input("Insert file1\n")
    fname2 = input("Insert file2\n")
    Task3(fname1, fname2)

if __name__ == "__main__":
    main()

