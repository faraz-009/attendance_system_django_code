# Generated by Django 4.1.7 on 2023-04-10 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HRM', '0007_alter_leaveandattendancecount_personal_leave_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveandattendancecount',
            old_name='Personal_leave',
            new_name='personal_leave',
        ),
    ]
