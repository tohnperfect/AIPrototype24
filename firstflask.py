from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/stat") 
def helloSTAT():
    return "Hello, STAT KKU!"

(__name__)

@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "Statistical Modeling of Climate Change Impacts",
        "Advanced Methods in Time Series Analysis",
        "Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "Bayesian Inference in Social Sciences",
        "Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    faculty, research_projects = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=faculty, research_projects=research_projects)



@app.route("/contact")
def contact_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
            }
            main {
                padding: 2rem;
                max-width: 600px;
                margin: auto;
                text-align: left;
                background: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h1 {
                color: #005ea6;
            }
            p {
                line-height: 1.6;
            }
            footer {
                text-align: center;
                margin-top: 2rem;
                font-size: 0.9rem;
                color: #666;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Contact Us</h1>
        </header>
        <main>
            <h2><a href="/statHTML">Admin</a> Contact Details</h2>
            <p><strong>Name:</strong> John Doe</p>
            <p><strong>Email:</strong> admin@example.com</p>
            <p><strong>Phone:</strong> +1-234-567-890</p>
            <p>If you have any questions or need assistance, please don’t hesitate to reach out. Our admin is here to help you!</p>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="/contact">Contact</a>
        </nav>
        <main>
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is dedicated to excellence in teaching and research in the field of statistics.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vehicula arcu id ligula vehicula, ac tincidunt mauris aliquet. Nulla facilisi. Cras et varius erat, nec luctus orci.</p>
    <p>Donec convallis lacus eget suscipit ullamcorper. Curabitur luctus ante in vestibulum egestas. Proin non dui nec erat fermentum euismod. Aenean a tincidunt augue, in eleifend orci.</p>
    <p>Suspendisse potenti. Integer non felis ac eros congue pellentesque. Nunc sit amet bibendum nisi, a ultricies elit. Sed id facilisis mauris, id consequat justo.</p>
    <p>Maecenas feugiat velit ut libero vulputate, a tincidunt elit blandit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>
    <p>Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam a tincidunt libero, nec viverra tortor. Suspendisse sit amet luctus ligula.</p>
    <p>Curabitur eget nisi vitae eros vulputate efficitur vel sit amet elit. Phasellus id nisl ut ligula convallis pharetra. Donec lacinia eros a lectus pulvinar, eget varius risus tincidunt.</p>
    <p>Praesent vitae tortor eget augue congue dapibus. Etiam at fermentum turpis, non fringilla ex. Vestibulum tristique libero a urna tincidunt suscipit.</p>
    <p>Integer ut urna non ipsum gravida feugiat. Aliquam a consequat ligula. Proin et sapien a nisi faucibus fringilla non in nunc. Vivamus vel turpis eget lacus mollis viverra.</p>
    <p>Nulla facilisi. Nam et justo eget quam lacinia bibendum. Etiam id arcu sit amet nisl dapibus convallis. Suspendisse potenti.</p>
    <p>Fusce ut est risus. Nunc consequat mauris euismod ligula blandit, vel posuere tortor rhoncus. Sed convallis, turpis at sodales aliquam, lorem nisl malesuada erat, non varius magna sapien ac libero.</p>

            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <p>Email: info@statkku.ac.th</p>
                <p>Phone: +66-1234-5678</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":   # run code 
    app.run()