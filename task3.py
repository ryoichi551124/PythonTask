import random

def randlist(num, lower=0, upper=100):
    answer_array = []

    for i in range(num):
        answer = random.randint(lower, upper)
        answer_array.append(answer)
    
    return answer_array


print(randlist(10))
print(randlist(5, lower=20))
print(randlist(3, upper=50))
print(randlist(6, lower=20, upper=50))