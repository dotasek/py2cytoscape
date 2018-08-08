import uuid
import json
import os

# ######## Default Values ###########

# Define default widget size
DEF_HEIGHT = 700
DEF_WIDTH = 1098 # Same as cell width of Jupyter

DEF_BACKGROUND_COLOR = '#FFFFFF'

HTML_TEMPLATE_FILE = 'template.html'
STYLE_FILE = 'default_style.json'
STYLE_FILE=os.path.abspath(os.path.dirname(__file__)) + '/' + STYLE_FILE


# Default elements
DEF_ELEMENTS = []

DEF_LAYOUT = 'preset'
DEF_STYLE = []

PRESET_LAYOUTS = {
    'Preset': 'preset',
    'Circle': 'circle',
    'Concentric': 'concentric',
    'Breadthfirst': 'breadthfirst',
    'Spring': 'cose',
    'Grid': 'grid'
}


# Init styles
#style_file = open(os.path.abspath(os.path.dirname(__file__)) + '/' + STYLE_FILE, 'r')
#style_list = json.load(style_file)
#STYLES = {}
#for style in style_list:
#    STYLES[style['title']] = style['style']


def set_styles(style_file=STYLE_FILE):
    style_file = open(style_file, 'r')
    style_list = json.load(style_file)
    STYLES = {}
    for style in style_list:
        STYLES[style['title']] = style['style']
    return STYLES

def render(elements,
           style,
           layout_algorithm=DEF_LAYOUT,
           background=DEF_BACKGROUND_COLOR,
           height=DEF_HEIGHT,
           width=DEF_WIDTH):
    """Render network data with embedded Cytoscape.js widget.

    :param elements: dict (required)
        The network data should be in Cytoscape.js JSON format.
    :param style: dict (required)
        If dict, it should be Cytoscape.js style CSS object
    :param layout_algorithm: str
        Name of Cytoscape.js layout algorithm
    :param background: str
        Background in CSS format
    :param height: int
        Height of the widget.
    :param width: int
        Width of the widget.
    """

    from jinja2 import Template
    from IPython.core.display import display, HTML

    if style is None:
        style = DEF_STYLE

    if elements is None:
        elements = DEF_ELEMENTS

    path = os.path.abspath(os.path.dirname(__file__)) + '/' + HTML_TEMPLATE_FILE
    template = Template(open(path).read())
    cyjs_widget = template.render(
        elements=json.dumps(elements),
        style=json.dumps(style),
        background=background,
        uuid="cy" + str(uuid.uuid4()),
        widget_width=str(width),
        widget_height=str(height),
        layout=layout_algorithm,
        style_json=json.dumps(style)
    )
    str(cyjs_widget)
    display(HTML(cyjs_widget))


# List of available layout algorithms
def get_layouts():
    return PRESET_LAYOUTS

def get_style_names(style_file=STYLE_FILE):
    STYLES=set_styles(style_file)
    return list(STYLES.keys())

def get_style(name,style_file=STYLE_FILE):
    STYLES=set_styles(style_file)
    if name in STYLES.keys():
        return STYLES[name]
    else:
        raise ValueError('Style does not exist: ' + name)
