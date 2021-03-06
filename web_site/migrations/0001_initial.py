# Generated by Django 3.2.6 on 2021-08-14 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('category_name', models.CharField(default=None, max_length=20, unique=True)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('BLOG', 'BLOG'), ('CODEGIST', 'CODEGIST')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CodeGist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coding_platform', models.CharField(choices=[('HACKERRANK', 'HACKERRANK'), ('CODECHEF', 'CODECHEF'), ('LEETCODE', 'LEETCODE')], max_length=30)),
                ('problem_url', models.URLField(default='')),
                ('language', models.CharField(choices=[('C', 'C'), ('PYTHON', 'Python'), ('JAVA', 'Java'), ('JAVASCRIPT', 'Javascript'), ('CPP', 'CPP')], max_length=20)),
                ('analogy', models.CharField(default='', max_length=250)),
                ('code_snippet', models.CharField(default='', max_length=250)),
                ('post_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_site.post')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('content', models.CharField(default=None, max_length=250)),
                ('post_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_site.post')),
            ],
        ),
    ]
