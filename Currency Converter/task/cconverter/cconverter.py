# write your code here!
import requests
import json
# amount = float(input())
currency_1 = str(input()).lower()
# rate = float(input('Please, enter the exchange rate:'))
# rates_dic = {'RUB':2.98, 'ARS':0.82, 'HNL':0.17, 'AUD':1.9622, 'MAD':0.208}
r = requests.get(f'http://www.floatrates.com/daily/{currency_1.upper()}.json')
dict_from_json = r.json()
cache_dict = {}
if currency_1 != 'usd':
    cache_dict['usd'] = dict_from_json['usd']
if currency_1 != 'eur':
    cache_dict['eur'] = dict_from_json['eur']
currency_2 = str(input()).lower()
while currency_2 not in ' ':
    amount = float(input())
    print('Checking the cache...')
    if currency_2 in cache_dict.keys():
        print('Oh! It is in the cache!')
        conversion = round((amount * cache_dict[currency_2]['rate']), 2)
        print('You received', conversion, currency_2.upper())
    else:
        print('Sorry, but it is not in the cache!')
        cache_dict[currency_2] = dict_from_json[currency_2]
        conversion = round((amount * cache_dict[currency_2]['rate']), 2)
        print('You received', conversion, currency_2.upper())
    currency_2 = str(input()).lower()
# rate_usd = dict_from_json['usd']['rate']
# rate_eur = dict_from_json['eur']['rate']
# print(dict_from_json['usd'])
# print(dict_from_json['eur'])
# for sym, rate in rates_dic.items():
#     conversion = round(amount * rate, 2)
#     print(f'I will get {conversion} {sym} from the sale of {amount} conicoins.')