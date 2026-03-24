# Category

forensics

# Overview

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image here.

# Analysis

문제에 제시된 `img.jpg`의 메타데이터를 확인해 본 결과, `Comment`의 값이 `base64`로 인코딩 되어있는 것으로 보이는 의심스러운 부분이 확인되었다.

```bash
$ exiftool img.jpg
ExifTool Version Number         : 13.50
...
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
...
Megapixels                      : 0.410
```

# Exploitation

1. `Comment` 메타데이터 부분을 `base64` 디코딩한 결과 `steghide`라는 단어와 또다른 `base64` 부분이 나와 다시 디코딩한 결과 `pAzzword`라는 값을 얻었다.

   ```bash
   # c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 base64 decoding
   echo c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 | base64 -d
   steghide:cEF6endvcmQ=

   # cEF6endvcmQ= base64 decoding
   echo cEF6endvcmQ= | base64 -d
   pAzzword
   ```

2. `steghide`라는 단어를 찾아보니 스테가노그래피 기술을 적용하거나 해독하는 툴이라는 것을 확인했고, 해당 이미지에 스테가노그래피 기술이 적용되어있으며, 추가적으로 디코딩한 `pAzzword`가 해당 복호화의 필요한 키값으로 의심이 되었다.

3. `steghide` 툴을 활용해 `img.jpg`를 복호화한 결과 `flag.txt`파일이 생성된 것을 확인할 수 있으며, 안에 flag값이 있는 것을 확인할 수 있다.

   ```bash
   # img.jpg(-sf img.jpg)를 steghide 사용해 passphrase값을 넣어 (-p pAzzword) 복호화(--extract)
   steghide --extract -p pAzzword -v -sf img.jpg
   ```

# Flag

`picoCTF{h1...45}`
