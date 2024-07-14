from flask import Flask, jsonify, Response, make_response, request
import requests
from bs4 import BeautifulSoup
import re
import html
import json
import re

app = Flask(__name__)

@app.route("/getCADetails", methods=["POST"])
def getCADetails():
    try:
        membershipNumber = request.json.get("membershipNumber")
        session = requests.Session()

        initialPostData = {
            "t1": membershipNumber
        }

        response = session.post(
            "http://112.133.194.254/lom.asp", data=initialPostData
        )

        htmlString = response.text
        cleaned_html_string = htmlString.replace('\n', '').replace('\r', '').replace('\t', '').replace('\\', '')
        cleaned_html_string = html.unescape(cleaned_html_string)

        soup = BeautifulSoup(cleaned_html_string, 'html.parser')
        tables = soup.find_all('table')

        table = tables[3]
        trows = table.find_all('tr')
        if(trows==0):
            return jsonify({"status": "Chattered Accountant Not Found"})

        name = trows[1].find('b').get_text().strip().replace("          ", " ")
        gender = trows[2].find('b').get_text().strip()
        qualification = trows[3].find('b').get_text().strip()

        indianAddress = trows[4].find_all('b')[0].get_text().strip()
        foreignAddress = trows[4].find_all('b')[1].get_text().strip()
        indianAddress += " " + trows[5].find_all('b')[0].get_text().strip()
        foreignAddress += " " + trows[5].find_all('b')[1].get_text().strip()
        indianAddress += " " + trows[6].find_all('b')[0].get_text().strip()
        foreignAddress += " " + trows[6].find_all('b')[1].get_text().strip()
        indianAddress += " " + trows[7].find_all('b')[0].get_text().strip()
        foreignAddress += " " + trows[7].find_all('b')[1].get_text().strip()
        indianAddress += " " + trows[8].find_all('b')[0].get_text().strip()
        foreignAddress += " " + trows[8].find_all('b')[1].get_text().strip()
        indianAddress += " " + trows[9].find_all('b')[0].get_text().strip()
        foreignAddress += " " + trows[9].find_all('b')[1].get_text().strip()
        # indianAddress += " " + trows[10].find_all('b')[0].get_text()
        foreignAddress += " " + trows[10].find_all('b')[0].get_text().strip()

        copStatus = trows[11].find('b').get_text().strip()
        associateYear = trows[12].find('b').get_text().strip()
        fellowYear = trows[13].find_all('b')[0].get_text().strip()
        regionInIndia = trows[13].find_all('b')[1].get_text().strip()

        jsonResponse = {
            "membershipNumber":membershipNumber,
            "name": name,
            "gender": gender,
            "qualification": qualification,
            "indianAddress": indianAddress,
            "regionInIndia": regionInIndia,
            "foreignAddress": foreignAddress,
            "COPStatus": copStatus,
            "associateYear": associateYear,
            "fellowYear": fellowYear
        }
        # print(response.text)
        return jsonify(jsonResponse)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching Chatterred Accountant Details"})


if __name__ == "__main__":
    app.run()