# Category

general skills

# Overview

내가 마지막으로 작업하던 게 뭐였지? 기억을 돕기 위해 메모를 썼던 게 기억나는데...

# Analysis

- drop-in/message.txt
  메시지에 커밋 기록에 관한 내용이 있어 .git 디렉토리를 확임함.

# Exploitation

git 변경사항을 확인하기위해 로그를 확인했고 커밋메시지로 입력된 flag를 획득할 수 있었다.

```bash
git log

commit b92bdd8ec87a21ba45e77bd9bed3e4893faafd0f (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:29 2024 +0000

    picoCTF{t1...75}
```

# Flag

`picoCTF{t1...75}`
