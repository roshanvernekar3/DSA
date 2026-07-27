n = [5, 6, 7, 7, 1, 9, 111, 1,1, 5, 1, 1]
freq_map = {}

for i in range(len(n)):
    if n[i] in freq_map:
        freq_map[n[i]] += 1
    else:
        freq_map[n[i]] = 1
print(freq_map)