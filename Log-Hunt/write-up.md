# Category

general skills

# Overview

서버 로그에 비밀 flag 조각들이 새어나오고 있는 것 같습니다. 조각들은 흩어져 있고 때로는 중복되기도 합니다. 원본 플래그를 재구성해 주실 수 있나요?

# Analysis

- server.log

```log
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:00:16] WARN Disk space low
[1990-08-09 10:00:19] DEBUG Cache cleared
[1990-08-09 10:00:23] WARN Disk space low
```

flag의 단서로 보이는 `FLAGPART:` 로 시작되는 flag들이 흩어지고 중복되어서 있는 것을 확인할 수 있음

# Exploitation

`FLAGPART:`라인을 추출하여 중복된 부분을 제거하면 `flag`를 얻을 수 있을 것으로 보임.

```bash
sed -n 's/.*FLAGPART: //p' server.log | uniq | head -4 | tr -d "\n"
```

# Flag

`picoCTF{us...fb}`
