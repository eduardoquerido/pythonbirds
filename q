[1mdiff --git a/atores.py b/atores.py[m
[1mindex f341281..bcd5712 100644[m
[1m--- a/atores.py[m
[1m+++ b/atores.py[m
[36m@@ -115,7 +115,8 @@[m [mclass Passaro(Ator):[m
         o status dos Passaro deve ser alterado para destruido, bem como o seu caracter[m
 [m
         """[m
[31m-        pass[m
[32m+[m[32m        if self.y<=0:[m
[32m+[m[32m            self.status=DESTRUIDO[m
 [m
     def calcular_posicao(self, tempo):[m
         """[m
[36m@@ -131,9 +132,10 @@[m [mclass Passaro(Ator):[m
         :param tempo: tempo de jogo a ser calculada a posição[m
         :return: posição x, y[m
         """[m
[31m-        if self.foi_lancado():[m
[32m+[m[32m        if self._esta_voando():[m
             delta_t = tempo-self._tempo_de_lancamento[m
             self._calcular_posicao_vertical(delta_t)[m
[32m+[m[32m            self._calcular_posicao_horizontal(delta_t)[m
         return super().calcular_posicao(tempo)[m
 [m
 [m
[36m@@ -146,17 +148,27 @@[m [mclass Passaro(Ator):[m
         :param tempo_de_lancamento:[m
         :return:[m
         """[m
[31m-        self._angulo_de_lancamento = angulo[m
[32m+[m[32m        self._angulo_de_lancamento = math.radians(angulo)[m
         self._tempo_de_lancamento = tempo_de_lancamento[m
 [m
     def _calcular_posicao_vertical(self, delta_t):[m
         y_atual = self._y_inicial[m
[31m-        angulo_radianos=math.radians(self._angulo_de_lancamento)[m
[32m+[m[32m        angulo_radianos=self._angulo_de_lancamento[m
         y_atual += self.velocidade_escalar*delta_t * math.sin(angulo_radianos)[m
         y_atual -= (GRAVIDADE*delta_t**2) / 2[m
         self.y=y_atual[m
 [m
 [m
[32m+[m[32m    def _calcular_posicao_horizontal(self, delta_t):[m
[32m+[m[32m        x_atual=self._x_inicial[m
[32m+[m[32m        angulo_radianos = self._angulo_de_lancamento[m
[32m+[m[32m        x_atual+=self.velocidade_escalar*delta_t*math.cos(angulo_radianos)[m
[32m+[m[32m        self.x=x_atual[m
[32m+[m
[32m+[m[32m    def _esta_voando(self):[m
[32m+[m[32m        return self.foi_lancado() and self.status == ATIVO[m
[32m+[m
[32m+[m
 class PassaroAmarelo(Passaro):[m
     _caracter_ativo = 'A'[m
     _caracter_destruido = 'a'[m
[1mdiff --git a/testes/atores_testes.py b/testes/atores_testes.py[m
[1mindex e833eb4..6339ade 100644[m
[1m--- a/testes/atores_testes.py[m
[1m+++ b/testes/atores_testes.py[m
[36m@@ -759,6 +759,7 @@[m [mclass PassaroAmareloTests(PassaroBaseTests):[m
         self.assert_passaro_posicao(1, y, ATIVO, passaro, tempo)[m
 [m
 [m
[32m+[m
 if __name__=='__main__':[m
     teste= AtorTestes()[m
     teste.teste_colisao_entre_atores_ativos()[m
