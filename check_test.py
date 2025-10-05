import pytest
from thuongtet import tinh_thuong
### Kiểm thử biên mạnh - 13 ca kiểm thử
BVA_CASES = [
    (-1, 50, "đầu vào không hợp lệ"), 
    (0,  50, "không thưởng"),          
    (1,  50, "không thưởng"),          
    (20, 50, "không thưởng"),          
    (39, 50, "không thưởng"),          
    (40, 50, "không thưởng"),          
    (41, 50, "đầu vào không hợp lệ"),  
    (20, -1,  "đầu vào không hợp lệ"), 
    (20,  0,  "không thưởng"),         
    (20,  1,  "không thưởng"),         
    (20, 99,  "thưởng 3 tháng lương"), 
    (20, 100, "thưởng 3 tháng lương"), 
    (20, 101, "đầu vào không hợp lệ"), 
]
@pytest.mark.parametrize("x,y,expected", BVA_CASES)
def test_bva_strong(x, y, expected):
    assert tinh_thuong(x, y) == expected


### 2) kiểm thử theo bảng quyết định - 20 ca kiểm thử
DT_CASES = [
    # x<0
    (-1,  -1, "đầu vào không hợp lệ"),
    (-1,  35, "đầu vào không hợp lệ"),
    (-1,  85, "đầu vào không hợp lệ"),
    (-1, 101, "đầu vào không hợp lệ"),

    # 0<=x<5
    (3,  -1,  "đầu vào không hợp lệ"),
    (3,  35,  "không thưởng"),
    (3,  85,  "thưởng 1 tháng lương"),
    (3, 101,  "đầu vào không hợp lệ"),

    # 5<=x<10
    (8,  -1,  "đầu vào không hợp lệ"),
    (8,  35,  "không thưởng"),
    (8,  85,  "thưởng 2 tháng lương"),
    (8, 101,  "đầu vào không hợp lệ"),

    # 10<=x<=40
    (25,  -1,  "đầu vào không hợp lệ"),
    (25,  35,  "không thưởng"),
    (25,  85,  "thưởng 3 tháng lương"),
    (25, 101,  "đầu vào không hợp lệ"),

    # x>40
    (41,  -1,  "đầu vào không hợp lệ"),
    (41,  35,  "đầu vào không hợp lệ"),
    (41,  85,  "đầu vào không hợp lệ"),
    (41, 101,  "đầu vào không hợp lệ"),
]

@pytest.mark.parametrize("x,y,expected", DT_CASES)
def test_decision_table(x, y, expected):
    assert tinh_thuong(x, y) == expected
