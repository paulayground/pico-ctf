# Category

forensics

# Overview

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

# Analysis

file의 hex값을 확인하면 첫라인에 `JFIF`로 시작되는 단서와 `FF D9`로 끝난다는 단서를 통해 jpg파일이였을 가능성을 생각해볼 수 있다. jpg의 헤드시그니처는 `FF D8 FF E0 xx xx 4A 46 49 46`와 같이 시작하고 푸터 시그니처는 `FF D9`와 같이 끝이난다.

# Exploitation

현재 앞부분에 있는 `5c 78` 부분이 `FF D8`로 변경되어야 올바른 jpg 헤드시그니처를 가져 jpg 파일로 실행될 수 있다.
hex 에디터를 통해 해당 부분을 수정하고 이미지 실행한 결과 이미지에 나타나있는 flag를 획득할 수 있다.

# Flag

`picoCTF{r3...c0}`
