# PIBIC FACEPE BIC-0251-1.03/24

Linha de pesquisa: Inteligência Computacional  
Título do projeto de iniciação científica: Método Agrupamento Difuso Multivariado usando Medoids  

Aluno candidato: Thomaz Cabral Corrêa de Araújo  

Sob supervisão: Profa. Dra Renata Maria Cardoso Rodrigues de Souza  
(Centro de Informática – CIn/UFPE)  

### Resumo

Este projeto de pesquisa visa realizar avanços no estado da arte de técnicas de agrupamento tipo partição através do desenvolvimento de pesquisas básica sobre método de agrupamento do paradigma difuso baseado em medoids e grau de pertinência multivariado. Distâncias com pesos e sem pesos também serão consideradas no método de agrupamento. Além disso, uma avaliação experimental com dados sintéticos e reais será realizada. Os métodos serão comparados com métodos de agrupamento tipo partição difuso da literatura baseado em medoids que não consideram graus de pertinência multivariado na presença de dados aberrantes.  

### 1. Introdução  

Análise de Agrupamentos pode ser compreendido como uma técnica estatística que em que dado um conjunto de dados, se busca reunir em um mesmo grupo observações que possuam um maior grau de similaridade, enquanto que observações que não possuam um alto grau de dissimilaridade são alocadas em grupos distintos. Dois grupos distintos de técnicas de partição podem ser considerados: rígido e difuso [1] [2].  

O método difuso c-médias é o método de agrupamento difuso mais conhecido e geralmente possui bons resultados na abordagem difusa, além de possuir uma relativa facilidade na implementação do algoritmo. Uma desvantagem desse método é o fato dele não possuir bom desempenho quando o conjunto de dados possui dados aberrantes (outliers).  

Existem métodos difuso que não utilizam médias para o cálculo dos protótipos, como é o caso do c-medoids. É um método bastante similar ao c-médias, porém, ao invés da utilização da média, uma observação do próprio conjunto de dados minimiza a distância desse ponto para os demais do grupo, conhecida como medoid [3] [4]. Ou seja, a principal diferença perante o difuso c-médias é encontrada na lista de formação dos centróides. Nesse caso, o método c-medoids permite usar diferentes distâncias e assim pode ser menos sensível na presença de dados aberrantes ou ruídos.  

Em [5] foi introduzido o primeiro método difuso usando um grau de pertinência associado a cada variável. Esse método é uma versão do tradicional método difuso c-médias [5] para graus de pertinência multivariado. Quanto à esta abordagem difusa multivariada, algumas vantagens são perceptíveis, como por exemplo, interpretar a relevância de cada observação para um determinado grupo de acordo com cada variável, a capacidade de obter mais informação dos conjuntos de dados ajudando a melhorar a qualidade dos agrupamentos e, por último, uma nova alternativa de agrupamentos utilizando o contexto multivariado. Uma desvantagem do método proposto em [5] é o seu baixo desempenho em conjuntos com presença de dados aberrantes (outliers ou ruídos), uma vez que usa a distância Euclidiana.  

### 3. Objetivo  

Este trabalho visa apresentar um método de agrupamento difuso em que os valores do grau de pertinência das observações para cada grupo são influenciados pelas variáveis. Ou seja, o nível de similaridade de uma observação com o protótipo é dado de acordo com cada variável do conjunto de dados. O uso dessa técnica multivariada objetiva a melhora na qualidade dos agrupamentos comparado com outros já existentes na literatura que não usam grau de pertinência multivariado. É importante destacar que o método estudado será avaliado na presença de dados aberrantes ou ruído e diferentes distâncias podem ser usadas.  

Nesse contexto, o intuito desse trabalho é responder duas perguntas (hipóteses) de pesquisa:  

1. É possível melhorar a qualidade de agrupamento difuso baseado em medoids através da utilização de graus de pertinência cujos valores são calculados segundo cada variável?  
2. É possível descrever a relevância de cada variável para cada grupo usando tais graus?  

### 4. Metodologia a ser empregada  

Os algoritmos de agrupamento, tipo partição, obtêm uma única partição de dados em vez de uma série encadeada de partições. A escolha do número de grupos desejados pode ser um problema, já que nem sempre existe informações a priori suficientes do conjunto de dados para definir este número. Métodos particionais podem ser classificados em duas principais categorias: rígido ou difuso [1][2]. Na primeira categoria, objetos pertencem a exatamente um grupo, onde o grau de pertinência de um objeto para um grupo pode estar no conjunto {0, 1}: 1 se o objeto pertencer ao grupo ou 0 caso contrário. Um dos métodos particionais rígido mais popular é o k-médias. Na segunda categoria de métodos particionais, os objetos têm graus de pertinência para todos os grupos, onde podem estar no intervalo [0,1]. O método difuso c-médias é popularmente usado em aplicações do mundo real. Esse método é a versão do k-médias em que os objetos podem pertencer a todos os grupos com graus de pertinência assumindo valores no intervalo [0,1].  

O método que será investigado nesse trabalho é uma extensão do método PAM (Partition Around Medoids) [3][4]. Este algoritmo possui como principal contraste perante o k-médias a escolha de observações do conjunto de dados para serem os centróides, denominados de medoids. Neste formato, há uma maior facilidade na interpretabilidade dos centróides dos clusters perante o k-médias que utiliza a média das observações dos grupos para capturar os centróides.  

Nesse contexto, este trabalho objetiva propor uma versão difusa para o método PAM considerando graus de pertinência multivariado para cada indivíduo/objeto do conjunto de dados. A ideia é melhorar a qualidade do agrupamento usando graus de pertinência definidos por indivíduo, grupo e variável conforme o trabalho descrito em [5]. Além disso, uma versão com distâncias ponderadas também será proposta e os métodos serão avaliados na presença de outliers (pontos aberrantes). Durante a investigação, serão realizadas as seguintes ações:  

1. Implementação de um ambiente experimental para avaliação das abordagens propostas com dados artificiais. O desempenho dos métodos será avaliado baseando-se no índice corrigido de Rand (medida de proximidade entre uma partição à priori e uma partição obtida pelo método de cluster) e na taxa de erro de classificação. Na validação com dados reais, serão considerados conjuntos de dados de tipo intervalo de um repositório de Machine Learning e/ou outros conjuntos pertinentes a aplicação de cunho prático.  

2. Implementação de um ambiente experimental para avaliação das abordagens propostas com conjuntos de dados artificiais. As medidas serão estimadas pelo método Monte Carlo com 100 replicações de cada conjunto.  

3. Estudo comparativo entre o método proposto com o método de agrupamento correspondente da literatura que não usa graus de pertinência multivariado. Os métodos serão implementados usando a linguagem Python.  

### 5. Plano de trabalho  

Como metas explicitamente especificadas, de modo a permitir o acompanhamento e avaliação do projeto, abaixo é apresentada uma lista de passos que serão seguidos:  

- Realizar Revisão Bibliográfica da literatura de agrupamento de partição (agosto a outubro 2024).  
- Construir ambientes de programação para realização dos experimentos com diferentes conjuntos de dados artificiais e reais (novembro 2024 a abril 2025).  
- Fazer uma análise estatística para avaliar o desempenho dos métodos (novembro 2024 a abril 2025).  
- Escrever artigo e relatório (maio a julho 2025).  

### 6. Principais contribuições  

Este trabalho visa contribuir de três maneiras diferentes:  

1. Realizar avanços no plano teórico relativo aos métodos de agrupamento tipo partição com publicação em conferência ou revista internacional.  
2. Formação de um aluno de graduação em uma área que apresenta potencial para aplicações em tratamento de imagens, comércio eletrônico, ciências biológicas, perfil de consumidores, etc.  
3. Criação de uma aplicação de agrupamento do mundo real para formação de perfis de dados.  

### 7. Referências  

1. Jain, A. K., Murty, M. N., & Flynn, P. J. (1999). Data clustering: a review. ACM computing surveys (CSUR), 31(3), 264-323.  
2. Jain, A. K. (2010). Data clustering: 50 years beyond K-means. Pattern Recognition Letters, 31(8), 651-666.  
3. Kaufman, L.; Rousseeu, P. J. Finding groups in data: An introduction to cluster analysis–john wiley & sons. Inc., New York, 1990.  
4. Kaufman, L. Clustering by means of medoids. In: Proc. Statistical Data Analysis Based on the L1 Norm Conference, Neuchatel, 1987. p. 405–416.  
5. Pimentel, B.A. e Souza, R.M.C.R. (2013). A Multivariate Fuzzy C-Means Method. Applied Soft Computing (Print). Applied Soft Computing, v.13, p.1592-1607.  
