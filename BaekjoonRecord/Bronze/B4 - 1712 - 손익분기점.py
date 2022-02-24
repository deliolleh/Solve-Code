fixed_cost, product_cost, benefit = map(int, input().split())


# fixed_cost + product_cost * n < benefit * n => 이익이 생긴다
# 알고리즘 수업 => 시간복잡도(O(n^2))
# 이익이 가변비용보다 같거나 적으면 적자 => 이익 발생 불가
if product_cost >= benefit:
    print(-1)
else:
    # i: 손해와 이득의 합이 0인 실수의 정수형(i의 소수부가 0이었어도 i일 때는 손익이 0이다)
    i = int(fixed_cost / (benefit - product_cost))
    # i < 이익발생 < i+1이므로 정수중에서 손익분기점을 넘는 최소값은 i+1이다
    print(i+1)
