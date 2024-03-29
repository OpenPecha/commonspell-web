from common_spell import get_common_spell_matrix
from common_spell import serialize_matrix_plaintext
from common_spell import serialize_matrix_docx


def test_common_spell_matrix():
    examplar_text = "རྒྱུ་དང་རྐྱེན་གྱིས་འཇུག་པ་ཡང་།"
    version_texts = {
        'version_2.txt': 'རྒྱུ་དད་རྐྱེན་ཀྱིས་འཇུག་པ་ཡང་།',
        'version_3.txt': 'རྒྱུ་དང་རྐྱེན་གྱིས་འཇུག་པའི་ཡང་།',
        'version_4.txt': 'རྒྱུ་དང་རྐྱེན་ཀྱིས་འཇུག་པ་ཡང་།'
    }

    common_spell_matrix = get_common_spell_matrix(examplar_text, version_texts)
    expected_common_spell_matrix = [
        [(0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100)],
        [(5, 8, 1, 'དང་', 75), (5, 8, 1, 'དད་', 25), (5, 8, 1, 'དང་', 75), (5, 8, 1, 'དང་', 75)],
        [(8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100)],
        [(14, 19, 1, 'གྱིས་', 50), (14, 19, 1, 'ཀྱིས་', 50), (14, 19, 1, 'གྱིས་', 50), (14, 19, 1, 'ཀྱིས་', 50)],
        [(19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100)],
        [(24, 26, 1, 'པ་', 75), (24, 26, 1, 'པ་', 75), (24, 28, 1, 'པའི་', 25), (24, 26, 1, 'པ་', 75)],
        [(26, 29, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100), (28, 31, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100)],
        [(29, 30, 1, '།', 100), (29, 30, 1, '།', 100), (31, 32, 1, '།', 100), (29, 30, 1, '།', 100)]
        ]
    assert common_spell_matrix == expected_common_spell_matrix

def test_serialize_plain_text():
    weighted_matrix = [
        [(0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100)],
        [(5, 8, 1, 'དང་', 75), (5, 8, 1, 'དད་', 25), (5, 8, 1, 'དང་', 75), (5, 8, 1, 'དང་', 75)],
        [(8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100)],
        [(14, 19, 1, 'གྱིས་', 25), (14, 19, 1, 'ཀྱིས་', 75), (14, 19, 1, 'ཀྱིས་', 75), (14, 19, 1, 'ཀྱིས་', 75)],
        [(19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100)],
        [(24, 26, 1, 'པའི་', 50), (24, 26, 1, 'པ་', 50), (24, 28, 1, 'པའི་', 50), (24, 26, 1, 'པ་', 50)],
        [(26, 29, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100), (28, 31, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100)],
        [(29, 30, 1, '།', 100), (29, 30, 1, '།', 100), (31, 32, 1, '།', 100), (29, 30, 1, '།', 100)],
        ]
    expected_serialized_matrix = "རྒྱུ་དང་རྐྱེན་ཀྱིས་འཇུག་པའི་ཡང་།"
    plain_text = serialize_matrix_plaintext(weighted_matrix)
    assert plain_text == expected_serialized_matrix

def test_serialize_docx():
    version_texts = {
        'version_1.txt': 'རྒྱུ་དང་རྐྱེན་གྱིས་འཇུག་པ་ཡང་།',
        'version_2.txt': 'རྒྱུ་དད་རྐྱེན་ཀྱིས་འཇུག་པ་ཡང་།',
        'version_3.txt': 'རྒྱུ་དང་རྐྱེན་གྱིས་འཇུག་པའི་ཡང་།',
        'version_4.txt': 'རྒྱུ་དང་རྐྱེན་ཀྱིས་འཇུག་པ་ཡང་།'
    }
    weighted_matrix = [
        [(0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100), (0, 5, 1, 'རྒྱུ་', 100)],
        [(5, 8, 1, 'དང་', 75), (5, 8, 1, 'དད་', 25), (5, 8, 1, 'དང་', 75), (5, 8, 1, 'དང་', 75)],
        [(8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100), (8, 14, 1, 'རྐྱེན་', 100)],
        [(14, 19, 1, 'གྱིས་', 25), (14, 19, 1, 'ཀྱིས་', 75), (14, 19, 1, 'ཀྱིས་', 75), (14, 19, 1, 'ཀྱིས་', 75)],
        [(19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100), (19, 24, 1, 'འཇུག་', 100)],
        [(24, 26, 1, 'པའི་', 50), (24, 26, 1, 'པ་', 50), (24, 28, 1, 'པའི་', 50), (24, 26, 1, 'པ་', 50)],
        [(26, 29, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100), (28, 31, 1, 'ཡང་', 100), (26, 29, 1, 'ཡང་', 100)],
        [(29, 30, 1, '།', 100), (29, 30, 1, '།', 100), (31, 32, 1, '།', 100), (29, 30, 1, '།', 100)],
        ]
    serialize_matrix_docx(weighted_matrix, version_texts)

