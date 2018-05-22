import unittest
import accum

class Accum(unittest.TestCase):

    def test_accum(self):
        self.assertEqual(accum.accum("bad"), "B-Aa-Ddd")
        self.assertEqual(accum.accum("GOOD"), "G-Oo-Ooo-Dddd")
        self.assertEqual(accum.accum("PyThOn"), "P-Yy-Ttt-Hhhh-Ooooo-Nnnnnn")
        self.assertEqual(accum.accum("KillOGraMM"), "K-Ii-Lll-Llll-Ooooo-Gggggg-Rrrrrrr-Aaaaaaaa-Mmmmmmmmm-Mmmmmmmmmm")
        self.assertEqual(accum.accum("DevOps"), "D-Ee-Vvv-Oooo-Ppppp-Ssssss")
