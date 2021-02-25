import pytest

from spin_the_wheel.player import InputPlayerScene


@pytest.fixture()
def monkeypatch_input(monkeypatch):
    def factory(to_print: [int, str, ...]):
        context = {'count': 0}

        def stub(_):
            count = context.get('count')
            content = to_print[count]
            context['count'] = count + 1
            return content

        monkeypatch.setattr('builtins.input', stub)

    return factory


class Test_input_players:
    def test_should_create_one_player_if_passed_only_1(self, monkeypatch_input):
        monkeypatch_input([1, 'wow'])
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'
        assert players[0].money == 0

    def test_should_create_the_number_of_players_it_was_passed(self, monkeypatch_input):
        monkeypatch_input([2, 'wow', 'go'])
        players = InputPlayerScene.input_players()

        assert len(players) == 2
        assert players[0].name == 'Wow'
        assert players[1].name == 'Go'

    def test_should_ask_again_for_the_player_name_if_none_was_given(self, monkeypatch_input):
        monkeypatch_input([2, 'wow', '', 'go'])
        players = InputPlayerScene.input_players()

        assert len(players) == 2
        assert players[0].name == 'Wow'
        assert players[1].name == 'Go'

    def test_should_ask_again_for_the_number_of_players_if_number_is_smaller_than_1(self, monkeypatch_input):
        monkeypatch_input([-1, 0, 1, 'wow'])
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'

    def test_should_ask_again_for_the_number_of_players_if_input_was_not_a_number(self, monkeypatch_input):
        monkeypatch_input(['a', '', 'vozes', 1, 'wow'])
        players = InputPlayerScene.input_players()

        assert len(players) == 1
        assert players[0].name == 'Wow'
