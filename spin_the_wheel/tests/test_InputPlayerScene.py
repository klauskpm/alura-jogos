import pytest

from spin_the_wheel.player import InputPlayerScene

INPUT = 'builtins.input'


@pytest.fixture()
def input_stub_factory():
    def factory(players_count: int, names: [str]):
        context = {'count': 0}

        def stub(string):
            content = None
            count = context.get('count')

            if count == 0:
                content = players_count
            else:
                content = names[count - 1]

            context['count'] = count + 1
            return content

        return stub

    return factory


class Test_input_players:
    def test_should_create_one_player_if_passed_only_1(self, monkeypatch, input_stub_factory):
        self.count = 0

        stub = input_stub_factory(1, ['wow'])

        monkeypatch.setattr(INPUT, stub)
        players = InputPlayerScene.input_players()

        assert players[0].name == 'Wow'
        assert players[0].money == 0
