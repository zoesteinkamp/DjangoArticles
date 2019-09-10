# Generated by Django 2.2.5 on 2019-09-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190910_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='ask_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='beta3y',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='bid_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='change_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='closepriceamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='currentpriceamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='dailyrange_maximumamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='dailyrange_minimumamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='dividend_yield',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='earningspershareamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='fiftytwoweek_maximumamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='fiftytwoweek_minimumamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='gross_margin',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='marketcapamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='marketcapchangeamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='openpriceamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='percent_change',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='percentofsharestraded',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='pricetoearningsratio',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='revenue_growth',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='year1ForwardEPSEstimateAmount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='year2ForwardEPSEstimateAmount',
            field=models.FloatField(),
        ),
    ]
