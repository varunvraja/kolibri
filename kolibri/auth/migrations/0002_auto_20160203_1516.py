# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kolibriauth', '0001_initial_squashed_0002_baseuser__is_device_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HierarchyNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('kind_id', models.IntegerField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='kolibriauth.HierarchyNode')),
            ],
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('_node', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.HierarchyNode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='_node',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.HierarchyNode'),
        ),
        migrations.AlterIndexTogether(
            name='hierarchynode',
            index_together=set([('kind', 'kind_id')]),
        ),
    ]
