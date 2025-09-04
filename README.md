
# 📊 BigQuery to PDF Report Generator

This project connects to **Google BigQuery**, runs SQL queries, and automatically generates a **PDF report** with tabular data using **Pandas + ReportLab**.

---

## 📂 Project Structure

```
.
├── bigquery_to_pdf.py                     # Main script
├── output.pdf                             # Generated PDF table
├── service_account.json                   # Google Cloud service account key (not uploaded!)
├── requirements.txt                       # Dependencies
└── README.md                              # Documentation
```

---

## ⚙️ Features

* 🔑 Authenticate using **Google Service Account**
* 📝 Run any **BigQuery SQL query**
* 📑 Export query results into a clean **PDF Table**
* 🎨 Styled table (header background, centered text, alternating colors)
* 🔄 Automatically opens the generated PDF

---

## 📦 Requirements

Install dependencies before running:

```bash
pip install google-cloud-bigquery google-auth reportlab pandas
```

---

## ▶️ How to Run

1. Place your **service account key JSON file** in the project folder.
2. Update the script with your key file path:

   ```python
   credentials = service_account.Credentials.from_service_account_file(
       "your-key.json"
   )
   ```
3. Add your BigQuery SQL inside the script:

   ```python
   query = ("""
       SELECT *
       FROM `bigquery-public-data.samples.natality`
       LIMIT 10
   """)
   ```
4. Run the script:

   ```bash
   python bigquery_to_pdf.py
   ```
5. Output:

   * A PDF file named **output.pdf** with query results.
   * Opens automatically in your default PDF viewer.

---

## 📝 Example Output in PDF

```
+---------+-----------+---------+
| Column1 | Column2   | Column3 |
+---------+-----------+---------+
|   ...   |   ...     |   ...   |
```

---

## 🔒 Security Note

⚠️ **Never commit your service account JSON to GitHub.**
Add the following to `.gitignore`:

```
*.json
*.pdf
```

---

## 👤 Author

**A.G. Hasan Zarook**
📍 University of Engineering and Technology, Lahore

