def Greet(name="Stranger"):
    print(f"Good morning , {name}")

def findMax(arr):
    mx = arr[0]
    for item in arr:
        mx = max(mx,item)
    return mx

if __name__ == "__main__":
    name = input("Enter your name: ")
    Greet(name)
    arr = [45,2,-56,234,56]
    print(findMax(arr))
