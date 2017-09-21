
"""
todo: docstring rsrs
"""

class Elevador:

    """
    todo: docstring
    """

    def __init__(self):

        """
        todo: docstring
        """

        self.andar_atual = 0
        self.porta = "aberta"
        self.status = "parado"
        self.direcao = "nenhuma"
        self.rota = []
        self.passageiros = 0
        self.limite = 10
        self.ativo = True

        self.atualiza_status()


    def atualiza_status(self):

        """
        todo: docstring
        """

        print("\n==================================================")
        print("===================== STATUS =====================")
        print("==================================================")
        print("Andar: " + str(self.andar_atual))
        print("Status: " + str(self.status))
        print("Porta: " + str(self.porta))
        print("Rota: " + str(self.rota))
        print("Passageiros: " + str(self.passageiros))
        print("Limite: " + str(self.limite))


    def seguir(self):

        """
        todo: docstring
        """

        if self.rota:

            if self.andar_atual < self.rota[0]:

                for i in range(self.andar_atual, self.rota[0] + 1):

                    self.andar_atual = i
                    self.status = "subindo"
                    self.porta = "fechada"

                    self.atualiza_status()

                    if self.andar_atual in self.rota:
                        self.rota.remove(self.andar_atual)
                        self.status = "parado"
                        self.porta = "aberta"
                        self.atualiza_status()
        
        if self.rota:

            if self.andar_atual > self.rota[0]:

                for i in range(self.andar_atual, self.rota[0] - 1, -1):

                    self.andar_atual = i
                    self.status = "descendo"
                    self.porta = "fechada"

                    self.atualiza_status()

                    if self.andar_atual in self.rota:
                        self.rota.remove(self.andar_atual)
                        self.status = "parado"
                        self.porta = "aberta"
                        self.atualiza_status()


    def solicitar(self, andar, direcao):

        """
        todo: docstring
        """

        if andar < 0 or andar > 10:
            raise Exception("Andar " + str(andar) + " nao existe.")

        if direcao == "subir":
            direcao = "cima"

        if direcao == "descer":
            direcao = "baixo"

        if not self.rota or self.direcao == "nenhuma":
            self.direcao = direcao

        self.atualiza_rota(andar)


    def atualiza_rota(self, andar):

        """
        todo: docstring
        """

        if andar < 0 or andar > 10:
            raise Exception("Andar " +  str(andar) + " nao existe.")

        rota1 = []
        rota2 = []

        self.rota.append(andar)

        for n in self.rota: # pylint: disable=invalid-name

            if n < self.andar_atual:
                rota1.append(n)

            if n > self.andar_atual:
                rota2.append(n)

        if self.direcao == "nenhuma":

            if self.rota[0] > self.andar_atual:
                self.direcao = "cima"

            if self.rota[0] < self.andar_atual:
                self.direcao = "baixo"

        if self.direcao == "cima":
            rota1 = sorted(list(set(rota1)), reverse=True)
            rota2 = sorted(list(set(rota2)))
            self.rota = rota2 + rota1

        if self.direcao == "baixo":
            rota1 = sorted(list(set(rota1)), reverse=True)
            rota2 = sorted(list(set(rota2)))
            self.rota = rota1 + rota2


    def embarcar(self, numPessoas):

        """
        todo: docstring
        """
        
        if self.passageiros + numPessoas > self.limite:
            print("Numero de passageiros superior a capacidade maxima.")
        else:
            self.passageiros += numPessoas


    def desembarcar(self, numPessoas):

        """
        todo: docstring
        """

        if self.passageiros - numPessoas < 0:
            raise Exception('Numero de passageiros invalido (negativo).')
        else:
            self.passageiros -= numPessoas
