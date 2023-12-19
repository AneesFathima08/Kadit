def plusmins(array):
    n=len(array)
    postive=sum(x>0 for x in array)
    native=sum(x<0 for x in array)
    zero=sum(x==0 for x in array)
    
    postive_ratio=postive/n
    native_ratio=native/n
    zero_ratio=zero/n
    
    print(f"{postive_ratio:.6f}")
    print(f"{native_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

n=int(input())
arr=list(map(int,input().split()))
plusmins(arr)