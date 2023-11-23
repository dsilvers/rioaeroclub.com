# Generated by Django 3.1.8 on 2021-04-19 17:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('content', '0002_homepageimages_button_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='PancakePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_text', models.CharField(blank=True, max_length=250)),
                ('hero_subtext', models.CharField(blank=True, max_length=250)),
                ('event_details_column1', wagtail.fields.RichTextField(blank=True)),
                ('event_details_column2', wagtail.fields.RichTextField(blank=True)),
                ('event_details_column3', wagtail.fields.RichTextField(blank=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PancakeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('pancake_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='pancake_images', to='content.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
