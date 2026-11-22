import re

# 로그 데이터 파일 읽기
with open("festival_log.txt", "r", encoding="utf-8") as file:
    text = file.read()


# 1. 유효한 이메일 추출
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+\b'
emails = re.findall(email_pattern, text)


# 2. 휴대폰 번호 추출
phone_pattern = r'(?<!\d)010[-. ]\d{4}[-. ]\d{4}(?!\d)'
phones = re.findall(phone_pattern, text)


# 3. 본교 재학생 학번과 학과 추출
student_pattern = r'\[(202\d{6})\s*/\s*([^\]]+)\]'
students = re.findall(student_pattern, text)


# 4-1. GitHub 저장소 URL 추출
github_pattern = r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?'
github_urls = re.findall(github_pattern, text)


# 4-2. 2026년도 유효 쿠폰 추출
coupon_pattern = r'\bFEST-2026-[A-Z0-9]{4}\b'
coupons = re.findall(coupon_pattern, text)


# 5. 부스별 총 매출액 추출
sales_pattern = r'매출:\s*([\d,]+)원'
sales = re.findall(sales_pattern, text)

# 쉼표 제거 후 정수로 변환
sales_amounts = [int(amount.replace(",", "")) for amount in sales]

# 전체 매출 합계
total_sales = sum(sales_amounts)


# 결과 출력
print("=" * 50)
print("2026 전주대학교 대동제 로그 데이터 분석")
print("=" * 50)

print("\n[1. 유효한 이메일]")
for email in emails:
    print(email)

print("\n[2. 휴대폰 번호]")
for phone in phones:
    print(phone)

print("\n[3. 본교 재학생 학번 및 학과]")
for student in students:
    print(f"학번: {student[0]}, 학과: {student[1]}")

print("\n[4-1. GitHub 저장소]")
for url in github_urls:
    print(url)

print("\n[4-2. 유효 쿠폰]")
for coupon in coupons:
    print(coupon)

print("\n[5. 부스별 총 매출액]")
for i, amount in enumerate(sales_amounts, start=1):
    print(f"{i}. {amount:,}원")

print(f"\n전체 매출 합계: {total_sales:,}원")
print("=" * 50)
