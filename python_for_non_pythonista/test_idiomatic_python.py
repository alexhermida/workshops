import pytest

from idiomatic_python import message_formatting, iterate_list, reverse_list


def test_message_formatting():
    # Input data
    msg_id, msg_type, msg_description = 1, "Warning", "Error in strings"
    # Expected result
    expected = "Message with identifier 1 has type Warning and the description"\
        " is Error in strings."

    assert message_formatting(msg_id, msg_type, msg_description) == expected


@pytest.mark.parametrize("input_list", [
    (["java", "c", "basic", "lisp", "php"]),
    (["aindustriosa", "VigoJUG", "basic"]),
    (["JSVigo"]),
])
def test_iteration(input_list):
    assert iterate_list(input_list) == input_list


@pytest.mark.parametrize("input_list, expected", [
    (["java", "c", "basic", "lisp", "php"], ['php', 'lisp', 'basic', 'c', 'java']),
    (["aindustriosa", "VigoJUG", "basic"], ['basic', 'VigoJUG', 'aindustriosa']),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
])
def test_reverse_iteration(input_list, expected):
    assert reverse_list(input_list) == expected
