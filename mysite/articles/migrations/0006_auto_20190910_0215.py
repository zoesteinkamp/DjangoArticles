# Generated by Django 2.2.5 on 2019-09-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20190910_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='beta3y',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='change_amount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='closepriceamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='currentpriceamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='dailyrange_minimumamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='earningspershareamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='fiftytwoweek_maximumamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='fiftytwoweek_minimumamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='marketcapchangeamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='openpriceamount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='pricetoearningsratio',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='revenue_growth',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='year1ForwardEPSEstimateAmount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='year2ForwardEPSEstimateAmount',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
    ]