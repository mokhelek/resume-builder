# Generated by Django 4.1.2 on 2022-11-03 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_app', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('project_thumbnail', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('project_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='personal_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(default='No profile', on_delete=django.db.models.deletion.CASCADE, to='profiles_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_description', models.TextField()),
                ('company_name', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='companies')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('profile', models.ForeignKey(default='No profile', on_delete=django.db.models.deletion.CASCADE, to='profiles_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('qualification_name', models.CharField(max_length=200)),
                ('education_description', models.TextField()),
                ('profile', models.ForeignKey(default='No profile', on_delete=django.db.models.deletion.CASCADE, to='profiles_app.profile')),
            ],
        ),
    ]