from flask_cors import CORS, cross_origin
from flask import Flask, request, session, jsonify
from flask_session import Session
import pandas as pd
import pickle
from dotenv import load_dotenv
from db import users, permap, feedback
import os
import bcrypt
from constants import options, persons, questions
import json
import numpy as np
import copy
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import (
    calinski_harabasz_score,
    silhouette_score,
    davies_bouldin_score,
)
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from random import randint
import google.generativeai as genai

genai.configure(api_key="AIzaSyABKgZYtF8FUWPyT5QRdXNBeiOlSKluR6k")

model = genai.GenerativeModel("gemini-pro")

# from tensorflow.keras.models import load_model
load_dotenv()

FRONTEND_URL = os.getenv("FRONTEND_URL")

app = Flask(__name__)

# Check Configuration section for more details
SESSION_PERMANENT = True
SESSION_TYPE = "filesystem"
SECRET_KEY = "somesecretkey"
SESSION_USE_SIGNER = True
app.secret_key = "thisistotest"
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True
app.config["SESSION_FILE_DIR"] = "./flask_session_cache"
app.config.from_object(__name__)
Session(app)

CORS(
    app, resources={r"/*": {"origins": "http://localhost:4200"}}
)  # Enable CORS for specific routes


def getOptions():
    return copy.deepcopy(options)


def getDummyUserObject():
    return {
        "UserInformation": {
            "username": "",
            "emailAddress": "",
            "firstName": "",
            "lastName": "",
            "company": "",
            "jobTitle": "",
            "university": "",
            "degree": "",
        },
        "ContactInformation": {
            "address": "",
            "city": "",
            "country": "",
            "postalCode": "",
        },
        "AboutMe": {
            "YearsCode": "",
            "YearsCodePro": "",
            "WorkExp": "",
            "CodingActivities": "",
            "DatabaseHaveWorkedWith": "",
            "DatabaseWantToWorkWith": "",
            "Employment": "",
            "LanguageHaveWorkedWith": "",
            "LanguageWantToWorkWith": "",
            "LearnCode": "",
            "LearnCodeCoursesCert": "",
            "LearnCodeOnline": "",
            "MiscTechHaveWorkedWith": "",
            "MiscTechWantToWorkWith": "",
            "NEWCollabToolsHaveWorkedWith": "",
            "NEWCollabToolsWantToWorkWith": "",
            "PlatformHaveWorkedWith": "",
            "PlatformWantToWorkWith": "",
            "ProfessionalTech": "",
            "ToolsTechHaveWorkedWith": "",
            "ToolsTechWantToWorkWith": "",
            "WebframeHaveWorkedWith": "",
            "WebframeWantToWorkWith": "",
            "ICorPM": "",
            "RemoteWork": "",
            "EdLevel": "",
            "DevType": "",
            "MainBranch": "",
            "Country": "",
            "Industry": "",
        },
        "Password": "",
    }


@app.route("/register", methods=["POST"])
@cross_origin(supports_credentials=True)
def register():
    data = request.json
    user = getDummyUserObject()
    userinfo = user["UserInformation"]
    userinfo["firstName"] = data["firstName"]
    userinfo["lastName"] = data["lastName"]
    userinfo["emailAddress"] = data["emailAddress"]
    userinfo["username"] = data["emailAddress"].split("@")[0]
    userinfo["company"] = data["company"]
    userinfo["jobTitle"] = data["jobTitle"]
    userinfo["university"] = data["university"]
    userinfo["degree"] = data["degree"]
    bytes = data["password"].encode("utf-8")
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(bytes, salt).decode("utf-8")
    user["Password"] = hashedPassword
    result = users.insert_one(user)
    session["user_id"] = result.inserted_id
    session.modified = True
    print(session["user_id"])
    response = jsonify({"success": True})
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


@app.route("/analyseFeedback", methods=["POST"])
@cross_origin(supports_credentials=True)
def analyze_feedback():
    user_id = session["user_id"]
    feedback_details = feedback.find_one({"mentee_id": user_id})
    response = jsonify({"success": True, "feedback": feedback_details})
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


@app.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login():
    data = request.json
    emailAddress = data["emailAddress"]
    password = data["password"]
    details = users.find_one({"UserInformation.emailAddress": emailAddress})
    if details == None:
        return {
            "success": False,
            "message": "Account does not exist with given email address",
        }
    hashedPassword = details["Password"].encode("utf-8")
    bytes = password.encode("utf-8")
    if bcrypt.checkpw(bytes, hashedPassword) == True:
        session["user_id"] = details["_id"]
        print(session["user_id"])
        session.modified = True
        response = jsonify({"success": True})
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Origin, X-Requested-With, Content-Type, Accept, x-auth",
        )
        return response
    else:
        return {"success": False, "message": "Incorrect login credentials!"}


@app.route("/isLoggedIn", methods=["GET"])
@cross_origin(supports_credentials=True)
def is_logged_in():
    user_id = session.get("user_id")
    success = False
    message = "Not Logged In"
    if user_id:
        success = True
    response = jsonify({"success": success, "message": message})
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


@app.route("/logout", methods=["POST"])
@cross_origin(supports_credentials=True)
def logout():
    del session["user_id"]
    response = jsonify(
        {"success": True, "message": "You are now logged out successfully."}
    )
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response

@app.route("/test", methods=["GET"])
@cross_origin(supports_credentials=True)
def test_api():
    return {"hello": "I am here"}


@app.route("/getUserProfile", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_user_profile():
    user_id = session.get("user_id")
    response = None
    if not user_id:
        response = jsonify({"success": False, "message": "Not Logged In"})
    else:
        result = users.find_one({"_id": user_id})
        user_details = {
            "UserInformation": result["UserInformation"],
            "ContactInformation": result["ContactInformation"],
            "AboutMe": result["AboutMe"],
        }
        response = jsonify({"success": True, "user_details": json.dumps(user_details)})
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


@app.route("/updateUserProfile", methods=["POST"])
@cross_origin(supports_credentials=True)
def update_user_profile():
    data = request.json
    print(data)
    user_id = session.get("user_id")
    user = users.find_one({"_id": user_id})
    data["Password"] = user["Password"]
    result = users.replace_one({"_id": user_id}, data, upsert=True)
    response = None
    if not result:
        response = jsonify({"success": False, "message": "Some error occurred!"})
    else:
        response = jsonify({"success": True})
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


@app.route("/findMyMentors", methods=["GET"])
@cross_origin(supports_credentials=True)
def find_my_mentors():
    user_id = session.get("user_id")
    user_details = users.find_one(filter={"_id": user_id})
    AboutMe = user_details["AboutMe"]
    data = getOptions()
    numerical_columns = ["YearsCode", "YearsCodePro", "WorkExp"]

    knn_model = pickle.load(open("model.pkl", "rb"))

    scaler = pickle.load(open("scaler.pkl", "rb"))
    train_data = pickle.load(open("train_data.pkl", "rb"))
    originalDF = pd.read_csv("survey_results_public.csv")

    genai_input = "Mentee's qualities are as shared in the questionnaire below :\n"
    for key in AboutMe:
        genai_input += questions[key] + "=> " + str(AboutMe[key]) + "\n"
        if key in numerical_columns:
            data[key] = int(AboutMe[key][1:])
        else:
            newKey = key + "_" + AboutMe[key]
            data[newKey] = 1
    df = pd.DataFrame(data, index=[0])
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

    random_professional = df.iloc[0]
    new_professional_array = np.array(random_professional).reshape(1, -1)
    # print(new_professional_array.shape)

    # Find nearest neighbors to the new professional
    distances, indices = knn_model.kneighbors(new_professional_array)

    # Get recommended mentors and their distances
    recommended_mentors = train_data.iloc[indices[0]]
    neighbor_distances = distances[0]
    # print(recommended_mentors.index)

    # Calculate confidence scores based on distances
    # You may need to normalize distances if required
    # For example, you can use the inverse of distances as confidence scores
    # Or you can use a normalization method such as min-max scaling or z-score normalization
    epsilon = 1e-10
    confidence_scores = 1 / (
        neighbor_distances + epsilon
    )  # Example of using inverse of distances as confidence scores

    # Normalize confidence scores to percentages
    confidence_scores_percent = (
        (confidence_scores - confidence_scores.min())
        / (confidence_scores.max() - confidence_scores.min())
        * 100
    )

    # # Print recommended mentors alongside their confidence scores
    # for i, (index, mentor) in enumerate(recommended_mentors.iterrows()):
    #     print(f"Mentor {i+1}:")
    #     print(
    #         f"Confidence Score: {confidence_scores_percent[i]:.2f}%"
    #     )  # Print confidence score as percentage
    #     print()

    mentors = []
    for i in range(3):
        mentor_index = recommended_mentors.index[i].item()
        exist_index = None
        try:
            exist_index = permap.find_one(
                {"mentor_index": mentor_index}, {"rand_index": 1, "_id": 0}
            )
            exist_index = exist_index["rand_index"]
        except Exception as err:
            print(err)
        if exist_index is not None:
            mentors.append(persons[exist_index])
        else:
            rand_index = randint(0, 14)
            while persons[rand_index] in mentors:
                rand_index = randint(0, 14)
            permap.insert_one(
                {"mentor_index": int(mentor_index), "rand_index": rand_index}
            )
            mentors.append(persons[rand_index])
        genai_input += "Mentor {} has below qualities as answered in this questionnaire below:\n".format(
            i + 1
        )
        for key in questions:
            genai_input += (
                questions[key] + "=> " + str(originalDF.iloc[mentor_index][key]) + "\n"
            )
    genai_input += "Explain elaborately how each of these 3 mentors will be a good match for the given mentee in 3 sections: 'Strengths', 'Potential limitations', 'Overall Recommendation'\n"
    genai_input += 'Provide me the output in JSON format with keys and values in double quotes as {"Mentor1": {"Strengths": [],  "Potential limitations": [], "Overall Recommendation": "value"}, "Mentor2": {"Strengths": [],  "Potential limitations": [], "Overall Recommendation": "value"}, "Mentor3": {"Strengths": [],  "Potential limitations": [], "Overall Recommendation": "value"}}\n'
    genai_input += "Use 'This mentor' while referring to 'Mentor 1', 'Mentor 2', and 'Mentor 3'. Use 'you' while referring to 'mentee' \n"
    response = model.generate_content(genai_input)
    while response.text.count('\\"') > 0:
        response = model.generate_content(genai_input)

    print(response.text)
    print(mentors)
    response = jsonify(
        {
            "success": True,
            "matches": json.dumps(response.text),
            "mentors": json.dumps(mentors),
        }
    )
    # response = jsonify({"success": True, "mentors": mentors})
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, x-auth",
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


if __name__ == "__main__":
    app.run(debug=True,port=5000)
