import miniflux
from config import config, Config

config: Config = config()

client = miniflux.Client(config.miniflux.url, api_key=config.miniflux.token)


def miniflux_backup():
    print(config.miniflux.token)
    opml = client.export_feeds()
    with open("data/miniflux.opml", "w") as f:
        f.write(opml)


if __name__ == '__main__':
    miniflux_backup()
