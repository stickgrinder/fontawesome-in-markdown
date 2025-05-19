# coding: utf-8
from __future__ import unicode_literals
import pytest
from markdown import Markdown
from fontawesome_in_markdown import FontAwesomeExtension

@pytest.fixture(params=[
    FontAwesomeExtension(),
    'fontawesome_in_markdown'
], ids=["import", "string"])
def fa_markdown(request):
    return Markdown(extensions=[request.param])


def test_example(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot:') == expected_markup


def test_unknown_icon_renders(fa_markdown):
    # Instead of raising an exception, unknown icons should render normally
    unknown_icon = 'arglebargle'
    expected_markup = f'<p>i ♥ <i class="fa-solid fa-{unknown_icon}"></i></p>'
    assert fa_markdown.convert(f"i ♥ :fa-{unknown_icon}:") == expected_markup


def test_unknown_prefix_renders(fa_markdown):
    # Test with an unknown prefix - should default to solid style
    expected_markup = '<p>i ♥ <i class="fa-solid fa-facebook"></i></p>'
    assert fa_markdown.convert("i ♥ :fa fa-facebook:") == expected_markup
    

def test_size(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-xs"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-xs:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-sm"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-sm:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-lg"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-lg:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-1x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-1x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-3x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-3x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-10x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-10x:') == expected_markup


def test_brand_icon(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-brands fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fab fa-facebook:') == expected_markup


def test_regular_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-regular fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :far fa-star:') == expected_markup


def test_solid_icon_without_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-star:') == expected_markup


def test_light_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-light fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fal fa-star:') == expected_markup


def test_pro_icon_should_render(fa_markdown):
    # This test verifies that pro-only icons still render HTML correctly
    expected_markup = '<p>i ♥ <i class="fa-solid fa-radar"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-radar:') == expected_markup