import unittest
import human_cat_dog_years


class HumanCatDogsTest(unittest.TestCase):

    def test_human_years_cat_years_dog_years(self):

        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(1), [1, 15, 15])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(2), [2, 24, 24])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(3), [3, 28, 29])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(4), [4, 32, 34])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(5), [5, 36, 39])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(10), [10, 56, 64])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(50), [50, 216, 264])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years(100), [100, 416, 514])

    def test_human_years_cat_years_dog_years_short(self):

        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(1), [1, 15, 15])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(2), [2, 24, 24])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(3), [3, 28, 29])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(4), [4, 32, 34])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(5), [5, 36, 39])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(10), [10, 56, 64])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(50), [50, 216, 264])
        self.assertEqual(human_cat_dog_years.human_years_cat_years_dog_years_short(100), [100, 416, 514])


if __name__ == '__main__':
    unittest.main()




