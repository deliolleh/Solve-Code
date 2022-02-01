A = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
sum = 0

A_map = list(map(lambda x: ord('E') - ord(x), A))

for i in range(len(A_map)):
    sum += A_map[i]

print(sum)