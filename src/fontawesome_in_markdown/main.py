from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
import re

fontawesome_pattern = r':(fa[bsrl]?)?\s?fa-([-\w]+)\s?(fa-(xs|sm|lg|[\d+]x|10x))?:'

prefix_to_style = {
    'fa': 'solid',
    'fas': 'solid',
    'fab': 'brands',
    'far': 'regular',
    'fal': 'light',
}


class FontAwesomeInlineProcessor(InlineProcessor):
    'Markdown inline processor class for matching things that look like FA icons'

    def handleMatch(self, m, data):
        el = etree.Element('i')
        prefix = m.group(1)
        icon_name = m.group(2)
        size = m.group(3)

        # If no prefix provided, default to 'fa' (solid)
        if not prefix:
            prefix = 'fa'

        # Get the style from the prefix, default to 'solid' if unknown prefix
        style = prefix_to_style.get(prefix, 'solid')

        # Set the class attribute for Font Awesome
        classes = f'fa-{style} fa-{icon_name}'
        if size:
            classes += f' {size}'

        el.set('class', classes)
        return el, m.start(0), m.end(0)


class FontAwesomeExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(FontAwesomeInlineProcessor(fontawesome_pattern, md), 'fontawesome', 175)


def makeExtension(**kwargs):
    return FontAwesomeExtension(**kwargs)