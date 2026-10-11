// Catálogo de matérias do portal.
// "arquivos" aponta para os arquivos de cada série (sem a extensão): <base>.js tem as questões e <base>.imagens.js as ilustrações.
// Para liberar uma matéria nova: criar os arquivos de dados, preencher "arquivos" e trocar "disponivel" para true (ver docs/ESTRUTURA.md).
window.CATALOGO = {
  disciplinas: [
    {
      codigo: 'CIEN', nome: 'Ciências', segmento: 'Ensino Fundamental II', disponivel: true,
      series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'],
      arquivos: {
        '6º Ano': 'dados/ciencias/6ano',
        '7º Ano': 'dados/ciencias/7ano',
        '8º Ano': 'dados/ciencias/8ano',
        '9º Ano': 'dados/ciencias/9ano'
      }
    },
    { codigo: 'PORT', nome: 'Língua Portuguesa', segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} },
    { codigo: 'MAT',  nome: 'Matemática',        segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} },
    { codigo: 'HIST', nome: 'História',          segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} },
    { codigo: 'GEOG', nome: 'Geografia',         segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} },
    { codigo: 'INGL', nome: 'Língua Inglesa',    segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} },
    { codigo: 'ARTE', nome: 'Arte',              segmento: 'Ensino Fundamental II', disponivel: false, series: ['6º Ano', '7º Ano', '8º Ano', '9º Ano'], arquivos: {} }
  ]
};
