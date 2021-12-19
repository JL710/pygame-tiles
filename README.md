# pygame-tiles

## install
```
pip install git+https://github.com/JL710/pygame-tiles.git
```

## updating
```
pip install --force-reinstall git+https://github.com/JL710/pygame-tiles.git
```

## class Tilelayer
parameters: \
`
images_path: str, tile_width: int, tile_height: int, tile_placing: list
`
### images_path
Path to the directory within all of the tile images.
> Note: the name of the images should be numbers

### tile_placing
A list that shows how the tiles are organised. \
Example: \
```python
tile_placing = [
    "0   0   0",
    " 000 000 ",
    "  00 00  ",
    "   0 0   ",
    "    0    ",
    "0   0   0",
    "000000000"]
```
Empty spots are spaces, tiles begin with 0 --> image numbers.