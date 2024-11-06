
get_int = lambda: int(input())
get_int_tuple = lambda: map(int, input().split())
get_int_list = lambda: list(map(int, input().split()))

t = get_int()
for _ in range(t):
    n = get_int()
    student_university = get_int_list()
    student_skill = get_int_list()
    u_skills = [[] for i in range(n)]
    for u,s in zip(student_university, student_skill):
        u_skills[u-1].append(s)
    for i in range(n):
        u_skills[i].sort()
    total_skill = [0]*n
    for i in range(n):
        for j in range(len(u_skills[i])-1):
            u_skills[i][j+1] += u_skills[i][j]
    for i in range(n):
        m = len(u_skills[i])
        for k in range(1, m+1):
            j = m%k-1
            total_skill[k-1] += u_skills[i][-1] - u_skills[i][j] if j>=0 else u_skills[i][-1]
    print(' '.join(map(str,total_skill))) 