#!/usr/bin/env python3
"""Valida os arquivos de questões em dados/ (somente biblioteca padrão do Python).

Uso: python3 scripts/validar_banco.py [pasta_dados]

ERRO   = problema de estrutura; o script termina com código 1.
AVISO  = problema de qualidade pedagógica (gabarito concentrado, correta sempre a mais longa);
         não impede nada, mas deve ser revisado antes de liberar um lote novo.
"""
import collections
import json
import os
import re
import sys

CAMPOS = ['id', 'uid', 'segmento', 'disciplina', 'serie', 'modulo', 'tema', 'dificuldade',
          'enunciado', 'alternativas', 'resposta_correta', 'justificativa', 'possui_imagem']
LETRAS = ['A', 'B', 'C', 'D', 'E']
DIFICULDADES = {'Fácil', 'Médio', 'Difícil'}
LIMITE_LETRA = 0.30      # aviso se uma letra for a correta em mais de 30% das questões do arquivo
LIMITE_MAIS_LONGA = 0.40  # aviso se a correta for a alternativa mais longa em mais de 40%


def ler_dados(caminho, abertura, fechamento):
    texto = open(caminho, encoding='utf-8').read()
    ini = texto.index(abertura) + len(abertura) - 1
    fim = texto.rindex(fechamento) + 1
    return json.loads(texto[ini:fim])


def validar_arquivo(caminho, erros, avisos, uids_vistos, enunciados_vistos):
    nome = os.path.relpath(caminho)
    questoes = ler_dados(caminho, '] = [', ']')
    imagens = {}
    img_arq = caminho[:-3] + '.imagens.js'
    if os.path.exists(img_arq):
        imagens = ler_dados(img_arq, 'Object.assign(window.BANCO_IMG, {', '}')

    for q in questoes:
        ident = q.get('uid', '?')
        faltando = [c for c in CAMPOS if c not in q]
        if faltando:
            erros.append(f'{nome} {ident}: campos ausentes {faltando}')
            continue
        if q['uid'] in uids_vistos:
            erros.append(f'{nome} {ident}: uid repetido')
        uids_vistos.add(q['uid'])
        if not re.fullmatch(r'[A-Z]+-\d+-\d{3}', q['uid']):
            erros.append(f'{nome} {ident}: uid fora do padrão <MATÉRIA>-<série>-<nnn>')
        if q['dificuldade'] not in DIFICULDADES:
            erros.append(f'{nome} {ident}: dificuldade inválida ({q["dificuldade"]})')
        alts = q['alternativas']
        if sorted(alts) != LETRAS or any(not str(alts[l]).strip() for l in LETRAS):
            erros.append(f'{nome} {ident}: precisa ter as alternativas A a E, todas preenchidas')
        elif len({str(alts[l]).strip().lower() for l in LETRAS}) < 5:
            erros.append(f'{nome} {ident}: há alternativas repetidas')
        if q['resposta_correta'] not in LETRAS:
            erros.append(f'{nome} {ident}: resposta_correta inválida ({q["resposta_correta"]})')
        for campo in ('enunciado', 'justificativa', 'modulo', 'tema'):
            if not str(q[campo]).strip():
                erros.append(f'{nome} {ident}: {campo} vazio')
        if q['possui_imagem'] != (q['uid'] in imagens):
            erros.append(f'{nome} {ident}: possui_imagem não confere com o arquivo .imagens.js')
        chave = re.sub(r'\W+', ' ', q['enunciado'].lower()).strip()
        if chave in enunciados_vistos:
            erros.append(f'{nome} {ident}: enunciado repetido (igual ao de {enunciados_vistos[chave]})')
        enunciados_vistos[chave] = q['uid']

    # qualidade do lote
    n = len(questoes)
    if n:
        letras = collections.Counter(q['resposta_correta'] for q in questoes)
        for letra, qtd in letras.items():
            if qtd / n > LIMITE_LETRA:
                avisos.append(f'{nome}: a letra {letra} é a correta em {qtd} de {n} questões ({qtd / n:.0%})')
        mais_longa = sum(1 for q in questoes
                         if len(q['alternativas'].get(q['resposta_correta'], '')) > max(
                             (len(v) for k, v in q['alternativas'].items() if k != q['resposta_correta']), default=0))
        if mais_longa / n > LIMITE_MAIS_LONGA:
            avisos.append(f'{nome}: a correta é a alternativa mais longa em {mais_longa} de {n} questões ({mais_longa / n:.0%})')
    return n


def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'dados')
    erros, avisos, uids, enunciados = [], [], set(), {}
    total = 0
    for raiz, _, arquivos in sorted(os.walk(pasta)):
        for arq in sorted(arquivos):
            if arq.endswith('.js') and not arq.endswith('.imagens.js') and arq != 'catalogo.js':
                total += validar_arquivo(os.path.join(raiz, arq), erros, avisos, uids, enunciados)
    print(f'{total} questões verificadas.')
    for a in avisos:
        print('AVISO:', a)
    for e in erros:
        print('ERRO: ', e)
    print(f'{len(erros)} erro(s), {len(avisos)} aviso(s).')
    sys.exit(1 if erros else 0)


if __name__ == '__main__':
    main()
