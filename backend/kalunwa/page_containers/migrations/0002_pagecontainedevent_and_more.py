# Generated by Django 4.0.3 on 2022-06-04 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_merge_20220509_2149'),
        ('page_containers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContainedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_order', models.IntegerField()),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='pagecontainedjumbotron',
            name='unique_container_order',
        ),
        migrations.AddConstraint(
            model_name='pagecontainedjumbotron',
            constraint=models.UniqueConstraint(fields=('container', 'section_order'), name='unique_container_order_for_contained_jumbotron'),
        ),
        migrations.AddField(
            model_name='pagecontainedevent',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_containers.pagecontainer'),
        ),
        migrations.AddField(
            model_name='pagecontainedevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.event'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedevent',
            constraint=models.UniqueConstraint(fields=('container', 'event', 'section_order'), name='unique_container_event_order'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedevent',
            constraint=models.UniqueConstraint(fields=('container', 'section_order'), name='unique_container_order_for_contained_event'),
        ),
        migrations.AddConstraint(
            model_name='pagecontainedevent',
            constraint=models.UniqueConstraint(fields=('container', 'event'), name='unique_container_event'),
        ),
    ]
