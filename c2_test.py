import pytest
from thuongtet import tinh_thuong

"""
C2 (branch/decision coverage) for tinh_thuong(x, y).

Decisions per CFG:
(1) Validity: 0<=x<=40 and 0<=y<=100
(3) x<5 and y>=70
(5) 5<=x<10 and y>=70
(7) x>=10 and y>=70

The 5 tests below ensure each decision takes both True and False at least once.
"""

C2_CASES = [
    # D(1) = False (invalid input)
    (-1, 70, "đầu vào không hợp lệ"),

    # D(1) = True, D(3) = True  -> 1 month
    (0, 70, "thưởng 1 tháng lương"),

    # D(1) = True, D(3) = False, D(5) = True -> 2 months
    (5, 70, "thưởng 2 tháng lương"),

    # D(1) = True, D(3) = False, D(5) = False, D(7) = True -> 3 months
    (10, 70, "thưởng 3 tháng lương"),

    # D(1) = True, D(3) = False, D(5) = False, D(7) = False -> no bonus
    (4, 69, "không thưởng"),
]

@pytest.mark.parametrize("x,y,expected", C2_CASES)
def test_branch_coverage(x, y, expected):
    assert tinh_thuong(x, y) == expected
