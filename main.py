"""
Elevador consiste em uma classe para simulacao de acoes de um elevador social.
"""

from Elevador import Elevador

elevador = Elevador() # pylint: disable=invalid-name

while elevador.ativo:

    elevador.atualiza_status()

    if elevador.status == "parado":

        entrada = input("Comando: ").split() # pylint: disable=invalid-name

        if entrada[0] == "fim":
            elevador.ativo = False

        if entrada[0] == "solicitar":
            elevador.solicitar(entrada[1], entrada[2])
