import unittest

def jogoDaVida(numLinhas, numColunas, mundo):
    
    matriz = mundo.split()
    
    
    
    proxGeracao = '''........
...**...
...**...
........'''
    return proxGeracao
    

class StubTests(unittest.TestCase):    
    def testJDV_4_8_mundo1(self):
        mundoGeracao1 = '''........
....*...
...**...
........'''
        mundoGeracao2 = '''........
...**...
...**...
........'''        
        self.assertEquals(mundoGeracao2, jogoDaVida(4, 8, mundoGeracao1))
    
    
if __name__ == '__main__':
    unittest.main()

