"""The BeautifulSoup module and the requests module are popular tools in the Python programming language that are
widely used for manipulating web pages and extracting data from HTML code.

The BeautifulSoup module:

BeautifulSoup is a Python library that allows you to parse HTML code and extract data from web pages. This module
simplifies HTML code parsing by providing easy-to-use methods for finding, extracting and manipulating web page
elements. BeautifulSoup allows working with different types of parsers, including built-in Python parsers and parsers
of third-party libraries such as lxml and html5lib. It allows you to search for elements in a web page by tags,
classes, identifiers, attributes and other CSS selectors. The BeautifulSoup module also provides easy-to-use methods
to navigate the HTML element tree and manipulate text content, attributes, links and forms in web pages. The requests
module:

requests is a Python module that allows you to send HTTP requests and receive responses from web servers. It provides
a simple and easy way to interact with web services and retrieve data from the web. It provides functions for sending
various types of requests including GET, POST, PUT, DELETE and others. It provides parameter passing of request,
header setting, cookie handling, session handling and other features to customize interaction with web servers. It
also provides convenient methods for handling server responses, such as fetching page content, accessing headers,
handling errors and other features for handling HTTP requests and responses. Together BeautifulSoup and requests
modules allow programmers to extract and process data from web pages with ease, making them indispensable tools for
web scraping, parsing and automating Python web applications."""

from bs4 import BeautifulSoup
import requests


def parse_html_from_url(url):
    # Load the HTML page from the URL
    response = requests.get(url)
    html_doc = response.text

    # Create a BeautifulSoup object for parsing HTML
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Recursively traverse the DOM and store it as a tree
    root = build_dom_tree(soup)

    return root


def build_dom_tree(element):
    # Create a node for the current element
    node = {
        'tag': element.name,
        'text': element.string.strip() if element.string else None,
        'children': []
    }

    # Recursively traverse the child elements
    for child in element.children:
        if child.name is not None:  # Exclude text nodes
            child_node = build_dom_tree(child)
            node['children'].append(child_node)

    return node


def search_text_by_tag(root, tag):
    found_texts = []

    # Recursively search for text based on the given tag
    search_text_recursive(root, tag, found_texts)

    return found_texts


def search_text_recursive(node, tag, found_texts):
    if node['tag'] == tag and node['text'] is not None:
        found_texts.append(node['text'])

    for child in node['children']:
        search_text_recursive(child, tag, found_texts)


# URL of the page to be parsed
url = 'https://beetroot.academy/'

# Parsing HTML and building the DOM tree
dom_tree = parse_html_from_url(url)

# Search text by tag
tag = 'p'
found_texts = search_text_by_tag(dom_tree, tag)
print(f"Texts with tag '{tag}':")
for text in found_texts:
    print(text)
