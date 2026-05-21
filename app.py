from flask import Flask, render_template_string, request

app = Flask(__name__)

students = []

HTML_PAGE = """

<!DOCTYPE html>
<html>

<head>
    <title>Student Management System</title>

    <style>

        body{
            font-family: Arial;
            background-color: #f4f4f4;
            padding: 40px;
        }

        h1{
            color: #333;
        }

        form{
            background: white;
            padding: 20px;
            border-radius: 10px;
            width: 400px;
        }

        input{
            width: 95%;
            padding: 10px;
            margin-top: 10px;
        }

        button{
            padding: 10px;
            margin-top: 15px;
            width: 100%;
            background: black;
            color: white;
            border: none;
            cursor: pointer;
        }

        table{
            margin-top: 30px;
            width: 100%;
            border-collapse: collapse;
            background: white;
        }

        table, th, td{
            border: 1px solid black;
        }

        th, td{
            padding: 10px;
            text-align: center;
        }

    </style>

</head>

<body>

    <h1>Student Management System</h1>

    <form method="POST">

        <input type="text" name="name" placeholder="Enter Student Name" required>

        <input type="number" name="rollno" placeholder="Enter Roll Number" required>

        <input type="number" name="english" placeholder="English Marks" required>

        <input type="number" name="maths" placeholder="Maths Marks" required>

        <input type="number" name="physics" placeholder="Physics Marks" required>

        <input type="number" name="chemistry" placeholder="Chemistry Marks" required>

        <input type="number" name="cs" placeholder="CS Marks" required>

        <button type="submit">Add Student</button>

    </form>

    <table>

        <tr>
            <th>Roll No</th>
            <th>Name</th>
            <th>English</th>
            <th>Maths</th>
            <th>Physics</th>
            <th>Chemistry</th>
            <th>CS</th>
        </tr>

        {% for student in students %}

        <tr>
            <td>{{ student.rollno }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.english }}</td>
            <td>{{ student.maths }}</td>
            <td>{{ student.physics }}</td>
            <td>{{ student.chemistry }}</td>
            <td>{{ student.cs }}</td>
        </tr>

        {% endfor %}

    </table>

</body>
</html>

"""

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        student = {

            "rollno": request.form["rollno"],
            "name": request.form["name"],
            "english": request.form["english"],
            "maths": request.form["maths"],
            "physics": request.form["physics"],
            "chemistry": request.form["chemistry"],
            "cs": request.form["cs"]

        }

        students.append(student)

    return render_template_string(HTML_PAGE, students=students)

if __name__ == "__main__":
    app.run(debug=True)