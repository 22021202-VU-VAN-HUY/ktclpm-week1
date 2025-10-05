import pytest
from thuongtet import tinh_thuong

C2_CASES = [
    # 0 − 1(𝐹) − 2 (invalid input)
    (-1, 70, "đầu vào không hợp lệ"),

    # 0 − 1(𝑇) − 3(𝑇) − 4  -> 1 month
    (0, 70, "thưởng 1 tháng lương"),

    # 0 − 1(𝑇) − 3(𝐹) − 5(𝑇) − 6 -> 2 months
    (5, 70, "thưởng 2 tháng lương"),

    # 0 − 1(𝑇) − 3(𝐹) − 5(𝐹) − 7(𝑇) − 8 -> 3 months
    (10, 70, "thưởng 3 tháng lương"),

    # 0 − 1(𝑇) − 3(𝐹) − 5(𝐹) − 7(𝐹) − 9 -> no bonus
    (4, 69, "không thưởng"),
]

@pytest.mark.parametrize("x,y,expected", C2_CASES)
def test_branch_coverage(x, y, expected):
    assert tinh_thuong(x, y) == expected
