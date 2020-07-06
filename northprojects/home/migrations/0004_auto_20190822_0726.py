# Generated by Django 2.2.4 on 2019-08-22 07:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailforms", "0003_capitalizeverbose"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("home", "0003_auto_20190812_1230"),
    ]

    operations = [
        migrations.AddField(
            model_name="standardpage",
            name="Body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "TwoCol_2",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "col1",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "col2",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "ImgText_3",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "preamble",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "paragraph",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "order",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left Image"),
                                            ("right", "Right Image"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "ImgOnText_4",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", default=""
                                    ),
                                ),
                                (
                                    "preamble",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "Staff_6",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "CImgText_8",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "richtext",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "order",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left Image"),
                                            ("right", "Right Image"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "ImgColorText_9",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "preamble",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "order",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left Image"),
                                            ("right", "Right Image"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "DoubleImgText_10",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image1", wagtail.images.blocks.ImageChooserBlock()),
                                ("image2", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "preamble",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "paragraph",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "order",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left Image"),
                                            ("right", "Right Image"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "USP_12",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "paragraph",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "question1",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "paragraph1",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "question2",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "paragraph2",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "question3",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "paragraph3",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "question4",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "paragraph4",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "order",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Left Image"),
                                            ("right", "Right Image"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="standardpage",
            name="Header",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "Hero",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("hero_img", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "heading",
                                    wagtail.core.blocks.RichTextBlock(
                                        classname="full title", required=False
                                    ),
                                ),
                                (
                                    "paragraph",
                                    wagtail.core.blocks.RichTextBlock(required=False),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.DeleteModel(name="ArticlePage"),
    ]