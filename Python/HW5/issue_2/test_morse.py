import pytest
from morse import decode


@pytest.mark.parametrize('s,exp', [
 ('STRING', '... - .-. .. -. --.'),
 ('123', '.---- ..--- ...--'),
 ('WITH./-()', '.-- .. - .... .-.-.- -..-. -....- -.--. -.--.- ')
])
def test_decode_correct_string(s, exp):
    assert s == decode(exp)
