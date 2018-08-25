from secretary import Renderer
from docutils.core import publish_string
from docutils.writers.docutils_xml import Writer 
import xmltodict
import json

with open('RESUME.rst', 'r') as src_file:
  src = src_file.read()

resume_xml = publish_string(src, writer=Writer(), settings=None)
data = xmltodict.parse(resume_xml)

resume = {
  'info': {
    'name': data['document']['title'],
    'address': data['document']['docinfo']['address']['#text']
    # 'email': data['document']['docinfo']['email']['#text'],
    # 'website': data['document']['docinfo']['website']['#text'],
    # 'github': data['document']['docinfo']['github']['#text'],
  }
}

print(json.dumps(data['document']['docinfo']['field'][0]))

print(data['document']['docinfo']['address']['#text'])



engine = Renderer()
result = engine.render('ResumeTemplate.odt', resume=resume)
output = open('rendered_document.odt', 'wb')
output.write(result)