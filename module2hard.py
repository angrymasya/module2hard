#one_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
results = []
n = int(input("Введите число от 3 до 20: "))
b = 0
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            b = b * 10 + i
            b = b * 10 + j
            #results.append(i)
            #results.append(j)
#result = ''.join(map(str, results))
# #print(result) или
#print(*results, sep='')
print(b)






