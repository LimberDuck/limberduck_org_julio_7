# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LimberDuck'
copyright = 'Copyright &copy; 2018-2024, <a href="https://damiankrawczyk.com">Damian Krawczyk</a>'
author = 'Damian Krawczyk'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # ...
    "sphinx_design",
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    "ablog",
    "sphinx.ext.intersphinx",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']

html_title = "LimberDuck"

html_logo = "_static/img/LimberDuck-logo.png"

html_favicon = "_static/img/favicon.ico"

html_theme_options = {
    # "announcement": "The content of the announcement",
    "accent_color": "orange",
    "github_url": "https://github.com/LimberDuck",
    "nav_links": [
        {
            "title": "About",
            "url": "/about/index",
        },
        {
            "title": "Tools",
            "children": [
                {
                    "title": "nessus file reader (nfr)",
                    "url": "/tools/nessus-file-reader/index",
                    "summary": "CLI tool and python module",
                },
                {
                    "title": "nessus file analyzer (nfa)",
                    "url": "/tools/nessus-file-analyzer/index",
                    "summary": "GUI tool",
                },
            ]
        },
        {
            "title": "Contact",
            "url": "/contact/index",
        },
        {
            "title": "News",
            "url": "blog/index",
        },
    ]

}

# html_context = {
#     "languages": [
#         ("🇺🇸 English", "/en/%s/", "en"),
#         ("🇵🇱 Polish", "/pl/%s/", "pl"),
#     ]
# }


blog_authors = {
    'Damian': ('Damian Krawczyk', 'https://damiankrawczyk.com'),
}
post_date_format = "%Y-%m-%d %H:%M:%S"


html_sidebars = {
   '**': ["ablog/postcard.html",
          "sidebars/localtoc.html",
        ]
}

rst_prolog =  """
.. |GUI| replace:: :abbr:`GUI (Graphical User Interface)`
.. |CLI| replace:: :abbr:`CLI (command-line interfaces)`
.. |csv| replace:: :abbr:`csv (comma-separated value)`
.. |xlsx| replace:: :abbr:`xlsx (Microsoft Excel Open XML Spreadsheet)`
.. |VA| replace:: :abbr:`VA (Vulnerability Assessment)`

.. nessus-file-analyzer:
.. |nfa| replace:: :abbr:`nfa (nessus-file-analyzer by Limberduck)`
.. _nessus-file-analyzer: https://github.com/LimberDuck/nessus-file-analyzer
.. _nessus-file-analyzer doc: https://nessus-file-analyzer.readthedocs.io

.. nessus-file-reader:
.. |nfr| replace:: :abbr:`nfr (nessus-file-reader by Limberduck)`
.. _nessus-file-reader: https://github.com/LimberDuck/nessus-file-reader
.. _nessus-file-reader doc: https://nessus-file-reader.readthedocs.io

.. Technology:
.. |OS| replace:: :abbr:`OS (Operating System)`
.. |RMB| replace:: :abbr:`RMB (Right Mouse Button)`
.. |FQDN| replace:: :abbr:`FQDN (Fully Qualified Domain Name)`
.. |IP| replace:: :abbr:`IP (Intrnet Protocol Address)`

.. Security:
.. |CVE| replace:: :abbr:`CVE (Common Vulnerabilities and Exposures)`

"""