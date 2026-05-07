#import "@preview/ilm:2.0.0": *

#set text(lang: "pt")

#show: ilm.with(
  title: [Relatório: Análise e Visualização de Dados],
  authors: "André Montenegro e Lucas Cardoso",
  abstract: [
    Este relatório apresenta uma análise da evolução dos principais indicadores do mercado de trabalho brasileiro: taxa de desocupação, nível de emprego e taxa de informalidade.
  ],
  figure-index: (enabled: false),
  table-index: (enabled: false),
  listing-index: (enabled: false),
  table-of-contents: none,
)

= Introdução
Neste relatório, exploramos a dinâmica do mercado de trabalho no Brasil. Utilizamos dados históricos trimestrais para entender como a *desocupação*, o *emprego* e a *informalidade* se comportaram ao longo da última década, com um olhar especial para a diferença entre homens e mulheres.

A compreensão desses indicadores é fundamental para avaliar a saúde econômica do país e a qualidade de vida de sua população. O período em análise abrange momentos de forte recessão econômica, como os anos de 2015 e 2016, as profundas distorções causadas pela pandemia da COVID-19 em 2020 e a fase de recuperação mais recente. A partir do cruzamento dessas métricas, buscamos não apenas traçar um panorama histórico, mas também jogar luz sobre desafios persistentes de desigualdade estrutural, evidenciados principalmente pelas marcantes diferenças na inserção produtiva por gênero.

== Metodologia
Os dados brutos foram processados em Python (`desocup.ipynb`, `emp.ipynb`, e `infor.ipynb`), onde as séries foram limpas, e os períodos de lacuna na coleta (como os ocorridos durante a pandemia) foram tratados. Os dados finais consolidados encontram-se na pasta `dados_tratados`.

Para garantir a integridade da análise, o processo de limpeza envolveu a padronização das datas para um formato trimestral uniforme e a conversão das taxas para dados puramente numéricos. O tratamento das lacunas na coleta — decorrentes das interrupções nas pesquisas governamentais durante os meses mais severos de isolamento social — exigiu técnicas de preenchimento adequadas para não distorcer as tendências. As bases resultantes (`des_trat.csv`, `df_emprego_clean.csv` e `df_informalidade_clean.csv`) foram estruturadas em colunas divididas por agregados globais e por gênero ("total", "homens" e "mulheres"), criando a base perfeita para as visualizações presentes neste documento.

= Análise dos Indicadores

== Taxa de Desocupação
A desocupação é um dos termômetros mais importantes da economia. Aqui, podemos inserir o gráfico gerado a partir de `des_trat.csv` mostrando a evolução da taxa geral, comparando também a situação entre homens e mulheres.

Ao analisar a série histórica, observa-se que a taxa de desocupação apresentou um crescimento expressivo a partir de 2015, atingindo seu pico no início de 2017 (chegando a 19% no geral). Um aspecto que chama a atenção é a disparidade de gênero: a taxa de desocupação entre as mulheres manteve-se consistentemente superior à dos homens em todo o período analisado, chegando a ultrapassar a marca de 21% no auge da crise. Nos anos mais recentes, a partir de 2024, nota-se uma tendência de queda contínua, com a taxa geral recuando para patamares abaixo de 10% no final de 2025.

#figure(
  image("desocupacao.png", width: 100%),
  caption: [Evolução da Taxa de Desocupação (2012-2025)]
)

== Emprego e Ocupação
O nível da ocupação nos mostra a proporção de pessoas em idade de trabalhar que estão efetivamente trabalhando.

Os dados revelam uma estabilidade no nível de emprego geral ao longo da década, flutuando em torno de 55%. No entanto, fica evidente uma forte desigualdade estrutural de gênero: enquanto o nível de ocupação dos homens orbita a faixa dos 67% a 69%, o das mulheres permanece significativamente menor, estacionado na casa dos 43% a 45%. Houve uma queda expressiva durante o ano de 2020 devido à pandemia, seguida de uma recuperação gradual nos anos subsequentes, atingindo picos de ocupação em 2024 antes de uma leve estabilização em 2025.

#figure(
  image("emprego.png", width: 100%),
  caption: [Evolução do Nível de Emprego]
)

== Informalidade
A partir do final de 2015, passamos a observar também a taxa de informalidade, que revela a precarização das relações de trabalho.

A informalidade no Brasil manteve-se em patamares elevados durante todo o período, oscilando majoritariamente entre 46% e 50%. Nota-se um pico em meados de 2022, onde a taxa geral atingiu 53%. Curiosamente, ao contrário da desocupação, a taxa de informalidade tende a ser ligeiramente superior entre os homens, frequentemente ultrapassando a marca dos 50%, enquanto para as mulheres a taxa oscila mais próxima aos 46%. Nos últimos trimestres de 2025, os dados mostram um leve arrefecimento, com o indicador geral retornando a níveis próximos a 46%.

#figure(
  image("informalidade.png", width: 100%),
  caption: [Evolução da Taxa de Informalidade (a partir de 2015)]
)

= Conclusão
Ao observar os dados tratados, notamos tendências importantes sobre a recuperação do mercado de trabalho e as disparidades de gênero. 

A análise conjunta dos indicadores de desocupação, nível de emprego e informalidade evidencia um mercado de trabalho marcado por oscilações fortes frente a crises econômicas, como a de 2015/2016 e a pandemia de 2020. Embora os anos mais recentes (2024 e 2025) apontem para uma recuperação efetiva – com queda contínua no desemprego e leve arrefecimento da informalidade –, a desigualdade de gênero permanece como um desafio estrutural persistente. As mulheres continuam apresentando maiores taxas de desocupação e níveis expressivamente menores de inserção em vagas de emprego em comparação aos homens, indicando que a recuperação econômica não atinge todos os grupos demográficos com a mesma intensidade.
