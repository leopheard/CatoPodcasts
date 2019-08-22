from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL1 = "https://www.cato.org/rss/multimedia/daily-podcast"
URL2 = "https://www.cato.org/rss/multimedia/cato-audio"
URL3 = "https://www.cato.org/rss/multimedia/events-podcast"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://object.cato.org/sites/cato.org/files/multimedia/podcasts/dailypodcast-20170131.jpg"},
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('audio_episodes'),
            'thumbnail': "https://object.cato.org/sites/cato.org/files/multimedia/podcasts/appicons_audiomonthly_3000x3000-min.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('event_episodes'),
            'thumbnail': "https://object.cato.org/sites/cato.org/files/multimedia/podcasts/appicons_eventspodcast_3000x3000-min.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/audio_episodes/')
def audio_episodes():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/event_episodes/')
def event_episodes():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items


if __name__ == '__main__':
    plugin.run()
