# Generated by Django 4.0.5 on 2022-06-27 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing_api', '0002_useranswer_questionary_alter_useranswer_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useranswer',
            options={'ordering': ('pk',), 'verbose_name': 'Ответы пользователя', 'verbose_name_plural': 'Ответы пользователей'},
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='questionary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_questionary', to='testing_api.questionary', verbose_name='Вопросник'),
        ),
    ]
