import os
import sys
from certificate_generator import add_text_to_image, convert_jpg_to_pdf, send_email
from excel import fetch_data_from_xlsx

def main():
    # Ensure the temp directory exists
    if not os.path.exists('./temp'):
        os.makedirs('./temp')

    file_path = "certificate_issue.xlsx"  # Replace with the path to your XLSX file
    data = fetch_data_from_xlsx(file_path)
    data1 =[['',1,'pratham p shetty','prathampshetty99sai@gmail.com','SENTIMENTAL REVIEW ANALYSIS ABOUT THE RECENT JAPAN EARTHQUAKE']]
    for i in data:
        # Example of email validation, adjust as needed
        if not i[3] or '@' not in i[3]:
            print(f"Invalid email address: {i[3]}")
            continue

        # Paths for the image and PDF files
        input_image_path = os.path.join('certificates', 'certificate.jpg')
        temp_image_path = './temp/certificate.jpg'
        temp_pdf_path = "./temp/certificate.pdf"

        add_text_to_image(input_image_path, [i[2], i[4]], temp_image_path)
        
        if not os.path.exists(temp_image_path):
            print(f"File not found: {temp_image_path}")
            continue
        
        convert_jpg_to_pdf(temp_image_path, temp_pdf_path)
        
        name = i[2]
        email = i[3]
        print(email)
        subject = "🎉 Congratulations! Your Participation Certificate is Ready 🎓"

        body = f"""<!DOCTYPE html>
<html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Conference Participation</title>
  <style type="text/css">
    body {{
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: white; /* Set background color to white */
      color: #161616;
    }}
    .container {{
      width: 100%;
      max-width: 600px; /* Adjusted max-width for the container */
      margin: 0 auto;
      padding: 20px; /* Added padding around the container */
    }}
    .card {{
      background-color: #1e1e1e;
      border-radius: 0px;
      padding: 20px;
      margin-bottom: 0px; /* Added margin between cards */
    }}
    .image-card {{
      max-width: 100%; /* Image card takes full width of container */
      border-radius: 12px;
      margin-bottom: 20px; /* Added margin below image */
    }}
    .image-card img {{
      width: 100%;
      border-radius: 12px;
    }}
    .text-content {{
      flex: 1;
    }}
    .text-content h1 {{
      text-align: center;
      color: #FFFFFF;
      font-size: 2em;
      margin-bottom: 20px;
    }}
    .text-content p {{
      max-width: 100%;
      line-height: 1.5;
      font-size: 1.2em;
      color: #FFFFFF;
      text-align: left;
    }}
    .text-content p span {{
      display: block;
      text-align: left;
      margin-top: 20px;
    }}
     .card:last-child {{
      margin-bottom: 0;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- First Card -->
    <div class="card ax-center text-white mb-10">
      <div class="image-card">
        <img src="https://college4u.in/wp-content/uploads/2020/05/srinn.jpg" alt="Event Image">
      </div>
    </div>
    
    <!-- Second Card -->
    <div class="card ax-center text-white mb-10">
      <div class="text-content">
        <h1>Conference Participation</h1>
        <p>
          Dear {name},<br><br>
          We are delighted to inform you that your certificate for presenting a paper at the recent conference is now available! 
          <br><br>Please find the attached PDF certificate for your records.<br><br>
          Thank you for your participation and valuable contributions. We hope you had a wonderful experience and look forward to seeing you at future events!
        </p>
        <p>
          Best regards,<br>ICRICS Team
        </p>
      </div>
    </div>
  </div>
</body>
</html>

"""

        try:
            send_email('@gmail.com', "password", email, subject, body, temp_pdf_path)
        except Exception as e:
            print(f"Failed to send email to {email} : {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
