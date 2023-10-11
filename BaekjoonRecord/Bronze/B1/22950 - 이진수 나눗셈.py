# M의 자릿수 => 불필요한 0을 만들어낼 수 있음 => 무시
N = int(input())
# M의 실제 값
num = input()
# 나누는 값 => 1과 2의 배수
K = int(input())
# num의 값을 10진수로 바꾸고 값을 나눈 결과가 0이 아니면 NO 없다면 YES
print("NO") if int(num, 2) % 2 ** K else print("YES")