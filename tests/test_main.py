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
    assert fa_markdown.convert('i ♥ :fa-s fa-mug-hot:') == expected_markup


# Legacy format tests
def test_legacy_solid(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa fa-star:') == expected_markup
    assert fa_markdown.convert('i ♥ :fas fa-star:') == expected_markup


def test_legacy_regular(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-regular fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :far fa-star:') == expected_markup


def test_legacy_light(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-light fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fal fa-star:') == expected_markup


def test_legacy_brands(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-brands fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fab fa-facebook:') == expected_markup


# New format tests - family-style order
def test_family_style_classic_solid(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-cl-s fa-star:') == expected_markup


def test_family_style_classic_regular(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-regular fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-cl-r fa-star:') == expected_markup


def test_family_style_duotone_solid(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-duotone fa-solid fa-circle-user"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-dt-s fa-circle-user:') == expected_markup


def test_family_style_sharp_regular(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-sharp fa-regular fa-envelope"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-sh-r fa-envelope:') == expected_markup


def test_family_style_sharp_duotone(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-sharp fa-duotone fa-solid fa-envelope"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-sd fa-envelope:') == expected_markup
    assert fa_markdown.convert('i ♥ :fa-sd-s fa-envelope:') == expected_markup


# New format tests - style-family order
def test_style_family_solid_classic(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-s-cl fa-star:') == expected_markup


def test_style_family_regular_duotone(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-duotone fa-regular fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-r-dt fa-star:') == expected_markup


def test_style_family_light_sharp(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-sharp fa-light fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-l-sh fa-star:') == expected_markup


# New format tests - single part prefixes (defaults apply)
def test_only_family_specified(fa_markdown):
    # When only family is specified, style defaults to solid
    expected_markup = '<p>i ♥ <i class="fa-sharp fa-solid fa-user"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-sh fa-user:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-duotone fa-solid fa-user"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-dt fa-user:') == expected_markup


def test_only_style_specified(fa_markdown):
    # When only style is specified, family defaults to classic
    expected_markup = '<p>i ♥ <i class="fa-regular fa-user"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-r fa-user:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-light fa-user"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-l fa-user:') == expected_markup


# Special cases
def test_brands_ignores_style(fa_markdown):
    # Brands should ignore any style specification
    expected_markup = '<p>i ♥ <i class="fa-brands fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-br fa-facebook:') == expected_markup
    assert fa_markdown.convert('i ♥ :fa-br-s fa-facebook:') == expected_markup
    assert fa_markdown.convert('i ♥ :fa-s-br fa-facebook:') == expected_markup


def test_unknown_icon_renders(fa_markdown):
    # Unknown icons should still render HTML
    unknown_icon = 'arglebargle'
    expected_markup = f'<p>i ♥ <i class="fa-solid fa-{unknown_icon}"></i></p>'
    assert fa_markdown.convert(f"i ♥ :fa-s fa-{unknown_icon}:") == expected_markup


def test_size_with_new_format(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-duotone fa-solid fa-user fa-lg"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-dt fa-user fa-lg:') == expected_markup