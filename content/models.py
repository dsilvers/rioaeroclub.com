from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable


"""
HOME PAGE
"""


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('home_images', label="Home images"),
    ]


class HomePageImages(Orderable):
    content_page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='home_images',
    )

    headline = models.CharField(max_length=250, blank=True)
    blurb = models.CharField(max_length=250, blank=True)
    button_text = models.CharField(max_length=250, blank=True)
    alignment_class = models.CharField(max_length=250, default="text-left")

    button_link = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="home_image_button_link",
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('headline'),
        FieldPanel('blurb'),
        FieldPanel('button_text'),
        FieldPanel('button_link'),
        FieldPanel('alignment_class'),
        FieldPanel('image'),
    ]


"""

PANCAKES

"""


class PancakePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    hero_text = models.CharField(max_length=250, blank=True)
    hero_subtext = models.CharField(max_length=250, blank=True)

    event_details_column1 = RichTextField(blank=True)
    event_details_column2 = RichTextField(blank=True)
    event_details_column3 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('hero_text'),
        FieldPanel('hero_subtext'),
        FieldPanel('event_details_column1'),
        FieldPanel('event_details_column2'),
        FieldPanel('event_details_column3'),
        InlinePanel('pancake_images', label="Pancake images"),
    ]


class PancakeImage(Orderable):
    pancake_page = ParentalKey(
        PancakePage,
        on_delete=models.CASCADE,
        related_name='pancake_images',
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]


"""

MEMBERSHIP

"""


class MembershipPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('membership_faq', label="Membership FAQ"),
    ]


class MembershipFAQ(Orderable):
    membership_page = ParentalKey(
        MembershipPage,
        on_delete=models.CASCADE,
        related_name='membership_faq',
    )

    question = models.CharField(max_length=250, blank=True)
    answer = RichTextField(blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('image'),
    ]


"""

AIRCRAFT


"""


class AircraftPage(Page):
    aircraft_details = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('aircraft_details'),
        InlinePanel('aircraft_images', label="Aircraft Images"),
    ]


class AircraftImage(Orderable):
    page = ParentalKey(
        AircraftPage,
        on_delete=models.CASCADE,
        related_name='aircraft_images',
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image'),
    ]


"""
AIRPORT CAMERAS
"""


class AirportPage(Page):
    airport_detail = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('airport_detail'),
        InlinePanel('cameras', label="Camera IDs"),
    ]


class Camera(Orderable):
    page = ParentalKey(
        AirportPage,
        on_delete=models.CASCADE,
        related_name='cameras',
    )

    camera_id = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('camera_id'),
    ]
