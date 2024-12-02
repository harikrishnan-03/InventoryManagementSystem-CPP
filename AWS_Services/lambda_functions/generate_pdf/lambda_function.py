import pymysql
from fpdf import FPDF
import boto3
import os

# RDS Configuration
RDS_HOST = "x23297948-ims.c9206kckwag4.us-east-1.rds.amazonaws.com"
RDS_USER = "root"
RDS_PASSWORD = "kausthubham"
RDS_DB = "ims_db"

# S3 Configuration
S3_BUCKET_NAME = "imsharipdfbucket"

def fetch_data_from_rds(user_id):
    # Fetch data from the RDS table.
    connection = pymysql.connect(
        host=RDS_HOST,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB,
    )
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM StockDetails WHERE user_id = %s;"
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()
            return results
    finally:
        connection.close()

def generate_pdf(data):
    # Generate a PDF with table data.
    pdf = FPDF(orientation="L", unit="mm", format="A4")  
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.cell(200, 10, txt="Stock DetailsInventory Management System Stock Report", ln=True, align='C')

    # Add table header
    pdf.set_font("Arial", style='B', size=10)
    pdf.cell(17, 10, "Stock ID", border=1)
    pdf.cell(50, 10, "Stock Name", border=1)
    pdf.cell(17, 10, "Amount", border=1)
    pdf.cell(17, 10, "Quantity", border=1)
    pdf.cell(60, 10, "Supplier", border=1)
    pdf.cell(30, 10, "Supplier Number", border=1)
    pdf.ln()

    # Add table rows
    pdf.set_font("Arial", size=10)
    for row in data:
        pdf.cell(17, 10, str(row[0]), border=1)
        pdf.cell(50, 10, str(row[1]), border=1)
        pdf.cell(17, 10, str(row[2]), border=1)
        pdf.cell(17, 10, str(row[3]), border=1)
        pdf.cell(60, 10, str(row[5]), border=1)
        pdf.cell(30, 10, str(row[6]), border=1)

        pdf.ln()

    # Save the PDF to /tmp directory
    pdf_path = "/tmp/stock_list.pdf"
    pdf.output(pdf_path)
    return pdf_path

def upload_to_s3(file_path, bucket_name, object_name):
    # Upload the PDF to an S3 bucket and generate a pre-signed URL.
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name)

    # Generate a pre-signed URL for downloading the file
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=3600  # URL expiry in seconds (1 hour)
    )
    return presigned_url

def lambda_handler(event, context):
    try:
        # Extract the user_id from the event
        user_id = event['user_id']

        # Fetch data from RDS
        data = fetch_data_from_rds(user_id)

        # Generate PDF
        pdf_path = generate_pdf(data)

        # Upload PDF to S3 and get pre-signed URL
        presigned_url = upload_to_s3(pdf_path, S3_BUCKET_NAME, "stock_list.pdf")

        # Return the pre-signed URL
        return {
            "statusCode": 200,
            "body": json.dumps(presigned_url) 
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }