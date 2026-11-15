from asset_calculator.calculator import calculate_future_assets

def test_calculate_future_assets():
    result = calculate_future_assets(
        currnet_assets=1_000_000,
        monthly_salary=3_200_000,
        monthly_expense=1_500_000,
        months=12
    )

    assert result == 21_400_000