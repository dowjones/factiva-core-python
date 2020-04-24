import requests
from factiva.helper import load_environment_value, mask_string
from factiva.core import const


class APIKeyUser(object):  # TODO: Create a DJUserBase class that defines root properties for all user types, and inherit here.
    """
    Class that represents an API user. This entity is identifiable by an API-Key.
    Parameters
    ----------
    api_key : string that contains the 32-character long APi Key\n
    request_info : boolean that indicates if user data has to be pulled from the server
    See Also
    --------
    UserOAuth: API user that follows the OAuth guidelines.
    Examples
    --------
    Creating a new API user.
    aku = APIKeyUser('abcd1234abcd1234abcd1234abcd1234')
    aku
        <class 'factiva.core.apikeyuser.APIKeyUser'>
          api_key = ****************************1234
          account_name = Demo Account
          account_type = account_with_limits
          active_products = Snapshots
          max_allowed_concurrent_extractions = 2
          max_allowed_extracted_documents = 100000
          max_allowed_extractions = 10
          total_downloaded_bytes = 12345678
          total_extracted_documents = 5500
          total_extractions = 2
          total_stream_subscriptions = 2
          total_stream_topics = 1
          remaining_documents = 94500
          remaining_extractions = 8
    """

    __API_ENDPOINT_BASEURL = f'{const.DJ_API_HOST}{const.DJ_API_ACCOUNT_BASEPATH}/'

    api_key = ''
    account_name = ''
    account_type = ''
    active_products = ''
    max_allowed_concurrent_extractions = 0
    max_allowed_extracted_documents = 0
    max_allowed_extractions = 0
    total_downloaded_bytes = 0
    total_extracted_documents = 0
    total_extractions = 0
    total_stream_subscriptions = 0
    total_stream_topics = 0

    def __init__(
        self,
        api_key=None,
        request_info=False
    ):
        if api_key is None:
            try:
                api_key = load_environment_value('FACTIVA_APIKEY')
            except Exception:
                raise ValueError('Factiva API-Key not provided and environment variable FACTIVA_APIKEY not set.')

        if len(api_key) != 32:
            raise ValueError('Factiva API-Key has the wrong length')

        self.api_key = api_key

        if request_info is True:
            self.get_info()
        else:
            self.account_name = ''
            self.account_type = ''
            self.active_products = ''
            self.max_allowed_concurrent_extractions = 0
            self.max_allowed_extracted_documents = 0
            self.max_allowed_extractions = 0
            self.total_downloaded_bytes = 0
            self.total_extracted_documents = 0
            self.total_extractions = 0
            self.total_stream_subscriptions = 0
            self.total_stream_topics = 0

    @property
    def remaining_extractions(self):
        return self.max_allowed_extractions - self.total_extractions

    @property
    def remaining_documents(self):
        return self.max_allowed_extracted_documents - self.total_extracted_documents

    def get_info(self):
        account_endpoint = f'{self.__API_ENDPOINT_BASEURL}{self.api_key}'
        req_head = {'user-key': self.api_key}
        resp = requests.get(account_endpoint, headers=req_head)  # TODO: Consider processing all GET/POST requests in a separate class/module
        if(resp.status_code == 200):
            try:
                resp_obj = eval(resp.text)
                self.account_name = resp_obj['data']['attributes']['name']
                self.account_type = resp_obj['data']['type']
                self.active_products = resp_obj['data']['attributes']['products']
                self.max_allowed_concurrent_extractions = resp_obj['data']['attributes']['max_allowed_concurrent_extracts']
                self.max_allowed_extracted_documents = resp_obj['data']['attributes']['max_allowed_document_extracts']
                self.max_allowed_extractions = resp_obj['data']['attributes']['max_allowed_extracts']
                self.total_downloaded_bytes = resp_obj['data']['attributes']['current_downloaded_amount']
                self.total_extracted_documents = resp_obj['data']['attributes']['tot_document_extracts']
                self.total_extractions = resp_obj['data']['attributes']['tot_extracts']
                self.total_stream_subscriptions = resp_obj['data']['attributes']['tot_subscriptions']
                self.total_stream_topics = resp_obj['data']['attributes']['tot_topics']
            except Exception:
                raise AttributeError('Unexpected Account Information API Response.')
        elif(resp.status_code == 403):
            raise ValueError('Factiva API-Key does not exist or inactive.')
        else:
            raise RuntimeError('Unexpected Account Information API Error')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        pprop = self.__dict__.copy()
        del pprop['api_key']
        masked_key = mask_string(self.__dict__['api_key'])

        ret_val = str(self.__class__) + '\n'
        ret_val += f'  api_key = {masked_key}\n'
        ret_val += '\n'.join(('  {} = {}'.format(item, pprop[item]) for item in pprop))
        ret_val += f'\n  remaining_documents = {self.remaining_documents}\n'
        ret_val += f'  remaining_extractions = {self.remaining_extractions}\n'
        return ret_val
