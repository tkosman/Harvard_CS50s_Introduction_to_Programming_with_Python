zakupy = {}
while True:
    try:
        produkt = input().upper().strip()
    except EOFError:
        sorted_keys = sorted(zakupy.keys())
        for one in sorted_keys:
            print(zakupy[one], one)

        break
    else:
        if produkt in zakupy:
            zakupy[produkt] += 1
        else:
            zakupy[produkt] = 1