#  https://www.immihelp.com/capitales-y-abreviaturas-de-los-estados-unidos/
#  curl -o us_state.js  https://leafletjs.com/examples/choropleth/us-states.js
# sed -i.bak 's/var statesData =//' us_state.js
# sed -i.bak2 's/;$//' us_state.js


import json
from pprint import pprint

regions = {
    "ME": "NORTHEAST",
    "VT": "NORTHEAST",
    "NY": "NORTHEAST",
    "NJ": "NORTHEAST",
    "PA": "NORTHEAST",
    "NH": "NORTHEAST",
    "MA": "NORTHEAST",
    "CT": "NORTHEAST",
    "RI": "NORTHEAST",
    "ND": "MIDWEST",
    "SD": "MIDWEST",
    "NE": "MIDWEST",
    "KS": "MIDWEST",
    "MN": "MIDWEST",
    "IA": "MIDWEST",
    "MO": "MIDWEST",
    "WI": "MIDWEST",
    "IL": "MIDWEST",
    "IN": "MIDWEST",
    "MI": "MIDWEST",
    "OH": "MIDWEST",
    "TX": "SOUTH",
    "OK": "SOUTH",
    "AR": "SOUTH",
    "LA": "SOUTH",
    "MS": "SOUTH",
    "AL": "SOUTH",
    "FL": "SOUTH",
    "GA": "SOUTH",
    "SC": "SOUTH",
    "NC": "SOUTH",
    "VA": "SOUTH",
    "DC": "SOUTH",
    "DE": "SOUTH",
    "MD": "SOUTH",
    "WV": "SOUTH",
    "KY": "SOUTH",
    "TN": "SOUTH",
    "WA": "WEST",
    "OR": "WEST",
    "CA": "WEST",
    "AK": "WEST",
    "ID": "WEST",
    "NV": "WEST",
    "AZ": "WEST",
    "UT": "WEST",
    "MT": "WEST",
    "WY": "WEST",
    "CO": "WEST",
    "HI": "WEST",
    "NM": "WEST",
}


with open("./us_state.json", "rb") as f:
    dataset = json.loads(f.read())

with open("./state_count.json", "rb") as f:
    count_state = json.loads(f.read())

with open("./state_mean.json", "rb") as f:
    mean_state = json.loads(f.read())


for feature in dataset.get("features"):
    state = feature["properties"]["state"]

    region = regions.get(state)
    if region is None:
        continue

    _count = count_state["price"][state]
    _price = mean_state["price"][state]
    _square_feet = mean_state["square_feet"][state]

    feature["properties"]["region"] = region
    feature["properties"]["count"] = _count
    
    feature["properties"]["price"] = round(_price)
    feature["properties"]["square_feet"] = round(_square_feet)

with open("./dataset.json", "w") as f:
    json.dump(dataset, f)
