
import pytest

from asset_calculator.calculator import (
    calculate_future_assets,
    calculate_rate,
)


def test_calculate_future_assets():
    result = calculate_future_assets(
        current_assets=1_000_000,
        monthly_salary=3_200_000,
        monthly_expense=1_500_000,
        months=12,
    )

    assert result == 21_400_000


def test_calculate_rate_zero():
    result = calculate_rate(
        current_assets=1_000_000,
        monthly_savings=1_700_000,
        annual_interest_rate=True,
        is_compound=True,
        rate=0,
        months=12,
    )

    assert result == 21_400_000


def test_annual_interest_rate():
    result = calculate_rate(
        current_assets=1_000_000,
        monthly_savings=0,
        annual_interest_rate=True,
        is_compound=True,
        rate=12,
        months=1,
    )

    assert result == 1_010_000


def test_simple_interest():
    result = calculate_rate(
        current_assets=1_000_000,
        monthly_savings=100_000,
        annual_interest_rate=False,
        is_compound=False,
        rate=1,
        months=2,
    )

    assert result == 1_221_000


def test_compound_interest():
    result = calculate_rate(
        current_assets=1_000_000,
        monthly_savings=100_000,
        annual_interest_rate=False,
        is_compound=True,
        rate=1,
        months=2,
    )

    assert result == 1_221_100


def test_compound_interest_12_months():
    result = calculate_rate(
        current_assets=1_000_000,
        monthly_savings=1_700_000,
        annual_interest_rate=True,
        is_compound=True,
        rate=5,
        months=12,
    )

    assert result == 21_925_216
