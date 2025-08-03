from typing import Literal


class BalanceBrackets:

    @staticmethod
    def is_balance_brackets(input: str) -> Literal["YES", "NO"]:
        bracket_stack = []
        for character in input:
            if character in ["{", "[", "("]:
                bracket_stack.append(character)

            elif character in ["}", "]", ")"]:
                if not bracket_stack:
                    return "NO"
                else:
                    counter_character = bracket_stack.pop()
                    if not BalanceBrackets.__is_pair(character, counter_character):
                        return "NO"

        return "NO" if bracket_stack else "YES"

    @staticmethod
    def __is_pair(character, counter_character):
        if character == "}":
            return counter_character == "{"
        elif character == "]":
            return counter_character == "["
        elif character == ")":
            return counter_character == "("
