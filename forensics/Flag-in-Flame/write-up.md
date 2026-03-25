# Category

forensics

# Overview

The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

# Analysis

logs.txt의 메타데이터를 확인한 결과 텍스트파일임에도 1라인에 끝나는 파일이며, 앞부분을 잠깐 출력한 결과도 의미를 지닌 문자들이 아니였다. 하지만 내용에 적혀있는 문자들이 base64 인코딩 방식과 유사했다.

```bash
$ exiftool logs.txt
File Name                       : logs.txt
...
File Type Extension             : txt
MIME Type                       : text/plain
MIME Encoding                   : us-ascii
Newlines                        : (none)
Line Count                      : 1
Word Count                      : 1
```

# Exploitation

1. base64 디코딩을 한 후 파일의 메타데이터를 확인한 결과 png파일로 확인되었으며 사진을 확인하였다.

   ```bash
   $ cat logs.txt | base64 -d > decode

   $ exiftool decode
   File Name                       : decode
   ...
   File Type                       : PNG
   File Type Extension             : png
   MIME Type                       : image/png
   ...
   ```

2. 사진에는 아래쪽에 `7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F63373564643038657D`와 같은 문자열이 있는 것을 확인했고 hex로 인코딩되어있는 것을 확인할 수 있었다.

3. hex로 이루어진 문자열을 string으로 변환하여 flag를 획득할 수 있다.

   ```python
   bytes.fromhex('7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F63373564643038657D').decode()
   ```

# Flag

`picoCTF{fo...8e}`
