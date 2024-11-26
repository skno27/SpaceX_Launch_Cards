from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)  # init flask app?


@app.route("/")
def index():
    return render_template("index.html", launches=launches)


@app.template_filter("date_only")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.date()


# load data using SpaceX API
def fetch_space_launches():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    # if successful ...
    if response.status_code == 200:
        launches = response.json()
        launches.sort(key=lambda x: x["date_utc"], reverse=True)
        return launches
    else:
        return []


def categorize_launches(launches):
    # filter launches such that each launch has the key  success and not the key upcoming...
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {"successful": successful, "failed": failed, "upcoming": upcoming}


launches = categorize_launches(fetch_space_launches())

# run only if we run THIS file..
if __name__ == "__main__":
    app.run(debug=True)  # update whenever we save , then refresh page
