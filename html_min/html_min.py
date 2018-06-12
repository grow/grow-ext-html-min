"""Html min extension for minifying HTML in Grow sites."""

import htmlmin
from grow import extensions
from grow.extensions import hooks
from grow.documents import document


class HtmlMinPostRenderHook(hooks.PostRenderHook):
    """Handle the post-render hook."""

    def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
        """Execute post-render modification."""
        if not isinstance(doc, document.Document) or not doc.view.endswith('.html'):
            return previous_result
        content = previous_result if previous_result else raw_content
        return htmlmin.minify(content, **self.extension.config.get('options', {}))


class HtmlMinExtension(extensions.BaseExtension):
    """Example Extension."""

    @property
    def available_hooks(self):
        """Returns the available hook classes."""
        return [HtmlMinPostRenderHook]
