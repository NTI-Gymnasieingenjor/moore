# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 11:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Section', verbose_name='Member of section'),
        ),
        migrations.AlterField(
            model_name='member',
            name='person_number_ext',
            field=models.CharField(blank=True, default='', help_text='Enter the last four digits of your Swedish person number, given by the Swedish tax authority', max_length=4, unique_for_date='birthday', validators=[django.core.validators.RegexValidator(message='The person number extension consists of four numbers', regex='^\\d{4}$')], verbose_name='Person number extension'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, default='', help_text='Enter a phone number so UTN may reach you', max_length=20, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number', regex='^\\+?\\d+$')], verbose_name='Phone number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='registration_year',
            field=models.CharField(blank=True, default='', help_text='Enter the year you started studying at the TakNat faculty', max_length=4, validators=[django.core.validators.RegexValidator(message='Please enter a valid year', regex='^\\d{4}$')], verbose_name='Registration year'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='abbreviation',
            field=models.CharField(blank=True, default='', help_text='Enter the abbreviation for the section', max_length=130, verbose_name='Section abbreviation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studyprogram',
            name='abbreviation_en',
            field=models.CharField(blank=True, default='', help_text='Enter the abbreviation for the study program', max_length=130, verbose_name='English program abbreviation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studyprogram',
            name='abbreviation_sv',
            field=models.CharField(blank=True, default='', help_text='Enter the abbreviation for the study program', max_length=130, verbose_name='Swedish program abbreviation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studyprogram',
            name='degree',
            field=models.CharField(blank=True, choices=[('bsc', 'Bachelor of Science'), ('msc', 'Master of Science'), ('be', 'Bachelor of Engineering'), ('msceng', 'Master of Science in Engineering')], max_length=20, verbose_name='Degree type'),
        ),
    ]
