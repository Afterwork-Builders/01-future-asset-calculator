from .constants import DEFAULT_MONTHS
from .calculator import calculate_future_assets

def main():
    print("===== 미래 자산 계산기 =====")

    current_assets = int(input("현재 자산: "))
    monthly_salary = int(input("월급: "))
    monthly_expense = int(input("월 지출: "))
    months = int(input("저축 개월수: "))

    future_assets = calculate_future_assets(
        current_assets,
        monthly_salary,
        monthly_expense,
        months
    )

    monthly_savings = monthly_expense

    print("\n===== 계산 결과 =====")
    print(f"월 저축 가능 금액: {monthly_savings:,}원")
    print(f"{months}개월 후 예상 자산: {future_assets:,}원")
    print("X 월급과 지출은 고정, 세금·이자·수익률은 미반영")

if __name__ == "__main__":
    main()