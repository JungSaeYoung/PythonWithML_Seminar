import re

def korean_to_number(korean: str) -> int:
    num_map = {
        "일": 1, "이": 2, "삼": 3, "사": 4, "오": 5,
        "육": 6, "칠": 7, "팔": 8, "구": 9, "영": 0
    }
    unit_map = {"십": 10, "백": 100, "천": 1000}
    large_unit_map = {"만": 10000, "억": 100000000}
    
    result = 0
    temp = 0
    current_sum = 0
    
    for char in korean:
        if char in num_map:
            temp = num_map[char]
        elif char in unit_map:
            if temp == 0:
                temp = 1  # "십", "백" 같은 단위가 앞에 단독으로 오는 경우
            temp *= unit_map[char]
            current_sum += temp
            temp = 0
        elif char in large_unit_map:
            if temp == 0 and current_sum == 0:
                temp = 1  # "만", "억" 단독으로 오는 경우
            current_sum += temp
            result += current_sum * large_unit_map[char] // 10000 if char == "억" and result > 0 else current_sum * large_unit_map[char]
            current_sum = 0
            temp = 0
        else:
            raise ValueError("Invalid character in Korean number string")
    
    return result + current_sum + temp

def number_to_korean(number: int) -> str:
    num_map = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    unit_map = ["", "십", "백", "천"]
    large_units = ["", "만", "억"]
    
    if number == 0:
        return "영"
    
    result = ""
    
    str_number = str(number)[::-1]  # 숫자를 뒤집어서 작은 자리부터 처리
    parts = [str_number[i:i+4] for i in range(0, len(str_number), 4)]
    
    for i, part in enumerate(parts):
        part_value = ""
        for j, digit in enumerate(part):
            if digit != "0":
                part_value = num_map[int(digit)] + unit_map[j] + part_value
        
        if part_value:
            result = part_value + large_units[i] + result
    
    return result

def convert(input_value):
    if isinstance(input_value, str):
        if re.fullmatch(r'[일이삼사오육칠팔구영십백천만억]+', input_value):
            return korean_to_number(input_value)
        elif input_value.isdigit():
            return number_to_korean(int(input_value))
        else:
            raise ValueError("Invalid input format")
    elif isinstance(input_value, int):
        return number_to_korean(input_value)
    else:
        raise TypeError("Unsupported input type")

# 테스트
print(convert("영")) # 0
print(convert("일천삼백이십오"))  # 1325
print(convert("삼만오천일백일십일"))  # 35111
print(convert("오백오십일만오"))  # 5510005
print(convert("육만오천오백삼십오"))  # 65535
print(convert("일억이천삼백사십오만육천칠백팔십구"))  # 123456789'
print(convert("일천이백삼십사억오천육백칠십팔만구천일십이"))  # 123456789012
print(convert(0))  # "영"
print(convert(1325))  # "일천삼백이십오"
print(convert(35111))  # "삼만오천일백일십일"
print(convert(65535))  # "육만오천오백삼십오"
print(convert(5510005)) # "오백오십일만오"
print(convert(123456789))  # "일억이천삼백사십오만육천칠백팔십구"
print(convert(123456789012)) # "일천이백삼십사억오천육백칠십팔만구천일십이"
# print(convert("오천이백삼십x"))  
# # ValueError: Invalid character in Korean number string이 발생하도록 설계했지만 
# convert에서 먼저 검사하기 때문에 ValueError: Invalid input foramt 발생
# print(convert("five"))  # ValueError: Invalid input format
# print(convert(3.14))  # TypeError: Unsupported input type