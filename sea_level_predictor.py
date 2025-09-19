import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Dados planilha", alpha=0.6)


    # Create first line of best fit
    inclinacao, intercepto, r_valor, p_valor, erro_padrao = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    todos_anos = pd.Series(range(1880, 2051))
    plt.plot(todos_anos, intercepto + inclinacao * todos_anos, 'r', label="Ajuste (1880-2050)")

    # Create second line of best fit
    df_grafico = df[df["Year"] >= 2000]
    inclinacao2, intercepto2, r_valor2, p_valor2, erro_padrao2 = linregress(df_grafico["Year"], df_grafico["CSIRO Adjusted Sea Level"])
    anos_recentes = pd.Series(range(2000, 2051))
    plt.plot(anos_recentes, intercepto2 + inclinacao2 * anos_recentes, 'g', label="Ajuste (2000-2050)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()