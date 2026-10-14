---
disciplina: "Algoritmos e Complexidade"
ciclo: "1° Ciclo"
ano: 2026
unidade_sagah: 3
titulo: "Métodos de Ordenação Interna de Dados"
data_criacao: 2026-10-12
status: "Concluído"
tags:
  - faculdade/algoritmos-e-complexidade
  - tipo/resumo-sagah
  - topico/ordenacao-interna
  - topico/bubble-sort
  - topico/quicksort
  - topico/estabilidade-algoritmica
---

# 📘 UA03: Métodos de Ordenação Interna de Dados

> [!abstract] **Objetivos de Aprendizagem (SAGAH)**
> - Diferenciar os métodos fundamentais de ordenação interna de dados na memória.
> - Compreender o funcionamento mecânico dos algoritmos: *Bubble Sort*, *Selection Sort*, *Insertion Sort* e *Quicksort*.
> - Identificar os critérios de avaliação de desempenho (número de comparações, trocas, estabilidade e complexidade assintótica).

---

## 📌 1. Introdução e Contextualização

A ordenação é uma das operações computacionais mais executadas no mundo. Sua importância primária não reside apenas em apresentar relatórios organizados visualmente, mas no fato de que **dados previamente ordenados possibilitam algoritmos de busca ultrarrápidos**, como a busca binária de complexidade $O(\log N)$, em contraste com a busca sequencial $O(N)$.

Classifica-se a ordenação em:
- **Ordenação Interna:** Quando todos os dados cabem simultaneamente na memória principal (RAM).
- **Ordenação Externa:** Quando o volume de dados excede a memória RAM e exige a manipulação coordenada de arquivos no disco rígido ou SSD.

> **Princípio-Chave:** A escolha do algoritmo de ordenação ideal depende não apenas da quantidade de elementos ($N$), mas do estado prévio dos dados (aleatórios, quase ordenados ou invertidos) e da necessidade de estabilidade.

---

## 🧬 2. Núcleo Conceitual (O "Como" e o "Porquê")

### 🃏 Métodos Elementares ($O(N^2)$)

#### 1. Ordenação Bolha (*Bubble Sort*)
- **Mecanismo:** Percorre o vetor repetidamente comparando pares adjacentes de elementos $(vetor[i], vetor[i+1])$ e trocando-os de posição se estiverem fora de ordem. A cada passagem, o maior elemento "flutua" para o final do vetor, como uma bolha de gás em um líquido.
- **Vantagem:** Muito fácil de implementar e compreender.
- **Desvantagem:** Lento e ineficiente para grandes volumes de dados.

#### 2. Ordenação por Seleção (*Selection Sort*)
- **Mecanismo:** Seleciona o menor elemento de todo o vetor e o troca com o elemento da primeira posição. Em seguida, busca o menor entre os restantes e o troca com o da segunda posição, repetindo o processo até o fim.
- **Característica Marcante:** Minimiza o número de trocas físicas na memória ($O(N)$ trocas), mas faz sempre o mesmo número de comparações ($O(N^2)$), mesmo se o vetor já estiver ordenado.

#### 3. Ordenação por Inserção (*Insertion Sort*)
- **Mecanismo:** Semelhante a organizar cartas de baralho na mão. O algoritmo percorre o vetor da esquerda para a direita; para cada elemento, desloca os elementos maiores já ordenados para a direita e insere o novo elemento exatamente em sua posição correta.
- **Comportamento Natural:** Altamente adaptativo. Se o vetor já estiver quase ordenado, ele executa em tempo linear **$O(N)$**, realizando pouquíssimas movimentações.

---

### ⚡ Método Avançado: Quicksort ($O(N \log N)$)
Proposto por Tony Hoare, o Quicksort utiliza o paradigma de **Divisão e Conquista**:
1. **Escolha do Pivô:** Seleciona um elemento de referência (por exemplo, o elemento central ou a mediana de três).
2. **Particionamento:** Reorganiza o vetor de modo que todos os elementos menores que o pivô fiquem à sua esquerda, e todos os maiores fiquem à sua direita. O pivô fica em sua posição final correta.
3. **Recursão:** Aplica o Quicksort independentemente na sublista da esquerda e na sublista da direita.

---

### ⚖️ Critérios Decisivos de Avaliação

* **Estabilidade Algorítmica:** Um algoritmo é **estável** se ele mantém a ordem relativa original de elementos com chaves iguais.
  * *Exemplo prático:* Se uma lista já ordenada por nomes for reordenada por idades, um algoritmo estável garante que pessoas com a mesma idade permaneçam em ordem alfabética.
  * **Estáveis:** *Insertion Sort*, *Bubble Sort*, *Merge Sort*.
  * **Não Estáveis:** *Selection Sort*, *Quicksort*.
* **Comportamento Natural:** Capacidade do algoritmo de trabalhar o mínimo possível quando os dados já entram ordenados e trabalhar o máximo apenas quando em ordem inversa.

---

## 📊 3. Síntese Comparativa de Desempenho

| Algoritmo | Complexidade (Melhor Caso) | Complexidade (Caso Médio) | Complexidade (Pior Caso) | É Estável? | Memória Adicional |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(N)$ *(com flag)* | $O(N^2)$ | $O(N^2)$ | **Sim** | $O(1)$ |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | ❌ **Não** | $O(1)$ |
| **Insertion Sort** | **$O(N)$** | $O(N^2)$ | $O(N^2)$ | **Sim** | $O(1)$ |
| **Quicksort** | **$O(N \log N)$** | **$O(N \log N)$** | $O(N^2)$ *(pivô ruim)* | ❌ **Não** | $O(\log N)$ |

---

## 🚀 4. Aplicação Prática: Implementação do Bubble Sort

Exemplo do algoritmo de ordenação por trocas em pseudocódigo estruturado (padrão VisuAlg / didático):

```plaintext
algoritmo "ordena_bolha"
var
   cartas: vetor[1..6] de inteiro
   i, j, temp: inteiro
inicio
   // Laço externo para passagens no vetor
   para i de 1 ate 5 faca
      // Laço interno comparando elementos adjacentes
      para j de 1 ate 6 - i faca
         se cartas[j] > cartas[j + 1] entao
            temp <- cartas[j]
            cartas[j] <- cartas[j + 1]
            cartas[j + 1] <- temp
         fimse
      fimpara
   fimpara
fimalgoritmo
```

---

## 🎯 5. Dica do Professor (Foco em Provas)

> [!tip] **O que mais costuma cair em avaliações:**
> 1. **Diferenciação dos Métodos Básicos:**
>    - Seleciona o menor e coloca no início ➔ **Selection Sort**.
>    - Desloca os maiores e insere no local exato ➔ **Insertion Sort**.
>    - Troca elementos adjacentes em pares sucessivos ➔ **Bubble Sort**.
> 2. **Estabilidade do Quicksort:** O Quicksort **NÃO** é um método estável, pois a troca de elementos distantes em torno do pivô pode inverter a ordem relativa de chaves iguais.
> 3. **Melhor Caso do Insertion Sort:** O Insertion Sort é a escolha ideal quando a lista já está previamente quase toda ordenada, pois sua complexidade cai para $O(N)$.
> 4. **Escolha do Pivô no Quicksort:** A técnica da **mediana de três chaves** (primeiro, meio e último elemento) é a melhor prática para evitar o pior caso $O(N^2)$ do Quicksort em vetores já ordenados.

---

## 🧠 6. Questões de Fixação (Active Recall & SAGAH)

> **P1: Com base na funcionalidade dos métodos internos simples de ordenação de dados, identifique qual método corresponde a cada descrição:**  
> I. Seleciona o menor entre os elementos e realiza a troca deste pelo primeiro elemento, repetindo para o restante.  
> II. Percorre elemento por elemento, deslocando os já ordenados e inserindo o novo elemento na posição correta.  
> III. Ordenação por trocas que envolve repetidas comparações de elementos vizinhos adjacentes.  
> **Resposta Correta:** **a) Ordenação por seleção – ordenação por inserção – ordenação bolha.**  
> 🎯 **Por quê?** I descreve a seleção direta do mínimo (*Selection*); II descreve a inserção em lista ordenada (*Insertion*); III descreve a flutuação por trocas adjacentes (*Bubble*).

---

> **P2: Analise e julgue as afirmativas acerca dos algoritmos de ordenação interna:**  
> I. O Insertion Sort apresenta ótimo desempenho quando os elementos já estão ordenados, e desempenho ruim se estiverem invertidos. (V)  
> II. Um algoritmo é considerado estável se não altera a posição relativa de elementos de mesmo valor. (V)  
> III. O método bolha é fácil de programar, mas ineficiente frente a outros métodos. (V)  
> IV. Insertion, Bolha e Selection possuem complexidade média de $O(N^2)$ comparações. (V)  
> **Resposta Correta:** **e) V, V, V, V.**  
> 🎯 **Por quê?** Todas as quatro afirmativas são conceitualmente verdadeiras e refletem fielmente a teoria dos métodos quadráticos elementares.

---

> **P3: Com relação aos fatores levados em consideração para avaliar métodos de ordenação interna, assinale a alternativa INCORRETA:**  
> **Resposta Correta:** **b) O número de comparações entre as chaves e o número de trocas não podem ser considerados uma forma de avaliar e comparar os métodos.**  
> 🎯 **Por quê?** Esta afirmação é falsa. A contagem do número de comparações e do número de trocas de elementos é precisamente a principal métrica matemática para comparar a eficiência entre algoritmos de ordenação.

---

> **P4: Considere a execução de um teste de mesa que busca o menor elemento do vetor e o coloca na primeira posição, repetindo para as posições subsequentes. Qual é o método utilizado?**  
> **Resposta Correta:** **c) Ordenação por seleção.**  
> 🎯 **Por quê?** A variável de controle `menor` que armazena a posição do elemento mínimo da iteração é a marca registrada do algoritmo *Selection Sort*.

---

> **P5: Sobre o método de ordenação Quicksort, analise as afirmativas e marque a que apresenta informações INCORRETAS:**  
> I. O método Quicksort é considerado um método de ordenação estável.  
> II. A escolha correta do pivô (ex.: mediana de três) é essencial para a eficiência.  
> III. O pivô pode ser o elemento do meio do vetor.  
> IV. Utiliza um pivô para dividir o vetor entre menores e maiores.  
> **Resposta Correta:** **a) I.**  
> 🎯 **Por quê?** A afirmativa I é incorreta porque o Quicksort padrão **não é estável**. O processo de partição faz saltos de elementos por cima do pivô, o que pode alterar a ordem original de registros com valores de chave idênticos.

---

## 📚 7. Referências e Conexões

- **ZIVIANI, N.** *Projeto de algoritmos com implementações em Pascal e C*. 3. ed. São Paulo: Cengage Learning, 2011.
- **CORMEN, T. H. et al.** *Algoritmos: teoria e prática*. Rio de Janeiro: Elsevier, 2012.
- Plataforma SAGAH: Unidade de Aprendizagem *Métodos de ordenação interna de dados*.
- [[UA01 - Modelos de Computação e Eficiência de Algoritmos]]
- [[UA02 - Divisão e Conquista em Programação Paralela]]
