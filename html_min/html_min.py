"""Html min extension for minifying HTML in Grow sites."""

import htmlmin
from grow import extensions
from grow.extensions import hooks


class HtmlMinPostRenderHook(hooks.BasePostRenderHook):
    """Handle the pre-render hook."""

    def trigger(self, previous_result, doc, raw_content):
        """Execute pre-render modification."""
        if not doc.view.endswith('.html'):
            return previous_result
        content = previous_result if previous_result else raw_content
        return htmlmin.minify(content, **self.extension.config.get('options', {}))


class HtmlMinExtension(extensions.BaseExtension):
    """Example Extension."""

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [HtmlMinPostRenderHook]

    def post_render_hook(self):
        """Hook handler for pre render."""
        return HtmlMinPostRenderHook(self)
