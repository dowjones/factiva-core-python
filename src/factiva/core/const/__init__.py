"""Define library's constant literals."""
# from factiva.core.const.errors import *

API_HOST = 'https://api.dowjones.com'
API_ACCOUNT_OAUTH2_HOST = 'https://accounts.dowjones.com/oauth2/v1/token'

# UserKey
API_ACCOUNT_BASEPATH = '/alpha/accounts'
API_ACCOUNT_STREAM_CREDENTIALS_BASEPATH = '/alpha/accounts/streaming-credentials'

# Dynamic Prefixes
ALPHA_BASEPATH = '/alpha'
DNA_BASEPATH = '/dna'  # Deprecated

# Snapshots
API_SNAPSHOTS_BASEPATH = '/alpha/extractions/documents'
API_EXPLAIN_SUFFIX = '/_explain'
API_ANALYTICS_BASEPATH = '/alpha/analytics'
API_EXTRACTIONS_BASEPATH = '/alpha/extractions'

API_SNAPSHOTS_TAXONOMY_BASEPATH = '/alpha/taxonomies'
API_SNAPSHOTS_COMPANIES_BASEPATH = '/alpha/companies'
API_SNAPSHOTS_COMPANY_IDENTIFIERS_BASEPATH = '/alpha/companies/identifiers'

# ANALYTICS
API_AVRO_FORMAT = 'avro'
API_CSV_FORMAT = 'csv'
API_JSON_FORMAT = 'json'
API_EXTRACTION_FILE_FORMATS = [API_AVRO_FORMAT, API_JSON_FORMAT, API_CSV_FORMAT]

API_DAY_PERIOD = 'DAY'
API_MONTH_PERIOD = 'MONTH'
API_YEAR_PERIOD = 'YEAR'
API_DATETIME_PERIODS = [API_DAY_PERIOD, API_MONTH_PERIOD, API_YEAR_PERIOD]

API_PUBLICATION_DATETIME_FIELD = 'publication_datetime'
API_MODIFICATION_DATETIME_FIELD = 'modification_datetime'
API_INGESTION_DATETIME_FIELD = 'ingestion_datetime'
API_DATETIME_FIELDS = [API_PUBLICATION_DATETIME_FIELD, API_MODIFICATION_DATETIME_FIELD, API_INGESTION_DATETIME_FIELD]

# Streams
API_STREAMS_BASEPATH = '/alpha/streams'
DOC_COUNT_EXCEEDED = "DOC_COUNT_EXCEEDED"
CHECK_EXCEEDED_WAIT_SPACING = 300
PUBSUB_MESSAGES_WAIT_SPACING = 10

# API STATES
API_JOB_CREATED_STATE = 'JOB_CREATED'
API_JOB_QUEUED_STATE = 'JOB_QUEUED'
API_JOB_PENDING_STATE = 'JOB_STATE_PENDING'
API_JOB_VALIDATING_STATE = 'JOB_VALIDATING'
API_JOB_STATE_VALIDATING = 'JOB_STATE_VALIDATING'
API_JOB_RUNNING_STATE = 'JOB_STATE_RUNNING'
API_JOB_DONE_STATE = 'JOB_STATE_DONE'
API_JOB_FAILED_STATE = 'JOB_STATE_FAILED'
API_JOB_CANCELLED_STATE = 'JOB_STATE_CANCELLED'

API_JOB_EXPECTED_STATES = [API_JOB_CREATED_STATE, API_JOB_QUEUED_STATE, API_JOB_PENDING_STATE,
                           API_JOB_VALIDATING_STATE,
                           API_JOB_STATE_VALIDATING, API_JOB_RUNNING_STATE, API_JOB_DONE_STATE, API_JOB_FAILED_STATE,
                           API_JOB_CANCELLED_STATE]

API_JOB_ACTIVE_WAIT_SPACING = 10

# SNAPSHOT FILES
SNAPSHOT_FILE_STATS_FIELDS = ['an', 'company_codes', 'company_codes_about',
    'company_codes_occur', 'industry_codes', 'ingestion_datetime',
    'language_code', 'modification_datetime',
    'publication_datetime',
    'publisher_name', 'region_codes', 'region_of_origin',
    'source_code', 'source_name',
    'subject_codes', 'title', 'word_count']

SNAPSHOT_FILE_DELETE_FIELDS = ['art', 'credit', 'document_type',
    'publication_date', 'modfication_date'] # publication_date and modification_date are deprecated
