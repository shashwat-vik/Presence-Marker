from flask import Flask, render_template, request
import queue, json

q = queue.Queue()

app = Flask(__name__)

status = {
        "A":(101, "INVALID NUMBER",),
        "B":(102, "ADDED"),
        "C":(103, "ALREADY EXISTS"),
        "D":(104, "DELETED"),
        "E":(105, "QUEUE EMPTY"),
        "F":(106, "POLLED")
        }

def form_response(status_idx, data):
    global status
    out = {"status":status[status_idx][0], "data":data}
    return json.dumps(out)

@app.route("/")
def homepage():
    return render_template("attendance_sheet.html")

@app.route("/add/<number>")
def add(number):
    global q
    try:
        number = int(number)
    except ValueError:
        return form_response("A", None)     # INVALID NUMBER
    if number not in q.queue:
        q.put(number)
        return form_response("B", None)     # ADDED
    return form_response("C", None)         # ALREDY EXISTS

@app.route("/display")
def display():
    global q
    print (list(q.queue))
    return ""

@app.route("/poll")
def poll():
    global q
    if not q.empty():
        return form_response("F", list(q.queue))     # POLLED
    return form_response("E", None)         # QUEUE EMPTY

@app.route("/delete", methods=['POST'])
def delete():
    global q
    data = request.json
    #print (repr(data))
    #data = json.loads(str(data))
    #print (type(data.get('data')))
    print (data)
    if not q.empty():
        for i in data.get('data'):
            x = q.get()
            if x != i:
                q.put(x)
        return form_response("D", None)     # DELETED
    return form_response("E", None)         # QUEUE EMPTY

if __name__ == '__main__':
    app.run(debug=True)
