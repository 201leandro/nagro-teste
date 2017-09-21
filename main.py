"""
Elevador consiste em uma classe para simulacao de acoes de um elevador social.
"""

from Elevador import Elevador

elevador = Elevador() # pylint: disable=invalid-name

while elevador.ativo:

    if elevador.status == "parado":

        entrada = input("\nComando: ").split() # pylint: disable=invalid-name

        if entrada[0] == "fim":
            elevador.ativo = False

        if entrada[0] == "solicitar":
            elevador.solicitar(int(entrada[1]), entrada[2])

        if entrada[0] == "seguir":
            elevador.seguir()

        if entrada[0] == "rota":
            for i in range(1, len(entrada)):
                elevador.atualiza_rota(int(entrada[i]))

        if entrada[0] == "andar":
            elevador.andar_atual = int(entrada[1])

        if entrada[0] == "dir":
            elevador.direcao = entrada[1]

