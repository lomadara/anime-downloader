from abc import ABC, abstractmethod

from lxml import html

class AnimeDownloaderInterface(ABC):
    @abstractmethod
    def get_tree(self) -> html:
        pass
    
    @abstractmethod
    def get_title(self) -> str:
        pass
    
    @abstractmethod
    def get_cover(self) -> str:
        pass
    
    @abstractmethod
    def get_sinopse(self) -> str:
        pass
    
    @abstractmethod
    def get_tags(self) -> list:
        pass

    @abstractmethod
    def get_episodes_url(self) -> str:
        pass
    
    @abstractmethod
    def create_folder(self, anime_title) -> None:
        pass
    
    @abstractmethod
    def download_cover(self, anime_title, cover_url) -> None:
        pass
    
    abstractmethod
    def get_episodes_informations(self, episodes_url) -> dict:
        pass
    
    @abstractmethod
    def download_episode(self, anime_title, anime_id, episode_id, episode_name) -> None:
        pass