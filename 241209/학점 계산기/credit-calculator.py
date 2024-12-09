n = int(input())
arr = list(map(float, input().split()))
grade = 'a'
avg_score = round(sum(arr)/n, 1)
if avg_score >= 4.0:
    grade = 'Perfect'
elif avg_score >= 3.0:
    grade = 'Good'
else:
    grade = 'Poor'
print(avg_score)
print(grade)