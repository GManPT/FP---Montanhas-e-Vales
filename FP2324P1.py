# "Montanhas e Vales" - Primeiro Projeto (FP2023)

# Declaração da variável global "alfabeto" para efeitos de uso
alfabeto = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


# Declaração de 2.1.1.
def eh_territorio(t):
    """Verifica se o argumento corresponde a um território válido.

    Args:
        t: O argumento a ser verificado.

    Returns:
        bool: True se for um território válido, False caso contrário.
    """
    # Verifique-se se t é um tuplo
    if not isinstance(t, tuple):
        return False  # Não é um território ou é um território vazio
        
    # t deve conter um número de subtuplos compreendidos entre 1 e 26
    elif not 1 <= len(t) <= 26:
        return False
    
    for x in range(len(t)):
        # Note-se que os elementos de t tem de ser eles tuplos também
        if not isinstance(t[x], tuple):
            return False
        
        # Considere-se o minimo de 1 de comprimento e máximo 99 de comprimento para subtuplo
        if not 1 <= len(t[x]) <= 99:
            return False

        # Veja-se se os elementos são 0 ou 1
        for w in t[x]:
            if w != 0 and w != 1 or type(w) != int:
                return False
    
    for y in range(len(t)-1):
        # O subtuplo que segue t[y] deve conter o mesmo tamanho de t[y+1]
        if len(t[y]) < len(t[y + 1]) or len(t[y]) > len(t[y + 1]):
            return False
    
    return True

# Declaração de 2.1.2.
def obtem_ultima_intersecao(t):
    """Obtém a última interseção do território.

    Args:
        t (tuple): O território.

    Returns:
        tuple: A última interseção (letra, número) ou False se não houver interseções válidas.
    """
    # Acede-se à letra do alfabeto que identifica esse elemento
    # Note-se que o indice "-1" faz corresponder ao último elemento
    if eh_territorio(t):
        return (alfabeto[len(t) - 1],len(t[-1]))
    return False

# Declaração de 2.1.3.
def eh_intersecao(i):
    """Verifica se o argumento corresponde a uma interseção válida.

    Args:
        i: O argumento a ser verificado.

    Returns:
        bool: True se for uma interseção válida, False caso contrário.
    """
    # Assume-se que i é tuplo em que: (letra,numero)
    # Aplique-se o valor a partir de 1,2,3,4
    
    # 1 - i é tuplo?
    if type(i) != tuple:
        return False

    # 2 - i tem 2 elementos?
    elif len(i) != 2:
        return False

    # 3 - i[0] é uma letra?
    elif type(i[0]) != str or i[0] not in alfabeto:
        return False
    
    # 4 - i[1] é um número compreendido entre 1 e 99?
    elif type(i[1]) != int or not (1 <= i[1] <= 99):
        return False
    
    return True

# Declaração de 2.1.4.
def eh_intersecao_valida(t, i):
    """Verifica se uma interseção é válida num dado território.

    Args:
        t (tuple): O território.
        i (tuple): A interseção a ser verificada (letra, número).

    Returns:
        bool: True se a interseção for válida, False caso contrário.
    """
    # Se t é território e se i obedeçe ao formato de interseção, então pode-se proceder à validação
    if eh_territorio(t) and eh_intersecao(i):
        # Localize-se o tuplo a que se refere a letra
        posalfabeto = alfabeto.index(i[0])

        # Veja-se se o indice da letra em questão é válido em t
        if not posalfabeto < len(t):
            return False
        # Note-se que i[1]-1 não pode ser maior ou igual que o tamanho do tuplo presente para o dado elemento t
        elif i[1]-1 >= len(t[posalfabeto]):
            return False
        
        return True
    
    return False

# Declaração de 2.1.5.
def eh_intersecao_livre(t, i):
    """Verifica se uma interseção é livre (não ocupada por montanhas) num dado território.

    Args:
        t (tuple): O território.
        i (tuple): A interseção a ser verificada (letra, número).

    Returns:
        bool: True se a interseção for livre, False caso contrário.
    """
    # Aproveite-se 2.1.4
    if eh_intersecao_valida(t,i):
        posalfabeto = alfabeto.index(i[0])

        # Verdadeiro ou falso, dependo se o elemento com indice i[1] dentro do tuplo específico for 0
        return t[posalfabeto][i[1] - 1] == 0
    
    return False

# Declaração de 2.1.6.
def obtem_intersecoes_adjacentes(t,i):
    """Obtém as interseções válidas adjacentes a uma interseção num dado território.

    Args:
        t (tuple): O território.
        i (tuple): A interseção de referência.

    Returns:
        tuple: Tuplo com as interseções válidas adjacentes em ordem de leitura.
    """
    # Seja "a" um tuplo vazio, onde futuramente usar-se-á na retoma da função
    # a deve conter informações relativas às direções (por ordem): Baixo, Esquerda, Direita, Cima
    a = ()

    if eh_intersecao_valida(t,i):
        posalfabeto = alfabeto.index(i[0])

        # Veja-se a direção "baixo" no que toca a interseções. Repara-se que se quer verificar a interseção abaixo da fornecida em i
        # Portanto tem-se de subtrair i[1]-2
        if i[1] - 2 >= 0:
            a = a + ((i[0],i[1] - 1),)
        
        # Veja-se a direção "esquerda"
        if posalfabeto - 1 >= 0:
            a = a + ((alfabeto[posalfabeto - 1], i[1]),)
        
        # Veja-se a direção "direita"
        if posalfabeto + 1 < len(t):
            a = a + ((alfabeto[posalfabeto + 1], i[1]),)

        # Veja-se a direção "cima"
        if i[1] + 1 <= len(t[posalfabeto]):
            a = a + ((i[0],i[1] + 1),)

    else:
        return False
    
    return a

# Declaração de 2.1.7.
def ordena_intersecoes(tup):
    """Ordena as interseções de acordo com a ordem de leitura do território.

    Args:
        tup (tuple): Tuplo de interseções.

    Returns:
        tuple: Tuplo com as interseções ordenadas.
    """
    # Converta-se tuplo para lista numa nova variável
    its = list(tup)

    # Considere-se o intervalo correspondente a [0, len(its) - 1[
    for x in range(len(its) - 1):
        # Lógica: Faça-se o número de iterações neste loop interno diminuir
        for y in range(0, len(its) - x - 1):
            # Nomeie-se os termos consecutivos
            its1 = its[y]
            its2 = its[y + 1]
            
            if its1[1] > its2[1] or (its1[1] == its2[1] and alfabeto.index(its1[0]) > alfabeto.index(its2[0])):
                # Troque-se a ordem das interseções
                its[y], its[y + 1] = its2, its1

    # O valor retomado é um tuplo, pelo que se tem de efetuar a modificação
    return tuple(its)

# Declaração de 2.1.8.
def territorio_para_str(t):
    """Converte um território numa representação de cadeia de caracteres.

    Args:
        t (tuple): O território.

    Returns:
        str: A representação do território como uma cadeia de caracteres.
    """
    if not eh_territorio(t):
        raise ValueError("territorio_para_str: argumento invalido")

    terr_str = ""

    # Adicione-se as letras na primeira linha
    terr_str += "   " + " ".join(alfabeto[:len(t)]) + "\n"

    num_colunas = len(t[0])

    for i in reversed(range(1, num_colunas + 1)):
        # Veja-se a explicação de {i:2d} na documentação oficial python: https://docs.python.org/3/library/stdtypes.html#str.format
        linha = f"{i:2d}"

        for j in range(len(t)):
            if eh_intersecao_valida(t, (alfabeto[j], i)):
                if t[j][i - 1] == 1:
                    linha += " X" 
                else:
                    linha += " ."

        linha += f" {i:2d}\n"
        terr_str += linha

    # Adicione-se as letras na última linha
    terr_str += "   " + " ".join(alfabeto[:len(t)])

    return terr_str


# Declaração de 2.2.1.
def obtem_cadeia(t, i):
    """Obtém uma cadeia de interseções conectadas a partir de uma interseção num território.

    Args:
        t (tuple): O território.
        i (tuple): A interseção de referência.

    Returns:
        tuple: Tuplo com as interseções conectadas em ordem de leitura.
    """
    # Verifique-se a interseção é válida
    if eh_intersecao_valida(t, i):
        # Obtenha-se a posição da letra no alfabeto
        posalfabeto = alfabeto.index(i[0])
        valor = t[posalfabeto][i[1] - 1]
        
        # Lista para armazenar as interseções únicas
        intersecoes = []
        fila = [(i[0], i[1])]

        while fila:
            # Remova-se a primeira interseção da fila
            intersecao = fila.pop(0)

            # Verifique-se se a interseção já foi explorada
            if intersecao not in intersecoes:
                intersecoes.append(intersecao)
            else:
                continue

            # Defina-se as variáveis x e y para a posição da interseção
            x = alfabeto.index(intersecao[0])
            y = intersecao[1] - 1

            # Veja-se as quatro direções possíveis
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                novo_x = x + dx
                novo_y = y + dy
                if 0 <= novo_x < len(t) and 0 <= novo_y < len(t[0]) and t[novo_x][novo_y] == valor:
                    nova_intersecao = (alfabeto[novo_x], novo_y + 1)
                    fila.append(nova_intersecao)

        # Retorne-se o resultado ordenado como um tuplo
        return ordena_intersecoes(tuple(intersecoes))
    else:
        raise ValueError("obtem_cadeia: argumentos invalidos")

# Declaração de 2.2.2.
def obtem_vale(t, i):
    """Obtém as interseções que fazem parte do vale de uma montanha.

    Args:
        t (tuple): O território.
        i (tuple): A interseção de referência (ocupada por montanha).

    Returns:
        tuple: Tuplo com as interseções que formam o vale.
    """
    if not eh_intersecao_valida(t, i):
        raise ValueError("obtem_vale: argumentos invalidos")
    
    if t[alfabeto.index(i[0])][i[1] - 1] == 1:
        # Obtenha-se a cadeia de montanhas da interseção
        cadeia = obtem_cadeia(t, i)

        vales = []  # Usamos uma lista para armazenar as interseções do vale

        # Percorra-se as interseções ao redor da cadeia
        for intersecao in cadeia:
            x = alfabeto.index(intersecao[0])
            y = intersecao[1] - 1

            # Verifique-se as quatro direções possíveis
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                novo_x, novo_y = x + dx, y + dy

                # Veja-se se a interseção é válida e está livre (valor 0)
                if 0 <= novo_x < len(t) and 0 <= novo_y < len(t[0]) and t[novo_x][novo_y] == 0:
                    nova_intersecao = (alfabeto[novo_x], novo_y + 1)

                    if nova_intersecao not in vales:
                        vales.append(nova_intersecao)

        return ordena_intersecoes(tuple(vales))

    else:
        raise ValueError("obtem_vale: argumentos invalidos")

# Declaração 2.3.1.
def verifica_conexao(t, i1, i2):
    """Verifica se duas interseções estão conectadas num dado território.

    Args:
        t (tuple): O território.
        i1 (tuple): Primeira interseção.
        i2 (tuple): Segunda interseção.

    Returns:
        bool: True se as interseções estão conectadas, False caso contrário.
    """
    if eh_intersecao_valida(t, i1) and eh_intersecao_valida(t, i2):
        cadeia1 = obtem_cadeia(t, i1)
        cadeia2 = obtem_cadeia(t, i2)

        # Se alguma interseção coicindir, estão necessariamente conectadas
        for i in cadeia1:
            if i in cadeia2:
                return True
        
        return False
    else:
        raise ValueError("verifica_conexao: argumentos invalidos")

# Declaração de 2.3.2. Calculo do número de montanhas
def calcula_numero_montanhas(t):
    """Calcula o número de interseções ocupadas por montanhas num dado território.

    Args:
        t (tuple): O território.

    Returns:
        int: O número de montanhas no território.
    """
    i = 0

    # O número de montanhas é a soma de todos os elementos do território
    if eh_territorio(t):
        for x in t:
            for y in x:
                i += y
        return i
    else:
        raise ValueError("calcula_numero_montanhas: argumento invalido")

# Declaração de 2.3.3.
def calcula_numero_cadeias_montanhas(t):
    """Calcula o número de cadeias de montanhas num dado território.

    Args:
        t (tuple): O território.

    Returns:
        int: O número de cadeias de montanhas no território.
    """
    if not eh_territorio(t):
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")

    # Definir uma lista para armazenar cadeias de montanhas únicas
    cadeias_montanhas = []
    montanhas = ()

    # Percorra-se o território para encontrar cadeias de montanhas
    for l in range(len(t)):
        for c in range(len(t[0])):
            if t[l][c] == 1:  # Encontra-se uma montanha
                intersecao = (alfabeto[l], c + 1)

                if intersecao not in montanhas:
                    cadeia = obtem_cadeia(t, intersecao)
                    montanhas += cadeia
                    cadeias_montanhas.append(cadeia)

    # Retorna-se o número de cadeias de montanhas encontradas
    return len(cadeias_montanhas)

# Declaração de 2.3.4.
def calcula_tamanho_vales(t):
    """Calcula o número total de interseções diferentes que formam todos os vales do território.

    Args:
        t (tuple): O território.

    Returns:
        int: O tamanho dos vales no território.
    """
    if not eh_territorio(t):
        raise ValueError("calcula_tamanho_vales: argumento invalido")

    lista_final = set()

    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == 0:
                if 0 <= i < len(t) and 0 <= j - 1 < len(t[i]) and t[i][j - 1] != 0:
                    # Verifique-se a esquerda
                    intersecao = (alfabeto[i], j + 1)
                    lista_final.add(intersecao)
                if 0 <= i - 1 < len(t) and 0 <= j < len(t[i]) and t[i - 1][j] != 0:
                    # Verifique-se acima
                    intersecao = (alfabeto[i], j + 1)
                    lista_final.add(intersecao)
                if 0 <= i < len(t) and 0 <= j + 1 < len(t[i]) and t[i][j + 1] != 0:
                    # Verifique-se a direita
                    intersecao = (alfabeto[i], j + 1)
                    lista_final.add(intersecao)
                if 0 <= i + 1 < len(t) and 0 <= j < len(t[i]) and t[i + 1][j] != 0:
                    # Verifique-se abaixo
                    intersecao = (alfabeto[i], j + 1)
                    lista_final.add(intersecao)

    return len(lista_final)

# Término