student_scores = [150, 142, 185, 120, 171, 184, 149, 59, 68]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
# print(max_score)

# Range function should be used in a conjunction with another function.
#  for number in range(a, b):
# 		print(number)

# for number in range(1, 11):
    # print(number)

total = 0
for num in range(1, 101):
    total += num
print(total)