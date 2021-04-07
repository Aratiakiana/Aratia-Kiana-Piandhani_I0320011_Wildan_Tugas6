print("====== Program Menghitung Nilai Rata-Rata ======")

#menginput banyaknya data
n = int(input("Banyaknya data yang ada yaitu: "))
data=[]
total = 0

for a in range(0, n):
    x = int(input("Masukkan angka ke-%d: " % (a + 1)))
    data.append(x)
    total += data[a]
    rata_rata = total / n
print("Hasil rata-rata dari data keseluruhan yaitu: %0.1f" % rata_rata)