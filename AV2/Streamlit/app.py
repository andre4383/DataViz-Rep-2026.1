import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="Mercado de Trabalho Brasileiro",
    page_icon="📊",
    layout="wide"
)

COLOR_TOTAL = '#A9A9A9'
COLOR_HOMENS = '#2A9D8F'
COLOR_MULHERES = '#E76F51'

@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, '..', 'Relatório', 'dados_tratados')
    
    df_desocup = pd.read_csv(os.path.join(data_dir, 'des_trat.csv'))
    df_emprego = pd.read_csv(os.path.join(data_dir, 'df_emprego_clean.csv'))
    df_infor = pd.read_csv(os.path.join(data_dir, 'df_informalidade_clean.csv'))
    
    for df in [df_desocup, df_emprego, df_infor]:
        df['periodo'] = pd.to_datetime(df['periodo'])
        
    return df_desocup, df_emprego, df_infor

try:
    df_desocup, df_emprego, df_infor = load_data()
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

st.title("Dinâmica do Mercado de Trabalho no Brasil")
st.markdown("""
**André Montenegro e Lucas Cardoso**

Análise do mercado de trabalho brasileiro (2012-2025), destacando os impactos das crises (2015/2016 e Pandemia 2020) e a desigualdade de gênero na inserção produtiva.
""")

st.divider()

st.header("1. Taxa de Desocupação")
st.markdown("""
A desocupação atingiu seu pico em 2017. Destaca-se que a **taxa feminina se manteve superior à masculina** em todo o período analisado.
""")

fig_desocup = go.Figure()

fig_desocup.add_vrect(x0="2015-01-01", x1="2017-06-01", fillcolor="red", opacity=0.1, line_width=0, annotation_text="Crise 2015-2016", annotation_position="top left")
fig_desocup.add_vrect(x0="2020-03-01", x1="2021-06-01", fillcolor="red", opacity=0.1, line_width=0, annotation_text="Pandemia", annotation_position="top left")

fig_desocup.add_trace(go.Scatter(x=df_desocup['periodo'], y=df_desocup['total'], mode='lines', name='Total', line=dict(color=COLOR_TOTAL, dash='dot')))
fig_desocup.add_trace(go.Scatter(x=df_desocup['periodo'], y=df_desocup['homens'], mode='lines', name='Homens', line=dict(color=COLOR_HOMENS, width=2)))
fig_desocup.add_trace(go.Scatter(x=df_desocup['periodo'], y=df_desocup['mulheres'], mode='lines', name='Mulheres', line=dict(color=COLOR_MULHERES, width=3)))

fig_desocup.update_layout(
    title='Evolução da Taxa de Desocupação (2012-2025)',
    yaxis_title='Taxa (%)',
    hovermode='x unified',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(gridcolor='lightgrey'),
    xaxis=dict(showgrid=False)
)
st.plotly_chart(fig_desocup, use_container_width=True)

st.divider()

st.header("2. Nível de Emprego")
st.markdown("""
O nível de ocupação evidencia a grande disparidade de gênero: a ocupação dos homens orbita **68%**, enquanto a das mulheres permanece na casa dos **44%**.
""")

fig_emprego = go.Figure()

fig_emprego.add_vrect(x0="2020-03-01", x1="2021-06-01", fillcolor="red", opacity=0.1, line_width=0, annotation_text="Queda Pandemia", annotation_position="bottom right")

fig_emprego.add_trace(go.Scatter(
    x=pd.concat([df_emprego['periodo'], df_emprego['periodo'][::-1]]),
    y=pd.concat([df_emprego['homens'], df_emprego['mulheres'][::-1]]),
    fill='toself', fillcolor='rgba(231, 111, 81, 0.1)', line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip", showlegend=False, name='Gap de Gênero'
))

fig_emprego.add_trace(go.Scatter(x=df_emprego['periodo'], y=df_emprego['total'], mode='lines', name='Total', line=dict(color=COLOR_TOTAL, dash='dot')))
fig_emprego.add_trace(go.Scatter(x=df_emprego['periodo'], y=df_emprego['homens'], mode='lines', name='Homens', line=dict(color=COLOR_HOMENS, width=2)))
fig_emprego.add_trace(go.Scatter(x=df_emprego['periodo'], y=df_emprego['mulheres'], mode='lines', name='Mulheres', line=dict(color=COLOR_MULHERES, width=3)))

fig_emprego.update_layout(
    title='Nível de Emprego por Gênero (Atenção ao Gap)',
    yaxis_title='Nível (%)',
    yaxis_range=[30, 80],
    hovermode='x unified',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(gridcolor='lightgrey'),
    xaxis=dict(showgrid=False)
)
st.plotly_chart(fig_emprego, use_container_width=True)

st.divider()

st.header("3. Taxa de Informalidade")
st.markdown("""
A informalidade flutua em níveis elevados (~48%). Ao contrário dos outros indicadores, a informalidade afeta ligeiramente mais os homens.
""")

fig_infor = go.Figure()

fig_infor.add_trace(go.Scatter(x=df_infor['periodo'], y=df_infor['total'], mode='lines', name='Total', line=dict(color=COLOR_TOTAL, dash='dot')))
fig_infor.add_trace(go.Scatter(x=df_infor['periodo'], y=df_infor['homens'], mode='lines', name='Homens', line=dict(color=COLOR_HOMENS, width=3)))
fig_infor.add_trace(go.Scatter(x=df_infor['periodo'], y=df_infor['mulheres'], mode='lines', name='Mulheres', line=dict(color=COLOR_MULHERES, width=2)))

fig_infor.update_layout(
    title='Evolução da Taxa de Informalidade (A partir de 2015)',
    yaxis_title='Taxa (%)',
    hovermode='x unified',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(gridcolor='lightgrey'),
    xaxis=dict(showgrid=False)
)
st.plotly_chart(fig_infor, use_container_width=True)

st.divider()
st.success("""
**Conclusão**  
Apesar da recente recuperação, a desigualdade entre homens e mulheres demonstra um desafio estrutural persistente no mercado de trabalho brasileiro.
""")
