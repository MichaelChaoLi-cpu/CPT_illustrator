
from joblib import dump, load
import numpy as np
from transformers import AutoTokenizer


def HtmlMaker(Input_File, Save_File, tokens):
    y_pred = load(Input_File)
    y_pred = np.concatenate((y_pred, np.full(59, np.nan)))

    num_lags = 60
    lagged_array = np.full((len(y_pred), num_lags), np.nan)
    for i in range(num_lags):
        lagged_array[i:, i] = y_pred[:len(y_pred) - i]

    column_means = np.nanmean(lagged_array, axis=1)

    ackground_color = '#00FF00'

    # Create an HTML string
    html_content = "<html><head></head><body>"

    # Iterate through tokens and their colors
    for token, alpha in zip(tokens, column_means):
        rgba_color = f'rgba(0, 255, 0, {alpha})'
        token = token + ' '
        span_element = f'<span style="background-color: {rgba_color};">{token}</span>'
        html_content += span_element

    # Close the HTML body and HTML document
    html_content += "</body></html>"

    # Save the HTML content to a file
    html_file = Save_File
    with open(html_file, "w") as file:
        file.write(html_content)


DataX = load('TempPDF/total_txt.joblib')

DataX_raw = []
for item in DataX:
    DataX_raw.append(item[0])
    
DataX_raw = DataX_raw + DataX[-1][1:] 

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.convert_ids_to_tokens(DataX_raw)

HtmlMaker('TempPDF/i0.joblib', "Results/Community.html", tokens)
HtmlMaker('TempPDF/i1.joblib', "Results/Air_Pollution.html", tokens)
HtmlMaker('TempPDF/i2.joblib', "Results/Greenhouse_Gas.html", tokens)
HtmlMaker('TempPDF/i3.joblib', "Results/Water_Consumption.html", tokens)
HtmlMaker('TempPDF/i4.joblib', "Results/Mining_Consumption.html", tokens)
HtmlMaker('TempPDF/i5.joblib', "Results/Work_Environment.html", tokens)
HtmlMaker('TempPDF/i6.joblib', "Results/Safety_Health.html", tokens)
HtmlMaker('TempPDF/i7.joblib', "Results/Human_Right.html", tokens)
HtmlMaker('TempPDF/i8.joblib', "Results/Governance_Risk.html", tokens)
HtmlMaker('TempPDF/i9.joblib', "Results/Production_Cost.html", tokens)
HtmlMaker('TempPDF/i10.joblib', "Results/Domestic_Job.html", tokens)
HtmlMaker('TempPDF/i11.joblib', "Results/Economic_Ripple.html", tokens)
HtmlMaker('TempPDF/i12.joblib', "Results/Domestic_Reflux.html", tokens)












