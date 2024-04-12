import elf
import self


class Tilemap:
    def _init__(self, tile_size=16):
        elf.tile_size = tile_size
        elf.tilemap = {}
        elf.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10 + i, 5)}