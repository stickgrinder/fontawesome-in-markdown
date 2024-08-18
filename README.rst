Font Awesome and Markdown, together!
####################################

For when words aren't enough.
-----------------------------

.. image:: https://travis-ci.org/bmcorser/fontawesome-markdown.svg?branch=0.2.4
    :target: https://travis-ci.org/bmcorser/fontawesome-markdown

A Markdown extension that looks for strings like ``:fa-hot-mug:`` and replaces
them with the corresponding Font Awesome icon markup.

Add ``'fontawesome_markdown'`` to your Markdown call and watch the
magic unfold:

.. code-block:: python

    >>> from markdown import Markdown

    >>> markdown = Markdown(extensions=['fontawesome_markdown']
    >>> markdown.convert('i ♥ :fa-hot-mug:')
    <p>i ♥ <i class="fa-solid fa-hot-mug"></i></p>

    >>> markdown.convert('i ♥ :far fa-star: fa-x3')
    <p>i ♥ <i class="fa-regular fa-fontawe fa-x3"></i></p>


Don't forget to make the Font Awesome v6.6 assets available to your DOM, and you're done!

Issue
========

* The `light` prefix, althought supported in code, is not working because it is not
  exposed by FontAwesome in their metadata.