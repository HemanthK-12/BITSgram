# Generated by Django 5.0.3 on 2024-04-20 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0004_auto_20240420_1858'),
    ]

    operations = [
        migrations.RunSQL("""
        CREATE TRIGGER update_hash_password_trigger1
        BEFORE UPDATE ON user
        FOR EACH ROW
        BEGIN
              SET NEW.passwordhash = SHA2(NEW.passwordhash, 256);
        END;
        """)
    ]