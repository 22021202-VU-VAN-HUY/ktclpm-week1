def tinh_thuong(x: int, y: int) -> str:
    result: str
    # Kiểm tra miền hợp lệ
    if not (0 <= x <= 40 and 0 <= y <= 100):
        result = "đầu vào không hợp lệ"
    elif x < 5 and y >= 70:
        result = "thưởng 1 tháng lương"
    elif 5 <= x < 10 and y >= 70:
        result = "thưởng 2 tháng lương"
    elif x >= 10 and y >= 70:
        result = "thưởng 3 tháng lương"
    else:
        result = "không thưởng"
    return result


if __name__ == "__main__":
    x = int(input("Thâm niên làm việc (0-40 năm):"))
    y = int(input("Hiệu suất (0-100 %):"))
    print("Kết quả:", tinh_thuong(x, y))
