# Generated by Django 4.0.5 on 2022-06-26 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='questionary',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_questionary', to='testing_api.questionary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_answer', to='testing_api.answer'),
        ),
    ]