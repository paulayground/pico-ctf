# Category

general skills

# Overview

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here: challenge.zip
Additional details will be available after launching your challenge instance.

# Analysis

제시된 sh파일을 보면 1~1000까지의 숫자가 랜덤하게 뽑히고 10번 안에 그 숫자를 맞추는 게임이다.

# Exploitation

1000까지의 숫자이기 때문에 이진 탐색 방법으로 $$log_2(1000)$$ 이기 때문에 10번 안에 정답을 찾을 수 있다는 것을 알 수 있다.

# Flag

`picoCTF{...}`
