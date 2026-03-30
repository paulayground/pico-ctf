# Category

forensics

# Overview

Download this image file and find the flag.

# Analysis

제시된 `drawing.flag.svg` 파일은 `svg`형식으로 `svg`는 `xml`기반으로 이루어진 이미지이기 때문에, 텍스트로 읽을 경우 `xml`코드가 나타나며 살펴본 결과 `tspan`태그에 flag와 유사한 형식의 글자들이 존재하는 것을 알 수 있다.

# Exploitation

`tspan` 태그의 value로 이루어진 내용들을 취합하면 flag를 획득할 수 있다.

```py
# solve.py
flag_parts: List[str] = []

# 현재노드(root = .)에서 모든 하위 노드(//) 탐색
for tspan in root.findall(".//svg:tspan", alias):
    if tspan.text:
        flag_parts.append(tspan.text.strip())

flag = "".join(flag_parts).replace(" ", "")
print(flag)
```

# Flag

`picoCTF{3n...dd}`
