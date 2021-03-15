def check_duplicates(list_values):
    list_duplicates = []
    list_without = set(list_values)
    for d in list_without:
        count = 0
        for e in list_values:
            if e == d:
                count += 1
        if count >=2:
            list_duplicates.append(d)
    return sorted(list_duplicates)
