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
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()