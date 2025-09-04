from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('E:\\BSc Computer Engineering\\semester5\\database\\taskproj-398609-2926bb2e71c9.json')


project_id = 'your id'

client = bigquery.Client(credentials= credentials,project=project_id)
query =("""
   
        
   
   """)
query_job = client.query(query)
results = query_job.result()
print(results)
print("finished")


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import pandas as pd

data = [list(result.values()) for result in results]
# Create a Pandas DataFrame from your query results
df = pd.DataFrame(data, columns=[results])


table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

# Create a PDF document
doc = SimpleDocTemplate("output.pdf", pagesize=letter)
# Define table styles (optional)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    
]))

# Build the PDF document
elements = [table]
doc.build(elements)

import webbrowser

webbrowser.open("output.pdf")



