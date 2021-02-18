import pytest

from spin_the_wheel.player import Player, InvalidAmount


class Test___init__:
    def test_should_set_the_player_name_and_money(self):
        player = Player('Test', 120)

        assert player.name == 'Test'
        assert player.money == 120

    def test_should_set_the_money_to_zero_if_none_is_declared(self):
        player = Player('Test')

        assert player.name == 'Test'
        assert player.money == 0

    def test_should_not_accept_a_negative_amount_of_money(self):
        with pytest.raises(InvalidAmount):
            Player('Test', -120)

    def test_should_clean_and_title_case_the_player_name(self):
        player = Player('   KLAUS kazlauskas PAoli machADO     ')

        assert player.name == 'Klaus Kazlauskas Paoli Machado'

    def test_should_not_let_the_money_to_be_reassigned(self):
        with pytest.raises(AttributeError):
            player = Player('Test')
            player.money = 20

    def test_should_not_let_the_name_to_be_reassigned(self):
        with pytest.raises(AttributeError):
            player = Player('Test')
            player.name = 'Error'


class Test_add_money:
    def test_should_increase_the_amount_of_money(self):
        player = Player('Test')
        player.add_money(12)

        assert player.money == 12

    def test_should_raise_error_if_negative_value_is_passed(self):
        with pytest.raises(InvalidAmount):
            player = Player('Test')
            player.add_money(-12)


class Test_takes_money:
    def test_should_decrease_and_return_the_amount_of_money(self):
        player = Player('Test', 100)
        money_taken = player.takes_money(100)

        assert money_taken == 100
        assert player.money == 0

    def test_should_raise_error_if_negative_value_is_passed(self):
        with pytest.raises(InvalidAmount):
            player = Player('Test', 100)
            player.takes_money(-100)

    def test_should_raise_error_if_amount_is_bigger_than_what_the_player_has(self):
        with pytest.raises(InvalidAmount):
            player = Player('Test', 100)
            player.takes_money(101)

