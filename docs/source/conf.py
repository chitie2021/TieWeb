# Configuration for building my website using Sphinx.

# -- Project information

project = '老铁学习网'
copyright = '2024, ChiTie'
author = 'ChiTie'

release = '0.2'
version = '0.2.26'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

intersphinx_disabled_reftypes = []

templates_path = ['_templates']

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'


# --隐藏首页的latest字符
html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# --隐藏“在GitHub上编辑”链接
# html_show_sourcelink = False




