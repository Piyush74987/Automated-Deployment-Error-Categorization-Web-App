# 🚀 Automated Deployment Error Categorization Web App

A Flask + NLP (NLTK) based web app to categorize failed deployment logs with detailed analysis and preventive measures.

## 🧠 Project Overview

This application intelligently analyzes and categorizes deployment failure logs using Natural Language Processing (NLP). Built with **Flask** and **NLTK**, it automates the identification of error types and provides actionable insights—improving troubleshooting speed and reducing deployment failures.

---

## 📸 UI Preview

<table border="1" width="500" cellspacing="0" cellpadding="8">
  <tr>
    <th>Input Form</th>
    <th>Prediction Result</th>
  </tr>
  <tr>
    <td>
      <img 
         width="1920" height="1080" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/26ea7c57-cc3f-4990-8b16-67e076cb297d"
        alt="Input Form"
        width="240"
      />
    </td>
    <td>
      <img 
        width="1920" height="1080" alt="Screenshot (42)" src="https://github.com/user-attachments/assets/2add93ac-7837-4562-bec7-9050c2534195"
        alt="Prediction Result"
        width="240"
      />
    </td>
  </tr>
</table>




## ✨ Features

- ✅ **Automated Error Categorization**  
  Classifies error logs into categories like "SQL Error", "Jenkins Plugin Issue", etc.

- ✅ **NLP-Powered Matching**  
  Uses tokenization, lemmatization, and fuzzy scoring for accurate classification.

- ✅ **Detailed Failure Reports**  
  Displays root cause, resolution steps, and preventive measures.

- ✅ **Real-Time Web Interface**  
  Flask-based responsive UI for ease of use.

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?logo=nltk)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![VS Code](https://img.shields.io/badge/IDE-VSCode-007ACC?logo=visualstudiocode)

---

## 📂 Project Structure

nlp_error_classifier/<br>
├── app.py # Flask main server<br>
├── error_anaylsis.py # NLP logic using NLTK<br>
├── templates/<br>
│ └── index.html # HTML frontend<br>
├── static/<br>
│ └── style.css # CSS for frontend<br>
├── requirements.txt<br>
└── README.md<br>
