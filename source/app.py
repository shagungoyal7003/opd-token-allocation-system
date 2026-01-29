from flask import Flask, request, jsonify

print("MY OPD SERVER FILE LOADED")

app = Flask(__name__)

doctors = {}
slots = {}
waiting_list = []
token_counter = 1

PRIORITY = {
    "normal": 1,
    "followup": 2,
    "priority": 3,
    "emergency": 4
}

@app.route("/")
def home():
    return "OPD Token System Running"


@app.route("/add-doctor", methods=["POST"])
def add_doctor():
    data = request.json

    doctor_id = data["id"]
    name = data["name"]

    doctors[doctor_id] = {
        "name": name,
        "slots": []
    }

    return jsonify({"message": "Doctor Added Successfully"})


@app.route("/create-slot", methods=["POST"])
def create_slot():
    data = request.json

    slot_id = data["slot_id"]
    doctor_id = data["doctor_id"]

    slots[slot_id] = {
        "doctor_id": doctor_id,
        "time": data["time"],
        "capacity": data["capacity"],
        "tokens": []
    }

    doctors[doctor_id]["slots"].append(slot_id)

    return jsonify({"message": "Slot Created Successfully"})


@app.route("/book-token", methods=["POST"])
def book_token():
    global token_counter

    data = request.json

    patient = data["patient"]
    ptype = data["type"]
    slot_id = data["slot_id"]

    slot = slots[slot_id]

    token = {
        "id": token_counter,
        "name": patient,
        "type": ptype
    }

    token_counter += 1

    if len(slot["tokens"]) < slot["capacity"]:
        slot["tokens"].append(token)
        return jsonify({"message": "Token Confirmed", "token": token})

    lowest = min(slot["tokens"], key=lambda x: PRIORITY[x["type"]])

    if PRIORITY[ptype] > PRIORITY[lowest["type"]]:
        slot["tokens"].remove(lowest)
        waiting_list.append(lowest)
        slot["tokens"].append(token)

        return jsonify({"message": "High Priority Inserted", "token": token})

    waiting_list.append(token)

    return jsonify({"message": "Added To Waiting List"})


@app.route("/cancel-token/<int:tid>")
def cancel_token(tid):

    for slot in slots.values():
        for token in slot["tokens"]:
            if token["id"] == tid:

                slot["tokens"].remove(token)

                if waiting_list:
                    slot["tokens"].append(waiting_list.pop(0))

                return jsonify({"message": "Token Cancelled"})

    return jsonify({"message": "Token Not Found"})


@app.route("/emergency", methods=["POST"])
def emergency():
    data = request.json
    data["type"] = "emergency"
    return book_token()


if __name__ == "__main__":
    app.run(debug=False)
