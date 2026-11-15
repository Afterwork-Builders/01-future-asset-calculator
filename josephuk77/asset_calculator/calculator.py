def calculate_future_assets(
    currnet_assets: int,
    monthly_salary: int,
    monthly_expense: int,
    months: int
) -> int:

    monthly_savings = monthly_salary - monthly_expense

    future_assets = currnet_assets + (monthly_savings * months)

    return future_assets