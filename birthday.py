def tallest(candle):
    tall = max(candle)
    count = candle.count(tall)
    return count
    
num=int(input())
candle = list(map(int,input().split()))
result = (tallest(candle))
print(result)