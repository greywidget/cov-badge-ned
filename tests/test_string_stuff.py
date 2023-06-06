import pytest

from string_functions import extract_non_ascii_words, get_words


def test_get_words():
    assert get_words("How now, you secret, black, and midnight hags.") == [
        "How",
        "now",
        "you",
        "secret",
        "black",
        "and",
        "midnight",
        "hags",
    ]


@pytest.mark.parametrize(
    "phrase, expected",
    [
        ("He wonede at Ernleȝe at æðelen are chirechen", ["Ernleȝe", "æðelen"]),
        ("Uppen Sevarne staþe sel þar him þuhte", ["staþe", "þar", "þuhte"]),
        ("Onfest Radestone, þer he bock radde", ["þer"]),
        ("Fichier non trouvé", ["trouvé"]),
        ("Over \u0e55\u0e57 57 flavours", ["๕๗"]),
        ("Sí ... habrá que saber algo de Unicode", ["Sí", "habrá"]),
        ("This string only contains ascii words", []),
    ],
)
def test_extract_non_ascii_words(phrase, expected):
    assert extract_non_ascii_words(phrase) == expected
