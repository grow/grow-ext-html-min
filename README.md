# grow-ext-html-min

Simple extension for minifying html after Grow renders a page.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-html-min`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
ext:
- extensions.html_min.HtmlMinExtension
```

When rendering HTML pages Grow will minify the resulting html.

### Disable per environment

To disable, set the `enabled` config to `False`.

```
ext:
- extensions.html_min.HtmlMinExtension:
    enabled@env.staging: False
```

### Options

The configuration can also be used with the options for [`htmlmin`](https://htmlmin.readthedocs.io/en/latest/reference.html#htmlmin.minify).

For example:

```
ext:
- extensions.html_min.HtmlMinExtension:
    options:
      remove_comments: true
      reduce_boolean_attributes: false
```
