# paper-analysis-grobid
This project extracts and analyzes information from **open-access scientific articles** using [Grobid](https://github.com/kermitt2/grobid).  
It generates **keyword clouds**, **visualizations**, and **extracts links** from the articles.

## 🚀 Features
✔ Extracts **title, abstract, figures count, and links** from PDFs.  
✔ Generates a **word cloud** from article abstracts.  
✔ Creates a **bar chart** showing the number of figures per article.  
✔ Uses **Grobid (Docker-based)** for processing PDFs.

## 📂 Folder Structure
📂 paper-analysis-grobid ┣ 📂 data/ # Folder for input PDFs ┣ 📂 results/ # Folder for extracted data & visualizations ┣ 📂 scripts/ # Python scripts for processing & visualization ┣ 📜 
README.md # Project documentation ┣ 📜 rationale.md # Explanation of validation process ┣ 📜 requirements.txt # Dependencies ┣ 📜 Dockerfile # Docker setup (if needed)

## 🛠 Installation
### **1️⃣ Install Dependencies**
Run:
```bash
pip3 install -r requirements.txt

2️⃣ Start Grobid (Docker)
Ensure Docker is running and execute:
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.6.2

3️⃣ Process PDFs
Place your research PDFs in data/ and run:
python3 scripts/extract_info.py

4️⃣ Generate Visualizations
Run:
python3 scripts/visualize_results.py

📊 Outputs

✔ results/resultados.csv → Extracted data from PDFs.
✔ results/wordcloud.png → Word cloud from abstracts.
✔ results/figures_per_article.png → Bar chart of figures per article.

🤖 Authors

Rodrigo Allende Rial
Based on the course "Open Science and AI in Research Software Engineering"
