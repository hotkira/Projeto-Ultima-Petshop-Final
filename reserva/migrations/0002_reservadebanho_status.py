# Generated by Django 4.2.6 on 2023-11-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservadebanho',
            name='status',
            field=models.CharField(choices=[('agendado', 'Agendado'), ('cancelado', 'Cancelado'), ('concluido', 'Concluído')], default='agendado', editable=False, max_length=20, verbose_name='Status'),
        ),
    ]