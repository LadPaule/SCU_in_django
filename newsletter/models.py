from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel 


class Newsletter(Campaign):
    headline = models.CharField(max_length=255, blank=True, null=True, help_text="The headline to use for the newsletter.")
    header_background = models.ForeignKey("wagtailimages.Image", blank=False, null=True, related_name="+", help_text="The image to use for the header backgound.",
        on_delete=models.SET_NULL,)
    newsletter_date = models.DateField(blank=True, null=True, help_text="The date to use for the newsletter.")
    newsletter_receiver = models.CharField(max_length=255, blank=True, null=True, help_text="The receiver of the newsletter.")
    newsletter_introduction = models.TextField(blank=True, null=True, help_text="The introduction to use for the newsletter.")
    newsletter_first_story = RichTextField(blank=True, null=True, help_text="The first story to use for the newsletter.")
    
    newsletter_second_story = RichTextField(blank=True, null=True, help_text="The first story to use for the newsletter.")
    second_story_image = models.ForeignKey("wagtailimages.Image", blank=True, null=True, related_name="+", help_text="The image to use for the second story.", on_delete=models.SET_NULL)
    newsletter_third_story = RichTextField(blank=True, null=True, help_text="The first story to use for the newsletter.")

    body = StreamField(DefaultBlocks())
    panels = Campaign.panels + [
        FieldPanel("headline"),
        FieldPanel("newsletter_date"),
        FieldPanel("newsletter_receiver"),
        ImageChooserPanel("header_background"),
        FieldPanel("newsletter_introduction"),
        FieldPanel("newsletter_first_story"),
        ImageChooserPanel("second_story_image"),
        FieldPanel("newsletter_second_story"),
        FieldPanel("newsletter_third_story"),
    ]