N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

m_num = max(nums)
prime = [True] * (m_num + 1)
prime[0], prime[1] = False, False
for i in range(2, m_num):
    if prime[i]:
        for j in range(2 * i, m_num + 1, i):
            prime[j] = False

prime_num = []
for k in range(m_num + 1):
    if prime[k]:
        prime_num.append(k)

for num in nums:
    now = num // 2
    if now in prime_num:
        print(now, now)
    else:
        while True:
            now -= 1
            if now in prime_num:
                another = num - now
                if another in prime_num:
                    print(now, another)
                    break