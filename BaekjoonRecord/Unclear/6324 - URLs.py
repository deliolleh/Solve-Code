import sys

N = int(input())

for n in range(1, N + 1):
    print(f"URL #{n}")
    url = sys.stdin.readline().rstrip()

    pro_end = url.find(":")

    print(f"Protocol = {url[:pro_end]}")

    url = url[pro_end + 3 :]

    if ":" in url:
        pro_end = url.find(":")
        print(f"Host     = {url[:pro_end]}")
        url = url[pro_end + 1 :]
        pro_end = url.find("/")
        print(f"Port     = {url[:pro_end]}")
    elif "/" in url:
        pro_end = url.find("/")
        print(f"Host     = {url[:pro_end]}")
        print(f"Port     = <default>")
    else:
        print(f"Host     = {url}")
        print(f"Port     = <default>")
        print(f"Path     = <default>")
        continue

    if url[:pro_end] + "/" == url:
        print(f"Path     = <default>")
    else:
        print(f"Path     = {url[pro_end + 1:]}")

    print()

# wrong
