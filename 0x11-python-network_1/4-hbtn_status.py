#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests
"""

if __name__ == "__main__":
    from requests import get

    html = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(html.text.__class__))
    print('\t- content: {}'.format(html.text))
