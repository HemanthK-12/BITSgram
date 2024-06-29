# Generated by Django 5.0.3 on 2024-04-20 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0002_auto_20240420_1841'),
    ]

    operations = [
         migrations.RunSQL("""
            CREATE TRIGGER update_email_trigger
            BEFORE UPDATE ON user
            FOR EACH ROW
            BEGIN
             DECLARE email_pattern VARCHAR(255);
             SET email_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    
              IF NEW.email NOT REGEXP email_pattern THEN
                SET NEW.email = 'dash';  -- Set email to 'dash' if it's invalid
             END IF;
            END;
        """)
    ]