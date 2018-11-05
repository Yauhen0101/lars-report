# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VoiceStarCallLog'
        db.create_table('main_voicestarcalllog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caller_number', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('caller_name', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('call_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('inbound_no', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('inbound_ext', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('forward_no', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('custom_id', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('account_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('group_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('campaign_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('a_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('g_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('c_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('call_s', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('answer_offset', self.gf('django.db.models.fields.IntegerField')()),
            ('call_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('disposition', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('listenedto', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('main', ['VoiceStarCallLog'])


    def backwards(self, orm):
        # Deleting model 'VoiceStarCallLog'
        db.delete_table('main_voicestarcalllog')


    models = {
        'main.account': {
            'Active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'Geo_MetroArea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'unique_together': "(('ServiceType', 'ServiceAccountId'), ('Name', 'ServiceType'))", 'object_name': 'Account'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ServiceAccountId': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'ServiceType': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.clientaccount': {
            'Account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Account']"}),
            'Client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.LarsClient']"}),
            'Meta': {'unique_together': "(('Client', 'Account'),)", 'object_name': 'ClientAccount'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.googleaccountperformancereport': {
            'AccountCurrencyCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'AccountDescriptiveName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'AccountId': ('django.db.models.fields.BigIntegerField', [], {}),
            'AccountTimeZoneId': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'AdNetworkType1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AdNetworkType2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AverageCpc': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'AveragePosition': ('django.db.models.fields.FloatField', [], {}),
            'ClickType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Clicks': ('django.db.models.fields.IntegerField', [], {}),
            'Cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'Ctr': ('django.db.models.fields.FloatField', [], {}),
            'Date': ('django.db.models.fields.DateField', [], {}),
            'Device': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ExternalCustomerId': ('django.db.models.fields.BigIntegerField', [], {}),
            'Impressions': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'unique_together': "(('ExternalCustomerId', 'Date', 'AdNetworkType1', 'AdNetworkType2', 'Device', 'ClickType'),)", 'object_name': 'GoogleAccountPerformanceReport'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.googlecampaignperformancereport': {
            'AccountCurrencyCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'AccountDescriptiveName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'AccountId': ('django.db.models.fields.BigIntegerField', [], {}),
            'AccountTimeZoneId': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'AdNetworkType1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AdNetworkType2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AverageCpc': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'AveragePosition': ('django.db.models.fields.FloatField', [], {}),
            'CampaignId': ('django.db.models.fields.BigIntegerField', [], {}),
            'CampaignName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'CampaignStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ClickType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Clicks': ('django.db.models.fields.IntegerField', [], {}),
            'ConversionRate': ('django.db.models.fields.FloatField', [], {}),
            'Conversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'Cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'CostPerConversion': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'Ctr': ('django.db.models.fields.FloatField', [], {}),
            'Date': ('django.db.models.fields.DateField', [], {}),
            'ExternalCustomerId': ('django.db.models.fields.BigIntegerField', [], {}),
            'Impressions': ('django.db.models.fields.BigIntegerField', [], {}),
            'Meta': {'unique_together': "(('ExternalCustomerId', 'Date', 'CampaignId', 'AdNetworkType1', 'AdNetworkType2', 'ClickType'),)", 'object_name': 'GoogleCampaignPerformanceReport'},
            'TotalConvValue': ('django.db.models.fields.FloatField', [], {}),
            'ValuePerConversion': ('django.db.models.fields.FloatField', [], {}),
            'ViewThroughConversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.googlegeoperformancereport': {
            'AccountCurrencyCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'AccountDescriptiveName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'AccountTimeZoneId': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'AdGroupId': ('django.db.models.fields.BigIntegerField', [], {}),
            'AdGroupName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'AdGroupStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'AdNetworkType1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AdNetworkType2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AverageCpc': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'AveragePosition': ('django.db.models.fields.FloatField', [], {}),
            'CampaignId': ('django.db.models.fields.BigIntegerField', [], {}),
            'CampaignName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'CampaignStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'CityCriteriaId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Clicks': ('django.db.models.fields.IntegerField', [], {}),
            'ConversionRate': ('django.db.models.fields.FloatField', [], {}),
            'Conversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'Cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'CostPerConversion': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'CountryCriteriaId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Ctr': ('django.db.models.fields.FloatField', [], {}),
            'Date': ('django.db.models.fields.DateField', [], {}),
            'Device': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ExternalCustomerId': ('django.db.models.fields.BigIntegerField', [], {}),
            'Impressions': ('django.db.models.fields.BigIntegerField', [], {}),
            'LocationType': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'Meta': {'unique_together': "(('ExternalCustomerId', 'Date', 'AdGroupId', 'LocationType', 'CountryCriteriaId', 'RegionCriteriaId', 'MetroCriteriaId', 'CityCriteriaId', 'AdNetworkType1', 'AdNetworkType2', 'Device'),)", 'object_name': 'GoogleGeoPerformanceReport'},
            'MetroCriteriaId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'RegionCriteriaId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'TotalConvValue': ('django.db.models.fields.FloatField', [], {}),
            'ValuePerConversion': ('django.db.models.fields.FloatField', [], {}),
            'ViewThroughConversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.googlekeywordperformancereport': {
            'AccountCurrencyCode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'AccountDescriptiveName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'AccountTimeZoneId': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'AdGroupId': ('django.db.models.fields.BigIntegerField', [], {}),
            'AdGroupName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'AdGroupStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'AdNetworkType1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AdNetworkType2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'AverageCpc': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'AveragePosition': ('django.db.models.fields.FloatField', [], {}),
            'CampaignId': ('django.db.models.fields.BigIntegerField', [], {}),
            'CampaignName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'CampaignStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ClickType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Clicks': ('django.db.models.fields.IntegerField', [], {}),
            'ConversionRate': ('django.db.models.fields.FloatField', [], {}),
            'Conversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'Cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'CostPerConversion': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'Ctr': ('django.db.models.fields.FloatField', [], {}),
            'Date': ('django.db.models.fields.DateField', [], {}),
            'Device': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ExternalCustomerId': ('django.db.models.fields.BigIntegerField', [], {}),
            'Impressions': ('django.db.models.fields.BigIntegerField', [], {}),
            'KeywordId': ('django.db.models.fields.BigIntegerField', [], {}),
            'KeywordMatchType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'KeywordText': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'unique_together': "(('ExternalCustomerId', 'Date', 'AdGroupId', 'KeywordId', 'AdNetworkType1', 'AdNetworkType2', 'Device', 'ClickType'),)", 'object_name': 'GoogleKeywordPerformanceReport'},
            'TotalConvValue': ('django.db.models.fields.FloatField', [], {}),
            'ValuePerConversion': ('django.db.models.fields.FloatField', [], {}),
            'ViewThroughConversions': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.larsclient': {
            'Budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'BudgetCurrency': ('django.db.models.fields.CharField', [], {'default': "'USD'", 'max_length': '5'}),
            'Meta': {'object_name': 'LarsClient'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.metroarea': {
            'DMACode': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'MetroArea'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.voicestarcalllog': {
            'Meta': {'object_name': 'VoiceStarCallLog'},
            'a_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'account_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'answer_offset': ('django.db.models.fields.IntegerField', [], {}),
            'c_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'call_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'call_s': ('django.db.models.fields.DateTimeField', [], {}),
            'call_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'caller_name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'caller_number': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'campaign_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'custom_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'disposition': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'forward_no': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'g_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inbound_ext': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'inbound_no': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'listenedto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        }
    }

    complete_apps = ['main']