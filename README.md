# Easily place FontAwesome icons in your MarkDown files

This is a Markdown extension to include FontAwesome icons in your Markdown text, without pasting bulky HTML.
Use emoticon-like strings like `:fa-mug-hot:` to place the corresponding FontAwesome markup in your text flow.

## Installation

```bash
pip install fontawesome-in-markdown
```

## How to use

Include your favorite version of FontAwesome CSS/assets in your HTML, then add `fontawesome_in_markdown` to your Markdown:

```python
from markdown import Markdown

markdown = Markdown(extensions=['fontawesome_in_markdown'])
```

## Basic Usage

```python
markdown.convert('I ♥ :fa-mug-hot:')
```

will output:

```html
<p>I ♥ <i class="fa-solid fa-mug-hot"></i></p>
```

## Icon Styles

You can specify different styles using prefixes:

### Legacy Format (Backward Compatible)

```markdown
:fa fa-star:    → <i class="fa-solid fa-star"></i>
:fas fa-star:   → <i class="fa-solid fa-star"></i>
:far fa-star:   → <i class="fa-regular fa-star"></i>
:fal fa-star:   → <i class="fa-light fa-star"></i>
:fab fa-github: → <i class="fa-brands fa-github"></i>
```

### New Format with Font Family and Style

The new format allows you to specify both family and style with more flexibility:

```markdown
:fa-cl-s fa-star:   → <i class="fa-solid fa-star"></i>          (Classic Solid)
:fa-cl-r fa-star:   → <i class="fa-regular fa-star"></i>        (Classic Regular)
:fa-cl-l fa-star:   → <i class="fa-light fa-star"></i>          (Classic Light)
:fa-cl-t fa-star:   → <i class="fa-thin fa-star"></i>           (Classic Thin)
:fa-sh-s fa-star:   → <i class="fa-sharp fa-solid fa-star"></i> (Sharp Solid)
```

Family codes:

- `cl` = Classic
- `sh` = Sharp
- `dt` = Duotone
- `sd` = Sharp-Duotone
- `br` = Brands

Style codes:

- `s` = Solid
- `r` = Regular
- `l` = Light
- `t` = Thin

You can also reverse the order (style-family):

```markdown
:fa-r-dt fa-star:   → <i class="fa-duotone fa-regular fa-star"></i>
:fa-l-sh fa-star:   → <i class="fa-sharp fa-light fa-star"></i>
```

### Simplified Format

You can omit parts, and they'll default to sensible values:

```markdown
:fa-star:         → <i class="fa-solid fa-star"></i>             (Default: Classic Solid)
:fa-s fa-star:    → <i class="fa-solid fa-star"></i>             (Only style specified)
:fa-r fa-star:    → <i class="fa-regular fa-star"></i>           (Only style specified)
:fa-dt fa-star:   → <i class="fa-duotone fa-solid fa-star"></i>  (Only family specified)
:fa-br fa-github: → <i class="fa-brands fa-github"></i>          (Brands ignore style)
```

## Size Modifiers

You can add size modifiers:

```markdown
:fa-star fa-xs:  → <i class="fa-solid fa-star fa-xs"></i>
:fa-star fa-sm:  → <i class="fa-solid fa-star fa-sm"></i>
:fa-star fa-lg:  → <i class="fa-solid fa-star fa-lg"></i>
:fa-star fa-2x:  → <i class="fa-solid fa-star fa-2x"></i>
:fa-star fa-10x: → <i class="fa-solid fa-star fa-10x"></i>
```

## Known Issues

Not a real issue, but worth mentioning: with this version, icon validation has been removed. Invalid icons are handed to FontAwesome and the behavior is handled by the library's CSS. This means that the library no longer warns you about possible typos or errors in the icon and style naming.

## Credits

This extension is a fork of [`fontawesome-markdown` by `bmcorser`](http://bmcorser.github.com/fontawesome-markdown).  
For some reasons, the original repository is abandoned, so I decided to publish this updated version, after waiting for a PR to be accepted.

Should the original author come back in the future, to maintain the original package, I will probably merge it back. In the meantime this should be a valid dropdown replacement.

## Contributions

I'll try my best to keep this repo up to date, reviewing and accepting contributions, but I'm not an expert Pythonista myself. Feel free to send in PRs as long as they describe the scope clearly, to ease the review process.

For those who, like me, don't work with Python on a daily basis, you can run tests in a docker container with:

```bash
docker run --rm -v "$(pwd):/app" -w /app python:bookworm bash -c "pip install -e .[test] pytest markdown && pytest -v"
```
