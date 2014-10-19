from osv import osv,fields
import urllib2 as u
import string
import simplejson as json

class res_currency_rate(osv.osv):
	_name = "res.currency.rate"
	_inherit = "res.currency.rate"
	
	def currency_schedule_update(self,cr,uid,context=None):

		url = 'http://api.bluelytics.com.ar/json/last_price'
		f = u.urlopen(url)
		data = f.read()
		data_json = json.loads(data)

		rate = data_json[3]['value_buy']

	        currency_obj = self.pool.get('res.currency')
	        currency_rate_obj = self.pool.get('res.currency.rate')
                currency_id = currency_obj.search(cr, uid, [('name', '=', 'USD')])
		print "Actualizacion USD"
		if not currency_id:
			print "No esta cargado el peso argentino"
		else:
			values = {
				'rate': 1/rate,
				'currency_id': currency_id[0],
				'currency_type_id': ''
				}
			currency_rate_obj.create(cr,uid,values)

		return True
	
res_currency_rate()
