import pytest
from thuongtet_week3 import tinh_thuong


ALL_USES_X_CASES = [
    # (x, y, expected, path_note)
    (-1, 70, "đầu vào không hợp lệ", "0-1-2-3-11"),
    (0,  70, "thưởng 1 tháng lương", "0-1-2-4-5-11"),
    (5,  70, "thưởng 2 tháng lương", "0-1-2-4-6-7-11"),
    (10, 70, "thưởng 3 tháng lương", "0-1-2-4-6-8-9-11"),
    (10, 69, "không thưởng",         "0-1-2-4-6-8-9-10-11"),
]

ALL_USES_Y_CASES = [
    # (x, y, expected, path_note)
    (-1, -1, "đầu vào không hợp lệ", "0-1-2-3-11"),
    (0,   80, "thưởng 1 tháng lương", "0-1-2-4-5-11"),
    (5,   80, "thưởng 2 tháng lương", "0-1-2-4-6-7-11"),
    (10,  80, "thưởng 3 tháng lương", "0-1-2-4-6-8-9-11"),
    (2,   69, "không thưởng",         "0-1-2-4-6-8-9-10-11"),
]

@pytest.mark.parametrize("x,y,expected,path_note", ALL_USES_X_CASES)
def test_all_uses_x_group(x, y, expected, path_note):
    """All-Uses coverage - nhóm đường đi nhấn mạnh biến x (theo bảng)."""
    got = tinh_thuong(x, y)
    assert got == expected, f"[Path {path_note}] expect: {expected}, got: {got}"

@pytest.mark.parametrize("x,y,expected,path_note", ALL_USES_Y_CASES)
def test_all_uses_y_group(x, y, expected, path_note):
    """All-Uses coverage - nhóm đường đi nhấn mạnh biến y (theo bảng)."""
    got = tinh_thuong(x, y)
    assert got == expected, f"[Path {path_note}] expect: {expected}, got: {got}"
