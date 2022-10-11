from Modules.Resume import Resume
from Modules.Json import jsonLoad

technologies = jsonLoad('Technologies.json')
tools = jsonLoad('Tools.json')
langs = jsonLoad('Languages.json')

pdf = Resume(jsonLoad('Profile.json'))
pdf.add_page(format = 'A4')

pdf.about()

pdf.topic('Linguagens e Frameworks')

for technology in technologies:
    pdf.subtopic(technology['name'])
    
    for lib in technology['libraries']:
        pdf.subtopicItem(lib['name'])

pdf.topic('Outros')

for tool in tools:
    pdf.topicItem(tool)

pdf.topic('Idiomas')

for lang in langs:
    pdf.topicItem(lang)

pdf.output('curriculo.pdf')
