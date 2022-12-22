import math
import numpy as np
import sympy as sy
from tabulate import tabulate


def trapezoid(f, a, b, n):
    """
    f: fungsi yang akan diintegrasi
    a: batas bawah integrasi
    b: batas atas integrasi
    n: jumlah subinterval
    """
    h = (b - a) / n  # lebar subinterval
    sum = 0.5 * (f(a) + f(b))  # inisiasi nilai awal
    for i in range(1, n):
        sum += f(a + i * h)  # penjumlahan nilai fungsi
    return sum * h  # mengembalikan nilai integral


def romberg(f, a, b, max_row):
    """
    f: fungsi yang akan diintegrasi
    a: batas bawah integrasi
    b: batas atas integrasi
    max_row: jumlah baris maksimal
    """
    matrix = np.zeros((max_row, max_row))  # membuat matriks nol
    for row in range(max_row):  # perulangan untuk setiap baris
        n = 2**row  # jumlah subinterval
        matrix[row, 0] = trapezoid(f, a, b, n)  # nilai integral untuk kolom pertama
        for col in range(1, row + 1):
            # nilai integral untuk kolom selanjutnya (dengan rumus Romberg)
            matrix[row, col] = (
                4**col * matrix[row, col - 1] - matrix[row - 1, col - 1]
            ) / (4**col - 1)
    return matrix  # mengembalikan matriks nilai integral


# main program
function = input("Masukkan fungsi yang diinginkan (gunakan variabel x):\nf(x) = ")
f = lambda x: eval(function)
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
max_row = int(input("Masukkan jumlah baris maksimal: "))

result = romberg(f, a, b, max_row)

print("\nIntegrasi Romberg f(x) = {} dari {} hingga {} adalah:".format(function, a, b))
print(tabulate(result))
print("Hasil integrasi Romberg:", round(result[max_row - 1, max_row - 1], 4))
print("Hasil integrasi Trapezodial 20 pias:", round(trapezoid(f, a, b, 20), 4))
x = sy.Symbol("x")
print("Hasil integrasi general:", round(sy.integrate(function, (x, a, b)), 4))
