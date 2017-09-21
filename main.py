"""
Elevador consiste em uma classe para simulacao de acoes de um elevador social.
"""

from Elevador import Elevador

elevador = Elevador() # pylint: disable=invalid-name

while elevador.ativo:

    if elevador.status == "parado":

        entrada = input("\nComando: ").split() # pylint: disable=invalid-name

        try:

            if entrada[0] == "fim":
                elevador.ativo = False

            elif entrada[0] == "solicitar":
                elevador.solicitar(int(entrada[1]), entrada[2])

            elif entrada[0] == "seguir":
                elevador.seguir()

            elif entrada[0] == "rota":
                for i in range(1, len(entrada)):
                    elevador.atualiza_rota(int(entrada[i]))

            elif entrada[0] == "embarcar":
                elevador.embarcar(int(entrada[1]))

            elif entrada[0] == "desembarcar":
                elevador.desembarcar(int(entrada[1]))

        except:
            raise ValueError('Comando invalido.')
