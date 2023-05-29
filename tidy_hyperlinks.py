def tidy_link(name, url, hovertext=None):
    if hovertext is None:
        return f'[{name}]({url})'
    return f'[{name}]({url} "{hovertext}")'