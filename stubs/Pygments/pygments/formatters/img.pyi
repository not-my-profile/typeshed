from typing import Any

from pygments.formatter import _BinaryFormatter

class PilNotAvailable(ImportError): ...
class FontNotFound(Exception): ...

class FontManager:
    font_name: Any
    font_size: Any
    fonts: Any
    encoding: Any
    def __init__(self, font_name, font_size: int = ...) -> None: ...
    def get_char_size(self): ...
    def get_text_size(self, text): ...
    def get_font(self, bold, oblique): ...

class ImageFormatter(_BinaryFormatter):
    name: str
    aliases: Any
    filenames: Any
    unicodeoutput: bool
    default_image_format: str
    encoding: str
    styles: Any
    background_color: str
    image_format: Any
    image_pad: Any
    line_pad: Any
    fonts: Any
    line_number_fg: Any
    line_number_bg: Any
    line_number_chars: Any
    line_number_bold: Any
    line_number_italic: Any
    line_number_pad: Any
    line_numbers: Any
    line_number_separator: Any
    line_number_step: Any
    line_number_start: Any
    line_number_width: Any
    hl_lines: Any
    hl_color: Any
    drawables: Any
    def get_style_defs(self, arg: str = ...) -> None: ...
    def format(self, tokensource, outfile) -> None: ...

class GifImageFormatter(ImageFormatter):
    name: str
    aliases: Any
    filenames: Any
    default_image_format: str

class JpgImageFormatter(ImageFormatter):
    name: str
    aliases: Any
    filenames: Any
    default_image_format: str

class BmpImageFormatter(ImageFormatter):
    name: str
    aliases: Any
    filenames: Any
    default_image_format: str
