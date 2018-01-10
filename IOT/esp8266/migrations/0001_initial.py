# Generated by Django 2.0 on 2018-01-05 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('y', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_create_user_fk', to=settings.AUTH_USER_MODEL)),
                ('updatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_update_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('sal_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('updatedTime', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sal_create_user_fk', to=settings.AUTH_USER_MODEL)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sal_emp_id_fk', to='esp8266.Employee')),
                ('updatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sal_update_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]