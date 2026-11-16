# 한 달 수입 계산기
'''
기본 월급: 267만원
세금: 24만원
사이트 수당: 근무 일수 x 2만원

세전 수입 = 기본 월급 + 사이트 수당(있으면)
세후 수입 = 세전 수입 - 24만원
'''

SALARY = 2_670_000
TAX = 240_000
SITE_PAY = 20_000
PHONE = 50_000
LIVING = 500_000
YOUTH_PAY = 500_000
YOUTH_MONTHS = 36
INVEST = 700_000
INVEST_RATE = -0.10

months = int(input("몇 개월을 계산하겠습니까? "))
apply_tax = input("세금을 적용하겠습니까? (Y/N): ").upper()

paid_months = 0
youth_total = 0
invest_total = 0
emergency = 0

for month in range(1, months + 1):
    print(f"\nヾ(•ω•`)o {month}개월 차 ヾ(•ω•`)o")

    # 사이트 수당 계산
    site = input("사이트 근무 여부 (Y/N): ").upper()
    days = 0

    if site == "Y":
        days = int(input("이번 달 사이트 근무 일수는 며칠입니까? "))

    site_pay = days * SITE_PAY

    # 수입, 세금 계산
    income = SALARY + site_pay
    tax_money = 0

    if apply_tax == "Y":
        tax_money = TAX

    balance = income - tax_money

    # 고정비, 경조사비 계산
    fixed = PHONE + LIVING
    balance -= fixed

    ceremony = int(input("이번 달 경조사비는 얼마입니까? "))
    balance -= ceremony

    # 청년미래적금 계산
    join_youth = input("청년미래적금에 이번 달 50만원을 납입합니까? (Y/N): ").upper()
    youth_pay = 0

    if join_youth == "Y" and paid_months < YOUTH_MONTHS:
        youth_pay = YOUTH_PAY
        paid_months += 1
        youth_total += youth_pay
    elif join_youth == "Y":
        print("청년미래적금은 이미 만기입니다.")

    balance -= youth_pay

    # 투자: 매달 70만원, 투자 계좌 전체에 -10% 수익률
    balance -= INVEST
    before_return = invest_total + INVEST
    profit = int(before_return * INVEST_RATE)
    invest_total = before_return + profit

    # 비상금
    emergency_pay = max(0, balance)
    emergency += emergency_pay
    minus = min(0, balance)

    print(f"월급: {SALARY:,}원")
    print(f"사이트 수당: {site_pay:,}원")
    print(f"세금 적용 후 수입: {income - tax_money:,}원")
    print(f"고정비: {fixed:,}원")
    print(f"경조사비: {ceremony:,}원")
    print(f"청년미래적금 납입액: {youth_pay:,}원")
    print(f"투자 납입액: {INVEST:,}원")
    print(f"투자 수익률: {INVEST_RATE:.0%}")
    print(f"이번 달 투자 손실: {profit:,}원")
    print(f"투자 계좌 잔액: {invest_total:,}원")
    print(f"비상금 계좌 입금액: {emergency_pay:,}원")
    print(f"비상금 계좌 잔액: {emergency:,}원")

    if minus < 0:
        print(f"이번 달 마이너스 금액: {minus:,}원")
    print(
        f"청년미래적금 납입 현황: "
        f"{paid_months}/{YOUTH_MONTHS}개월"
    )
    print(f"청년미래적금 납입 원금: {youth_total:,}원")

print("\nq(≧▽≦q) 총자산 리포트 q(≧▽≦q)")
print(
    f"청년 미래 적금 납입 횟수: {paid_months}/"
    f"{YOUTH_MONTHS}개월"
)
print(f"누적 납입 원금: {youth_total:,}원")
print(f"투자 계좌 잔액: {invest_total:,}원")
print(f"비상금 계좌 잔액: {emergency:,}원")
print(
    "총자산: "
    f"{youth_total + invest_total + emergency:,}원"
)

