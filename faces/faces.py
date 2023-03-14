def main():
    done = convert(input())
    print(done)

def convert(str):
    return str.replace(":(", "🙁").replace(":)","🙂")

main()