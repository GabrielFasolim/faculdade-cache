class Cache:
    def __init__(self,size):
        self.size = size
        self.cache = [-1] * size
        self.miss = 0
        self.hits = 0

        print('Memoria Inicializada')
        print('Tamanho da cache:', self.size)
        self.__printCache(0)

    def __printCache(self, position):
        print('\n')
        print('Posição desejada:', position)
        print('Hits:', self.hits)
        print('Miss:', self.miss)

        if self.hits+self.miss !=0:
            print('Acertividade:', self.hits/(self.miss+self.hits))

        print('Memórias acessadas:', self.hits+self.miss)

        for i in range (0,len(self.cache)):
            print(i, ' - ', self.cache[i])


    def mapeamentoDireto(self, positions):
        for position in positions:
            line = position % self.size

            if self.cache[line] == line:
                self.hits+=1
            else:
                self.miss+=1

            self.cache[line] = position
            self.__printCache(position)






