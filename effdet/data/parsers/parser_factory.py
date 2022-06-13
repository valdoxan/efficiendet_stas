""" Parser factory

Copyright 2020 Ross Wightman
"""
from .parser_coco import CocoParser
from .parser_voc import VocParser,VocParserWithoutAnnotation
from .parser_open_images import OpenImagesParser


def create_parser(annotation, name, **kwargs):
    if name == 'coco':
        parser = CocoParser(**kwargs)
    elif name == 'voc' and annotation=="T":
        parser = VocParser(**kwargs)
    elif name == 'voc' and annotation=="F":
        parser = VocParserWithoutAnnotation(**kwargs)
    elif name == 'openimages':
        parser = OpenImagesParser(**kwargs)
    else:
        assert False, f'Unknown dataset parser ({name})'
    return parser
