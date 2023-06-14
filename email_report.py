#!/usr/bin/env python3
"""
Generate and send an email report with attached PDF
"""
import os
import datetime
import reports
import emails

dt = datetime.date.today().strftime("%B  %d, %Y")
date = "Processed Update on " + dt

summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
