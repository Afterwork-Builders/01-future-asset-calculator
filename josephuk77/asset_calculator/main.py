from .calculator import calculate_future_assets, calculate_rate


def main():
    print("===== 미래 자산 계산기 =====")

    # 기본 정보 입력
    current_assets = int(input("현재 자산: "))
    monthly_salary = int(input("월급: "))
    monthly_expense = int(input("월 지출: "))

    months_input = input(f"저축 개월수 (기본 12개월): ")
    months = int(months_input) if months_input else 12

    # 이자 설정
    print("\n===== 이자 설정 =====")

    annual_interest_rate = input("1. 연이율 / 2. 월이율: ") == "1"
    is_compound = input("1. 복리 / 2. 단리: ") == "1"
    rate = float(input("이자율 (%): "))

    if months <= 0 or rate < 0:
        print("계산 기간과 이자율을 확인해 주세요.")
        return

    # 월 저축 가능 금액
    monthly_savings = monthly_salary - monthly_expense

    # 이자를 제외한 미래 자산
    future_assets = calculate_future_assets(
        current_assets,
        monthly_salary,
        monthly_expense,
        months
    )

    # 이자를 포함한 미래 자산
    future_assets_total = calculate_rate(
        current_assets=current_assets,
        monthly_savings=monthly_savings,
        annual_interest_rate=annual_interest_rate,
        is_compound=is_compound,
        rate=rate,
        months=months
    )

    # 결과 출력
    print("\n===== 계산 결과 =====")
    print(f"월 저축 가능 금액: {monthly_savings:,}원")
    print(f"{months}개월 후 예상 자산: {future_assets:,}원")
    print(f"이자 포함 예상 자산: {future_assets_total:,}원")
    print(f"예상 이자 수익: {future_assets_total - future_assets:,}원")

    print("\nX 월급과 지출은 고정, 세금 및 수수료 미반영")


if __name__ == "__main__":
    main()
