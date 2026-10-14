

---

Com a crescente utilização de sistemas embarcados, seja para controle aeronáutico, monitoramento de pacientes em um hospital ou, simplesmente, para controlar objetos inteligentes em residências, os sistemas operacionais embarcados estão se tornando mais necessários ao longo dos anos. Muitas das aplicações modernas precisam atender prazos cada vez mais curtos e com necessidades de precisão. Assim, o _real time operation system_ (RTOS), ou sistema operacional de tempo real, em português, se torna uma ferramenta de alta importância na construção desses dispositivos.

Nesta Unidade de Aprendizagem, você aprenderá os conceitos que cercam o RTOS. Com isso, compreenderá seus objetivos e fará uma comparação com um GPOS — _system purpose operation system_ (sistemas de uso geral), para definir quais são as melhores situações para empregar cada um. Por fim, entenderá as diferenças entre RTOS do tipo _hard_ e _soft_.

Bons estudos.

#### Ao final desta Unidade de Aprendizagem, você deve apresentar os seguintes aprendizados:

- Definir os objetivos do uso de RTOS.
- Comparar sistemas operacionais embarcados de uso comum e os RTOS.
- Definir os tipos de RTOS _hard_ e _soft_.

---

	# Sistemas Operacionais de Tempo Real (RTOS) — Resumo

## Sistemas Operacionais Embarcados

Os **sistemas operacionais embarcados** são utilizados em dispositivos eletrônicos para gerenciar recursos do sistema e executar aplicações específicas.

Eles permitem que o desenvolvedor:

- foque na **lógica da aplicação**
    
- utilize **funções já implementadas**
    
- tenha **maior confiabilidade no sistema**
    

---

# Tipos de Sistemas Operacionais

Os sistemas embarcados podem ser classificados em dois tipos principais:

## GPOS (General Purpose Operating System)

São **sistemas operacionais de uso geral**, projetados para suportar muitas aplicações e diferentes recursos.

### Características

- grande número de aplicações
    
- suporte a diversos dispositivos de **entrada e saída (I/O)**
    
- multitarefa
    
- interface mais completa
    

### Exemplos

- Linux
    
- Windows
    
- Android
    

### Limitação

Não possuem **tempo de resposta determinístico**, por isso **não são ideais para aplicações críticas em tempo real**.

---

# RTOS (Real-Time Operating System)

Os **RTOS** são sistemas operacionais projetados para aplicações que exigem **resposta dentro de limites de tempo definidos**.

### Características

- resposta **determinística**
    
- alta **confiabilidade**
    
- controle preciso de tarefas
    
- **baixo consumo de recursos**
    
- tamanho reduzido
    

---

# Classificação de Sistemas de Tempo Real

## Hard Real-Time

Sistemas onde **os prazos devem ser obrigatoriamente cumpridos**.

Se o tempo não for respeitado, o sistema **falha**.

### Exemplos

- controle de tráfego aéreo
    
- sistemas médicos
    
- airbags automotivos
    

---

## Soft Real-Time

Permitem **pequenos atrasos**, sem causar falha grave no sistema.

### Exemplos

- streaming de vídeo
    
- sistemas multimídia
    
- telecomunicações
    

---

# Aplicações de RTOS

RTOS são mais indicados em sistemas que exigem **alta confiabilidade e resposta rápida**.

### Exemplos

- controle de tráfego aéreo
    
- equipamentos médicos (ex: maca inteligente)
    
- automação industrial
    
- sistemas automotivos
    

---

# Vantagens de Sistemas Operacionais Embarcados

Utilizar um sistema operacional embarcado traz diversos benefícios.

### Principais vantagens

- grande quantidade de **funcionalidades prontas**
    
- **maior confiabilidade**
    
- **facilidade de desenvolvimento**
    
- redução do **tempo de projeto**
    
- **redução de custos**
    

Isso permite que os desenvolvedores se concentrem **nas funções específicas da aplicação**, sem precisar implementar toda a estrutura do sistema.

---

# Pontos Importantes para Prova

Estude principalmente:

### Diferença entre GPOS e RTOS

|GPOS|RTOS|
|---|---|
|Uso geral|Tempo real|
|Muitas aplicações|Aplicações específicas|
|Tempo não determinístico|Tempo determinístico|

---

### Tipos de RTOS

- **Hard Real-Time** → prazos obrigatórios
    
- **Soft Real-Time** → pequenos atrasos permitidos
    

---

### Vantagens de usar SO embarcado

- funcionalidades prontas
    
- confiabilidade
    
- facilidade de implementação
    
- menor custo de desenvolvimento
    

---
