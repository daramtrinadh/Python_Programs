sample_set = {1, 2, 3, 4, 5, "apple", "banana", "orange"}
min_len=str(next(iter(sample_set)))
max_len=min_len
for i in sample_set:
    if len(str(i))< len(str(min_len)):
        min_len=i
    elif len(str(i))>len(str(max_len)):
        max_len=i
print(f"Mininmum length value <{min_len}>:",len(str(min_len)))
print(f"Maximum length value <{max_len}>:",len(str(max_len)))


