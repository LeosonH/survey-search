# Generated by Django 2.0.2 on 2018-03-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyDetails',
            fields=[
                ('survey_num', models.IntegerField(db_column='survey_num', primary_key=True, serialize=False)),
                ('survey_key', models.CharField(db_column='survey_key', max_length=500)),
                ('survey_name', models.CharField(db_column='survey_name', max_length=1000)),
                ('num_participants', models.IntegerField(db_column='num_participants')),
                ('org_conduct', models.CharField(db_column='org_conduct', max_length=1000)),
                ('num_questions', models.IntegerField(db_column='num_questions')),
                ('data_link', models.CharField(db_column='data_link', max_length=1000)),
                ('doc_link', models.CharField(db_column='doc_link', max_length=1000)),
                ('source_link', models.CharField(db_column='source_link', max_length=1000)),
                ('summary', models.CharField(db_column='summary', max_length=3000)),
                ('survey_questions_document', models.FileField(db_column='document', upload_to='documents/')),
            ],
            options={
                'db_table': 'survey_details_new',
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestions',
            fields=[
                ('row_num', models.IntegerField(db_column='row_num', primary_key=True, serialize=False)),
                ('survey_key', models.CharField(db_column='survey_key', max_length=500)),
                ('var_name', models.CharField(db_column='var_name', max_length=200)),
                ('var_text', models.CharField(db_column='var_text', max_length=1000)),
            ],
            options={
                'db_table': 'survey_questions',
            },
        ),
    ]
