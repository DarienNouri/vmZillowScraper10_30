import json
from csv import DictWriter
from furl import furl

url_current = 'https://www.zillow.com/new-york-ny/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.49741171289062%2C%22east%22%3A-73.46195028710937%2C%22south%22%3A40.32354617219259%2C%22north%22%3A41.07006558882081%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A1000000%7D%2C%22mp%22%3A%7B%22min%22%3A5026%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'


class DecodeUrl:
    def __init__(self, starturl=None):
        self.start_url = starturl

    def decode_url(self):
        url = furl(self.start_url)
        args = dict(url.args)
        for key, value in args.items():
            if value.startswith('{'):
                args[key] = json.loads(value)
        return args

    def get_url_filters(self, decoded_url, price=None):

        enter = decoded_url['searchQueryState']

        if price is not None:

            val = {'min': price}
        else:
            val = enter['filterState']['price']

        filter_dict = [{
            'map_bounds': enter['mapBounds'],
            'region_selector': enter['regionSelection']},
            {

                'price_min': val,
                'sort_value': enter['filterState']['sort']
            }]

        return filter_dict

    def set_url_filters(self,input_filters):
        with open('args.json') as f:
            args = json.load(f)

            args['searchQueryState']['mapBounds'] = input_filters[0]['map_bounds']
            args['searchQueryState']['regionSelection'] = input_filters[0]['region_selector'][0]
            args['searchQueryState']['filterState']['price'] = input_filters[1]['price_min']
            args['searchQueryState']['filterState']['sort'] = input_filters[1]['sort_value']

            '''
            for key, val in input_filters[0].items():


                args['searchQueryState'][key] = val
            for key, val in input_filters[1].items():

                args['searchQueryState']['filterState'][key] = val

            '''

            args['searchQueryState']['requestId'] = str(1)
            args['searchQueryState']['pagination'] = {'currentPage': 1}
        return args

    def generate_url(self,filters, page_num):


        filters['searchQueryState']['requestId'] = str(page_num)
        filters['searchQueryState']['pagination'] = {'currentPage': page_num}
        url = 'https://www.zillow.com/search/GetSearchPageState.htm?'
        # serialize in their format
        for k, v in filters.items():
            s_args = str(v)
            s_args = s_args.replace(' ', '')
            v = f'{k}={s_args}&'
            url += v
        return url


