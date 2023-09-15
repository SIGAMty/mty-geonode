# Generated by Django 3.2.4 on 2021-09-27 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0039_harvestableresource_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestingsession',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('on-going', 'on-going'), ('finished-all-ok', 'finished-all-ok'), ('finished-all-failed', 'finished-all-failed'), ('finished-some-failed', 'finished-some-failed'), ('aborting', 'aborting'), ('aborted', 'aborted')], default='pending', editable=False, max_length=50),
        ),
        migrations.CreateModel(
            name='AsynchronousHarvestingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_type', models.CharField(choices=[('harvesting', 'harvesting'), ('discover-harvestable-resources', 'discover-harvestable-resources')], editable=False, max_length=50)),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('on-going', 'on-going'), ('finished-all-ok', 'finished-all-ok'), ('finished-all-failed', 'finished-all-failed'), ('finished-some-failed', 'finished-some-failed'), ('aborting', 'aborting'), ('aborted', 'aborted')], default='pending', editable=False, max_length=50)),
                ('details', models.TextField(blank=True)),
                ('total_records_to_process', models.IntegerField(default=0, editable=False, help_text='Number of records being processed in this session')),
                ('records_done', models.IntegerField(default=0, help_text='Number of records that have already been processed')),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='harvesting.harvester')),
            ],
        ),
    ]
