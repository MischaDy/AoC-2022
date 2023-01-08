import unittest

from Day25.main import dec_to_snafu, snafu_to_dec, dec_to_pent


class TestSNAFU(unittest.TestCase):
    dec_snafu_examples = [
        ('1', '1'),
        ('2', '2'),
        ('3', '1='),
        ('4', '1-'),
        ('5', '10'),
        ('6', '11'),
        ('7', '12'),
        ('8', '2='),
        ('9', '2-'),
        ('10', '20'),
        ('15', '1=0'),
        ('20', '1-0'),
        ('2022', '1=11-2'),
        ('12345', '1-0---0'),
        ('314159265', '1121-1110-1=0'),
        # ------------------------------------
        ('1747', '1=-0-2'),
        ('906', '12111'),
        ('198', '2=0='),
        ('11', '21'),
        ('201', '2=01'),
        ('31', '111'),
        ('1257', '20012'),
        ('32', '112'),
        ('353', '1=-1='),
        ('107', '1-12'),
        ('7', '12'),
        ('3', '1='),
        ('37', '122'),
    ]

    dec_pent_examples = [
        ('37', '122'),
        ('8', '13'),
        ('99', '344'),
        ('12345', '343340'),
        ('86205', '10224310'),
        ('2621902375', '20332201334000'),
    ]

    @unittest.skip
    def test_dec_to_snafu(self):
        for dec, snafu in self.dec_snafu_examples:
            self.assertEqual(snafu, dec_to_snafu(dec))

    def test_snafu_to_dec(self):
        for dec, snafu in self.dec_snafu_examples:
            self.assertEqual(dec, snafu_to_dec(snafu))

    def test_dec_to_pent(self):
        for i in range(5):
            i_str = str(i)
            self.assertEqual(i_str, dec_to_pent(i_str))
        for dec, pent in self.dec_pent_examples:
            self.assertEqual(pent, dec_to_pent(dec))


if __name__ == '__main__':
    unittest.main()
