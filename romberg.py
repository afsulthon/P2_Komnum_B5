import numpy as np
from tabulate import tabulate

def trapezoidal(f, a, b, n):

    h = (b - a) / n
    x = a

    In = f(a)
    for k in range(1, n):
        x = x + h
        In += 2*f(x)

    return (In + f(b))*h*0.5


def romberg(f, a, b, p):

    I = np.zeros((p, p))
    for k in range(0, p):
        I[k, 0] = trapezoidal(f, a, b, 2**k)

        for j in range(0, k):
            # Romberg formula
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)
    return I

if __name__ == '__main__':
  
    def f(x):
        f = eval(func)
        return f

    func = input("Masukkan fungsi: ")
    p_rows = (int (input("Masukkan jumlah baris: ")))
    upper = (int (input("Masukkan batas atas: ")))
    lower = (int (input("Masukkan batas bawah: ")))

    I = romberg(f, upper, lower, p_rows) 
    solution = I[p_rows-1, p_rows-1]
    solution = round(solution, 4)
    print("Tabel Hasil:")
    print(tabulate(I, tablefmt="fancy_grid"))
    print("Hasil: ", solution)