# P2_Komnum_B5

**Praktikum 2 Komputasi Numerik**  
**Kelas Komputasi Numerik (B)**

**Kelompok 5**

1. Akmal Sulthon Fathulloh (5025211047)
2. Thariq Agfi Hermawan (5025211215)
3. Tigo S Yoga (5025211125)

## Soal

Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut.

## Penjelasan

Metode integrasi Trapezoidal adalah salah satu metode numerik untuk menghitung aproksimasi nilai integral suatu fungsi dengan cara membagi domain integral menjadi sejumlah bagian kecil, kemudian menggunakan bentuk trapesium untuk menghitung setiap luasan partisi tersebut. Nilai integral diperoleh dengan menjumlahkan luas dari setiap trapesium yang dibentuk.

Secara umum, rumus integrasi Trapezoidal adalah sebagai berikut:

$$
∫ f(x) dx ≈ \frac{h}{2} \left[f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n) \right]
$$

dimana:  
`h` adalah panjang interval, dihitung sebagai $(x_n - x_0)/n%$ dengan `n` adalah jumlah subinterval.

Implementasi dalam bahasa Python:

```python
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum += f(a + i * h)
    return sum * h
```

Metode ini hanya menggunakan dua titik di setiap subintervalnya untuk menghitung luasan. Hal ini dapat menyebabkan hasil yang kurang akurat jika fungsi yang diintegrasikan memiliki bentuk yang kompleks dan tajam. Untuk meningkatkan akurasi dari metode Trapezoidal, dapat diterapkan metode yang disebut integrasi Romberg. Metode ini didasarkan pada teknik ekstrapolasi Richardson yang melibatkan perhitungan sejumlah aproksimasi integral dengan jumlah titik penyampling berbeda, kemudian menggunakan hasilnya untuk menghitung nilai integral yang lebih akurat. Perlu diperhatikan bahwa setiap penerapan ekstrapolasi Richardson akan menaikkan orde galat pada hasilnya sebesar dua.

Secara umum, rumus integrasi Romberg dengan ekstrapolasi Richardson adalah sebagai berikut:

$$
R_{j,k} = {4^kR_{j,k-1} - R_{j-1,k-1} \over 4^k -1}
$$

untuk $2<=k<=j$, dengan nilai awal ($R_{j,1}$) adalah hasil integrasi Trapezoidal.

Berikut adalah langkah penyelesaian integrasi dengan metode Romberg:

1. Menentukan fungsi yang akan diintegrasi
2. Menentukan batas bawah dan batas atas
3. Menentukan jumlah baris maksimum yang akan digunakan
4. Menghitung nilai integrasi kolom pertama menggunakan metode Trapezoidal dengan jumlah subinterval (`n`) $2^i$ dimana $i=0,1,2,\dots$
5. Menghitung nilai integrasi kolom kedua dan seterusnya dengan metode ekstrapolasi Richardson
6. Mengulangi langkah 4 dan 5 hingga nilai integrasi yang diinginkan diperoleh (disesuaikan dengan jumlah baris maksimum)

Implementasi dalam bahasa Python:

```python
def romberg(f, a, b, max_row):
    matrix = np.zeros((max_row, max_row))
    for row in range(max_row):
        n = 2**row
        matrix[row, 0] = trapezoid(f, a, b, n)
        for col in range(1, row + 1):
            matrix[row, col] = (
                4**col * matrix[row, col - 1] - matrix[row - 1, col - 1]
            ) / (4**col - 1)
    return matrix
```

## Hasil Implementasi

Input:

```
Masukkan fungsi yang diinginkan (gunakan variabel x):
f(x) = np.sin(x)**2 + 2*x**3 + 2
Masukkan batas bawah: 1
Masukkan batas atas: 5
Masukkan jumlah baris maksimal: 5
```

Output:

```
Integrasi Romberg f(x) = np.sin(x)**2 + 2*x**3 + 2 dari 1.0 hingga 5.0 adalah:
-------  -------  -------  -------  -------
515.255    0        0        0        0
369.667  321.138    0        0        0
334.233  322.422  322.507    0        0
325.333  322.366  322.362  322.36     0
323.106  322.363  322.363  322.363  322.363
-------  -------  -------  -------  -------
Hasil integrasi Romberg: 322.3634
```

## Prerequisites

Program ini dijalankan menggunakan [Python](https://www.python.org/) 3.11.1.
Berikut adalah daftar library yang digunakan:

1. [NumPy](https://numpy.org/)
2. [SymPy](https://www.sympy.org/en/index.html)
3. [Tabulate](https://pypi.org/project/tabulate/)
4. [SciPy](https://www.scipy.org/)

Untuk memasang library-library tersebut, jalankan perintah berikut:

```bash
python -m pip install -r requirements.txt
```

## Referensi

1. [Romberg Integration](https://en.wikipedia.org/wiki/Romberg%27s_method)
2. [Trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
3. [Integrasi Numerik (Bag. 2) - Rinaldi Munir IF-STEI ITB](<https://informatika.stei.itb.ac.id/~rinaldi.munir/MetNum/2010-2011/Integrasi%20Numerik%20(Bagian%202).pdf>)
