import hashlib

# flag와 관련있는 변수들
key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

# 지정된 전역변수
bUsername_trial = b"BENNETT"

# 해시화
hashed = hashlib.sha256(bUsername_trial).hexdigest()

# 해시화된 지정된 요소값들만 순차적으로 재배치
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

flag = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(flag)
