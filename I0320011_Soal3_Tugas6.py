print("====== Program Pengulangan Bilangan Prima ======")
x = 10
y = 25

for a in range(x,y):
    if a > 1:
        for b in range(2,a):
            if (a % b) == 0:
                print(a, "bukan prima")
                break
        else:
            print(a, "adalah bilangan prima")