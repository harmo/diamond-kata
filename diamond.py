class Diamond:

    def create(self, char):
        return ''.join(self.get_chars_list(char))

    def get_chars_list(self, char):
        result = []
        for c in self.get_letters_from(char):
            indent = self.indent(c, char)
            if indent != '':
                result.append(indent)

            result.append(c)

            separator = self.separator(c)
            if separator != '':
                result.append(separator)

            if c != 'a':
                result.append(c)

            result.append('\n')

        return result

    def separator(self, current):
        distance = ord(current) - ord('a')
        return ' ' * (distance * 2 - 1)

    def indent(self, current, limit):
        return ' ' * (ord(limit) - ord(current))

    def get_letters_from(self, limit):
        from_a_to_limit = range(ord('a'), ord(limit))

        for o in from_a_to_limit:
            yield chr(o)

        yield limit

        for o in reversed(from_a_to_limit):
            yield chr(o)
