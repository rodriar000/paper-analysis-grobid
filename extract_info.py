

import os
import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Ruta al servidor de Grobid
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Ruta de la carpeta con los PDFs
PDF_FOLDER = "data/"

# Carpeta donde guardar los resultados
OUTPUT_FOLDER = "results/"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Función para procesar un PDF con Grobid
def process_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        files = {'input': pdf_file}
        response = requests.post(GROBID_URL, files=files)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"❌ Error al procesar {pdf_path}: {response.status_code}")
        return None

# Función para extraer información del XML
def extract_info(xml_content):
    root = ET.fromstring(xml_content)

    # Extraer título
    title = root.find('.//{http://www.tei-c.org/ns/1.0}title')
    title_text = title.text if title is not None else "No encontrado"

    # Extraer resumen (abstract)
    abstract = root.find('.//{http://www.tei-c.org/ns/1.0}abstract')
    if abstract is not None:
        abstract_text = " ".join(p.text for p in abstract.findall('.//{http://www.tei-c.org/ns/1.0}p') if p.text)
    else:
        abstract_text = "No encontrado"

    # Contar figuras en el documento
    figures = root.findall('.//{http://www.tei-c.org/ns/1.0}figure')
    num_figures = len(figures)

    # Extraer enlaces (URLs dentro del documento)
    links = [ref.text for ref in root.findall('.//{http://www.tei-c.org/ns/1.0}ref') if ref.text and "http" in ref.text]

    return title_text, abstract_text, num_figures, links

# Procesar todos los PDFs en la carpeta
results = []
for pdf_file in os.listdir(PDF_FOLDER):
    pdf_path = os.path.join(PDF_FOLDER, pdf_file)
    
    print(f"📄 Procesando: {pdf_file}...")
    xml_data = process_pdf(pdf_path)
    
    if xml_data:
        title, abstract, num_figures, links = extract_info(xml_data)
        results.append({
            "PDF": pdf_file,
            "Título": title,
            "Resumen": abstract,
            "Número de Figuras": num_figures,
            "Enlaces": ", ".join(links)
        })

# Guardar los resultados en un archivo CSV
df = pd.DataFrame(results)
df.to_csv(os.path.join(OUTPUT_FOLDER, "resultados.csv"), index=False)

print("✅ Análisis completado. Resultados guardados en 'results/resultados.csv'")

