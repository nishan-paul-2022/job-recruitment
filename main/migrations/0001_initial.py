# Generated by Django 3.2.6 on 2021-12-25 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_username', models.TextField()),
                ('username', models.TextField()),
                ('company_picture', models.TextField()),
                ('company_name', models.TextField()),
                ('company_category', models.TextField()),
                ('company_location', models.TextField()),
                ('company_tagline', models.TextField()),
                ('company_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_company_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('freelancer_picture', models.TextField()),
                ('freelancer_name', models.TextField()),
                ('freelancer_type', models.TextField()),
                ('freelancer_phone', models.TextField()),
                ('freelancer_salary', models.TextField()),
                ('freelancer_skills', models.TextField()),
                ('freelancer_tagline', models.TextField()),
                ('freelancer_nationality', models.TextField()),
                ('freelancer_description', models.TextField()),
                ('freelancer_stats_company', models.TextField()),
                ('freelancer_stats_job', models.TextField()),
                ('freelancer_stats_job_offers', models.TextField()),
                ('freelancer_stats_job_proposals', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_username', models.TextField()),
                ('username', models.TextField()),
                ('company_username', models.TextField()),
                ('job_picture', models.TextField()),
                ('job_timebegin', models.TextField()),
                ('job_timeend', models.TextField()),
                ('job_title', models.TextField()),
                ('job_location', models.TextField()),
                ('job_type', models.TextField()),
                ('job_category', models.TextField()),
                ('job_salary', models.TextField()),
                ('job_postion', models.TextField()),
                ('job_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_job_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_job_offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('job_username', models.TextField()),
                ('job_offers_email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_job_proposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('job_username', models.TextField()),
                ('job_proposals_cv', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Models_nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.TextField()),
            ],
        ),
    ]