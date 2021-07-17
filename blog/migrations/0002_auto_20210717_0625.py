# Generated by Django 3.2.5 on 2021-07-17 06:25

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('star', models.PositiveIntegerField(default=0)),
                ('topbanner', models.ImageField(blank=True, null=True, upload_to=blog.models.get_topbanner_filename)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=blog.models.get_image_filename, verbose_name='Image')),
                ('blog', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myimage', models.ImageField(blank=True, default='user_image_noimg/jobs.jpg', null=True, upload_to=blog.models.get_user_image_filename)),
                ('author', models.OneToOneField(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('author', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='commentreply',
            name='usrimg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.userimage'),
        ),
        migrations.AddField(
            model_name='commentreply',
            name='whichcomment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='usrimg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.userimage'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.hashtag'),
        ),
    ]