# 1-m
my_tuple = ("a", "b", "c", "d")
print(my_tuple)
natija = tuple((i, el) for i, el in enumerate(my_tuple))
print(natija)

# 2-m
t = ("apple", "banana", "ok")
print(t)
yangi = tuple(s[::-1] for s in t)

print(yangi)

# 3-m
d = {"a": "1", "b": "2"}
print(d)
yangi = {}
for k, v in d.items():
    yangi[v] = k
print(yangi)

# 4-m
d = {"it": "vov", "mushuk": "miyov", "sigir": "muu"}
hayvon = input("Hayvon kiriting: ")
print(d.get(hayvon, "Bunday hayvon bazada yo‘q"))

# 5-m
def bahola(t):
    natija = []
    for ball in t:
        if ball >= 90:
            natija.append("A")
        elif ball >= 70:
            natija.append("B")
        elif ball >= 50:
            natija.append("C")
        else:
            natija.append("D")
    return natija
print(bahola((95, 67, 40, 82)))

# 6-m
def tasnifla(ismlar):
    natija = []

    for ism in ismlar:
        uzun = len(ism)
        if uzun < 3:
            natija.append("juda qisqa")
        elif uzun <= 5:
            natija.append("normal")
        else:
            natija.append("uzun")

    return natija
print(tasnifla(["Ali", "Doniyor", "Ziyod", "Noz", 'ok']))

