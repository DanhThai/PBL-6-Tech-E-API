# Generated by Django 4.1.3 on 2022-12-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tech_ecommerce', '0001_initial'),
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(blank=True, default=0)),
                ('order_count', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='authenticate.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PayIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_time', models.DateTimeField(blank=True, null=True)),
                ('number_money', models.FloatField(blank=True, default=0)),
                ('status_payment', models.BooleanField(blank=True, default=False)),
                ('type_payment', models.CharField(choices=[('online', 'online'), ('offline', 'offline')], max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_in', to='order_payment.order')),
            ],
        ),
        migrations.CreateModel(
            name='PayOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(blank=True, default=0)),
                ('account', models.CharField(max_length=14)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_out', to='authenticate.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('money', models.FloatField()),
                ('pay_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='order_payment.payin')),
                ('pay_out', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='order_payment.payout')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('price', models.FloatField(blank=True, default=0)),
                ('total_price', models.FloatField(blank=True, default=0)),
                ('discount', models.FloatField(blank=True, default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='order_payment.order')),
                ('product_child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='tech_ecommerce.productchilds')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='authenticate.seller')),
            ],
        ),
    ]
