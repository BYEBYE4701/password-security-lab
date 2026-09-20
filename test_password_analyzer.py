import password_analyzer


def test_character_types():
    result = password_analyzer.check_character_types("Test123!")

    assert result == (True, True, True, True)


def test_lowercase_only():
    result = password_analyzer.check_character_types("hello")

    assert result == (False, True, False, False)

def test_entropy_lowercase():
    result = password_analyzer.calculate_entropy(
        "hello",
        False,
        True,
        False,
        False
    )

    entropy = result[1]

    assert round(entropy, 2) == 23.50

def test_crack_time():
    result = password_analyzer.estimate_crack_time(30)

    seconds = result[1]

    assert round(seconds, 4) == 1.0737