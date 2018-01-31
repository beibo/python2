from lab1 import removeVowle
from lab2 import characterlocator
from ass3 import mulitiTable
from ass4 import calcArea
from lab5 import dictionary
from ass6 import marioPyradim
import unittest

class Testlab1(unittest.TestCase):
    def test_removeVowle(self):
        self.assertEqual(removeVowle("ahmed"),"hmd");
        self.assertEqual(removeVowle("MobilE"),"Mbl");
        self.assertEqual(removeVowle("rEmOve"),"rmv");

    def test_characterlocator(self):
        self.assertEqual(characterlocator("mohamed","m"),[0,4]);
        self.assertEqual(characterlocator("assso","o"),[4]);

    def test_mulitiTable(self):
        self.assertEqual(mulitiTable(3),[[1], [2, 4], [3, 6, 9]]); 
        self.assertEqual(mulitiTable(2),[[1], [2, 4]]);
        self.assertEqual(mulitiTable(4),[[1],[2,4],[3,6,9],[4,8,12,16]]);

    def test_calcArea(self):
        self.assertEqual(calcArea("t",4,5),10.0);
        self.assertEqual(calcArea("c",4),12);
        self.assertEqual(calcArea("r",4,2),16);
        self.assertEqual(calcArea("mm",4,5),"your char not corect plez enter anthor one");

    def test_dictionary(self):
        self.assertEqual(dictionary(['fggggggggg', 'atma', 'ibrahim']),{'a': ['atma'], 'i': ['ibrahim'], 'f': ['fggggggggg']});


    # def test_marioPyradim(self):
    #     self.assertEqual(marioPyradim(3),"""('  ', '*')
    #     (' ', '**')
    #     ('', '***')""");    


        
            





if __name__=="__main__":

    unittest.main();    