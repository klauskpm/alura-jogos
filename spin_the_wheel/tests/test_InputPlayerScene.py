from unittest import mock

from spin_the_wheel.player import InputPlayerScene


class Test_input_players:
    @mock.patch('builtins.input', side_effect=[1, 'wow'])
    def test_should_create_one_player_if_passed_only_1(self, _input):
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'
        assert players[0].money == 0
        assert _input.call_count == 2

    @mock.patch('builtins.input', side_effect=[2, 'wow', 'go'])
    def test_should_create_the_number_of_players_it_was_passed(self, _input):
        players = InputPlayerScene.input_players()

        assert len(players) == 2
        assert players[0].name == 'Wow'
        assert players[1].name == 'Go'
        assert _input.call_count == 3

    @mock.patch('builtins.input', side_effect=[2, 'wow', '', 'go'])
    def test_should_ask_again_for_the_player_name_if_none_was_given(self, _input):
        players = InputPlayerScene.input_players()

        assert len(players) == 2
        assert players[0].name == 'Wow'
        assert players[1].name == 'Go'
        assert _input.call_count == 4

    @mock.patch('builtins.input', side_effect=[-1, 0, 1, 'wow'])
    def test_should_ask_again_for_the_number_of_players_if_number_is_smaller_than_1(self, _input):
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'
        assert _input.call_count == 4

    @mock.patch('builtins.input', side_effect=['a', '', 'vozes', 1, 'wow'])
    def test_should_ask_again_for_the_number_of_players_if_input_was_not_a_number(self, _input):
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'
        assert _input.call_count == 5
