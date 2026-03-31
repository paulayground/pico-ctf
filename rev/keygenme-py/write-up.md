# Category

rev

# Overview

keygenme-trial.py 분석

# Analysis

- 전역 변수로 나타난 변수들을 통해 flag와 관련된 내용들이 있는 변수를 확인했다.

  ```py
  # keygenme-trial.py
  key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
  key_part_dynamic1_trial = "xxxxxxxx"
  key_part_static2_trial = "}"
  key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
  ```

- `key_full_template_trial`는 `check_key()`함수에 사용되며, `enter_license()`함수에서 호출하는 함수이고 역으로 따라 올라가면, 대화형 프로그램에서 라이선스를 입력하는 부분을 검사하는 과정에서 flag의 정답을 찾는 내용이라는 것을 확인할 수 있다.

- `check_key(key, username_trial)`함수는 사용자가 입력한 라이선스 입력값과 전역변수에 지정된 `bUsername_trial = b"BENNETT"`가 사용된다.

  첫번째로 `key_part_static1_trial`의 일치여부을 검사하고, 두번째로
  값이 `xxxxxxxx`로 지정된 `key_part_dynamic1_trial`의 부분을 확인하는데, 이는 `hashlib.sha256(username_trial).hexdigest()`를 통해 해시화한 내용의 지정된 요소들과 유저의 입력값을 비교하여 일치여부를 확인한다.

# Exploitation

1. `key_part_dynamic1_trial`의 내용을 알기 위해 해시화한 후, 코드상에 지정된 리스트의 순서에 맞게 출력하면 일치하는 값을 확인할 수 있다.

   ```py
   # solve.py
   bUsername_trial = b"BENNETT"
   hashed = hashlib.sha256(bUsername_trial).hexdigest()

   key_part_dynamic1_trial = (
       hashed[4]
       + hashed[5]
       + hashed[3]
       + hashed[6]
       + hashed[2]
       + hashed[7]
       + hashed[1]
       + hashed[8]
   )
   ```

2. 획득한 `key_part_dynamic1_trial`와 함께 `key_part_static1_trial`,
   `key_part_static2_trial`를 결합하면 flag를 획득할 수 있다.

3. `keygenme-trial.py`를 실행시켜 얻은 flag를 라이선스에 입력하면 통과되며 올바른 flag인것을 알 수 있다.

# Flag

`picoCTF{1n...a4}`
