from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]

class BlogIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]

class PortfolioIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]



class StoryBlock(blocks.StreamBlock):
    h2 = blocks.CharBlock(icon='title')
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    wide_image = ImageChooserBlock(label='wide image')
    code = CodeBlock(label='Code')

class PortfolioPage(Page):
    body = StreamField(StoryBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    

class BlogPage(Page):
    date = models.DateField('Post date')
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    story = StreamField(StoryBlock(), default=None)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname='full'),
        StreamFieldPanel('story')
    ]
