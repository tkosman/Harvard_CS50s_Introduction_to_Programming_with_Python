months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        data = input("Date: ").strip()
        if data.count("/") == 2:
            M, D, Y = data.split("/")
            if 1 <= int(M) <= 12 and 1 <= int(D) <= 31:
                print(Y, M.zfill(2), D.zfill(2), sep="-")
                break
        elif data.count(",") == 1:
            cos, Y = data.split(",")
            M, D = cos.split(" ")
            if M in months and 1 <= int(D) <= 31:
                print(Y.strip(), str(months.index(M) + 1).zfill(2), D.zfill(2), sep="-")
                break
    except ValueError:
        pass


