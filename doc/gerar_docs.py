#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Geração da Documentação Formal em DOCX (.docx)
Repositório: Estudos-feito-de-atividades-do-sagah
Gera doc/DOCUMENTACAO_SISTEMA_ESTUDOS.docx formatado profissionalmente.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Define a cor de fundo de uma célula da tabela."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Define as margens internas de uma célula."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for margin_name, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{margin_name}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(doc, text, title="NOTA DE GOVERNANÇA:"):
    """Adiciona um bloco em estilo Callout com barra lateral e fundo cinza."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=120, bottom=120, left=200, right=200)
    
    # Borda esquerda destacada (azul petróleo)
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:sz'), '24') # 3pt
    left.set(qn('w:space'), '0')
    left.set(qn('w:color'), '1A365D')
    tcBorders.append(left)
    
    for b_name in ['top', 'bottom', 'right']:
        b = OxmlElement(f'w:{b_name}')
        b.set(qn('w:val'), 'none')
        tcBorders.append(b)
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run_title = p.add_run(f"{title} ")
    run_title.bold = True
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(26, 54, 93)
    
    run_txt = p.add_run(text)
    run_txt.font.size = Pt(10)
    run_txt.font.color.rgb = RGBColor(45, 55, 72)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def format_table(table, header_bg="1A365D", alt_bg="F7FAFC"):
    """Formata tabela com cabeçalho escuro e linhas zebradas."""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Cabeçalho
    for cell in table.rows[0].cells:
        set_cell_background(cell, header_bg)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.size = Pt(10)
                r.font.color.rgb = RGBColor(255, 255, 255)
    
    # Linhas de dados
    for i, row in enumerate(table.rows[1:], start=1):
        bg = alt_bg if i % 2 == 1 else "FFFFFF"
        for cell in row.cells:
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(45, 55, 72)

def generate_document():
    doc = Document()
    
    # Configuração de Margens da Página (A4: 2.5 cm em todas as bordas)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
    
    # ==================== CAPA FORMAL ====================
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(80)
    title_p.paragraph_format.space_after = Pt(12)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = title_p.add_run("MANUAL DE OPERAÇÃO E GOVERNANÇA DE CONHECIMENTO")
    r_title.bold = True
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = RGBColor(26, 54, 93)
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(40)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub_p.add_run("Arquitetura de Informação, Metodologia de Síntese SAGAH e Gestão de Vault no Obsidian")
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(74, 85, 104)
    
    # Tabela de Metadados da Capa
    meta_table = doc.add_table(rows=5, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Repositório / Projeto:", "Estudos-feito-de-atividades-do-sagah"),
        ("Autor Principal:", "Jean Vitor Da Silva Lopes"),
        ("Engenharia de Documentação:", "Google DeepMind / Antigravity Assistant"),
        ("Versão do Documento:", "v1.2.0 (Edição Oficial Outubro/2026)"),
        ("Classificação:", "Documento Técnico e Operacional Interno")
    ]
    for row_idx, (label, val) in enumerate(meta_data):
        cell_lbl, cell_val = meta_table.rows[row_idx].cells
        cell_lbl.paragraphs[0].add_run(label).bold = True
        cell_val.paragraphs[0].add_run(val)
        set_cell_margins(cell_lbl, top=80, bottom=80, left=100, right=100)
        set_cell_margins(cell_val, top=80, bottom=80, left=100, right=100)
    
    doc.add_page_break()
    
    # ==================== SUMÁRIO EXECUTIVO ====================
    h1 = doc.add_heading("1. Visão Geral e Propósito do Sistema", level=1)
    h1.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    doc.add_paragraph(
        "Este manual descreve a governança de engenharia de conhecimento aplicada ao repositório de estudos acadêmicos "
        "do estudante Jean Vitor Da Silva Lopes. O sistema foi projetado para atuar como um Segundo Cérebro (PKM - Personal "
        "Knowledge Management), convertendo os conteúdos programáticos densos e Unidades de Aprendizagem (UAs) da plataforma "
        "SAGAH em notas atômicas, estruturadas, hiperconectadas e otimizadas para retenção de longo prazo e revisão para exames."
    )
    
    add_callout(
        doc,
        "A governança estabelece que nenhuma nota deve ser criada sem o bloco padronizado de metadados YAML na linha 1, "
        "e todos os conteúdos devem seguir a metodologia Golden Standard para garantir escaneabilidade e Active Recall.",
        "DIRETRIZ ESTRATÉGICA:"
    )
    
    # ==================== 2. ARQUITETURA DE DIRETÓRIOS ====================
    h2 = doc.add_heading("2. Arquitetura da Informação e Estrutura de Pastas", level=1)
    h2.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    doc.add_paragraph(
        "A taxonomia de diretórios adota um modelo Crono-Temático modular, segmentando os materiais por ano letivo e disciplinas formais. "
        "Recentemente, foi padronizada a criação de subpastas por Unidade de Aprendizagem (AU01 a AU06) para abrigar arquivos de entrada brutos "
        "(PDFs e textos) junto aos seus respectivos resumos gerados."
    )
    
    tree_text = (
        ".\n"
        "├── .obsidian/                       # Configurações do vault\n"
        "├── doc/                             # Manuais e documentações executivas\n"
        "│   ├── README.md                    # Documentação técnica em Markdown\n"
        "│   ├── GUIA_PADRONIZACAO.md         # Guia rápido de regras e checklist\n"
        "│   ├── PROMPT_CRIACAO_RESUMOS.md    # Template de prompt mestre para IA\n"
        "│   └── DOCUMENTACAO_SISTEMA_ESTUDOS.docx # Este documento formal\n"
        "├── 2025/                            # Ciclos letivos anteriores\n"
        "│   ├── Banco-de-Dados/\n"
        "│   ├── Desenvolvimento-Mobile/\n"
        "│   └── Metodologia-Agil/\n"
        "└── 2026/                            # Ciclos acadêmicos vigentes\n"
        "    ├── Algoritmos-e-Complexidade/   # Modelos teóricos, paralelismo e ordenação\n"
        "    │   ├── UA01 - Modelos de Computação e Eficiência de Algoritmos/\n"
        "    │   ├── UA02 - Divisão e Conquista em Programação Paralela/\n"
        "    │   └── UA03 - Métodos de Ordenação Interna de Dados/\n"
        "    ├── Inteligencia-Artificial/     # Ecossistema Python, ML clássico, clustering e PDI\n"
        "    │   ├── UA01 - Introdução ao Python e Ambiente de Desenvolvimento/\n"
        "    │   ├── UA02 - Funções e Programação Orientada a Objetos em Python/\n"
        "    │   ├── UA03 - Conceitos Básicos de Aprendizado de Máquina/\n"
        "    │   ├── UA04 - Árvores de Decisão e Regressão com Scikit-Learn/\n"
        "    │   ├── UA05 - Agrupamento e Métricas de Validação de Clusters/\n"
        "    │   └── UA06 - Fundamentos do Processamento Digital de Imagens/\n"
        "    ├── Governança-de-TI/            # Governança corporativa e alinhamento\n"
        "    │   ├── assets/                  # Imagens e infográficos locais\n"
        "    │   ├── UA01 - Fatores Motivadores da Governança de TI/\n"
        "    │   ├── UA02 - Mecanismos de Decisão em TI/\n"
        "    │   ├── UA03 - Objetivos Normas e Boas Práticas/\n"
        "    │   ├── UA04 - Alinhamento Estratégico e Planejamento de TI/\n"
        "    │   ├── UA05 - Projeto de Governança de TI/\n"
        "    │   └── UA06 - Regulamentações da Governança em TI/\n"
        "    ├── Desenvolvimento-de-Games/\n"
        "    └── IoT Rafael/                  # Sistemas embarcados e RTOS"
    )
    p_code = doc.add_paragraph()
    r_code = p_code.add_run(tree_text)
    r_code.font.name = "Courier New"
    r_code.font.size = Pt(8.5)
    r_code.font.color.rgb = RGBColor(44, 62, 80)

    add_callout(
        doc,
        "Subpastas e arquivos de módulos NÃO devem utilizar prefixos genéricos como 'AU01' ou 'AU02'. "
        "É obrigatório nomear cada subpasta com o identificador 'UA{NN}' acompanhado do nome da matéria/tópico "
        "(exemplo: 'UA02 - Mecanismos de Decisão em TI'). Isso viabiliza busca global e indexação rápida no Obsidian.",
        "REGRA DE NOMENCLATURA DE MÓDULOS:"
    )
    
    # ==================== 3. METADADOS E FRONTMATTER ====================
    h3 = doc.add_heading("3. Especificação de Metadados e Frontmatter YAML", level=1)
    h3.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    doc.add_paragraph(
        "Toda nota técnica deve conter o cabeçalho padronizado em formato YAML. Este esquema garante que ferramentas analíticas, "
        "como o plugin Dataview do Obsidian, consigam indexar, filtrar e criar painéis dinâmicos de estudo."
    )
    
    table_yaml = doc.add_table(rows=7, cols=4)
    table_yaml.rows[0].cells[0].paragraphs[0].text = "Campo"
    table_yaml.rows[0].cells[1].paragraphs[0].text = "Tipo"
    table_yaml.rows[0].cells[2].paragraphs[0].text = "Obrigatoriedade"
    table_yaml.rows[0].cells[3].paragraphs[0].text = "Descrição e Propósito"
    
    yaml_fields = [
        ("disciplina", "String", "Obrigatório", "Nome institucional padronizado da matéria."),
        ("ciclo", "String", "Obrigatório", "Ciclo ou semestre letivo (ex: '1° Ciclo')."),
        ("ano", "Integer", "Obrigatório", "Ano cronológico de realização (ex: 2026)."),
        ("unidade_sagah", "Integer", "Recomendado", "Número identificador da UA do SAGAH (ex: 1, 2)."),
        ("titulo", "String", "Obrigatório", "Nome completo do tema central da nota."),
        ("status", "Enum", "Obrigatório", "Estado da nota: 'Rascunho', 'Revisão' ou 'Concluído'.")
    ]
    for idx, (f, t, o, d) in enumerate(yaml_fields, start=1):
        table_yaml.rows[idx].cells[0].paragraphs[0].text = f
        table_yaml.rows[idx].cells[1].paragraphs[0].text = t
        table_yaml.rows[idx].cells[2].paragraphs[0].text = o
        table_yaml.rows[idx].cells[3].paragraphs[0].text = d
    format_table(table_yaml)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # ==================== 4. METODOLOGIA DIDÁTICA ====================
    h4 = doc.add_heading("4. Metodologia Pedagógica: Golden Standard", level=1)
    h4.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    doc.add_paragraph(
        "Para combater a ilusão de competência gerada por resumos meramente descritivos, o modelo adota quatro princípios pedagógicos:"
    )
    
    doc.add_paragraph(
        "• Técnica Feynman: Tradução de jargões técnicos complexos em metáforas do mundo real (ex: o carro como sistema de informação, "
        "onde hardware é chassi/motor, software é injeção eletrônica e dados são combustível).\n"
        "• Síntese Visual e Contraste: Inclusão obrigatória de tabelas de comparação lado a lado (ex: QuickSort vs MergeSort, K-Means vs DBSCAN).\n"
        "• Foco em Avaliações (Dica do Professor): Destaque explícito para armadilhas conceituais e tópicos de alta frequência em provas.\n"
        "• Recordação Ativa (Active Recall): Resolução comentada das 5 questões oficiais da UA, fornecendo a justificativa do gabarito "
        "e explicando por que as alternativas falsas foram desconsideradas."
    )
    
    # ==================== 5. ESTUDOS DE CASO E DISCIPLINAS IMPLEMENTADAS ====================
    h5 = doc.add_heading("5. Disciplinas e Estudos de Caso Implementados (Ciclo 2026)", level=1)
    h5.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    doc.add_paragraph(
        "Todas as matérias ativas de 2026 foram sintetizadas integralmente no padrão Golden Standard, abrangendo:"
    )
    
    doc.add_paragraph(
        "1. Governança de TI: Fatores motivadores (SI, Applegate), mecanismos de decisão, COBIT/ITIL, alinhamento estratégico e LGPD.\n"
        "2. Algoritmos e Complexidade (UAs 01 a 03): Modelos computacionais (RAM, Turing), classes P/NP, Teorema Mestre e paralelismo PRAM, "
        "além de análise detalhada de ordenação interna (QuickSort, MergeSort, HeapSort, ShellSort).\n"
        "3. Inteligência Artificial (UAs 01 a 06): Do ambiente Python e POO até Machine Learning supervisionado (Árvores de Decisão, "
        "Regressão Linear/Logística, Overfitting), não-supervisionado (k-Means, Silhueta, Calinski-Harabasz) e Processamento Digital de Imagens "
        "(Bartlane, JPL/NASA, convoluções espaciais e segmentação HSV)."
    )
    
    # ==================== 6. CONTROLE DE VERSÕES ====================
    h6 = doc.add_heading("6. Controle de Versões e Histórico de Mudanças (Changelog)", level=1)
    h6.runs[0].font.color.rgb = RGBColor(26, 54, 93)
    
    tbl_ver = doc.add_table(rows=5, cols=4)
    tbl_ver.rows[0].cells[0].paragraphs[0].text = "Versão"
    tbl_ver.rows[0].cells[1].paragraphs[0].text = "Data"
    tbl_ver.rows[0].cells[2].paragraphs[0].text = "Autor"
    tbl_ver.rows[0].cells[3].paragraphs[0].text = "Resumo das Alterações"
    
    vers = [
        ("v1.0.0", "12/10/2026", "Jean Vitor & Antigravity", "Auditoria do repositório, criação do GUIA_PADRONIZACAO.md e Golden Standard."),
        ("v1.1.0", "12/10/2026", "Jean Vitor & Antigravity", "Inclusão de Governança de TI, criação da UA01 e PROMPT_CRIACAO_RESUMOS.md."),
        ("v1.2.0", "12/10/2026", "Jean Vitor & Antigravity", "Subpastas AU01-AU06, doc/ centralizada, README raiz e script DOCX."),
        ("v1.3.0", "13/10/2026", "Jean Vitor & Antigravity", "Expansão de Algoritmos e Complexidade (UAs 1-3) e IA (UAs 1-6); eliminação de prefixos AU0X; sincronização MD e DOCX.")
    ]
    for idx, (v, dt, au, desc) in enumerate(vers, start=1):
        tbl_ver.rows[idx].cells[0].paragraphs[0].text = v
        tbl_ver.rows[idx].cells[1].paragraphs[0].text = dt
        tbl_ver.rows[idx].cells[2].paragraphs[0].text = au
        tbl_ver.rows[idx].cells[3].paragraphs[0].text = desc
    format_table(tbl_ver)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(20)
    
    # Salvamento do documento
    output_path = os.path.join(os.path.dirname(__file__), "DOCUMENTACAO_SISTEMA_ESTUDOS.docx")
    doc.save(output_path)
    print(f"Documento DOCX gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    generate_document()
