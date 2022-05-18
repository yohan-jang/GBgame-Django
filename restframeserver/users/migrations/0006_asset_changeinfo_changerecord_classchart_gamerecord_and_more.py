# Generated by Django 4.0.4 on 2022-05-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_users_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('mail', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cash', models.IntegerField(blank=True, null=True)),
                ('money', models.IntegerField(blank=True, null=True)),
                ('user_num', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'asset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Changeinfo',
            fields=[
                ('change_num', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.CharField(blank=True, max_length=20, null=True)),
                ('prior_rank', models.CharField(blank=True, max_length=10, null=True)),
                ('next_rank', models.CharField(blank=True, max_length=10, null=True)),
                ('prior_money', models.IntegerField(blank=True, null=True)),
                ('next_money', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('avg_rank', models.IntegerField(blank=True, null=True)),
                ('user_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'changeinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ChangeRecord',
            fields=[
                ('change_num', models.IntegerField(primary_key=True, serialize=False)),
                ('user_num', models.IntegerField(blank=True, null=True)),
                ('cash_amount', models.IntegerField(blank=True, null=True)),
                ('change_type', models.CharField(blank=True, max_length=45, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'change_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassChart',
            fields=[
                ('class_name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('max_point', models.IntegerField(blank=True, null=True)),
                ('min_point', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_chart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('user_num1', models.IntegerField(primary_key=True, serialize=False)),
                ('user_num2', models.IntegerField()),
                ('user_num3', models.IntegerField()),
                ('user_num4', models.IntegerField()),
                ('user_num5', models.IntegerField()),
                ('user_num6', models.IntegerField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('avg_rank', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'game_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JoinRecord',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_num', models.IntegerField(blank=True, null=True)),
                ('ip', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'join_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_num', models.IntegerField(primary_key=True, serialize=False)),
                ('user_num', models.IntegerField(blank=True, null=True)),
                ('item_id', models.IntegerField(blank=True, null=True)),
                ('orderdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('mail', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tier', models.CharField(blank=True, max_length=10, null=True)),
                ('rankpoint', models.IntegerField(blank=True, null=True)),
                ('user_num', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('product_num', models.IntegerField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(blank=True, max_length=20, null=True)),
                ('product_name', models.CharField(blank=True, max_length=20, null=True)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_detail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'shop',
                'managed': False,
            },
        ),
    ]
