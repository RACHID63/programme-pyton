import requests
from bs4 import BeautifulSoup
import pdfkit
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    return [link['href'] for link in links]

def save_webpage_as_pdf(url, output_filename):
    links = get_links(url)
    html = """
    <html>
    <head>
        <title>Hello, Rachid</title>
    </head>
    <body>
        <h1>Hello, Rachid</h1>
        <p>Voici les adresses des liens Internet que j'ai trouvés sur la page Web que vous avez spécifiée :</p>
        <ul>
            {links}
        </ul>
    </body>
    </html>
    """.format(links="\n".join([f"<li><a href='{link}'>{link}</a></li>" for link in links]))

    wkhtmltopdf_path =  r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    pdfkit.from_string(html, output_filename)

url = 'https://sitefacile.net/index.html'
output_filename = 'output.pdf'
save_webpage_as_pdf(url, output_filename)
