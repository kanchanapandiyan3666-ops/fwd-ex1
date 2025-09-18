# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>HTML Table Example</title>
</head>
<body>

    <h1>Simple Data Table</h1>

    <table>
        <thead>
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
                <th>Header 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1A</td>
                <td>Data 1B</td>
                <td>Data 1C</td>
            </tr>
            <tr>
                <td>Data 2A</td>
                <td>Data 2B</td>
                <td>Data 2C</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>Footer 1</td>
                <td>Footer 2</td>
                <td>Footer 3</td>
            </tr>
        </tfoot>
    </table>

    <h2>Table with Caption</h2>

    <table>
        <caption>Monthly Sales Report</caption>
        <thead>
            <tr>
                <th>Month</th>
                <th>Product A Sales</th>
                <th>Product B Sales</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>January</td>
                <td>$10,000</td>
                <td>$8,500</td>
            </tr>
            <tr>
                <td>February</td>
                <td>$12,000</td>
                <td>$9,200</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
~~~

## OUTPUT:
![alt text](<Screenshot 2025-09-18 145512.png>)
![alt text](<Screenshot 2025-09-18 145611.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.

