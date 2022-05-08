from email.policy import default
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField, StreamField
# from wagtail_embed_videos import get_embed_video_model_string
# from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, StreamFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel
from wagtail.search import index
from wagtailcaptcha.models import WagtailCaptchaEmailForm

# Home Page
class HomePage(Page):
    page_title = models.CharField(max_length=255, blank=True, null=True)
    current_need = RichTextField(blank=True, null=True)
    current_need_link=models.CharField(max_length=255, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('page_title', help_text="This is the title of the page"),
        FieldPanel('current_need', help_text="This is the current need"),
        FieldPanel('current_need_link', help_text="This is the current need link"),
        InlinePanel('carousel_items', label="Home Page Images", max_num=10, min_num=1, help_text="This is the home page carousel section"),
        InlinePanel('cards', label="Home Page Sections", max_num=3, min_num=1, help_text="This is the home page cards section"),
    ]

class HomePageCarousel(Orderable):
    page = ParentalKey('HomePage', related_name='carousel_items')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    image_title = models.CharField(blank=True, max_length=255)
    image_intro = RichTextField(blank=True, null=True)
    image_link = models.CharField(blank=True, max_length=255)
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('image_title'),
        FieldPanel('image_intro'),
        FieldPanel('image_link'),
    ]
class HomePageCards(Orderable):
    page = ParentalKey('HomePage', related_name='cards')
    title = models.CharField(blank=True, max_length=255)
    intro = RichTextField(blank=True, null=True)
    icon_class = models.CharField(blank=True, max_length=255)
    panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        FieldPanel('icon_class'),
    ] 
    # Discipleship Page
class DiscipleshipPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    featured_image_title= models.CharField(blank=True, max_length=255)
    brief_intro = models.CharField(blank=True, max_length=750)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('featured_image_title', help_text="This is the title of the page or Image"),
        FieldPanel('brief_intro', help_text="This is the title of the page"),
        InlinePanel('cards', label="Discipleship Page Sections", max_num=3, min_num=1, help_text="This is the discipleship page cards section"),
    ]
    
class DiscipleshipPageCards(Orderable):
    page = ParentalKey('DiscipleshipPage', related_name='cards')
    title = models.CharField(blank=True, max_length=255)
    intro = RichTextField(blank=True, null=True)
    icon_class = models.CharField(blank=True, max_length=255)
    card_lead = models.CharField(blank=True, max_length=255)
    panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        FieldPanel('icon_class'),
        FieldPanel('card_lead'),
    ]
    # Education Page
class EducationPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    featured_image_title= models.CharField(blank=True, max_length=255)
    brief_intro = models.CharField(blank=True, max_length=750)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('featured_image_title', help_text="This is the title of the page or Image"),
        FieldPanel('brief_intro', help_text="This is the title of the page"),
        InlinePanel('cards', label="Education Page Sections", max_num=3, min_num=1, help_text="This is the discipleship page cards section"),
    ]
class EducationPageCards(Orderable):
    page = ParentalKey('EducationPage', related_name='cards')
    title = models.CharField(blank=True, max_length=255)
    intro = RichTextField(blank=True, null=True)
    icon_class = models.CharField(blank=True, max_length=255)
    card_lead = models.CharField(blank=True, max_length=255)
    panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        FieldPanel('icon_class'),
        FieldPanel('card_lead'),
    ]
# Skilling Page
class SkillingPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    featured_image_title= models.CharField(blank=True, max_length=255)
    brief_intro = models.CharField(blank=True, max_length=750)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('featured_image_title', help_text="This is the title of the page or Image"),
        FieldPanel('brief_intro', help_text="This is the title of the page"),
        InlinePanel('cards', label="Skilling Page Sections", max_num=3, min_num=1, help_text="This is the discipleship page cards section"),
    ]
class SkillingPageCards(Orderable):
    page = ParentalKey('SkillingPage', related_name='cards')
    title = models.CharField(blank=True, max_length=255)
    intro = RichTextField(blank=True, null=True)
    icon_class = models.CharField(blank=True, max_length=255)
    card_lead = models.CharField(blank=True, max_length=255)
    panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        FieldPanel('icon_class'),
        FieldPanel('card_lead'),
    ]

# Crisis Page
class CrisisPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    featured_image_title= models.CharField(blank=True, max_length=255)
    brief_intro = models.CharField(blank=True, max_length=750)
    side_image= models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('featured_image_title', help_text="This is the title of the page or Image"),
        FieldPanel('brief_intro', help_text="This is the title of the page"),
        ImageChooserPanel('side_image'),
        FieldPanel('body', help_text="This is the body of the page"),
        InlinePanel('faqs', label="Crisis Page Sections", max_num=3, min_num=1, help_text="This is the discipleship page cards section"),
    ]
class CrisisPageFAQS(Orderable):
    page = ParentalKey('CrisisPage',on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(blank=True, max_length=255)
    answer = models.CharField(blank=True, max_length=255)
    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
    ]
    
# Contact Page
class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True, null=True)
    thank_you_message = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', help_text="This is the title of the page"),
        InlinePanel('form_fields', label="Contact form Sections", help_text="This is the contact page form section"),
        FieldPanel('thank_you_message', help_text="This is the title of the page"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
        
    ]
class ContactPageFormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')

class ParticipagePage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    bg_design_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    intro = models.CharField(blank=True, null=True,max_length=750)
    tours_image_1 = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    tours_image_2 = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    tours_image_3 = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    tours_text = RichTextField(blank=True, null=True)
    missions_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    missions_text = RichTextField(blank=True, null=True)
    support_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    support_text = RichTextField(blank=True, null=True)
    gap_year_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    gap_year_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        ImageChooserPanel('bg_design_image'),
        FieldPanel('intro', help_text="This is the introduction of the page"),
        ImageChooserPanel('tours_image_1'),
        ImageChooserPanel('tours_image_2'),
        ImageChooserPanel('tours_image_3'),
        FieldPanel('tours_text', help_text="This is the text about the tours and safaris"),
        ImageChooserPanel('missions_image'),
        FieldPanel('missions_text', help_text="This is the text about the missions"),
        ImageChooserPanel('support_image'),
        FieldPanel('support_text', help_text="This is the text about the support"),
        ImageChooserPanel('gap_year_image'),
        FieldPanel('gap_year_text', help_text="This is the text about the gap year"),
    ]

class PrivacyPage(Page):
    intro = models.CharField(blank=True, null=True,max_length=750)
    Body = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', help_text="This is the introduction of the page"),
        FieldPanel('Body', help_text="This is the body of the page"),
    ]

class TermsPage(Page):
    intro = models.CharField(blank=True, null=True,max_length=750)
    Body = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', help_text="This is the introduction of the page"),
        FieldPanel('Body', help_text="This is the body of the page"),
    ]
