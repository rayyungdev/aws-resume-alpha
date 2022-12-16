from flask import Flask, jsonify, make_response, request
from lib import builder, templates

app = Flask(__name__)

data = './data/data.yaml'
@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/build_resume", methods = ['POST'])
def build_resume():
    req = request.get_json(force = True)

    # tags = req.get('tags', None)
    tags = ['programming', 'technology']
    me = req.get('max_experience', None)
    ms = req.get('max_skills', None)
    # dps = req.get('display_skills', None)

    header_size = 12
    body_size = 10.5
    title_size = 20

    resume = builder.builder_from_yaml(data)
    template = templates.template_basic()

    response = make_response(
        resume.build_resume(
            template = template,
            output = "test.pdf",
            keys = tags, 
            max_experience = me, 
            max_skills = ms, 
            display_project_skills=True, 
            header_font_size= header_size, 
            body_font_size=body_size, 
            title_font_size=title_size
        )
    )
    response.headers["Content-Type"] = "application/pdf"

    return response

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
