# CloudmersiveValidateApiClient.DateTimeApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dateTimeGetNowSimple**](DateTimeApi.md#dateTimeGetNowSimple) | **GET** /validate/date-time/get/now | Get current date and time as of now
[**dateTimeGetPublicHolidays**](DateTimeApi.md#dateTimeGetPublicHolidays) | **POST** /validate/date-time/get/holidays | Get public holidays in the specified country and year
[**dateTimeParseNaturalLanguageDateTime**](DateTimeApi.md#dateTimeParseNaturalLanguageDateTime) | **POST** /validate/date-time/parse/date-time/natural-language | Parses a free-form natural language date and time string into a date and time
[**dateTimeParseStandardDateTime**](DateTimeApi.md#dateTimeParseStandardDateTime) | **POST** /validate/date-time/parse/date-time/structured | Parses a standardized date and time string into a date and time


<a name="dateTimeGetNowSimple"></a>
# **dateTimeGetNowSimple**
> DateTimeNowResult dateTimeGetNowSimple()

Get current date and time as of now

Gets the current date and time.  Response time is syncronized with atomic clocks, and represents a monotonic, centrally available, consistent clock.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.DateTimeApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.dateTimeGetNowSimple(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DateTimeNowResult**](DateTimeNowResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="dateTimeGetPublicHolidays"></a>
# **dateTimeGetPublicHolidays**
> PublicHolidaysResponse dateTimeGetPublicHolidays(input)

Get public holidays in the specified country and year

Enumerates all public holidays in a given country for a given year.  Supports over 100 countries.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.DateTimeApi();

var input = new CloudmersiveValidateApiClient.GetPublicHolidaysRequest(); // GetPublicHolidaysRequest | Input request


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.dateTimeGetPublicHolidays(input, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetPublicHolidaysRequest**](GetPublicHolidaysRequest.md)| Input request | 

### Return type

[**PublicHolidaysResponse**](PublicHolidaysResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="dateTimeParseNaturalLanguageDateTime"></a>
# **dateTimeParseNaturalLanguageDateTime**
> DateTimeStandardizedParseResponse dateTimeParseNaturalLanguageDateTime(input)

Parses a free-form natural language date and time string into a date and time

Parses an unstructured, free-form, natural language date and time string into a date time object.  This is intended for lightweight human-entered input, such as \&quot;tomorrow at 3pm\&quot; or \&quot;tuesday\&quot;.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.DateTimeApi();

var input = new CloudmersiveValidateApiClient.DateTimeNaturalLanguageParseRequest(); // DateTimeNaturalLanguageParseRequest | Input request


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.dateTimeParseNaturalLanguageDateTime(input, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DateTimeNaturalLanguageParseRequest**](DateTimeNaturalLanguageParseRequest.md)| Input request | 

### Return type

[**DateTimeStandardizedParseResponse**](DateTimeStandardizedParseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="dateTimeParseStandardDateTime"></a>
# **dateTimeParseStandardDateTime**
> DateTimeStandardizedParseResponse dateTimeParseStandardDateTime(input)

Parses a standardized date and time string into a date and time

Parses a structured date and time string into a date time object.  This is intended for standardized date strings that adhere to formatting conventions, rather than natural language input.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.DateTimeApi();

var input = new CloudmersiveValidateApiClient.DateTimeStandardizedParseRequest(); // DateTimeStandardizedParseRequest | Input request


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.dateTimeParseStandardDateTime(input, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DateTimeStandardizedParseRequest**](DateTimeStandardizedParseRequest.md)| Input request | 

### Return type

[**DateTimeStandardizedParseResponse**](DateTimeStandardizedParseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

