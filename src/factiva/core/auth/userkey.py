"""Factiva Core UserKey Class."""
import json
from factiva.helper import load_environment_value, mask_string, api_send_request
from factiva.core import const


class UserKey:  # TODO: Create a DJUserBase class that defines root properties for all user types, and inherit here.
    """Class that represents an API user. This entity is identifiable by a User Key.

    Parameters
    ----------
    key : str
        String containing the 32-character long APi Key. If not provided, the
        constructor will try to obtain its value from the FACTIVA_USERKEY
        environment variable.
    stats : boolean, optional (Default: False)
        Indicates if user data has to be pulled from the server. This operation
        fills account detail properties along with maximum, used and remaining
        values. It may take several seconds to complete.

    Examples
    --------
    Creating a new UserKey instance providing the key string explicitly and requesting to retrieve the latest account details:
        >>> u = UserKey('abcd1234abcd1234abcd1234abcd1234', stats=True)
        >>> print(u)
            <class 'factiva.core.userkey.UserKey'>
            |-key = ****************************1234
            |-cloud_token = **Not Fetched**
            |-account_name = AccName1234
            |-account_type = account_with_contract_limits
            |-active_products = DNA
            |-max_allowed_concurrent_extractions = 5
            |-max_allowed_extracted_documents = 200,000
            |-max_allowed_extractions = 3
            |-currently_running_extractions = 0
            |-total_downloaded_bytes = 7,253,890
            |-total_extracted_documents = 2,515
            |-total_extractions = 1
            |-total_stream_instances = 4
            |-total_stream_subscriptions = 1
            |-enabled_company_identifiers = [{'id': 4, 'name': 'isin'}, {'id': 3, 'name': 'cusip'}, {'id': 1, 'name': 'sedol'}, {'id': 5, 'name': 'ticker_exchange'}]
            |-remaining_documents = 197,485
            |-remaining_extractions = 2

    Creating a new instance taking the key value from the environment varaible FACTIVA_USERKEY, and not requesting account statistics (default).
        >>> u = UserKey()
        >>> print(u)
            <class 'factiva.core.userkey.UserKey'>
            |-key = ****************************1234
            |-cloud_token = **Not Fetched**
            |-account_name =
            |-account_type =
            |-active_products =
            |-max_allowed_concurrent_extractions = 0
            |-max_allowed_extracted_documents = 0
            |-max_allowed_extractions = 0
            |-currently_running_extractions = 0
            |-total_downloaded_bytes = 0
            |-total_extracted_documents = 0
            |-total_extractions = 0
            |-total_stream_instances = 0
            |-total_stream_subscriptions = 0
            |-enabled_company_identifiers = []
            |-remaining_documents = 0
            |-remaining_extractions = 0

    """
    # pylint: disable=too-many-instance-attributes
    # Twelve is reasonable in this case.

    __API_ENDPOINT_BASEURL = f'{const.API_HOST}{const.API_ACCOUNT_BASEPATH}/'
    __API_CLOUD_TOKEN_URL = f'{const.API_HOST}{const.API_ACCOUNT_STREAM_CREDENTIALS_BASEPATH}'

    key = ''
    cloud_token = {}
    account_name = ''
    account_type = ''
    active_products = ''
    max_allowed_concurrent_extractions = 0
    max_allowed_extracted_documents = 0
    max_allowed_extractions = 0
    currently_running_extractions = 0
    total_downloaded_bytes = 0
    total_extracted_documents = 0
    total_extractions = 0
    total_stream_instances = 0
    total_stream_subscriptions = 0
    enabled_company_identifiers = []

    def __init__(
        self,
        key=None,
        stats=False
    ):
        """Construct the instance of the class."""
        if key is None:
            try:
                key = load_environment_value('FACTIVA_USERKEY')
            except Exception:
                raise ValueError('Factiva user key not provided and environment variable FACTIVA_USERKEY not set.')

        if len(key) != 32:
            raise ValueError('Factiva User-Key has the wrong length')

        self.key = key
        self.cloud_token = {}

        if stats is True:
            self.get_stats()
        else:
            self.account_name = ''
            self.account_type = ''
            self.active_products = ''
            self.max_allowed_concurrent_extractions = 0
            self.max_allowed_extracted_documents = 0
            self.max_allowed_extractions = 0
            self.currently_running_extractions = 0
            self.total_downloaded_bytes = 0
            self.total_extracted_documents = 0
            self.total_extractions = 0
            self.total_stream_instances = 0
            self.total_stream_subscriptions = 0
            self.enabled_company_identifiers = []

    @property
    def remaining_extractions(self):
        """Account remaining extractions."""
        return self.max_allowed_extractions - self.total_extractions

    @property
    def remaining_documents(self):
        """Account remaining documents."""
        return self.max_allowed_extracted_documents - self.total_extracted_documents

    # [MB] TODO: Please move this method to factiva-news/snapshot/snapshot.py
    # The number of extractions is OK under this class for account management
    # information (get_info), but the extraction list belongs to the Snapshot class.
    # def get_extractions(self) -> pd.DataFrame:
    #     """Request a list of the extractions of the account.

    #     Returns
    #     -------
    #     Dataframe containing the information about the account extractions

    #     Raises
    #     ------
    #     - ValueError when the API Key provided is not valid
    #     - RuntimeError when the API returns an unexpected error

    #     """
    #     endpoint = f'{const.API_HOST}{const.API_EXTRACTIONS_BASEPATH}'

    #     headers_dict = {'user-key': self.key}

    #     response = api_send_request(method='GET', endpoint_url=endpoint, headers=headers_dict)

    #     if response.status_code != 200:
    #         if response.status_code == 403:
    #             raise ValueError('Factiva API-Key does not exist or inactive.')

    #         raise RuntimeError(f'Unexpected API Error with message: {response.text}')

    #     response_data = response.json()

    #     extraction_list = [flatten_dict(extraction) for extraction in response_data['data']]

    #     return pd.DataFrame(extraction_list)

    def get_stats(self) -> bool:
        """Request the account details to the Factiva Account API Endpoint.

        This operation can take several seconds to complete.

        Returns
        -------
        True if the operation was completed successfully. All returned values
        are assigned to the object's properties directly.

        Examples
        --------
        >>> u = UserKey('abcd1234abcd1234abcd1234abcd1234')
        >>> print(u)
            <class 'factiva.core.userkey.UserKey'>
            |-key = ****************************1234
            |-cloud_token = **Not Fetched**
            |-account_name =
            |-account_type =
            |-active_products =
            |-max_allowed_concurrent_extractions = 0
            |-max_allowed_extracted_documents = 0
            |-max_allowed_extractions = 0
            |-currently_running_extractions = 0
            |-total_downloaded_bytes = 0
            |-total_extracted_documents = 0
            |-total_extractions = 0
            |-total_stream_instances = 0
            |-total_stream_subscriptions = 0
            |-enabled_company_identifiers = []
            |-remaining_documents = 0
            |-remaining_extractions = 0
        >>> u.get_stats()
        >>> print(u)
            <class 'factiva.core.userkey.UserKey'>
            |-key = ****************************1234
            |-cloud_token = **Not Fetched**
            |-account_name = AccName1234
            |-account_type = account_with_contract_limits
            |-active_products = DNA
            |-max_allowed_concurrent_extractions = 5
            |-max_allowed_extracted_documents = 200,000
            |-max_allowed_extractions = 3
            |-currently_running_extractions = 0
            |-total_downloaded_bytes = 7,253,890
            |-total_extracted_documents = 2,515
            |-total_extractions = 1
            |-total_stream_instances = 4
            |-total_stream_subscriptions = 1
            |-enabled_company_identifiers = [{'id': 4, 'name': 'isin'}, {'id': 3, 'name': 'cusip'}, {'id': 1, 'name': 'sedol'}, {'id': 5, 'name': 'ticker_exchange'}]
            |-remaining_documents = 197,485
            |-remaining_extractions = 2

        """
        account_endpoint = f'{self.__API_ENDPOINT_BASEURL}{self.key}'
        req_head = {'user-key': self.key}
        resp = api_send_request(method='GET', endpoint_url=account_endpoint, headers=req_head)
        # resp = requests.get(account_endpoint, headers=req_head)  # TODO: Remove if OK
        if resp.status_code == 200:
            try:
                resp_obj = eval(resp.text)
                self.account_name = resp_obj['data']['attributes']['name']
                self.account_type = resp_obj['data']['type']
                self.active_products = resp_obj['data']['attributes']['products']
                self.max_allowed_concurrent_extractions = resp_obj['data']['attributes']['max_allowed_concurrent_extracts']
                self.max_allowed_extracted_documents = resp_obj['data']['attributes']['max_allowed_document_extracts']
                self.max_allowed_extractions = resp_obj['data']['attributes']['max_allowed_extracts']
                self.currently_running_extractions = resp_obj['data']['attributes']['cnt_curr_ext']
                self.total_downloaded_bytes = resp_obj['data']['attributes']['current_downloaded_amount']
                self.total_extracted_documents = resp_obj['data']['attributes']['tot_document_extracts']
                self.total_extractions = resp_obj['data']['attributes']['tot_extracts']
                self.total_stream_instances = resp_obj['data']['attributes']['tot_topics']
                self.total_stream_subscriptions = resp_obj['data']['attributes']['tot_subscriptions']
                self.enabled_company_identifiers = resp_obj['data']['attributes']['enabled_company_identifiers']
            except Exception:
                raise AttributeError('Unexpected Account Information API Response.')
        elif resp.status_code == 403:
            raise ValueError('Factiva User-Key does not exist or inactive.')
        else:
            raise RuntimeError('Unexpected Account Information API Error')
        return True

    def get_cloud_token(self) -> bool:
        """
        Request a cloud token to the API and saves its value
        in the cloud_token property

        Returns
        -------
        True if the operation was completed successfully. Returned value
        is assigned to the cloud_token property.

        Raises
        ------
        ValueError: When the credentials are not valid
        RuntimeError: When API request returns unexpected error

        """
        req_head = {'user-key': self.key}
        response = api_send_request(
            method="GET",
            endpoint_url=f'{self.__API_CLOUD_TOKEN_URL}',
            headers=req_head
        )

        if response.status_code == 401:
            message = '''
                Extraction API authentication failed for given
                credentials header:{}
                '''.format(req_head)
            raise RuntimeError(message)
        try:
            # TODO: Keys without cloud credentials fail at this point. Need to imporove
            #       exception handling and message.
            streaming_credentials_string = response.json()['data']['attributes']['streaming_credentials']
        except TypeError:
            raise ValueError(
                '''
                Unable to get a cloud token for the given key. This account might have limited access.
                '''
            )

        self.cloud_token = json.loads(streaming_credentials_string)
        return True

    def __print_property__(self, property_value) -> str:
        if type(property_value) == int:
            pval = f'{property_value:,d}'
        else:
            pval = property_value
        return pval

    def __repr__(self):
        """Return a string representation of the object."""
        return self.__str__()

    def __str__(self, detailed=True, prefix='  |-', root_prefix=''):
        # TODO: Improve the output for enabled_company_identifiers
        pprop = self.__dict__.copy()
        del pprop['key']
        del pprop['cloud_token']
        masked_key = mask_string(self.key)
        if self.cloud_token == {}:
            masked_token = '**Not Fetched**'
        else:
            masked_token = mask_string(self.cloud_token['private_key'][58:92], 12)

        ret_val = f'{root_prefix}{str(self.__class__)}\n'
        ret_val += f'{prefix}key = {masked_key}\n'
        ret_val += f'{prefix}cloud_token = {masked_token}\n'
        if detailed:
            ret_val += '\n'.join((f'{prefix}{item} = {self.__print_property__(pprop[item])}' for item in pprop))
            ret_val += f'\n{prefix}remaining_documents = {self.__print_property__(self.remaining_documents)}\n'
            ret_val += f'{prefix}remaining_extractions = {self.__print_property__(self.remaining_extractions)}\n'
        else:
            ret_val += f'{prefix}...'
        return ret_val

    @staticmethod
    def create_user_key(key=None, stats=False):
        """Determine the way to initialize an api key user according to the type of parameter provided.

        Parameters
        ----------
        api_user : None, str, UserKey
                Source to create a UserKey instance
        stats : boolean, optional (Default: False)
                Indicates if user data has to be pulled from the server

        Returns
        -------
        UserKey instance accordingly:
            - When None is passed, UserKey instance using credentials from ENV variables
            - When str is passed, UserKey instance using the provided parameter as credentials
            - When UserKey is passed, it returns the same instance

        Raises
        ------
            RuntimeError: When an UserKey instance cannot be created using the provided parameters

        """
        if isinstance(key, UserKey):
            return key

        if isinstance(key, str):
            try:
                return UserKey(key, stats=stats)
            except Exception:
                raise RuntimeError("User cannot be obtained from the provided key.")

        if key is None:
            try:
                return UserKey(stats=stats)
            except Exception:
                raise RuntimeError("User cannot be obtained from ENV variables")

        raise RuntimeError("Unexpected api_user value")
