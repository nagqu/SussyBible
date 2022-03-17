import pytest
from sus import make_sussy, get_verse, fuck


@pytest.mark.parametrize("test_input, expected_string, expected_bool",
                         [("Deuteronomy 11:29 When the Lord your God brings you into the land you are to Kill, you must kill the blessing on Mount Gerizim and the curse on Mount Ebal.", str, True),
                          ("Isaiah 32:20 you will be blessed,you who plant seed by all the banks of the streams, you who let your ox and donkey graze.", str, False),
                          ("God,", str, True),
                          ("Father.", str, True)])
def test_regex_anal_testing(test_input, expected_string, expected_bool):
    string, status = make_sussy(test_input)
    assert type(string) is expected_string
    assert status is expected_bool


def test_get():
    assert type(get_verse()) is not None
