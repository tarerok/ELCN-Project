import os
from flask import Flask, render_template, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

app= Flask(__name__)

GROUPS = {
    "volunteers": [
        "ethcarmo@iu.edu",
        "ethan.carmona@gmail.com",
        "tarerok@gmail.com"
    ],
    "coordinators": [
        "coord1@example.com",
        "coord2@example.com",
        "coord3@example.com",
    ],
    "speakers": [
        "speaker1@example.com",
        "speaker2@example.com",
        "speaker3@example.com"

    ]
}


@app.route("/")
def home():
    from_email = "tarerok@gmail.com"
    return render_template("index.html", from_email = from_email, groups=GROUPS)

@app.route("/send", methods=["POST"])
def send_email():
    sendType = request.form.get("send_type")
    singleEmail = request.form.get("email")
    groupName = request.form.get("group")
    subject = request.form.get("subject")
    messageText = request.form["message"]
    
    if not subject or not messageText:
        return render_template(
            "index.html",
            error="Subject and message are required.",
            email=singleEmail,
            subject=subject,
            message=messageText,
            from_email="tarerok@gmail.com",
            groups=GROUPS
        )
    recipients = []
    
    if sendType == "single":
        if not singleEmail:
            return render_template (
                "index.html",
                error="Please enter a recipient email.",
                email=singleEmail,
                subject=subject,
                message=messageText,
                from_email="tarerok@gmail.com",
                groups=GROUPS
            )
        recipients = [singleEmail]
        
    elif sendType == "group":
        if not groupName or groupName not in GROUPS:
            return render_template(
                "index.html",
                error="Please select a valid group",
                subject=subject,
                message=messageText,
                from_email="tarerok@gmail.com",
                groups=GROUPS
            )
        recipients = GROUPS[groupName]
        
    else:
        return render_template(
            "index.html",
            error="Invalid send option",
            subject=subject,
            message=messageText,
            from_email="tarerok@gmail.com",
            groups=GROUPS
        )
    
    
    
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

        for recipient in recipients:
            email_message = Mail(
                from_email="tarerok@gmail.com",
                to_emails=recipient,
                subject=subject,
                plain_text_content=messageText
            )
            sg.send(email_message)

        return render_template(
            "success.html",
            recipients=recipients,
            subject=subject,
            message=messageText
        )

    except Exception:
        return render_template(
            "index.html",
            error="We couldn't send the email right now. Please try again later.",
            email=singleEmail,
            subject=subject,
            message=messageText,
            from_email="tarerok@gmail.com",
            groups=GROUPS
        )

if __name__ == "__main__":
    app.run(debug=True)