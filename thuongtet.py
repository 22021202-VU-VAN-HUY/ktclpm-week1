def tinh_thuong(x: int, y: int) -> str:
    # Kiểm tra miền hợp lệ
    if not (0 <= x <= 40 and 0 <= y <= 100):
        return "đầu vào không hợp lệ"
    if x < 5 and y >= 70:
        return "thưởng 1 tháng lương"
    if 5 <= x < 10 and y >= 70:
        return "thưởng 2 tháng lương"
    if x >= 10 and y >= 70:
        return "thưởng 3 tháng lương"

    return "không thưởng"


if __name__ == "__main__":
    x = int(input("Thâm niên làm việc (0-40 năm):"))
    y = int(input("Hiệu suất (0-100 %):"))
    print("Kết quả:", tinh_thuong(x, y))
