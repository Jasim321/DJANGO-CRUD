# Generated by Django 3.2.5 on 2021-09-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('adminId', models.AutoField(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=30)),
                ('lName', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=50)),
                ('menuId', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='chef',
            fields=[
                ('chefId', models.AutoField(primary_key=True, serialize=False)),
                ('lName', models.CharField(max_length=30)),
                ('fName', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=30)),
                ('phoneNumber', models.TextField(max_length=30)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('phoneNo', models.TextField(max_length=30)),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('payementId', models.TextField(max_length=50)),
                ('foodId', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('foodId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.TextField(max_length=30)),
                ('unitPrice', models.TextField(max_length=30)),
                ('itemCategory', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuId', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.TextField(max_length=30)),
                ('startDate', models.TextField(max_length=30)),
                ('endDate', models.TextField(max_length=30)),
                ('foodId', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderDate', models.TextField(max_length=30)),
                ('customerId', models.TextField(max_length=30)),
                ('quantity', models.TextField(max_length=30)),
                ('pickUpDate', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('foodId', models.TextField(max_length=25)),
                ('quantity', models.TextField(max_length=25)),
                ('unitPrice', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('paymentId', models.AutoField(primary_key=True, serialize=False)),
                ('customerId', models.TextField(max_length=30)),
                ('orderId', models.TextField(max_length=50)),
                ('paymentDate', models.TextField(max_length=50)),
                ('amount', models.TextField(max_length=30)),
                ('paymentType', models.CharField(max_length=30)),
            ],
        ),
    ]
