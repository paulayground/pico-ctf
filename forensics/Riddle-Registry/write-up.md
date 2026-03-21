# Category

forensics

# Overview

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.

# Analysis

confidential.pdf 파일이 주어지며 내용을 확인할 시, 일부 글자가 검은색 박스로 마스킹되어서 보이는 것을 알 수 있다. 일단 마스킹 부분을 확인해보면 드래그해서 다른 편집창에서 확인해보면 아래와 같이 별 의미 없는 문자임을 알 수 있고 flag 단서는 여기 없다는 것을 알 수 있다.

```pdf confidential.pdf
# 1번째 마스킹
Aenean lacinia bibendum nulla sed consectetur
# 2번째 마스킹
Lorem ipsum dolor sit amet
# 3번째 마스킹
The author have done a great and good job
# 4번째 마스킹
No flag here. Nice try though!
```

문제에서 제시한 metadata의 flag를 확인하라는 문구를 통해 metadata를 확인해보기로 했다.

# Exploitation

exiftool를 사용해 메타데이터를 확인한 결과 아래와 같은 결과에 `Author` 부분이 base64 방식으로 인코딩 되어있는 것으로 의심되는 부분을 확인할 수 있다.

```bash
exiftool confidential.pdf
ExifTool Version Number         : 13.50
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2026:03:20 15:34:44+09:00
File Access Date/Time           : 2026:03:20 16:37:15+09:00
File Inode Change Date/Time     : 2026:03:20 16:37:14+09:00
File Permissions                : -rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0=
```

해당 부분을 base64 디코딩을 통해 해당 부분을 바꿔보면 flag를 획득할 수 있다.

```bash
echo cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0= | base64 -d
picoCTF{pu...b2}
```

# Flag

`picoCTF{pu...b2}`
