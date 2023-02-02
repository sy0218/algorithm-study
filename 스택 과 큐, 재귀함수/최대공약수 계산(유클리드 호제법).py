#유클리드 호제법(두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘)
#두자연수 a,b에 대해(a>b) a를 b로 나눈 나머지를 r이라고함
#이떄 a와b의 최대공약수는 b와 r의 최대공약수와 같음
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(192,162))