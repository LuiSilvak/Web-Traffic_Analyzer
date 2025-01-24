# Analisador de Dados de Tráfego Web

## Descrição

Este projeto tem como objetivo analisar dados de tráfego web e gerar insights sobre o comportamento dos usuários em um site. Ele coleta e processa dados como número de visitas, páginas mais acessadas, origem do tráfego e outras métricas importantes. A análise busca identificar padrões que podem ser utilizados para otimizar a experiência do usuário e melhorar o desempenho do site.

## Funcionalidades

1. Importação de dados de tráfego web a partir de arquivos CSV.
2. Cálculo de métricas como número de visitas, páginas mais acessadas e tempo médio de permanência.
3. Análise da origem do tráfego, como visitantes diretos, de pesquisa ou de redes sociais.
4. Visualização gráfica de métricas como as páginas mais populares e o crescimento de visitas ao longo do tempo.
5. Geração de insights sobre o comportamento do usuário no site.

## Pré-requisitos

1. Certifique-se de ter os seguintes requisitos instalados no seu ambiente:

    - Python 3.7 ou superior.
    - Bibliotecas necessárias:
        - pandas
        - matplotlib
        - seaborn

2. Você pode instalar as dependências utilizando o comando:

```bash
    pip install pandas matplotlib seaborn
```

3. Como Usar

    Clone este repositório:

```bash
    git clone https://github.com/LuiSilvak/Web-Traffic_Analyzer.git
    cd Web-Traffic_Analyzer
```

4. Certifique-se de ter um arquivo CSV contendo os dados de tráfego web. O arquivo deve conter, no mínimo, as seguintes colunas:

    - Data
    - Visitas
    - Páginas_Acessadas
    - Fonte_Trafego
    - Tempo_Permanencia

5. Exemplo de formato do arquivo:

```bash
    Data,Visitas,Páginas_Acessadas,Fonte_Trafego,Tempo_Permanencia
    2025-01-01,1000,5,Google,300
    2025-01-02,1200,7,Facebook,400
    2025-01-03,900,6,Direct,350
```

6. Execute o script principal:

```bash
    python Web-Traffic_Analyzer.py
```

7. Visualize as saídas no console e nos gráficos gerados.

## Exemplo de Saída

1. Estatísticas Sumarizadas:

```bash
    Visitas Totais: 3100
    Páginas Acessadas: 18
    Fonte de Tráfego Mais Popular: Google
    Tempo Médio de Permanência: 350 segundos
```

2. Gráficos Gerados:
    - Gráfico de barras mostrando as páginas mais acessadas.
    - Gráfico de pizza com a distribuição do tráfego por origem (Google, Facebook, Direct, etc.).
    - Gráfico de linha mostrando o crescimento de visitas ao longo do tempo.

## Estrutura do Projeto

```bash
    Web-Traffic_Analyzer/
    │
    ├── Web-Traffic_Analyzer.py      # Script principal
    ├── README.md                    # Documentação do projeto
    └── LICENÇA                      # Licença do projeto
```

## Expansões Futuras

1. Implementação de métricas avançadas, como taxa de rejeição (bounce rate) e tempo de interação com o site.
2. Análise de páginas de saída mais frequentes.
3. Integração com Google Analytics API para análise em tempo real.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

