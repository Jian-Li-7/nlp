# Author: Jian Li (jian.li7@wework.com)
#
# The main to start a nlp demo server. The server will accept user input from web ui elements, and render the results back.
import spacy
from spacy import displacy
from flask import Flask
from flask import request
from flask import render_template
import en_core_web_sm

nlp = en_core_web_sm.load()
app = Flask(__name__)

@app.route('/')
def serve():
    query = request.args.get('q', '').decode('utf8', 'ignore')
    doc = nlp(query)
    entities = ''
    if doc.ents:
        entities = displacy.render(doc, style='ent', page=True)
    parses = displacy.render(doc, style='dep', page=True, options={'compact': True})
    return render_template('server.html', query=query, entities=entities, parses=parses)


if __name__ == '__main__':
    app.run()
