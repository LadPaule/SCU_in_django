from email.policy import default
from django.db import models
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField, StreamField
# from wagtail_embed_videos import get_embed_video_model_string
# from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, StreamFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index


from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmedia.edit_handlers import MediaChooserPanel
from wagtail.search import index
from wagtailcaptcha.models import WagtailCaptchaEmailForm

class SponsorListingPage(RoutablePageMixin, Page):
    page_title = models.CharField(max_length=255, blank=True, null=True)
    introduction=RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('page_title', help_text="This is the title of the page"),
        FieldPanel('introduction', help_text="This is the introduction of the page"),  
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        #@TODO: Handling Pagination
        all_sponsored_pages = SponsorPage.objects.live().public().order_by('-last_published_at')

        paginator = Paginator(all_sponsored_pages, 4) #@TODO: paginate change integer to 8 per page
        page = request.GET.get('page')
        try:
            sponsored_pages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            sponsored_pages = paginator.page(1)    
        except EmptyPage:  
            # If page is out of range (e.g. 9999), deliver last page of results.
            sponsored_pages = paginator.page(paginator.num_pages)
        context["sponsored_pages"] = sponsored_pages

        return context

class SponsorPage(RoutablePageMixin, Page):
    child_photo = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    child_name = models.CharField(blank=True, max_length=255)
    child_DOB = models.CharField(blank=True, max_length=255, default="unknown")
    child_story = RichTextField(blank=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('child_name', partial_match=True, boost=10),
        index.SearchField('child_DOB', partial_match=True),
        index.SearchField('child_story', partial_match=True),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('child_photo'),
        FieldPanel('child_name'),
        FieldPanel('child_DOB'),
        FieldPanel('child_story'),
    ]

    @route(r"^search/$")
    def search(self, request, *args, **kwargs):
        search_query = request.GET.get("q", None)
        self.sponsored_pages = self.get_sponsored_pages().objects.live().autocomplete("child_name", search_query)
        if search_query:
            self.sponsored_pages = self.sponsored_pages.search(search_query)
        return self.render(request)

class AboutPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_caption = models.CharField(max_length=1000, blank=True, null=True)
    side_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    introduction=RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('image_title'),
        FieldPanel('image_caption'),
        ImageChooserPanel('side_image'),
        FieldPanel('introduction'),
        InlinePanel('strategies', label="Organizational Strategies"),
    ]
class AboutPageStrategy(Orderable):
    page = ParentalKey('AboutPage', related_name='strategies')
    strategy = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    panels = [
        FieldPanel('strategy'),
        FieldPanel('content'),
        FieldPanel('icon_class'),
    ]
class VolunteerPage(Page):
    featured_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    volunteer_name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=1000, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    linkedIn = models.CharField(max_length=1000, blank=True, null=True)
    mail = models.CharField(max_length=1000, blank=True, null=True)
    introduction=RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('volunteer_name'),
        FieldPanel('designation'),
        FieldPanel('facebook'),
        FieldPanel('linkedIn'),
        FieldPanel('mail'),
        FieldPanel('introduction'),
    ]