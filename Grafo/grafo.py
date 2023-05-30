class Grafo(object):
    # Classe base para as classes GrafoListaAdj  e Grafo MatrizAdj
    def __init__(self, orientado=False):
        #Grafo se orientado = False ou Digrafo se orientado = True
        self.n = None
        self.m = None
        self.orientado = orientado

    def DefinirN(self, n):
        #Define o número n de vértices
        self.n = n
        self.m = 0

    def V(self):
        #retorna a lista de vértices
        for i in range(1, self.n+1):
            yield i

    def E(self, IterarSobreNo=False):
        '''
        Retorna lista de arestas uv, onde u é um inteiro e v é um inteiro
        se o grafo é GrafoMatrizAdj e IterarSobreNo=False
        ou v é GrafoListaAdj.NoAresta, caso contrário
        '''
        for v in self.V():
            for w in self.N(v, Tipo = "+" if self.orientado else "*", IterarSobreNo=IterarSobreNo):
                enumerar = True
                if not self.orientado:
                    wint = w if isinstance(w,int) else w.Viz
                    enumerar = v < wint
                if enumerar:
                    yield (v, w)

class GrafoMatrizAdj(Grafo):
    def DefinirN(self, n):
        super(GrafoMatrizAdj, self).DefinirN(n)
        self.M = [None]*(self.n + 1)
        for i in range(1, self.n + 1):
            self.M[i] = [0] * (self.n + 1)

    def RemoverAresta(self, u, v):
        self.M[u][v] = 0
        if not self.orientado:
            self.M[v][u] = 0
        self.m = self.m - 1

    def AdcionarAresta(self, u, v):
        self.M[u][v] = 1
        if not self.orientado:
            self.M[v][u] = 1
        self.m = self.m + 1

    def SaoAdj(self, u, v):
        #Retorna True sss uv é uma aresta
        return self.M[u][v] == 1

    def N(self, v, Tipo="*", Fechada=False, IterarSobreNo=False):
        '''
            Retorna lista de vértices vizinhos do vértice v
            Se Fechada=True, o próprio v é incluido na lista
            Tipo ="*" => lista todas as arestas incidentes em v
                e G é orientado
            Tipo ="+" => lista as arestas de saída de v
            Tipo ="-" => lista as arestas de entrada em v
            IterarSobreNo não tem efeito em  Matriz de Adj
        '''
        if Fechada:
            yield v
        w = 1
        t = "+" if Tipo == "*" and self.orientado else Tipo
        while w <= self.n:
            if t == "+":
                orig, dest, viz = v, w, w
            else:
                orig, dest, viz = w, v, w
            if self.SaoAdj(orig, dest):
                yield w
            w = w + 1
            if w > self.n and t == "+" and Tipo == "*":
                t, w = "-", 1


class GrafoListaAdj(Grafo):
    class NoAresta(object):
        """
        Objeto nó da lista de adjacência.
        Atributos:
        - Viz (vizinho)
        - e (aresta)
        - Tipo (+/-)
        - Prox (proxima aresta na lista de adjacência)
        - Ant (aresta anterior na lista de adjacência, se a lista for 
            duplamente encadeada)
        """

        def __init__(self):
            self.Viz = None
            self.e = None
            self.Prox = None
    class Aresta(object):
        """
        Objeto único para representar a aresta.
        Atributos:
        - v1, No1 (um dos vertices da aresta e seu respectivo nó, i.e, v1 == No1.Viz)
        - v2, No2 (análogo em relação ao segundo vertice)
        """

        def __init__(self):
            self.v1, self.No1 = None, None
            self.v1, self.No2 = None, None
        
    def DefinirN(self, n, VizinhancaDuplamenteLigada=False):
        """
        Define o número n de vértices.
        Se VizinhancaDuplamenteLigada=True, a lista encadeada
        dos vizinhos de um vertice é duplamente ligada,
        permitindo remoção de arestas de tempo constante.
        """

        super(GrafoListaAdj, self).DefinirN(n)
        self.L = [None]*(self.n+1)
        for i in range(1, self.n+1):
            self.L[i] = GrafoListaAdj.NoAresta() #nó cabeça
        self.VizinhancaDuplamenteLigada = VizinhancaDuplamenteLigada
    