from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
import re

# Updated pattern to capture both formats:
# 1. Legacy format: :fa fa-star:, :fas fa-star:, :far fa-star:, etc.
# 2. New format: :fa-cl-s fa-star:, :fa-dt fa-star:, etc.
fontawesome_pattern = r':(?:fa([bsrl]?)|(fa-(?:([a-z]{1,2})(?:-([a-z]{1}))?(?:-([a-z]{1,2}))?)))\s?fa-([-\w]+)\s?(fa-(xs|sm|lg|[\d+]x|10x))?:'

# Family prefixes
prefix_to_family = {
    'cl': 'classic',
    'sh': 'sharp',
    'dt': 'duotone',
    'sd': 'sharp-duotone',
    'br': 'brands',
}

# Style prefixes
prefix_to_style = {
    '': 'solid',
    's': 'solid',
    'r': 'regular',
    'l': 'light',
    't': 'thin',
}

# Legacy prefix mapping for backward compatibility
legacy_prefix_map = {
    'fa': {'family': 'classic', 'style': 'solid'},
    'fas': {'family': 'classic', 'style': 'solid'},
    'far': {'family': 'classic', 'style': 'regular'},
    'fal': {'family': 'classic', 'style': 'light'},
    'fab': {'family': 'brands', 'style': None},
}


class FontAwesomeInlineProcessor(InlineProcessor):
    'Markdown inline processor class for matching things that look like FA icons'

    def handleMatch(self, m, data):
        el = etree.Element('i')

        # Check if we're dealing with the legacy format
        legacy_suffix = m.group(1)
        if legacy_suffix is not None:
            legacy_prefix = f'fa{legacy_suffix}'
            family = legacy_prefix_map[legacy_prefix]['family']
            style = legacy_prefix_map[legacy_prefix]['style']
            icon_name = m.group(6)  # Icon name is now at group 6
            size = m.group(7)       # Size is now at group 7
        else:
            # We have the new format
            prefix1 = m.group(3) if m.group(3) else ''
            prefix2 = m.group(4) if m.group(4) else ''
            prefix3 = m.group(5) if m.group(5) else ''
            icon_name = m.group(6)
            size = m.group(7)

            # Process all prefix parts
            family = None
            style = None

            # Process the prefix parts
            for prefix in [prefix1, prefix2, prefix3]:
                if not prefix:
                    continue

                # Check if this prefix represents a family
                if prefix in prefix_to_family:
                    family = prefix_to_family[prefix]
                # Check if this prefix represents a style
                elif prefix in prefix_to_style:
                    style = prefix_to_style[prefix]

            # Apply defaults
            if family is None:
                family = 'classic'  # Default family is classic

            if style is None and family != 'brands':
                style = 'solid'     # Default style is solid (if not brands)

        # Build the class string
        classes = []

        # Add family class
        if family == 'classic':
            # Classic doesn't need a specific prefix
            pass
        elif family == 'sharp-duotone':
            classes.append('fa-sharp fa-duotone')
        else:
            classes.append(f'fa-{family}')

        # Add style class (if applicable)
        if style and family != 'brands':
            classes.append(f'fa-{style}')

        # Add icon name
        classes.append(f'fa-{icon_name}')

        # Add size if provided
        if size:
            classes.append(size)

        # Set class attribute
        el.set('class', ' '.join(classes))
        return el, m.start(0), m.end(0)


class FontAwesomeExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(FontAwesomeInlineProcessor(fontawesome_pattern, md), 'fontawesome', 175)


def makeExtension(**kwargs):
    return FontAwesomeExtension(**kwargs)