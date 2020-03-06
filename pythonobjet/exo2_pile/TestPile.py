import unittest

# empiler
# depiler
# exception quand pile est pleine
#exception quand pile est vide
from pythonobjet.exo2_pile.Pile import Pile
from pythonobjet.exo2_pile.PileException import PileExceptionPleine, PileExceptionVide


class TestPile(unittest.TestCase):

    def testEmpiler(self):
        print("=====debut test empiler====")
        p = Pile(2)
        self.assertEqual(p.getTaille(), 0)
        p.empiler(20)
        self.assertEqual(p.getTaille(), 1)

    def testDepiler(self):
        print("=====debut test depiler====")
        p = Pile(2)
        p.empiler(20)
        self.assertEqual(p.getTaille(), 1)
        p.depiler()
        self.assertEqual(p.getTaille(), 0)

    def testExceptionPilePleine(self):
        print("=====debut test testExceptionPilePleine====")
        p = Pile(2)
        p.empiler(20)
        p.empiler(20)
        with self.assertRaises(PileExceptionPleine) as context:
            p.empiler(20)


    def testExceptionPileVide(self):
        print("=====debut test testExceptionPileVide====")
        p = Pile(2)
        p.empiler(20)
        p.depiler()

        with self.assertRaises(PileExceptionVide) as context:
            p.depiler()




if __name__ == '__main__':
    unittest.main()
