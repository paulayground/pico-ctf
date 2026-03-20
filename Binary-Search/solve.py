import random

count = 0
min = 1
max = 1000
random_number = random.randrange(start=min, stop=max + 1)

while True:
    guess = (min + max) // 2
    count = count + 1

    if guess > random_number:
        print(f"higher guess - {guess} / count - {count}")
        max = guess - 1
    elif guess < random_number:
        print(f"lower guess - {guess} / count - {count}")
        min = guess + 1
    else:
        print(f"correct!!! guess - {guess} / count - {count}")
        break

    if count >= 100:
        print(random_number)
        break
