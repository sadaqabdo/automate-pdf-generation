import pdfkit

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

data = {
    'poste': 'Data Scientist',
    'nombre': '3',
    'domaine': 'Data Science',
    'competence': 'Python'
}
text = template.render(data)

filename = f'Application for {data["poste"]} Post.pdf'
pdfkit.from_string(text, filename)