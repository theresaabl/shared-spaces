# Generated by Django 4.2.18 on 2025-01-31 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_eventspacebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.IntegerField(choices=[(0, 'Submit a maintenance request'), (1, 'Message the community administrators')], default=0)),
                ('urgent', models.BooleanField()),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Open'), (1, 'In Progress'), (2, 'Closed')], default=0)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resident_requests_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
