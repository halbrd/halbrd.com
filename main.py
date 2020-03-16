from flask import Flask, render_template

from views.bumps import bumps

app = Flask(__name__)

app.register_blueprint(bumps)

EXTERNAL_LINKS = [
    { 'img': 'will.sx', 'username': 'professional site', 'location': 'https://will.sx' },
    { 'img': 'github', 'username': 'halbrd', 'location': 'https://github.com/halbrd' },
    { 'img': 'reddit', 'username': 'halbrd', 'location': 'https://reddit.com/u/halbrd' },
    { 'img': 'keybase', 'username': 'halbrd', 'location': 'https://keybase.io/halbrd' },
    { 'img': 'wikipedia', 'username': 'Halbrd', 'location': 'https://en.wikipedia.org/wiki/Special:Contributions/Halbrd' },
    { 'img': 'paypal', 'username': 'halbrd', 'location': 'https://www.paypal.me/halbrd' },
    { 'img': 'youtube', 'username': 'halbrd', 'location': 'https://youtube.com/halbrd' },
    { 'img': 'twitter', 'username': 'halbrd_', 'location': 'https://twitter.com/halbrd_' },
    { 'img': 'steam', 'username': 'halbrd', 'location': 'https://steamcommunity.com/id/halbrd' },
    { 'img': 'trakt', 'username': 'halbrd', 'location': 'https://trakt.tv/users/halbrd' },
    { 'img': 'hacker-news', 'username': 'halbrd', 'location': 'https://news.ycombinator.com/user?id=halbrd' },
    { 'img': 'bandcamp', 'username': 'halbrd', 'location': 'https://bandcamp.com/halbrd' },
    { 'img': 'patreon', 'username': 'halbrd', 'location': 'https://www.patreon.com/halbrd' },
    { 'img': 'twitch', 'username': 'halbrd', 'location': 'https://twitch.tv/halbrd' },
    { 'img': 'discord', 'username': 'halbrd#0087', 'location': 'https://discordapp.com/channels/@me/' },
    { 'img': 'xbox', 'username': 'halbrd', 'location': 'https://account.xbox.com/en-us/profile?gamertag=halbrd' },
]

@app.route('/')
def index():
    return render_template('index/index.html',
        external_links=EXTERNAL_LINKS
    )

if __name__ == '__main__':
    # debug mode - not for production
    app.run(host='0.0.0.0', debug=True, port=5000)
