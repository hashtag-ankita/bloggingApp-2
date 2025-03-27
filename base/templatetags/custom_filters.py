import re
from django import template

register = template.Library()

def minimal_markdown(text):
    '''
    Converts markdown to HTML
    '''
    # Convert bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Convert italic text
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    # Convert underlined text
    text = re.sub(r'__(.*?)__', r'<u>\1</u>', text)

    # Convert strikethrough text
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)

    # Convert inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)

    # Convert links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    return text


@register.filter
def markdown_text(text):
    '''
    Django filter to convert markdown to HTML
    '''
    return minimal_markdown(text)
