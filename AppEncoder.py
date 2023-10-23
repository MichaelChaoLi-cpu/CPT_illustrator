
from glob import glob
from joblib import dump, Parallel, delayed
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import PyPDF2
import regex as re
import shutil
import spacy
from transformers import BertTokenizer

def readAnnualReportPdf(Time_Everytime_10_Reports, Downloaded_PDF_Folder):
    annual_report_list = glob(Downloaded_PDF_Folder + '*.pdf')
    combinaiton_of_reports = ''
    scaned_reports = []
    if (Time_Everytime_10_Reports*10) < len(annual_report_list):
        annual_report_list_this_time = annual_report_list[Time_Everytime_10_Reports*10:(Time_Everytime_10_Reports+1)*10]
    else:
        annual_report_list_this_time = annual_report_list[(Time_Everytime_10_Reports)*10:len(annual_report_list)]
    #print(annual_report_list_this_time)
    for annual_report in annual_report_list_this_time:
        # Open the PDF file in binary mode
        try:
            with open(annual_report, 'rb') as pdf_file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Get the number of pages in the PDF document
                num_pages = len(pdf_reader.pages)
                # Initialize a variable to store the combined text
                combined_text = ' XXXXX '
                # Loop through each page and extract the text
                for page_num in range(num_pages):
                    page_obj = pdf_reader.pages[page_num]
                    page_text = page_obj.extract_text()
                    combined_text += page_text
                # Print the combined text (optional)
                # print(len(combined_text))
                # Append the extracted text to the 'combinaiton_of_reports' and 'scaned_reports' lists (if needed)
                combinaiton_of_reports += combined_text
                scaned_reports.append(annual_report)
        except Exception as e:
            print(f"file name: {annual_report}\nAn error occurred: {e}")
    return combinaiton_of_reports, scaned_reports

def readSingleAnnualReportPdf(Address_Of_Pdf):
    annual_report = Address_Of_Pdf
    print(f'address is {annual_report}')
    combinaiton_of_reports = ''
    try:
        with open(annual_report, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Get the number of pages in the PDF document
            num_pages = pdf_reader.getNumPages()
            # Loop through each page and extract the text
            single_total_text = ' XXXXX '
            for page_num in range(num_pages):
                page_obj = pdf_reader.getPage(page_num)
                page_text = page_obj.extractText()
                single_total_text = single_total_text + page_text
            #print(len(single_total_text))
            combinaiton_of_reports = combinaiton_of_reports + single_total_text
    except Exception as e:
        print(f"file name: {annual_report}\nAn error occurred: {e}")
    return combinaiton_of_reports
    
def makeTextBeautiful(Documents):
    Documents = re.sub('(<.*?>)', '', Documents)
    output_string = Documents
    output_string = re.sub(r'[^a-zA-Z\s\d,.-]', '', output_string)
    # drop special character
    output_string = re.sub(r'[\xa0\u2002\u2009\u200a\u202f]', ' ', output_string)
    output_string = re.sub(r'[\t\n\x0b\x0c\r\u2003\u2004\u2006]', ' ', output_string)
    # drop digital
    output_string = re.sub(r'[\d]', ' ', output_string)
    # drop ,.-
    output_string = re.sub(r'[,.-]', ' ', output_string)
    # drop mutli blanks
    output_string = re.sub(r'\s+', ' ', output_string)
    # convert uppercase into lower case 
    output_string = re.sub(r'[A-Z]', lambda m: m.group(0).lower(), output_string)
    return output_string


def makeFileSimple(Documents):
    ### this function has potential dangager data is to large, 
    ### so we could convert part by part
    #convert Ns to N, Ves to v, etc.
    try:
        nlp = spacy.load('en_core_web_sm')
        nlp.max_length = 1000000000
        doc = nlp(Documents)
        simple_words = [token.lemma_ for token in doc]
        simple_text = ' '.join(simple_words)
    except:
        simple_text = ' '
        print("makeFileSimple Fail!")
    return simple_text

def judgeStopWords(word, stop_list):
    if word not in stop_list:
        return word
    else:
        return None

def Encoder_PDFReader(Downloaded_PDF_Folder, Fatal_List=[]):
    """
    Convert PDF to Str

    Parameters
    ----------
    Downloaded_PDF_Folder : str
        A full address ending by '/'.
    Fatal_List : list, optional
        During conversion, there may be some sections with fatal errors, to 
        save time, directly skip them.

    Returns
    -------
    Total_Reports : str
        A long str of all content from PDF. In this file, except . , and 
        number, other non-character symbol has been droped. Words have been
        convert to basic shape.


    """
    Total_Reports = ''
    Total_Times = len(glob(Downloaded_PDF_Folder + '*.pdf'))//10
    for Time_Index in list(range(Total_Times + 1)):
        if Time_Index in Fatal_List:
            pass
        else:
            print(f'Here we are:{Time_Index}')
            Content_Of_Reports, Scaned_Reports = readAnnualReportPdf(Time_Index, Downloaded_PDF_Folder)
            Beautiful_Reports = makeTextBeautiful(Content_Of_Reports)
            Simple_Reports = makeFileSimple(Beautiful_Reports)
            Total_Reports = Total_Reports + '' + Simple_Reports
        
    return Total_Reports



def Encoder_StopWordDropper(Total_Reports):
    """
    drop the stop words in the content

    Parameters
    ----------
    Total_Reports : str
        A long str of all content from PDF. In this file, except . , and 
        number, other non-character symbol has been droped. Words have been
        convert to basic shape.

    Returns
    -------
    Filtered_Text : str
        A long str of all content from PDF without stop words.

    """
    nltk.download('stopwords')
    nltk.download('punkt')
    # tokenize the string
    words = word_tokenize(Total_Reports)
    stop_list = stopwords.words('english')
    # remove stop words
    filtered_words = Parallel(n_jobs=-1)(delayed(judgeStopWords)(word, stop_list) for word in words) 
    filtered_words = list(filter(None, filtered_words))
    # join filtered words back to string
    Filtered_Text = ' '.join(filtered_words)
    return Filtered_Text

def Encoder_BertEncoder(Documents):
    """
    convert word to token ids

    Parameters
    ----------
    Documents : str
        A long str of all content from PDF without stop words.

    Returns
    -------
    tokens : list
        A list of id based on Bert Tokenizer.

    """
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(Documents)
    tokens = tokenizer.convert_tokens_to_ids(tokens)  
    return tokens

def Encoder_FullContentMaker(Downloaded_PDF_Folder, Fatal_List=[]):
    """
    Convert PDF to BERT word tokens

    Parameters
    ----------
    Downloaded_PDF_Folder : str
        A full address ending by '/'.
    Fatal_List : list, optional
        During conversion, there may be some sections with fatal errors, to 
        save time, directly skip them.

    Returns
    -------
    tokens : list
        A list of id based on Bert Tokenizer.


    """
    Total_Reports = Encoder_PDFReader(Downloaded_PDF_Folder, Fatal_List=[])
    Filtered_Text = Encoder_StopWordDropper(Total_Reports)
    Tokens = Encoder_BertEncoder(Filtered_Text)
    return Tokens

UPLOAD_LOCATION = 'RunPDF/'
Total_Reports = Encoder_FullContentMaker(UPLOAD_LOCATION)

DataX = []
for i in range(0, len(Total_Reports) - 60 - 1 , 1):
    seq_in = Total_Reports[i:i + 60]
    DataX.append(seq_in)
dump(DataX, 'TempPDF/total_txt.joblib')




