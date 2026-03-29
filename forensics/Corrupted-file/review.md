# 배운 점

jpg
SOI(start of image): `FF D8`
Appn JFIF Marker:APP0~APP15까지 오고 썸네일데이터가 들어간다 `FF E0-F` JFIF라는 문자열도 들어간다
EOI(end of image): `FF D9`

# 풀이 과정 기록

이상하게 반복되는 값들이 많아 해당 값 때문인가 지워봤지만, 별 소득은 없었고, 앞자리의 JPIF를 검색한 결과 jpg와 관련된 내용, 또 이와 관련해서 시그니처를 찾아본 결과 해당 값들이 미묘하게 다른 것을 확인할 수 있었다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

# 참고

- https://m.blog.naver.com/ginger2009/222040985394
