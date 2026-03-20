# Category

General Skills

# Overview

파일에서 플래그를 찾을 수 있나요? 수동으로 찾아보는 건 정말 지루할 텐데, 뭔가 더 나은 방법이 있을 것 같아요.
플래그는 이 파일에 있습니다.

# Analysis

file을 확인 결과 한줄짜리 긴 텍스트 문자열이 제공 되었음

# Exploitation

grep을 통해서 picoCTF{FLAG} 형태를 추출한다.

```bash
grep -o "picoCTF{.*}" file
```

# Flag

`picoCTF{gr...F7}`
