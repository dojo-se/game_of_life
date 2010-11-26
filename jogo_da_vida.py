import unittest

def jogo_da_vida(num_linhas, num_colunas, mundo):

    matriz = mundo.split()
    
    for pos_linha, linha in enumerate(matriz):
        for pos_coluna, celula in enumerate(linha):
            num_vizinhos_vivos = 0
            
            #diagonal superior esquerda
            if pos_linha -1 >= 0 and pos_coluna -1 >= 0:
                if matriz[pos_linha -1][pos_coluna -1] == '*':
                    num_vizinhos_vivos += 1
                    
            #superior
            if pos_linha - 1 >= 0:
                if matriz[pos_linha - 1][pos_coluna] == '*':
                    num_vizinhos_vivos += 1
                    
            #diagonal superior direita
            if pos_linha - 1 >= 0 and pos_coluna + 1 < num_colunas :
                if matriz[pos_linha - 1][pos_coluna + 1] == '*':
                    num_vizinhos_vivos += 1
            
            #lateral direita
            if pos_coluna + 1 < num_colunas:
                if matriz[pos_linha][pos_coluna + 1] == '*':
                    num_vizinhos_vivos += 1
            
            #diagonal inferior direita
            if pos_linha + 1 < num_linhas and pos_coluna + 1 < num_colunas:
                if matriz[pos_linha + 1][pos_coluna + 1] == '*':
                    num_vizinhos_vivos += 1
            
            #inferior
            if pos_linha +1 < num_linhas:
                if matriz[pos_linha + 1][pos_coluna] == '*':
                    num_vizinhos_vivos+= 1
                    
            #diagonal inferior esquerda
            if pos_linha + 1 < num_linhas and pos_coluna - 1 >= 0:
                if matriz[pos_linha + 1][pos_coluna - 1] == '*':
                    num_vizinhos_vivos += 1
            
            #lateral esquerda
            if pos_coluna - 1 >= 0:
                if matriz[pos_linha][pos_coluna - 1] == '*':
                    num_vizinhos_vivos += 1

            #ele morre 
            if celula == '*' and num_vizinhos_vivos < 2 or num_vizinhos_vivos > 3:
                lista = list(matriz[pos_linha])
                lista[pos_coluna] = '.'
                matriz[pos_linha] = reduce(lambda x,y: x + y, lista)           
            
            #ele surge 
            if celula == '.' and num_vizinhos_vivos == 3:
                lista = list(matriz[pos_linha])
                lista[pos_coluna] = '*'
                matriz[pos_linha] = reduce(lambda x,y: x + y, lista)
                
    proxima_geracao = ''            
    for linha in matriz:
        proxima_geracao += linha + '\n'            
                
    return proxima_geracao[:-1]
    
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

