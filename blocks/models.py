from django.db import models

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldRowPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel

COLOUR_CHOICES = [
    ('white', 'White'),
    ('grey', 'Grey'),
    ('blue', 'Blue'),
]

class TwoColumnBlock(blocks.StructBlock):
 
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-left', label='Left column content')
 
    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-right', label='Right column content')
 
    class Meta:
        template = 'yourapp/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

