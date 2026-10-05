from flask import Flask
import pandas as pd
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="duplicate_detection"
)


@app.route("/")
def home():

    # Load CSV
    data = pd.read_csv("data/input_data.csv")

    # Clean text
    data["name"] = data["name"].str.strip().str.lower()
    data["email"] = data["email"].str.strip().str.lower()
    data["city"] = data["city"].str.strip().str.lower()

    # Detect duplicates
    duplicates = data[
        data.duplicated(
            subset=["name", "email", "phone", "city"],
            keep=False
        )
    ]

    # Remove duplicates
    final_data = data.drop_duplicates(
        subset=["name", "email", "phone", "city"],
        keep="first"
    )

    # Clear old MySQL records
    cursor = db.cursor()
    cursor.execute("DELETE FROM records")

    # Insert cleaned records into MySQL
    for _, row in final_data.iterrows():

        cursor.execute(
            """
            INSERT INTO records
            (id, name, email, phone, city)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                int(row["id"]),
                row["name"],
                row["email"],
                str(row["phone"]),
                row["city"]
            )
        )

    db.commit()
    cursor.close()

    # Display result
    html = """
    <h1>Duplicate Data Detection System</h1>

    <h2>Project Summary</h2>
    """

    html += f"<p>Total Records: {len(data)}</p>"
    html += f"<p>Duplicate Records: {len(duplicates)}</p>"
    html += f"<p>Final Cleaned Records: {len(final_data)}</p>"
    html += f"<p>Records Removed: {len(data) - len(final_data)}</p>"

    html += "<h2>Cleaned Data</h2>"

    html += final_data.to_html(index=False)

    return html


if __name__ == "__main__":
    app.run(debug=True)