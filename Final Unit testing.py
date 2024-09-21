import unittest
import Final_Coursework_1_Grid_Method


class TestmyFinal_Coursework_1_Grid_Method(unittest.TestCase):        
    
    def test_create_first_row(self):
        self.assertEqual(Final_Coursework_1_Grid_Method.create_first_row(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
                                                    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8'
                                                    , '9', ' ', '.', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '\\', '|', '}', ']', '{', '[', ':', ';', '?', '/', '>',
                                                    '<', "'", "'", '\n'])
    
    def test_create_grid(self):
        self.assertEqual(len(Final_Coursework_1_Grid_Method.create_grid(Final_Coursework_1_Grid_Method.create_first_row())), 95)
    
    
    def test_crate_index_dict(self):
        self.assertEqual(len(Final_Coursework_1_Grid_Method.create_index_dictionary(Final_Coursework_1_Grid_Method.create_first_row())), 94)
    

    def test_encrypt_phrase(self):
        self.assertEqual(Final_Coursework_1_Grid_Method.encrypt_phrase("sad", "Hello", Final_Coursework_1_Grid_Method.create_grid(Final_Coursework_1_Grid_Method.create_first_row()), Final_Coursework_1_Grid_Method.create_index_dictionary(Final_Coursework_1_Grid_Method.create_first_row())), "z4!|!")

    def test_decrypt_phrase(self):
        self.assertEqual(Final_Coursework_1_Grid_Method.decrypt_phrase("sad", "z4!|!", Final_Coursework_1_Grid_Method.create_grid(Final_Coursework_1_Grid_Method.create_first_row()), Final_Coursework_1_Grid_Method.create_index_dictionary(Final_Coursework_1_Grid_Method.create_first_row())), "Hello")



if __name__ == "__main__":
    unittest.main()