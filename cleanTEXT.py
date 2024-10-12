import re

def clean_text(text):
    text = re.sub(r'\)\n', ')', text)
    text = re.sub(r'\)\r\s*', ')', text)
    text = re.sub(r'(\d)\.\r\s*', r'\1.', text)
    text = re.sub(r'<<', "'", text)
    text = re.sub(r'"', "'", text)
    text = re.sub(r'^\d+\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+ \n', '', text, flags=re.MULTILINE)
    
    return text

def process_document(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    cleaned_text = clean_text(text)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

if __name__ == "__main__":
    input_file = 'Dok_Trajtuara_Trankit\Tarification_infrastructure_ferroviaireAL.txt' 
    output_file = 'Dok_Trajtuara_Trankit\CLTarification_infrastructure_ferroviaireAL.txt' 
    
    process_document(input_file, output_file)
