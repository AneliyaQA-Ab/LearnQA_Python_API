class TestPhraseLength:
    def test_check_phrase(self):
        phrase = input("Set a phrase less than 15 symbols: ")
        expected_len = 14 #фраза должна быть короче 15 символов, граничное допустимое  значение символов 14
        assert len(phrase) <= expected_len, f"Length of input phrase  should not exceed {expected_len} symbols"




