import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_graph(csv_path, output_path, title, ylabel):
    df = pd.read_csv(csv_path)
    df['periodo'] = pd.to_datetime(df['periodo'])
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['periodo'], df['total'], label='Total', color='black', linewidth=2)
    plt.plot(df['periodo'], df['homens'], label='Homens', color='blue', linestyle='--')
    plt.plot(df['periodo'], df['mulheres'], label='Mulheres', color='red', linestyle='--')
    
    plt.title(title)
    plt.xlabel('Ano')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

# Plot Desocupação
plot_graph(
    'dados_tratados/des_trat.csv', 
    'desocupacao.png', 
    'Taxa de Desocupação por Gênero', 
    'Taxa (%)'
)

# Plot Emprego
plot_graph(
    'dados_tratados/df_emprego_clean.csv', 
    'emprego.png', 
    'Nível de Emprego por Gênero', 
    'Nível (%)'
)

# Plot Informalidade
plot_graph(
    'dados_tratados/df_informalidade_clean.csv', 
    'informalidade.png', 
    'Taxa de Informalidade por Gênero', 
    'Taxa (%)'
)

print("Gráficos gerados com sucesso!")
