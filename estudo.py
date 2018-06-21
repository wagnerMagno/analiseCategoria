import pandas as pd

listaPalavraNaoCategorizada = set()

class Review(object):
    def __init__(self, comentario, categoria):
        self.categoria = categoria
        self.comentario = comentario
    
    def __repr__(self):
        return "Comentario: %s, Categoria: %s" % (self.comentario, self.categoria)

    def get_categoria(self):
        return self.categoria

    def get_comentario(self):
        return self.comentario

class Categoria(object):
    def __init__(self, categoria, termo):
        self.categoria = categoria
        self.termo = termo

    def __repr__(self):
        return "Categoria:%s Valor:%s" % (self.categoria, self.termo)

    def get_categoria(self):
        return self.categoria

    def get_termo(self):
        return self.termo
    
def analise():
    datasetCategorias = pd.read_excel("./categorias.xlsx")    
    lista = []
    for x in datasetCategorias.values:
        categoria = Categoria(x[0], x[1])
        lista.append(categoria)

    listaOrdenada = sorted(lista, key = Categoria.get_termo)

    categoriaString = set()

    listaComentario = listarComentarios();
    
    for comentario in listaComentario:
        categoriaString = set()
        listaPalavra =  comentario.split()
        print("------------------------------------------------")
        for palavra in listaPalavra:
            categorizacao = buscaBinaria(listaOrdenada, palavra)
            categoriaString.add(categorizacao)
        
        review = Review(comentario, categoriaString)
        print(review)
        print("------------------------------------------------")

    print("\n\n************** Palavras Não Categorizadas **********************\n\n")
    print(listaPalavraNaoCategorizada)



def buscaBinaria(lista, palavra):
    meio = len(lista) // 2

    if(len(lista) == 1 and lista[0].termo.upper().strip() == palavra.upper().strip()):
        print("\nPalavra "+ palavra + " Categoria " + lista[0].categoria +"\n")
        return lista[0].categoria
    elif(len(lista) == 1 and lista[0].termo.upper().strip() != palavra.upper().strip()):
        listaPalavraNaoCategorizada.add(palavra)
        return "termo sem categoria"    
    
    if( palavra < lista[meio].termo):
        return buscaBinaria(lista[:meio], palavra)
    else:
        return buscaBinaria(lista[meio:], palavra)

def listarComentarios():
    lista = ["Muita burocracia para transferências... Fora que o próprio app da pau na hora de realizar o desbloqueio do celular. Estou a dois dias tentando é sempre da “sessão expirada” no final.",
            "Esse app é muito bom. Estou usando há pouco tempo, mas o que preciso ele atende bem Acho que poderia ter um chat para ficar 10!",
            "App atende aos serviços básicos, porém pode ter maior estabilidade.",
            "Show de bola.",
            "So funciona depois da segunda tentativa, na primeira sempre acontece algo de errado, e o app é encerrado. Não tem um acesso direto para extrato, o que nao faz o menor sentido. Tá longe de ficar mais ou menos.",
            "1 nível de criptografia de segurança bom."+
            "2 consigo realizar todos pagamentos"+
            "3 ótimo pra realizar transferência" +
            "4 não trava no meu iPhone e nunca deu nenhum problema!"+
            "5 perfeito para minhas necessidades!",
            "Não funciona para fazer transferência , é de “lua” um aplicativo de BANCO NÃO PODE FUNCIONAR , AS VEZES SIM, AS VEZES NÃO",
            "Muita burocracia para transferências... Fora que o próprio app da pau na hora de realizar o desbloqueio do celular. Estou a dois dias tentando é sempre da “sessão expirada” no final.",
            "Esse app é muito bom. Estou usando há pouco tempo, mas o que preciso ele atende bem Acho que poderia ter um chat para ficar 10!",
            "App atende aos serviços básicos, porém pode ter maior estabilidade.",
            "Show de bola.",
            "So funciona depois da segunda tentativa, na primeira sempre acontece algo de errado, e o app é encerrado. Não tem um acesso direto para extrato, o que nao faz o menor sentido. Tá longe de ficar mais ou menos.",
            "1 nível de criptografia de segurança bom."+
            "2 consigo realizar todos pagamentos"+
            "3 ótimo pra realizar transferência" +
            "4 não trava no meu iPhone e nunca deu nenhum problema!"+
            "5 perfeito para minhas necessidades!",
            "Não funciona para fazer transferência , é de “lua” um aplicativo de BANCO NÃO PODE FUNCIONAR , AS VEZES SIM, AS VEZES NÃO",
            "Muita burocracia para transferências... Fora que o próprio app da pau na hora de realizar o desbloqueio do celular. Estou a dois dias tentando é sempre da “sessão expirada” no final.",
            "Esse app é muito bom. Estou usando há pouco tempo, mas o que preciso ele atende bem Acho que poderia ter um chat para ficar 10!",
            "App atende aos serviços básicos, porém pode ter maior estabilidade.",
            "Show de bola.",
            "So funciona depois da segunda tentativa, na primeira sempre acontece algo de errado, e o app é encerrado. Não tem um acesso direto para extrato, o que nao faz o menor sentido. Tá longe de ficar mais ou menos.",
            "1 nível de criptografia de segurança bom."+
            "2 consigo realizar todos pagamentos"+
            "3 ótimo pra realizar transferência" +
            "4 não trava no meu iPhone e nunca deu nenhum problema!"+
            "5 perfeito para minhas necessidades!",
            "Não funciona para fazer transferência , é de “lua” um aplicativo de BANCO NÃO PODE FUNCIONAR , AS VEZES SIM, AS VEZES NÃO"]
    return lista

if __name__ == "__main__":
    analise()
