# Kiểm thử và đảm bảo chất lượng phần mềm — Bài toán Thưởng Tết

Bài toán xác định **mức thưởng Tết cuối năm** cho nhân viên dựa trên hai yếu tố đầu vào: **thâm niên làm việc** và **điểm đánh giá hiệu suất công việc**.

## Đầu vào
- **Thâm niên (x)**: số năm làm việc, số nguyên, `0 ≤ x ≤ 40`
- **Hiệu suất (y)**: phần trăm %, số nguyên, `0 ≤ y ≤ 100`

## Kết quả
- Nếu `x < 5` **và** `y ≥ 70` → **thưởng 1 tháng lương**.
- Nếu `5 ≤ x < 10` **và** `y ≥ 70` → **thưởng 2 tháng lương**.
- Nếu `x ≥ 10` **và** `y ≥ 70` → **thưởng 3 tháng lương**.
- **Không thưởng**: các trường hợp còn lại trong **khoảng hợp lệ**.
- **Đầu vào không hợp lệ**: khi `x` hoặc `y` **nằm ngoài** khoảng cho phép.
