#  https://www.immihelp.com/capitales-y-abreviaturas-de-los-estados-unidos/
#  curl -o us_state.js  https://leafletjs.com/examples/choropleth/us-states.js
# sed -i.bak 's/var statesData =//' us_state.js
# sed -i.bak2 's/;$//' us_state.js


import json
import pandas as pd
from collections import namedtuple


State = namedtuple("State", ["name", "state", "region"])

with open("./dataset.json", "rb") as f:
    dataset = json.loads(f.read())


states = []

for feature in dataset.get("features"):
    _property = feature["properties"]
    states.append(_property)

    # feature["properties"]["region"] = region
dt = pd.read_json(json.dumps(states))
dt.to_csv('small.csv')
