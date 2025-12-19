import subprocess
import sys

# Paths
paths = [
    'projects/1_OrdenaFluxo/main.py',
    'projects/2_DijkstraNet/main.py',
    'projects/3_HuffmanCompressor/main.py',
    'projects/4_PairView/main.py',
    'projects/5_SeqAlign/main.py'
]

# Python script
try:
    subprocess.run(['python', paths[int(sys.argv[1])-1]])
except IndexError:
    print('Erro: Você deve executar o script no terminal com o argumento "1-5".')
except Exception:
    print('Erro: O argumento deve ser um inteiro de 1 a 5.')