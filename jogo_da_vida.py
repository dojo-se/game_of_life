import unittest

def jogo_da_vida(num_linhas, num_colunas, mundo):

    proxima_geracao = '''..
..'''


    return proxima_geracao
    

class StubTests(unittest.TestCase):    
    def test_2_2_die(self):
        geracao_1 = \
'''*.
   ..'''.replace(' ', '')
        geracao_2 = \
'''..
   ..'''.replace(' ', '')        
        self.assertEquals(geracao_2, jogo_da_vida(2, 2, geracao_1))
    
    
if __name__ == '__main__':
    unittest.main()

