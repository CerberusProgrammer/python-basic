l = ["Manzana", "Fresa", "Kiwi"]
l.append("Naranja")
l.insert(1, "Zanahoria")
l.remove("Fresa")
print(len(l))
print(l)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist.clear()