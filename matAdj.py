# Teoria dos Grafos => 16/05/2023


class Grafo(object):
  def __init__(self, orientado=False):
    self.n, self.m, self.orientado = None, None, orientado # n = |v|, m = |e|

  def DefinirN(self, n):
    self.n, self.m = n, 0

  def V(self): #gera os vertices
    for i in range(1, self.n+1):
      yield i # yield <==> iteracao

  def E(self, IterarSobreNo=False):
    for v in self.V():
      for w in self.N(v, Tipo="+" if self.orientado else "*", IterarSobreNo=IterarSobreNo):
        enumerar = True
        if not self.orientado():
          wint = w if isinstance(w, int) else w.Viz
          enumerar = v < wint
        if enumerar:
          yield (v, w)

class GrafoMatrizAdj(Grafo):
  def DefinirN(self, n):
    super(GrafoMatrizAdj, self).DefinirN(n)
    self.M = [None] * self.n+1
    for i in range(1, self.n +1):
      self.M[i] = [0]*self.n+1
    
  def RemoverAresta(self, u, v):
    self.M[u][v] = 0
    if not self.orientado:
      self.M[v][u]=0
    self.m = self.m-1

  def AdicionarAresta(self, u, v):
    self.M[u][v] = 1
    if not self.orientado:
      self.M[v][u] = 1

  def SaoAdj(self, u, v):
    return self.M[u][v] == 1

  def N(self, v, Tipo = "*",  Fechada = False, IterarSobreNo=False):
    if Fechada:
      yield v
    w = 1
    t = "+" if Tipo == "*" and self.orientado else Tipo
    while w <= self.n:
        if t =="+":
            orig, dest, viz = v, w, w
        else:
            orig, dest, viz = w, v, w

        if self.SaoAdj(orig, dest):
            yield w
        w = w + 1
        if w > self.n and t == "+" and Tipo == "*":
            t, w = "-", 1