def tidy_link(url, name, hovertext=None):
    if hovertext is None:
        return f'[{name}]({url})'
    return f'[{name}]({url} "{hovertext}")'


print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
print(tidy_link("https://google.com", "google", "Google Search"))
print(tidy_link("https://youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))
