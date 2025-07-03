from flask import Flask, render_template, request, jsonify
import piechart
# Create an instance of the Flask class
app = Flask(__name__)
def data():
    pass
# Define a route for the root URL ("/")
@app.route("/", methods=["GET", "POST"] )
def hello_world():
    if(request.method=="POST"):
        data = request.get_json()
        
    # Return a string to be displayed in the browser
    return render_template("index.html")
#The post request data is jsonified and a pie chart is returned
@app.route("/submit-tasks", methods=["GET", "POST"])
def submit_task():
    data =  request.get_json()
    file_name = piechart.pieplot(data)
    return jsonify({"message": "Tasks received successfully!",
                    "chart_url": f"/static/{file_name}"})
                   

# Run the application if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables the debugger and reloader