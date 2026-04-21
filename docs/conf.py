# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

import re

project = 'enigmapython'
copyright = '2026, Denis Maggiorotto'
author = 'Denis Maggiorotto'

# Dynamically extract version from setup.py
setup_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/enigma/setup.py'))
library_version = 'unknown'
try:
    with open(setup_py_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('version='):
                match = re.search(r'version=["\']([^"\']+)["\']', line)
                if match:
                    library_version = match.group(1)
                break
except Exception:
    pass

release = library_version
version = '.'.join(release.split('.')[:2]) if release != 'unknown' else 'unknown'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_js_files = [
    'js/svg-pan-zoom.min.js',
    'js/zoom_setup.js',
]
