from validators import is_valid_email

def test_valid_email():
    assert is_valid_email("alice@example.com")

def test_invalid_email():
    assert not is_valid_email("not-an-email")

def test_non_string_email():
    assert not is_valid_email(None)
