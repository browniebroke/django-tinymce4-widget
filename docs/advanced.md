# Advanced Usage

(custom-css)=

## Applying custom CSS

The [content_style](https://www.tinymce.com/docs/configure/content-appearance/#content_style) and [content_css](https://www.tinymce.com/docs/configure/content-appearance/#content_css) TinyMCE configuration options allow to define custom Cascading Style Sheets for the content in TinyMCE editor window.

The `contents_style` option defines inline styles and the `content_css` option defines a URL or a list of URLs for CSS files. For large Style Sheets the latter option is preferable because a browser can cache CSS files.

For example, if your website uses [Bootstrap](http://getbootstrap.com/) styles, you can apply those styles to edited content in the TinyMCE widget:

```python
TINYMCE_DEFAULT_CONFIG = {
    ...
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    ...
}
```

## Code Samples

TinyMCE v4.3 and later includes [codesample](https://www.tinymce.com/docs/plugins/codesample/) plugin that allows to insert the samples of programming code into edited content with pretty syntax highlighting. The `codesample` plugin uses [Prism](http://prismjs.com/) library for syntax highlighting (default theme). The plugin supports the following languages: **HTML/XML**, **JavaScript**, **CSS**, **PHP**, **Ruby**, **Python**, **Java**, **C#** and **C**/**C++**.

The `codesample` plugin already includes the necessary Prism components to correctly display code samples in TinyMCE, but to make code samples correctly appear on webpages authored with TinyMCE you need to include the links to Prism JavaScript/CSS files into the HTML code of your pages. The **tinymce4-widget** application already includes {file}`prism.js` and {file}`prism.css` files that can be referenced in your Django templates. For example:

```django
{% load static from staticfiles %}
<!DOCTYPE html>
<html>
<head>
  ...
<!-- Prism CSS -->
<link href="{% static "tinymce/css/prism.css" %}" rel="stylesheet">
</head>
<body>
...
<!-- Prism JS -->
<script src="{% static "tinymce/js/prism.js" %}"></script>
</body>
</html>
```

You can use different Prism themes for your webpages but in TinyMCE the content is always displayed with the default Prism theme.

## The Preview Button

The [preview](https://www.tinymce.com/docs/plugins/preview/) plugin in TinyMCE 4, unlike in TinyMCE 3, does not support custom preview dialogs. Use {ref}`custom Style Sheets<custom-css>` as described in the first subsection on this page. They work for the preview window too.
