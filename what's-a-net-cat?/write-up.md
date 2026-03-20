# Category

general skills

# Overview

`net-cat(nc)` 사용이 상당히 중요할 것입니다. `flickle-tempest.picoctf.net`의 `59870` 포트에 연결하여 플래그를 획득할 수 있나요?

# Analysis

# Exploitation

59870포트로 `fickle-tempest.picoctf.net`에 nc를 통해 연결할 경우 flag를 얻을 수 있다.

```bash
nc fickle-tempest.picoctf.net 59870
```

# Flag

`picoCTF{nE..,2C}`
