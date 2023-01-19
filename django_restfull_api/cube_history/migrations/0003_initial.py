# Generated by Django 4.1.5 on 2023-01-19 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=100)),
                ('create_date', models.CharField(max_length=100)),
                ('cube_type', models.CharField(max_length=100)),
                ('item_upgrade_result', models.CharField(max_length=100)),
                ('miracle_time_flag', models.CharField(max_length=100)),
                ('item_equip_part', models.CharField(max_length=100)),
                ('item_level', models.CharField(max_length=100)),
                ('target_item', models.CharField(max_length=100)),
                ('potential_option_grade', models.CharField(max_length=100)),
                ('additional_potential_option_grade', models.CharField(max_length=100)),
                ('before_potential_options_grade_1', models.CharField(max_length=100)),
                ('before_potential_options_value_1', models.CharField(max_length=100)),
                ('before_potential_options_grade_2', models.CharField(max_length=100)),
                ('before_potential_options_value_2', models.CharField(max_length=100)),
                ('before_potential_options_grade_3', models.CharField(max_length=100)),
                ('before_potential_options_value_3', models.CharField(max_length=100)),
                ('after_potential_options_grade_1', models.CharField(max_length=100)),
                ('after_potential_options_value_1', models.CharField(max_length=100)),
                ('after_potential_options_grade_2', models.CharField(max_length=100)),
                ('after_potential_options_value_2', models.CharField(max_length=100)),
                ('after_potential_options_grade_3', models.CharField(max_length=100)),
                ('after_potential_options_value_3', models.CharField(max_length=100)),
            ],
        ),
    ]