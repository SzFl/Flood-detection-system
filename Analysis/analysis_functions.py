import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def analysis_functions(model_data_path:str) -> pd.DataFrame:

    deepseek_r1_kaggle = pd.read_csv(model_data_path+'/kaggle_messages.csv',sep=';')
    deepseek_r1_kaggle_resp = pd.read_csv(model_data_path+'/kaggle_messages_response.csv',sep=';')
    kaggle = pd.concat([deepseek_r1_kaggle, deepseek_r1_kaggle_resp], axis=1)
    kaggle.insert(0,'Source','kaggle')
    
    deepseek_r1_generated = pd.read_csv(model_data_path+'/test_messages.csv',sep=';')
    deepseek_r1_generated_resp = pd.read_csv(model_data_path+'/test_messages_response.csv',sep=';')
    generated = pd.concat([deepseek_r1_kaggle, deepseek_r1_kaggle_resp], axis=1)
    generated.insert(0,'Source','test')
    
    deepseek_results = pd.concat([kaggle, generated], axis=0)
    return deepseek_results

def generate_conf_matrix(data:pd.DataFrame):
    data = data.copy()

    data['is_about_flood'] = data['is_about_flood'].map({
        0: 'No Flood',
        1: 'Flood'
    })
    
    data['predictions'] = data['predictions'].map({
        0: 'No Flood',
        1: 'Flood'
    })

    cm_df = pd.crosstab(
        data['is_about_flood'],
        data['predictions'],
        rownames=['Actual'],
        colnames=['Predicted'],
        dropna=False
    )

    
    # Plot as heatmap
    labels = cm_df.index.tolist()
    matrix = cm_df.values
    
    fig, ax = plt.subplots()
    im = ax.imshow(matrix, aspect='equal', cmap='Blues')
    
    # Tick labels
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    
    # Axis labels
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    
    # Annotate cells
    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, matrix[i, j], ha='center', va='center')
    
    plt.tight_layout()
    plt.show()
















    