import pytest
from problems.simple_text_editor.simple_text_editor import SimpleTextEditor


class TestSimpleTextEditor:

    @pytest.fixture()
    def empty_simple_text_editor(self):
        return SimpleTextEditor("")

    def test_able_to_instantiate_simple_text_editor_with_empty_string(
        self, empty_simple_text_editor
    ):
        assert empty_simple_text_editor.initial_str == ""

    def test_able_to_instantiate_simple_text_editor_with_non_empty_string(
        self,
    ):
        text_editor = SimpleTextEditor("abcde")
        assert text_editor.initial_str == "abcde"

    def test_empty_string_text_editor_appends_word_should_work(
        self, empty_simple_text_editor
    ):
        empty_simple_text_editor.append("abc")
        assert empty_simple_text_editor.current_str == "abc"

    def test_non_empty_string_text_editor_appends_word_should_work(self):
        text_editor = SimpleTextEditor("This is a non-empty Text Editor")
        text_editor.append(" - Version 1.1")
        assert (
            text_editor.current_str == "This is a non-empty Text Editor - Version 1.1"
        )

    def test_empty_string_text_editor_delete_k_last_characters_should_do_nothing(
        self, empty_simple_text_editor
    ):
        empty_simple_text_editor.delete_last(3)
        assert empty_simple_text_editor.current_str == ""

    def test_abcde_text_editor_delete_3_last_characters_should_return_ab(self):
        text_editor = SimpleTextEditor("abcde")
        text_editor.delete_last(3)
        assert text_editor.current_str == "ab"

    def test_abc_text_editor_delete_4_last_characters_should_return_empty(self):
        text_editor = SimpleTextEditor("abc")
        text_editor.delete_last(4)
        assert text_editor.current_str == ""

    def test_text_editor_delete_all_chacters_should_return_empty(self):
        text_editor = SimpleTextEditor("abc")
        text_editor.delete_last(3)
        assert text_editor.current_str == ""

    def test_text_editor_print_3rd_of_abcde(self):
        text_editor = SimpleTextEditor("abcde")
        assert text_editor.print(3) == "c"

    def test_text_editor_print_3rd_of_empty_string_should_return_empty(self):
        text_editor = SimpleTextEditor("")
        assert "" == text_editor.print(1)

    def test_text_editor_print_last_character(self):
        text_editor = SimpleTextEditor("abc")
        assert "c" == text_editor.print(3)

    def test_text_editor_print_negative_1_of_non_empty_string_should_return_empty(self):
        text_editor = SimpleTextEditor("abc")
        assert "" == text_editor.print(-1)

    def test_text_editor_print_3_of_len_2_string_should_return_empty(self):
        text_editor = SimpleTextEditor("ab")
        assert "" == text_editor.print(3)

    def test_text_editor_able_to_undo_no_previous_action(self):
        text_editor = SimpleTextEditor("Inital String")
        text_editor.undo()
        assert text_editor.current_str == "Inital String"

    def test_text_editor_undo_append_string_revert_to_previous_state(self):
        text_editor = SimpleTextEditor("Inital String")
        text_editor.append("Additional Text")
        text_editor.undo()
        assert text_editor.current_str == "Inital String"

    def test_text_editor_undo_delete_3_last_chacters_should_revert_to_previous_state(
        self,
    ):
        text_editor = SimpleTextEditor("Inital String")
        text_editor.delete_last(3)
        text_editor.undo()
        assert text_editor.current_str == "Inital String"

    def test_text_editor_undo_more_than_action_should_work(self):
        text_editor = SimpleTextEditor("Initial String")
        text_editor.append("1")
        text_editor.append("2")
        text_editor.undo()
        text_editor.undo()
        text_editor.undo()

        assert text_editor.current_str == "Initial String"
