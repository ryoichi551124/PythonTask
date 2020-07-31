import random

def randlist(num):
    answer_array = []

    for i in range(num):
        answer = random.randint(0, 100)
        answer_array.append(answer)
    
    return answer_array

print(randlist(10))
print(randlist(5))
print(randlist(3))
