# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 22:24:31 2025

@author: dbrav
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 

#%%

path_result = r"D:\2026\ISBI2026\EndoYao_Benchmark-main\1_dataset_guide\questions\QA original\results"

results_path = [
        ["Level1","Gemini-2.5-flash","NoMark","Results_Image.xlsx"],    
        ["Level1","GPT4o","NoMark","Results_Image.xlsx"],
        ["Level1","llama","NoMark","Results_Image.xlsx"],
        ["Level1","JanusPro","NoMark","Results_Image.xlsx"],

        ["Level2","Gemini-2.5-flash","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["Level2","Gemini-2.5-flash","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["Level2","Gemini-2.5-flash","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["Level2","GPT4o","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["Level2","GPT4o","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["Level2","GPT4o","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["Level2","JanusPro","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["Level2","JanusPro","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["Level2","JanusPro","Dot","Results_qa_dots_all_images_add_Image.xlsx"],
        ["Level2","llama","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["Level2","llama","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["Level2","llama","Dot","Results_qa_dots_all_images_add_Image.xlsx"],
        
        ["Level3","Gemini-2.5-flash","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["Level3","Gemini-2.5-flash","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["Level3","Gemini-2.5-flash","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["Level3","GPT4o","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["Level3","GPT4o","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["Level3","GPT4o","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["Level3","JanusPro","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["Level3","JanusPro","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["Level3","JanusPro","Dot","Results_qa_dots_all_images_add_Image.xlsx"],
        ["Level3","llama","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["Level3","llama","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["Level3","llama","Dot","Results_qa_dots_all_images_add_Image.xlsx"],
         
        ["AS","Gemini-2.5-flash","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["AS","Gemini-2.5-flash","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["AS","Gemini-2.5-flash","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["AS","GPT4o","Letter","Results_qa_letters_all_images_Image.xlsx"],
        ["AS","GPT4o","Number","Results_qa_numbers_all_images_Image.xlsx"],
        ["AS","GPT4o","Dot","Results_qa_dots_all_images_Image.xlsx"],
        ["AS","JanusPro","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["AS","JanusPro","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["AS","JanusPro","Dot","Results_qa_dots_all_images_add_Image.xlsx"],
        ["AS","llama","Letter","Results_qa_letters_all_images_add_Image.xlsx"],
        ["AS","llama","Number","Results_qa_numbers_all_images_add_Image.xlsx"],
        ["AS","llama","Dot","Results_qa_dots_all_images_add_Image.xlsx"]

         ]

list_dataframe = []
for question, name_model, type_expe, filename in results_path: 
    path_file = os.path.join(path_result, question, name_model, filename) 
    if os.path.exists(path_file):
        df = pd.read_excel(path_file)
        df["question"] = question
        df["name_model"] = name_model
        df["type_expe"] = type_expe
        
        list_dataframe.append(df)
    else:
        print("Do not exists {} - {} - {}".format(question, name_model, type_expe) ) 
        print(path_file)
        
df_result = pd.concat(list_dataframe)
df_result[['Accuracy_Mean','question', 'name_model', 'type_expe']] 

df_result.to_excel("general_results.xlsx") 


#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ==============================
# CONFIGURACIÓN DE LOS DATOS
# ==============================

label_map = {
    "Level1": "Level 1",
    "Level2": "Level 2",
    "Level3": "Level 3",
    "AS": "Ablation Study"
}
order_x = ["Level 1", "Level 2", "Level 3", "Ablation Study"]
#df_result["question"] = df_result["question"].str.strip().str.upper()
#df_result["question"] = pd.Categorical(df_result["question"], categories=order_x, ordered=True)
df_result["question"] = df_result["question"].map(label_map)
#df_result["question"] = pd.Categorical(df_result["question"], categories=order_x, ordered=True)
# Normaliza accuracy (0–100 → 0–1)
df_result["Accuracy_Mean"] = df_result["Accuracy_Mean"] 

# Posiciones base
pos_base = {lab: i for i, lab in enumerate(order_x)}

# Desplazamiento por modelo (orden GPT4o → JanusPro → LlaMa)
offsets = {"Gemini-2.5-flash": -0.4, 'GPT4o': -0.13, 'JanusPro': 0.13, 'llama': 0.4}

# Colores y marcadores
palette = {"Gemini-2.5-flash": '#f4b400',  # amarillo Google
           'GPT4o': '#4a90e2',
           'JanusPro': '#7dbb89',
           'llama': '#d48079'}
markers = {'NOMARK': '^', 'DOT': 'o', 'LETTER': 's', 'NUMBER': 'D'}

# ==============================
# GRÁFICO
# ==============================

plt.figure(figsize=(10,5))

# Graficar puntos
for (model, type_expe), g in df_result.groupby(["name_model","type_expe"]):
    x_positions = g["question"].map(lambda q: pos_base[q] + offsets.get(model, 0))
    plt.scatter(
        x_positions, g["Accuracy_Mean"],
        s=250,
        color=palette.get(model, 'gray'),
        marker=markers.get(str(type_expe).upper(), 'hline'),
        edgecolor='black', alpha=0.8
    )

# Fondo sombreado alterno
for i, lab in enumerate(order_x):
    if i % 2 == 0:
        plt.axvspan(i - 0.5, i + 0.5, color='gray', alpha=0.08)

# Ejes
plt.ylabel("Mean Accuracy (%)", fontsize=12)
plt.xlabel("")
plt.ylim(0, 110)

# ---- Etiquetas del eje X ----
x_ticks, x_labels = [], []
model_order = ["Gemini-2.5-flash", "GPT4o", "JanusPro", "llama"]
for rq in order_x:
    for model in model_order:
        x_ticks.append(pos_base[rq] + offsets[model])
        x_labels.append(model)

plt.xticks(x_ticks, x_labels, rotation=90, fontsize=10)

# Etiquetas de RQs centradas (debajo)
#for rq in order_x:
#    plt.text(pos_base[rq], 0.21, rq, ha='center', va='center', fontsize=11, fontweight='bold')
for rq in order_x:
    plt.text(
        pos_base[rq],
        2,
        rq,  # ya viene "Level 1", "Level 2", etc.
        ha='center',
        va='center',
        fontsize=11,
        fontweight='bold'
    )
# ==============================
# LEYENDAS INTERNAS (LADO A LADO)
# ==============================

# Leyenda de modelos (color)
legend_models = [
    Line2D([0], [0], marker='>', color='w', label='Gemini 2.5 Pro',
           markerfacecolor=palette['Gemini-2.5-flash'], markeredgecolor='black', markersize=10),
    Line2D([0], [0], marker='>', color='w', label='GPT-4o',
           markerfacecolor=palette['GPT4o'], markeredgecolor='black', markersize=10),
    Line2D([0], [0], marker='>', color='w', label='JanusPro',
           markerfacecolor=palette['JanusPro'], markeredgecolor='black', markersize=10),
    Line2D([0], [0], marker='>', color='w', label='llama',
           markerfacecolor=palette['llama'], markeredgecolor='black', markersize=10),
]

# Leyenda de tipo de marcador (forma)
legend_markers = [
    Line2D([0],[0], marker='^', color='w', label='NoMark', markerfacecolor='gray', markeredgecolor='black', markersize=10),
    Line2D([0],[0], marker='o', color='w', label='Dot',     markerfacecolor='gray', markeredgecolor='black', markersize=10),
    Line2D([0],[0], marker='s', color='w', label='Letter',  markerfacecolor='gray', markeredgecolor='black', markersize=10),
    Line2D([0],[0], marker='D', color='w', label='Number',  markerfacecolor='gray', markeredgecolor='black', markersize=10),
]


# Añadir segunda leyenda (Marker Type) a la derecha de la primera
plt.legend(
    handles=legend_markers,
    title="Marker Type",
    loc='upper left',
    bbox_to_anchor=(0.02, 0.97),  # 📍 misma altura, desplazada hacia la derecha
    frameon=True,
    fontsize=9,
    title_fontsize=10
)

# ==============================
# GUARDAR Y MOSTRAR
# ==============================
plt.tight_layout()
plt.savefig("mean_accuracy_plot.png", dpi=300, bbox_inches="tight")
plt.show()

