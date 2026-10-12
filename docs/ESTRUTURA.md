# Estrutura do projeto

O portal (`index.html`) não guarda mais as questões dentro do código. Os dados ficam em `dados/`
e são carregados sob demanda, uma série por vez.

```
index.html                       portal (interface e regras do simulado)
dados/
  catalogo.js                    lista de matérias e onde estão os arquivos de cada série
  ciencias/
    6ano.js  7ano.js  8ano.js  9ano.js              questões (uma por linha)
    6ano.imagens.js  7ano.imagens.js  ...            ilustrações em base64, por série
scripts/validar_banco.py         valida os arquivos de dados
docs/ESTRUTURA.md                este arquivo
DOSSIE.md                        decisões, problemas conhecidos e banco de ideias
```

O portal funciona aberto direto do computador (duplo clique em `index.html`, com a pasta inteira)
e pelo GitHub Pages. Baixar só o `index.html` não basta mais: a pasta `dados/` precisa acompanhar.

## Formato de uma questão

Cada arquivo `dados/<matéria>/<série>.js` registra um vetor em `window.BANCO[<código da matéria>][<série>]`.
Uma questão por linha, para facilitar a revisão de mudanças no GitHub.

| Campo | Exemplo | Observação |
|-------|---------|-----------|
| `id` | `1` | número dentro do arquivo original |
| `uid` | `"CIEN-6-001"` | `<MATÉRIA>-<série>-<nnn>`; único em todo o banco |
| `segmento` | `"Ensino Fundamental II"` | |
| `disciplina` | `"Ciências"` | |
| `serie` / `ano` | `"6º Ano"` | `ano` repete `serie` e existe só por compatibilidade |
| `modulo` | `"Módulo 14: Transformações Químicas"` | |
| `tema` | `"Fenômenos Físicos e Químicos"` | |
| `dificuldade` | `"Fácil"` | `Fácil`, `Médio` ou `Difícil` |
| `enunciado` | texto | |
| `alternativas` | `{"A": "...", ..., "E": "..."}` | exatamente cinco, todas diferentes |
| `resposta_correta` | `"B"` | letra da ordem original; o simulado embaralha na hora |
| `justificativa` | texto | não deve citar alternativas por letra, porque a ordem muda no simulado |
| `possui_imagem` | `true` / `false` | se `true`, o `uid` precisa estar no arquivo `.imagens.js` |

O arquivo `<série>.imagens.js` guarda, por `uid`, `{"url": "data:image/png;base64,...", "titulo": "...", "legenda": "..."}`.

## Como acrescentar questões a uma série existente

1. Acrescentar as linhas no arquivo da série (e as ilustrações no `.imagens.js`, se houver).
2. Rodar `python3 scripts/validar_banco.py`. Erros precisam ser corrigidos; avisos (gabarito concentrado em uma letra,
   correta sempre a alternativa mais longa) devem ser revistos antes de liberar o lote.
3. Abrir o portal e conferir a série.

## Como acrescentar uma matéria nova

1. Criar `dados/<matéria>/<série>.js` (e `.imagens.js`) no formato acima, com `uid` começando pelo código da matéria.
2. Em `dados/catalogo.js`, preencher `arquivos` da matéria e trocar `disponivel` para `true`.
3. Validar com o script.

Atenção: o portal ainda **não tem seletor de matéria**, e partes do código são específicas de Ciências (listas fixas
de módulos no filtro e no simulado automático, textos de turma, contagens nos botões de série). Isso é o próximo passo
do esqueleto (ver `DOSSIE.md`, ideia I-13). Até lá, a única matéria ativa é `CIEN`.

## Regras de conteúdo

- Nenhum arquivo, texto, imagem ou trecho de material didático de terceiros entra neste repositório, que é público.
  Ver `DOSSIE.md`, seção 2.1.
- As questões devem ser escritas de forma original a partir dos tópicos do currículo.
