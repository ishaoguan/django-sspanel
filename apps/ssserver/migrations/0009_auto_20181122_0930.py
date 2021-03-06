# Generated by Django 2.1.3 on 2018-11-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssserver', '0008_auto_20181009_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='country',
            field=models.CharField(choices=[('US', '美国'), ('CN', '中国'), ('TW', '台湾'), ('HK', '香港'), ('JP', '日本'), ('FR', '法国'), ('DE', '德国'), ('KR', '韩国'), ('JE', '泽西岛'), ('NZ', '新西兰'), ('MX', '墨西哥'), ('CA', '加拿大'), ('BR', '巴西'), ('CU', '古巴'), ('CZ', '捷克'), ('EG', '埃及'), ('FI', '芬兰'), ('GR', '希腊'), ('GU', '关岛'), ('IS', '冰岛'), ('MO', '澳门'), ('NL', '荷兰'), ('NO', '挪威'), ('PL', '波兰'), ('IT', '意大利'), ('IE', '爱尔兰'), ('AR', '阿根廷'), ('PT', '葡萄牙'), ('AU', '澳大利亚'), ('RU', '俄罗斯联邦'), ('CF', '中非共和国')], default='CN', max_length=2, verbose_name='国家'),
        ),
    ]
