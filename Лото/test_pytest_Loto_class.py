from Loto_class import Loto


class TestLoto:
    def test_refill_numbers_in_game(self):
        loto = Loto()
        loto.numbers_in_game.remove(1)
        assert loto.numbers_in_game == list(range(2, 91))
        loto.refill_numbers_in_game()
        assert loto.numbers_in_game == list(range(1, 91))

    def test_get_random_number(self):
        loto = Loto()
        loto.get_random_number()
        assert loto.current_number != any(loto.numbers_in_game)

    def test_new_card_number(self):
        loto = Loto()
        loto.new_card_number()
        for number in loto.card_number:
            assert number in list(range(1, 91))

    def test_compute_card(self):
        loto = Loto()
        loto.new_card_number()
        loto.compute_card()
        for number in loto.card_number:
            assert str(number) in loto.card
