import xml.etree.ElementTree as ET
from typing import List

# XML파일을 트리구조로 읽음
tree = ET.parse("./drawing.flag.svg")

# 최상위 노드(<svg>) 가져옴
root = tree.getroot()

"""
SVG는 namespace가 존재함: <svg xmlns="http://www.w3.org/2000/svg">
ElementTree 내부에서는 태그가 {http://www.w3.org/2000/svg}tspan 형태로 저장됨
alias 설정하여 불필요한 이름인 {http://www.w3.org/2000/svg}를 줄일 수 있다.
alias 미적용: .//{http://www.w3.org/2000/svg}tspan
alias 적용:  .//svg:tspan
"""
alias = {"svg": "http://www.w3.org/2000/svg"}

flag_parts: List[str] = []

# 현재노드(root = .)에서 모든 하위 노드(//) 탐색
for tspan in root.findall(".//svg:tspan", alias):
    if tspan.text:
        flag_parts.append(tspan.text.strip())

flag = "".join(flag_parts).replace(" ", "")
print(flag)
