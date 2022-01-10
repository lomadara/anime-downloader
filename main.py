from downloaders.SaikoAnimeDownloader import SaikoAnimeDownloader
from downloaders.Downloader import Dowloader
from utils.Constants import season_animes
from utils.CustomErrors import NotFoundError

saiko_anime_downloader = SaikoAnimeDownloader()

for season_anime in season_animes:
    try:
        downloader = Dowloader(season_anime)
        downloader.download(saiko_anime_downloader)
    
    except NotFoundError as ex:
        print("\033[1;31;40m {} {}".format(season_anime, ex))
        
    except Exception as ex:
        print("\033[1;31;40m {}".format(ex))