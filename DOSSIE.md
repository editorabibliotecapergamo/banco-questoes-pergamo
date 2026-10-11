# Dossiê do Projeto — Banco de Questões e Simulados (Colégio Nova Jornada)

Memória escrita do projeto. Serve para registrar o que já foi decidido, o que está
em estudo e as ideias para o futuro, evitando contradições entre conversas.

**Como usar:** antes de propor ou alterar algo, conferir as seções "Decisões" e
"Princípios". Novas ideias entram em "Banco de ideias"; quando o Augusto decide, o
item sobe para "Decisões" com a data. Itens nunca são apagados: se uma decisão
mudar, a antiga fica riscada com o motivo.

Última atualização: 2026-10-11

---

## 1. O projeto em poucas linhas

- Arquivo único `index.html` (HTML, CSS e JavaScript puros, sem bibliotecas nem servidor).
- 1.000 questões de Ciências, 250 por série (6º ao 9º ano), em 17 módulos, com 5 alternativas (A a E).
- 229 questões têm imagem embutida (PNG em base64), o que deixa o arquivo com cerca de 10 MB.
- As questões ficam em `const BANCO_COMPLETO = [...]`, em uma única linha do `index.html`.
- Funções: filtros (série, módulo, dificuldade, imagem), simulado de até 40 questões
  (manual ou automático), visualização em formato de prova, gabarito do professor,
  cartão-resposta, exportação para Word e impressão.

## 2. Princípios do uso (ditos pelo Augusto)

- O simulado impresso é a prova do aluno; o **gabarito de respostas** é gerado junto e
  será usado para **comparar as respostas dos alunos** (conferência feita pelo professor).
- Por isso, a ordem das alternativas na prova e a letra do gabarito têm de coincidir sempre.

## 3. Decisões tomadas

| Data | Decisão | Observações |
|------|---------|-------------|
| 2026-10-11 | As alternativas são **embaralhadas ao levar as questões para a aba "Visualizar Simulado"**. O banco de questões continua mostrando a ordem original. | Implementado no PR #1 (já incorporado). |
| 2026-10-11 | A ordem embaralhada **fica fixa** enquanto a página estiver aberta, e vale para tela, impressão, Word e gabarito. | O botão "🔀 Embaralhar de novo" sorteia outra ordem para todo o simulado. |

## 4. Em estudo / aguardando resposta do Augusto

- A segunda ideia que o Augusto mencionou ("pensei em duas coisas") ainda não foi dita. **Perguntar de novo.**
- Quais das sugestões do banco de ideias (seção 6) entram e em que ordem.
- **Expansão para todas as matérias e um ano inteiro de conteúdo** (pedido do Augusto em 2026-10-11, ideia I-13). Avaliada como viável, mas exige mudar a arquitetura (ver I-13). Aguardando as respostas do Augusto: quais matérias e séries, e qual material didático servirá de base.

## 5. Problemas conhecidos

1. **Gabarito muito concentrado na letra B.** Na ordem original, B é a correta em 834 das 1.000
   questões (A: 137, C: 25, D: 4, E: 0). *Resolvido na visualização do simulado pelo embaralhamento (decisão de 2026-10-11).*
2. **A alternativa correta costuma ser a mais longa:** 819 das 1.000 questões. Embaralhar não
   resolve isso; é um problema de redação das alternativas erradas, que precisam ficar com
   tamanho e detalhamento parecidos com o da correta. Exige revisão de conteúdo.
3. **A ordem embaralhada se perde ao recarregar a página.** Se o professor imprimir a prova,
   recarregar e imprimir o gabarito depois, as letras não vão bater. Regra prática por
   enquanto: **imprimir/baixar prova e gabarito na mesma sessão.** (Ver ideia I-02.)
4. **"Gerar Simulado Automático" sempre devolve as mesmas questões**, porque pega as primeiras
   de cada dificuldade em cada módulo (`slice(0, n)`), sem sorteio. (Ver ideia I-03.)
5. **"4º BIMESTRE DE 2026" está fixo no texto** do cabeçalho e da folha de respostas (a turma
   já é editável na tela). (Ver ideia I-07.)
6. O arquivo tem cerca de 10 MB por causa das imagens embutidas, o que deixa a abertura mais lenta.

Verificações já feitas nos dados (2026-10-11): nenhum enunciado duplicado; códigos `uid`
únicos; todo gabarito aponta para uma alternativa existente; **nenhuma justificativa,
enunciado ou alternativa cita outra alternativa por letra** (por isso o embaralhamento é
seguro: nenhum texto vira "errado" ao trocar a ordem).

## 6. Banco de ideias (ainda não decididas)

Prioridade sugerida: **A** (alta), **M** (média), **B** (baixa). Nenhuma foi aprovada ainda.

| ID | Prio. | Ideia | Observações |
|----|-------|-------|-------------|
| I-01 | A | Revisar as alternativas erradas para equilibrar o tamanho em relação à correta | Problema 2. Dá para listar primeiro as questões mais desbalanceadas. |
| I-02 | A | **Código da prova** (ex.: `Prova 7K3F`) impresso no cabeçalho, que permite regenerar exatamente a mesma ordem e o mesmo gabarito depois | Resolve o problema 3; base para as versões A/B. |
| I-03 | A | Simulado automático com **sorteio** das questões, mantendo a distribuição por módulo e dificuldade | Problema 4. |
| I-04 | A | **Correção assistida:** digitar ou colar as respostas de cada aluno e calcular nota, acertos por aluno e por questão | Liga com o uso descrito pelo Augusto (comparar respostas com o gabarito). |
| I-05 | M | Versões A/B/C da mesma prova (ordem das questões e das alternativas diferentes) | Depende de I-02. |
| I-06 | M | Salvar a seleção e simulados prontos no navegador, para não perder o trabalho ao recarregar | Hoje a seleção some ao recarregar. |
| I-07 | M | Campos editáveis para bimestre, ano e data no cabeçalho e na folha de respostas | Problema 5. |
| I-08 | M | Busca por palavra e filtro por tema | |
| I-09 | M | Marcar questões como "revisar" ou "problema" durante o uso | Alimenta I-01. |
| I-10 | B | Separar os dados e as imagens do código (arquivos próprios) | Deixa a página mais leve e facilita editar questões. |
| I-11 | B | Publicar no GitHub Pages (link para os professores abrirem) | |
| I-12 | B | README com instruções de uso | |
| I-13 | A (longo prazo) | **Super banco de questões:** todas as matérias, um ano inteiro de conteúdo, embasado em material didático escolar | Hoje: 1.000 questões = cerca de 9,8 MB, sendo 1,2 MB de texto e 8,6 MB de imagens (cerca de 37 KB por imagem). Em escala (dezenas de milhares de questões) não cabe em um `index.html`: precisa de dados em arquivos separados por matéria e série (carregados sob demanda) e imagens em arquivos próprios (depende de I-10). Qualidade: precisa de roteiro de conteúdo por matéria (currículo/BNCC e o material do colégio), checagens automáticas (equilíbrio do gabarito, tamanho das alternativas, duplicatas, estrutura) e revisão por professor, em amostra, antes de liberar cada lote. Direitos autorais: usar o material próprio do colégio e a BNCC como base; não copiar livros de editoras. |

## 7. Histórico

- 2026-10-11 — Primeira análise do repositório; criado este dossiê; embaralhamento das alternativas implementado (PR #1).
