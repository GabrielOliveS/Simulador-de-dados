import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gerar_dados(distribuicao="normal", tamanho=100):  # utiliza o np para gerar dados aleatórios com o parâmetros utilizados.
    if distribuicao == "normal":  # se distribuição for normal.
        dados = np.random.normal(loc=50, scale=10, size=tamanho)  # média 50, desvio padrão 10
    elif distribuicao == "uniforme":  # se distribuição for uniforme.
        dados = np.random.uniform(low=10, high=100, size=tamanho)  # entre 10 e 100
    return dados

def calcular_estatisticas(dados):  # cria um dicionário com as descrições das estatísticas e usa os dados como entrada.
    estatisticas = {
        "Média": np.mean(dados),
        "Mediana": np.median(dados),
        "Desvio Padrão": np.std(dados),
        "Mínimo": np.min(dados),
        "Máximo": np.max(dados),
        "Total": len(dados)  # Adiciona a contagem total de dados
    }
    return estatisticas
 # -> gráfico dificíl de entender.
 # def plotar_dados(dados):  # utilizando matplotlib para montar um gráfico com os dados.
 # plt.hist(dados, bins=10, color='skyblue', edgecolor='black')
 # plt.title("Distribuição dos Dados")
 # plt.xlabel("Valor")
 # plt.ylabel("Frequência")
 # plt.show()

def plotar_dados(dados, estatisticas): #novo gráfico.
    plt.figure(figsize=(10, 6))  # Aumenta o tamanho da figura
    plt.hist(dados, bins=15, color='skyblue', edgecolor='black')  # Aumenta o número de bins para mais detalhes
    plt.title(
        f"Distribuição dos Dados\nMédia: {estatisticas['Média']:.2f}, Mediana: {estatisticas['Mediana']:.2f}, Desvio Padrão: {estatisticas['Desvio Padrão']:.2f}")
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.grid(True, linestyle='--', alpha=0.7)  # Adiciona linhas de grade ao gráfico
    # Adicionando anotações para o valor mínimo e máximo
    plt.annotate(f'Mínimo: {estatisticas["Mínimo"]:.2f}',
                 xy=(estatisticas["Mínimo"], 0),
                 xytext=(estatisticas["Mínimo"] + 5, 1),
                 arrowprops=dict(facecolor='red', shrink=0.01),
                 fontsize=10, color='red')

    plt.annotate(f'Máximo: {estatisticas["Máximo"]:.2f}',
                 xy=(estatisticas["Máximo"], 0),
                 xytext=(estatisticas["Máximo"] - 15, 1),
                 arrowprops=dict(facecolor='green', shrink=0.01),
                 fontsize=10, color='green')
    plt.annotate(f'Total de Dados: {estatisticas["Total"]}',
                 xy=(0.5, 0.95),  # Posição em coordenadas normalizadas (0 a 1)
                 xycoords='axes fraction',  # Usar frações do eixo para a posição
                 fontsize=10, color='blue', ha='center')
    plt.show()

def exportar_dados_para_csv(dados):
        # Definindo o caminho padrão para exportação
        caminho_arquivo = os.path.join(os.getcwd(), 'dados_exportados.csv')
        df = pd.DataFrame(dados, columns=["Dados"])
        df.to_csv(caminho_arquivo, index=False)
        print(f"Dados exportados para: {caminho_arquivo}")  # Exibe onde o arquivo foi salvo

def main():  # função main.
    while True: #repetir o programa enquanto for true.
        distribuicao = input("Escolha a distribuição:\n"
                             "'normal' = Distribuição em forma de sino, onde a maioria dos valores se concentra em torno da média.\n"
                             "ou\n"
                             "'uniforme' = Distribuição em que todos os valores em um intervalo específico têm a mesma probabilidade de ocorrer: ").strip().lower()

        tamanho = int(input("Escolha o tamanho do conjunto de dados: "))
        # gerar dados utilizando os inputs das linhas anteriores.
        dados = gerar_dados(distribuicao, tamanho)

        # calcular estatísticas usando os dados aleatórios gerados.
        estatisticas = calcular_estatisticas(dados)
        print("\nEstatísticas dos Dados:")
        for chave, valor in estatisticas.items():
            print(f"{chave}: {valor:.2f}")

        # plotar gráfico
        plotar_dados(dados, estatisticas)

        print("\nDados Gerados:")
        print(dados)

        #Pergunta ao usuário se quer exportar os dados.
        exportar = input("\nDeseja exportar os dados para um arquivo CSV? (s / digite qualquer tecla): ").strip().lower()
        if exportar == 's':
            exportar_dados_para_csv(dados)
        #Pergunta o usuário se quer salvar o gráfico.
        salvar_imagem = input("\nDeseja salvar a imagem do gráfico? (s / digite qualquer tecla): ").strip().lower()
        if salvar_imagem == 's':
            if salvar_imagem == 's':
                # Chama a função para plotar os dados antes de salvar a imagem
                plotar_dados(dados, estatisticas)
                caminho_imagem = os.path.join(os.getcwd(), 'grafico_dados.png')
                plt.savefig(caminho_imagem)  # Salva a imagem
                plt.close()  # Fecha a figura atual
                print(f"Gráfico salvo em: {caminho_imagem}")

        # Pergunta ao usuário se deseja realizar outro cálculo.
        continuar = input("\nDeseja realizar outro cálculo? (s / digite qualquer tecla para sair.): ").strip().lower()
        if continuar != 's':
            print("Saindo do aplicativo.")
            return  # Sai do loop se o usuário não quiser continuar


# executa o programa
if __name__ == "__main__":
    main()





