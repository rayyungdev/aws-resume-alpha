from lib import builder, templates


template = templates.template_basic()

resume = builder.builder_from_yaml('./data/data.yaml')
resume.build_resume(template, output = 'test.pdf', keys = ['programming', 'technology'], max_experience = 7, max_skills = 7, display_project_skills=True, header_font_size= 12, body_font_size=10.5, title_font_size=20)
