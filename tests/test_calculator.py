"""
Test suite for the Calculator class.
"""

import pytest
from src.calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance for tests."""
    return Calculator()

class TestAddition:
    """Tests for the add method (Assignment 1)."""

    def test_add_positive_numbers(self, calc):
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self, calc):
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self, calc):
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self, calc):
        assert calc.add(-5, 3) == -2

    def test_add_positive_with_zero(self, calc):
        assert calc.add(5, 0) == 5

    def test_add_zero_with_positive(self, calc):
        assert calc.add(0, 5) == 5

    def test_add_floats(self, calc):
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:
    """Tests for the subtract method (Assignment 1)."""

    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self, calc):
        assert calc.subtract(-5, -3) == -2

    def test_subtract_positive_and_negative(self, calc):
        assert calc.subtract(5, -3) == 8

    def test_subtract_negative_and_positive(self, calc):
        assert calc.subtract(-5, 3) == -8

    def test_subtract_positive_with_zero(self, calc):
        assert calc.subtract(5, 0) == 5

    def test_subtract_zero_with_positive(self, calc):
        assert calc.subtract(0, 5) == -5

    def test_subtract_zero_with_negative(self, calc):
        assert calc.subtract(0, -5) == 5

    def test_subtract_floats(self, calc):
        assert calc.subtract(2.5, 3.7) == pytest.approx(-1.2)


class TestMultiplication:
    """Tests for the multiply method (Assignment 1)."""

    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(5, 3) == 15
    
    def test_multiply_negative_numbers(self, calc):
        assert calc.multiply(-5, -3) == 15

    def test_multiply_positive_and_negative(self, calc):
        assert calc.multiply(5, -3) == -15

    def test_multiply_negative_and_positive(self, calc):
        assert calc.multiply(-5, 3) == -15
    
    def test_multiply_zero_with_positive(self, calc):
        assert calc.multiply(0, 5) == 0

    def test_multiply_zero_with_negative(self, calc):
        assert calc.multiply(0, -5) == 0

    def test_multiply_floats(self, calc):
        assert calc.multiply(2.5, 3.7) == pytest.approx(9.25)


class TestDivision:
    """Tests for the divide method (Assignment 1)."""

    def test_divide_positive_numbers(self, calc):
        assert calc.divide(5, 3) == pytest.approx(1.6666666666666667)

    def test_divide_negative_numbers(self, calc):
        assert calc.divide(-5, -3) == pytest.approx(1.6666666666666667)

    def test_divide_positive_and_negative(self, calc):
        assert calc.divide(5, -3) == pytest.approx(-1.6666666666666667)

    def test_divide_negative_and_positive(self, calc):
        assert calc.divide(-5, 3) == pytest.approx(-1.6666666666666667)

    def test_divide_zero_with_positive(self, calc):
        assert calc.divide(0, 5) == 0

    def test_divide_zero_with_negative(self, calc):
        assert calc.divide(0, -5) == 0

    def test_divide_floats(self, calc):
        assert calc.divide(2.5, 3.7) == pytest.approx(0.6756756756756757)

    def test_divide_by_zero(self, calc):
        """Test division by zero raises appropriate error."""
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)


# --- ここから下が今回不足していた部分です（必ず含めてください） ---

class TestInvalidInputs:
    """
    Tests for Assignment 2: Coverage & Bug Fix Verification.
    ここがないと、入力チェック部分のカバレッジが上がらず、Mutantも倒せません。
    """
    
    def test_input_too_large(self, calc):
        """Test with value exceeding MAX_VALUE (1,000,000)."""
        # 最大値より大きい値を入れたらエラーになるかチェック
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 1)

    def test_input_too_small(self, calc):
        """Test with value below MIN_VALUE (-1,000,000)."""
        # 最小値より小さい値を入れたらエラーになるかチェック
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 1)

    def test_invalid_second_argument(self, calc):
        """
        2番目の引数もしっかりチェックしているか。
        （calculator.pyの修正が効いているか確認）
        """
        with pytest.raises(InvalidInputException):
            calc.add(1, 1000001)

    def test_invalid_multiple_arguments_divide(self, calc):
        """割り算でもチェックが効くか"""
        with pytest.raises(InvalidInputException):
            calc.divide(1000001, 1)


class TestBoundaries:
    """
    Tests for Assignment 3: Mutation Testing (Boundary Analysis).
    ここがないと、> と >= の違いなどのMutantが生き残ります。
    """

    def test_boundary_max_value(self, calc):
        """
        ちょうど 1,000,000 はOKなはず。
        これがあれば 'val > MAX' を 'val >= MAX' に書き換えられたときに検知できます。
        """
        assert calc.add(1000000, 0) == 1000000

    def test_boundary_min_value(self, calc):
        """
        ちょうど -1,000,000 はOKなはず。
        これがあれば 'val < MIN' を 'val <= MIN' に書き換えられたときに検知できます。
        """
        assert calc.add(-1000000, 0) == -1000000

    def test_boundary_just_above_max(self, calc):
        """1,000,001 は即アウトになるべき"""
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 0)

    def test_boundary_just_below_min(self, calc):
        """-1,000,001 は即アウトになるべき"""
        with pytest.raises(InvalidInputException):
            calc.add(-1000001, 0)