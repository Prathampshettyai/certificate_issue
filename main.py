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
    for i in data:
        if i[3] == 'email':
            continue

        # Paths for the image and PDF files
        input_image_path = os.path.join('certificates', 'certificate12.jpg')
        temp_image_path = './temp/certificate.jpg'
        temp_pdf_path = "./temp/certificate.pdf"

        add_text_to_image(input_image_path,  [i[2], i[4]], temp_image_path)
        
        if not os.path.exists(temp_image_path):
            print(f"File not found: {temp_image_path}")
            continue
        
        convert_jpg_to_pdf(temp_image_path, temp_pdf_path)
        
        name = i[2]
        email = i[3]
        print(email)
        subject = "🎉 Congratulations! Your Participation Certificate is Ready 🎓"
        body = f"""
        <html>
        <head>
            <style>
                table[name="blk_permission"], table[name="blk_footer"] {{display:none;}}
            </style>
        </head>
       <body>
    <div class="header">
        <img src="https://i0.wp.com/krazytech.com/wp-content/uploads/2017/07/Latest-Technical-Paper-Presentation-Topics.jpg?w=510&ssl=1" alt="Event Image" style="width:100%; max-width:750px; height:auto;">
        <h1>Conference Participation<br>_______</h1>
    </div>
    <div class="content">
        <p>Dear {name},</p>
        <p>We are delighted to inform you that your certificate for presenting a paper at the recent conference is now available! 🌟</p>
        <p>Please find the attached PDF certificate for your records.</p>
        <p>Thank you for your participation and valuable contributions. We hope you had a wonderful experience and look forward to seeing you at future events!</p>
        <p>Best regards,<br>Conference Team</p>
    </div>
</body>
</html>
        """

        try:
            send_email('example@gmail.com', "app password", email, subject, body, temp_pdf_path)
        except Exception as e:
            print(f"Failed to send email to {email} : {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
