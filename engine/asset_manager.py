import os
import pygame 

class AssetManager:
        def __init__(self):
            self.assets = {}
            path = os.path.dirname(os.path.abspath(__file__))
            asset_path = os.path.join(path, "..","assets")
            self.load_assets(asset_path)

        def load_assets(self, path):
            asset_categories = ["tiles", "monsters", "items", "characters", "effects"]
            for category in asset_categories:
                self.assets[category] = self.recurse_dir(os.path.join(path, category))

        def recurse_dir(self, path):
            assets = {}
            for folder in os.listdir(path):
                assets[folder] = {}
                for file in os.listdir(os.path.join(path, folder)):
                    if file.endswith(".png"):
                        im_path = os.path.join(path, folder, file)
                        assets[folder][file[:-4]] = pygame.image.load(im_path).convert_alpha()
            return assets

        @property
        def monsters(self):
            return self.assets["monsters"]
        @property
        def tiles(self):
            return self.assets["tiles"]
        @property
        def items(self):
            return self.assets["items"]
        @property
        def characters(self):
            return self.assets["characters"]
        @property
        def effects(self):
            return self.assets["effects"]
        