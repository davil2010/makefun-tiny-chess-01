import base64,lzma,pathlib
d=pathlib.Path(__file__).parent
# split pack
exec(lzma.decompress(base64.b85decode((d/"a").read_text()+(d/"b").read_text())))
