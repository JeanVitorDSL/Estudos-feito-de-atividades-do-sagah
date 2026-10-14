![GitHub repo size](https://img.shields.io/github/repo-size/JeanVitorDSL/Resumos-Atividades)
![GitHub stars](https://img.shields.io/github/stars/JeanVitorDSL/Resumos-Atividades)
![GitHub last commit](https://img.shields.io/github/last-commit/JeanVitorDSL/Resumos-Atividades)

# 📚 Repositório de Estudos e Gestão de Conhecimento Acadêmico
> Vault do Obsidian dedicado à centralização, síntese metodológica e retenção ativa de conteúdos universitários e Unidades de Aprendizagem (UAs) da plataforma **SAGAH**.

---

## 🎯 Visão Geral e Propósito

Este repositório atua como o **Segundo Cérebro (PKM - Personal Knowledge Management)** acadêmico de Jean Vitor Da Silva Lopes, combinando o poder do **Obsidian** (hiperlinks bidirecionais e visualização em grafo), rigorosa **padronização semântica** e **automação controlada por Inteligência Artificial**.

### Objetivos Centrais:
- 📖 **Centralização Estruturada:** Armazenar de forma crono-temática todas as disciplinas dos ciclos universitários.
- 🧠 **Aprendizagem Ativa e Retenção:** Converter leituras extensas e infográficos em resumos focados em *Active Recall* (perguntas e respostas comentadas), *Técnica Feynman* (analogias cotidianas) e tabelas comparativas.
- 🎯 **Foco em Exames:** Destacar armadilhas conceituais e tópicos críticos para provas acadêmicas.
- 🛠️ **Governança e Portabilidade:** Manter a base 100% versionada em Git, garantindo histórico contínuo e interoperabilidade.

---

## 📂 Arquitetura do Repositório

O repositório é organizado de forma **Crono-Temática** (por ano letivo e disciplinas canônicas):

```text
.
├── .obsidian/                                  # Configurações globais e plugins do vault
├── doc/                                        # Documentação técnica e governança oficial
│   ├── README.md                               # Manual completo de operação de ponta a ponta
│   ├── GUIA_PADRONIZACAO.md                    # Guia rápido de regras e checklist de revisão
│   ├── PROMPT_CRIACAO_RESUMOS.md               # Prompt mestre para geração automatizada via IA
│   └── DOCUMENTACAO_SISTEMA_ESTUDOS.docx       # Versão formal executiva da documentação
│
├── 2025/                                       # Ciclos acadêmicos de 2025
│   ├── Banco-de-Dados/                         # Álgebra relacional, SGBD, BI e Data Marts
│   ├── Desenvolvimento-Mobile/                 # Ecossistema .NET, mockups, UX e APIs nativas
│   └── Metodologia-Agil/                       # Estimativas de custos (PMBOK), riscos e Scrum
│
└── 2026/                                       # Ciclos acadêmicos de 2026
    ├── Algoritmos-e-Complexidade/              # Modelos computacionais, divisão e conquista, ordenação interna
    │   ├── UA01 - Modelos de Computação e Eficiência de Algoritmos/
    │   ├── UA02 - Divisão e Conquista em Programação Paralela/
    │   └── UA03 - Métodos de Ordenação Interna de Dados/
    ├── Inteligencia-Artificial/                # Python OOP, ML básico, árvores de decisão, k-Means, PDI
    │   ├── UA01 - Introdução ao Python e Ambiente de Desenvolvimento/
    │   ├── UA02 - Funções e Programação Orientada a Objetos em Python/
    │   ├── UA03 - Conceitos Básicos de Aprendizado de Máquina/
    │   ├── UA04 - Árvores de Decisão e Regressão com Scikit-Learn/
    │   ├── UA05 - Agrupamento e Métricas de Validação de Clusters/
    │   └── UA06 - Fundamentos do Processamento Digital de Imagens/
    ├── Governança-de-TI/                       # Governança corporativa, matrizes de decisão e alinhamento
    │   ├── assets/                             # Infográficos e recursos visuais locais
    │   ├── UA01 - Fatores Motivadores da Governança de TI/
    │   ├── UA02 - Mecanismos de Decisão em TI/
    │   ├── UA03 - Objetivos Normas e Boas Práticas/
    │   ├── UA04 - Alinhamento Estratégico e Planejamento de TI/
    │   ├── UA05 - Projeto de Governança de TI/
    │   └── UA06 - Regulamentações da Governança em TI/
    ├── Desenvolvimento-de-Games/               # Tétrade elementar, círculo mágico, ludologia e flow
    └── IoT Rafael/                             # Sistemas embarcados, ARM, RTOS e microcontroladores
```

---

## 🎓 Metodologia de Síntese (Golden Standard)

Todas as notas de estudo seguem um padrão uniforme de engenharia pedagógica:

1. **Metadados (Frontmatter YAML):** Cabeçalho padronizado contendo disciplina, ciclo, unidade SAGAH, status e taxonomia de tags aninhadas (`#faculdade/...`, `#tipo/...`, `#topico/...`).
2. **Técnica Feynman:** Explicações claras acompanhadas de analogias do mundo real (ex: carro de alta performance, biblioteca pública, almoxarifado).
3. **Síntese Visual:** Tabelas comparativas em Markdown contrastando modelos técnicos (ex: RISC vs CISC, GPOS vs RTOS, Suporte vs Estratégico).
4. **Dica do Professor:** Alertas destacados sobre os pontos mais cobrados em avaliações e concursos.
5. **Active Recall:** Questões oficiais de autoavaliação do SAGAH com gabarito comentado e justificativas pedagógicas detalhadas (*"🎯 Por quê?"*).

---

## 📖 Central de Documentação e Manuais

Para acessar as diretrizes completas de governança, templates e procedimentos operacionais, consulte a pasta [`doc/`](file:///home/jeann/Documentos/Project/Estudos-feito-de-atividades-do-sagah/doc/):

| Documento | Descrição |
| :--- | :--- |
| 📘 **[`doc/README.md`](file:///home/jeann/Documentos/Project/Estudos-feito-de-atividades-do-sagah/doc/README.md)** | Manual operacional de ponta a ponta: arquitetura, Dataview queries, neurociência do estudo e pipeline do aluno. |
| 📋 **[`doc/GUIA_PADRONIZACAO.md`](file:///home/jeann/Documentos/Project/Estudos-feito-de-atividades-do-sagah/doc/GUIA_PADRONIZACAO.md)** | Regras rápidas de estilo, taxonomia de tags, templates em Markdown e checklist pré-commit. |
| 🤖 **[`doc/PROMPT_CRIACAO_RESUMOS.md`](file:///home/jeann/Documentos/Project/Estudos-feito-de-atividades-do-sagah/doc/PROMPT_CRIACAO_RESUMOS.md)** | Prompt mestre para geração automatizada de novos resumos a partir de materiais brutos do SAGAH. |

---

## 🚀 Como Utilizar Este Repositório

### No Obsidian (Uso Recomendado):
1. Abra o Obsidian e selecione a opção **"Open folder as vault"**.
2. Aponte para a pasta raiz deste repositório.
3. Navegue pela árvore de pastas ou utilize o grafo de conhecimento para visualizar as conexões entre notas.
4. Para consultas automáticas, certifique-se de ter o plugin comunitário **Dataview** ativado.

### Adicionando Novos Resumos com IA:
1. Cole os materiais brutos da nova Unidade na pasta da matéria (ex: `2026/Governança-de-TI/UA02 - Mecanismos de Decisão em TI/`).
2. Utilize o prompt configurado em [`doc/PROMPT_CRIACAO_RESUMOS.md`](file:///home/jeann/Documentos/Project/Estudos-feito-de-atividades-do-sagah/doc/PROMPT_CRIACAO_RESUMOS.md).
3. O arquivo final formatado será gerado diretamente com Frontmatter, tabelas comparativas e questões comentadas.

---

## 👨‍💻 Autor

**Jean Vitor Da Silva Lopes**  
- 📎 GitHub: [https://github.com/JeanVitorDSL](https://github.com/JeanVitorDSL)

---

⭐ *Caso este repositório auxilie em sua jornada acadêmica, considere deixar uma estrela no GitHub!*
