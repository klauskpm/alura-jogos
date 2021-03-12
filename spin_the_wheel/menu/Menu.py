from .exceptions import InvalidMenuOption


class Menu:
    def __init__(self, label, options: dict):
        self._label = label
        self._options = options

    def input_menu(self):
        print(self._label)
        for key in self._options.keys():
            option = self._options.get(key)
            description = option['description']
            print(f'[{key}] {description}')

        input_option = input('')
        selected_option = self._options.get(input_option)

        if selected_option is None:
            raise InvalidMenuOption('Escolha uma opção válida')

        return selected_option['action']
