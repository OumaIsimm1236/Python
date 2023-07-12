#ex1

result = 1 + 1
print(result)
#ex2

sequence = 'A' * 20
print(sequence)
#ex3

sequence = 'A' * 20 + 'GC' * 20
print(sequence)
#ex4

a = "salut"
b = 102
c = 10.318
print("a: {}, b: {}, c: {:.2f}".format(a, b, c))
#ex5

perc_GC = ((4500 + 2575) / 14800) * 100
# Affichage avec 0 décimale
print("1 Le pourcentage de GC est {:.0f} %".format(perc_GC))

# Affichage avec 1 décimale
print("2 Le pourcentage de GC est {:.1f} %".format(perc_GC))

# Affichage avec 2 décimales
print("3 Le pourcentage de GC est {:.2f} %".format(perc_GC))

# Affichage avec 3 décimales
print("4 Le pourcentage de GC est {:.3f} %".format(perc_GC))
