# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import ablog

project = 'LimberDuck'
copyright = 'Copyright &copy; 2018-2026, <a href="https://damiankrawczyk.com">Damian Krawczyk</a>'
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
    "myst_parser",
    "sphinx_iconify",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']

html_title = "LimberDuck"
html_baseurl = "https://limberduck.org/en/latest"
sitemap_url_scheme = "{link}"

html_logo = "_static/img/LimberDuck-logo.png"

html_favicon = "_static/img/favicon.ico"

html_theme_options = {
    "announcement": "<b>NFR</b> v0.8.0 with Nessus plugins publication date charts! Check out the latest <a href='https://limberduck.org/en/latest/blog/index.html'>News</a>!",
    "accent_color": "orange",
    "github_url": "https://github.com/LimberDuck",
    "linkedin_url": "https://www.linkedin.com/company/LimberDuck",
    "youtube_url": "https://www.youtube.com/@LimberDuck",
    "twitter_url": "https://twitter.com/LimberDuckOrg",
    "facebook_url": "https://www.facebook.com/limberduck",
    "instagram_url": "https://www.instagram.com/limberduck",
    "mastodon_url": "https://mastodon.social/@limberduck",
    "og_image_url" : "https://limberduck.org/en/latest/_static/img/limberduck-logo-bg.png",
    "nav_links": [
        {
            "title": "About",
            "url": "about/index",
        },
        {
            "title": "Tools",
            "children": [
                {
                    "title": "nessus file reader (NFR)",
                    "url": "tools/nessus-file-reader/index",
                    "summary": "Parse VA scan results from <i>Tenable Nessus</i> and <i>Tenable Security Center</i>",
                },
                {
                    "title": "nessus file analyzer (NFA)",
                    "url": "tools/nessus-file-analyzer/index",
                    "summary": "Generate reports of VA scan results from <i>Tenable Nessus</i> and <i>Tenable Security Center</i>",
                },
                {
                    "title": "Converter CSV",
                    "url": "tools/converter-csv/index",
                    "summary": "Bulk convert CSV files to XLSX format",
                },
                {
                    "title": "TNSCM",
                    "url": "tools/tnscm/index",
                    "summary": "Manage <i>Tenable Nessus</i> via API",
                },
                {
                    "title": "TSCCM",
                    "url": "tools/tsccm/index",
                    "summary": "Manage <i>Tenable Security Center</i> via API",
                },
            ]
        },
        {
            "title": "News",
            "url": "blog/index",
        },
        {
            "title": "FAQ",
            "url": "faq/index",
        },
        {
            "title": "Contact",
            "url": "contact/index",
        },
        {
            "title": "Missing feature?",
            "url": "contact/index",
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
blog_title = "LimberDuck News"
blog_path = "blog"
blog_baseurl = "https://limberduck.org/en/latest/"
blog_feed_archives = True
blog_feed_fulltext = True

html_sidebars = {
   '**': ["ablog/postcard.html",
          "sidebars/localtoc.html",
        #   "sidebars/ethical-ads.html",
        ]
}

html_css_files = [
  'custom.css',
]

rst_prolog =  """
.. |GUI| replace:: :abbr:`GUI (Graphical User Interface)`
.. |CLI| replace:: :abbr:`CLI (command-line interfaces)`
.. |csv| replace:: :abbr:`csv (comma-separated value)`
.. |xlsx| replace:: :abbr:`xlsx (Microsoft Excel Open XML Spreadsheet)`
.. |VA| replace:: :abbr:`VA (Vulnerability Assessment)`
.. |TLDR| replace:: :abbr:`TLDR (Too Long; Didn't Read.)`
.. |PyPI| replace:: :abbr:`PyPI (The Python Package Index)`

.. nessus-file-analyzer:
.. |NFA| replace:: :abbr:`NFA (nessus file analyzer (NFA) by Limberduck)`
.. |**NFA**| replace:: :abbr:`NFA (nessus file analyzer (NFA) by Limberduck)`
.. _nessus-file-analyzer: https://github.com/LimberDuck/nessus-file-analyzer
.. _nessus-file-analyzer doc: https://nessus-file-analyzer.readthedocs.io

.. nessus-file-reader:
.. |NFR| replace:: :abbr:`NFR (nessus file reader (NFR) by Limberduck)`
.. |**NFR**| replace:: :abbr:`NFR (nessus file reader (NFR) by Limberduck)`
.. _nessus-file-reader: https://github.com/LimberDuck/nessus-file-reader
.. _nessus-file-reader doc: https://nessus-file-reader.readthedocs.io

.. Technology:
.. |OS| replace:: :abbr:`OS (Operating System)`
.. |RMB| replace:: :abbr:`RMB (Right Mouse Button)`
.. |FQDN| replace:: :abbr:`FQDN (Fully Qualified Domain Name)`
.. |IP| replace:: :abbr:`IP (Intrnet Protocol Address)`
.. |API| replace:: :abbr:`API (Application Programming Interface)`
.. |CSV| replace:: :abbr:`CSV (Comma-separated values)`
.. |SSL| replace:: :abbr:`SSL (Secure Sockets Layer)`
.. |JSON| replace:: :abbr:`JSON (JavaScript Object Notation)`

.. Security:
.. |CVE| replace:: :abbr:`CVE (Common Vulnerabilities and Exposures)`
.. |VPR| replace:: :abbr:`VPR (Vulnerability Priority Rating)`
.. |EPSS| replace:: :abbr:`EPSS (Exploit Prediction Scoring System)`
.. |CVSS| replace:: :abbr:`CVSS (Common Vulnerability Scoring System)`
.. |CVSSv2| replace:: :abbr:`CVSSv2 (Common Vulnerability Scoring System version 2)`
.. |CVSSv3| replace:: :abbr:`CVSSv3 (Common Vulnerability Scoring System version 3)`
.. |CVSSv4| replace:: :abbr:`CVSSv4 (Common Vulnerability Scoring System version 4)`

"""