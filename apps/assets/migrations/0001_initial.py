# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('username', models.CharField(max_length=16, verbose_name='Username')),
                ('_password', models.CharField(blank=True, max_length=256, verbose_name='Password')),
                ('_private_key', models.CharField(blank=True, max_length=4096, verbose_name='SSH private key')),
                ('_public_key', models.CharField(blank=True, max_length=4096, verbose_name='SSH public key')),
                ('as_default', models.BooleanField(default=False, verbose_name='As default')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('date_created', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=32, null=True, verbose_name='Created by')),
            ],
            options={
                'db_table': 'admin_user',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('other_ip', models.CharField(blank=True, max_length=255, null=True, verbose_name='Other IP')),
                ('remote_card_ip', models.CharField(blank=True, max_length=16, null=True, verbose_name='Remote card IP')),
                ('hostname', models.CharField(blank=True, max_length=128, verbose_name='Hostname')),
                ('port', models.IntegerField(default=22, verbose_name='Port')),
                ('mac_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mac address')),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='Brand')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=128, null=True, verbose_name='Memory')),
                ('disk', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Disk')),
                ('os', models.CharField(blank=True, max_length=128, null=True, verbose_name='OS')),
                ('cabinet_no', models.CharField(blank=True, max_length=32, null=True, verbose_name='Cabinet number')),
                ('cabinet_pos', models.IntegerField(blank=True, null=True, verbose_name='Cabinet position')),
                ('number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Asset number')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='Serial number')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now=True, null=True, verbose_name='Date added')),
                ('comment', models.TextField(blank=True, max_length=128, null=True, verbose_name='Comment')),
                ('admin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assets.AdminUser', verbose_name='Admin user')),
            ],
            options={
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='AssetExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='KEY')),
                ('value', models.CharField(max_length=64, verbose_name='VALUE')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'db_table': 'asset_extend',
            },
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now=True, null=True, verbose_name='Date added')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'db_table': 'asset_group',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('bandwidth', models.CharField(blank=True, max_length=32, verbose_name='Bandwidth')),
                ('contact', models.CharField(blank=True, max_length=16, verbose_name='Contact')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Address')),
                ('intranet', models.TextField(blank=True, verbose_name='Intranet')),
                ('extranet', models.TextField(blank=True, verbose_name='Extranet')),
                ('date_created', models.DateTimeField(auto_now=True, null=True, verbose_name='Date added')),
                ('operator', models.CharField(blank=True, max_length=32, verbose_name='Operator')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'db_table': 'idc',
            },
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('username', models.CharField(max_length=16, verbose_name='Username')),
                ('_password', models.CharField(blank=True, max_length=256, verbose_name='Password')),
                ('protocol', models.CharField(choices=[('ssh', 'ssh')], default='ssh', max_length=16, verbose_name='Protocol')),
                ('_private_key', models.CharField(blank=True, max_length=4096, verbose_name='SSH private key')),
                ('_public_key', models.CharField(blank=True, max_length=4096, verbose_name='SSH public key')),
                ('as_default', models.BooleanField(default=False, verbose_name='As default')),
                ('auto_push', models.BooleanField(default=True, verbose_name='Auto push')),
                ('auto_update', models.BooleanField(default=True, verbose_name='Auto update pass/key')),
                ('sudo', models.TextField(default='/user/bin/whoami', max_length=4096, verbose_name='Sudo')),
                ('shell', models.CharField(default='/bin/bash', max_length=64, verbose_name='Shell')),
                ('home', models.CharField(blank=True, max_length=64, verbose_name='Home')),
                ('uid', models.IntegerField(blank=True, null=True, verbose_name='Uid')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='Created by')),
                ('comment', models.TextField(blank=True, max_length=128, verbose_name='Comment')),
            ],
            options={
                'db_table': 'system_user',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64, verbose_name='VALUE')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='assets.Asset', verbose_name='Asset')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='assetgroup',
            name='system_users',
            field=models.ManyToManyField(blank=True, related_name='asset_groups', to='assets.SystemUser'),
        ),
        migrations.AlterUniqueTogether(
            name='assetextend',
            unique_together=set([('key', 'value')]),
        ),
        migrations.AddField(
            model_name='asset',
            name='env',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='env_asset', to='assets.AssetExtend', verbose_name='Asset environment'),
        ),
        migrations.AddField(
            model_name='asset',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='assets', to='assets.AssetGroup', verbose_name='Asset groups'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assets.IDC', verbose_name='IDC'),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_asset', to='assets.AssetExtend', verbose_name='Asset status'),
        ),
        migrations.AddField(
            model_name='asset',
            name='system_users',
            field=models.ManyToManyField(blank=True, related_name='assets', to='assets.SystemUser', verbose_name='System User'),
        ),
        migrations.AddField(
            model_name='asset',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_asset', to='assets.AssetExtend', verbose_name='Asset type'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('value', 'asset')]),
        ),
        migrations.AlterUniqueTogether(
            name='asset',
            unique_together=set([('ip', 'port')]),
        ),
    ]