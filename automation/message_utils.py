from jinja2 import Template

def load_message_template(template_path, context):
    """
    Load and render a message template using Jinja2.
    :param template_path: Path to the template file.
    :param context: Dict of values to fill in the template.
    :return: Rendered message as a string.
    """
    with open(template_path, "r") as file:
        template = Template(file.read())
    return template.render(context)