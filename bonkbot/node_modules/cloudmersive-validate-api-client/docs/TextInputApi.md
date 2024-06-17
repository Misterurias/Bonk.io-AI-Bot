# CloudmersiveValidateApiClient.TextInputApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**textInputCheckHtmlSsrf**](TextInputApi.md#textInputCheckHtmlSsrf) | **POST** /validate/text-input/html/check/ssrf | Protect html input from Server-side Request Forgery (SSRF) attacks
[**textInputCheckSqlInjection**](TextInputApi.md#textInputCheckSqlInjection) | **POST** /validate/text-input/check/sql-injection | Check text input for SQL Injection (SQLI) attacks
[**textInputCheckSqlInjectionBatch**](TextInputApi.md#textInputCheckSqlInjectionBatch) | **POST** /validate/text-input/check/sql-injection/batch | Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch
[**textInputCheckXss**](TextInputApi.md#textInputCheckXss) | **POST** /validate/text-input/check/xss | Check text input for Cross-Site-Scripting (XSS) attacks
[**textInputCheckXssBatch**](TextInputApi.md#textInputCheckXssBatch) | **POST** /validate/text-input/check-and-protect/xss/batch | Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch
[**textInputCheckXxe**](TextInputApi.md#textInputCheckXxe) | **POST** /validate/text-input/check/xxe | Protect text input from XML External Entity (XXE) attacks
[**textInputCheckXxeBatch**](TextInputApi.md#textInputCheckXxeBatch) | **POST** /validate/text-input/check/xxe/batch | Protect text input from XML External Entity (XXE) attacks
[**textInputProtectXss**](TextInputApi.md#textInputProtectXss) | **POST** /validate/text-input/protect/xss | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization


<a name="textInputCheckHtmlSsrf"></a>
# **textInputCheckHtmlSsrf**
> HtmlSsrfDetectionResult textInputCheckHtmlSsrf(value, opts)

Protect html input from Server-side Request Forgery (SSRF) attacks

Detects SSRF (Server-side request forgery) attacks and unsafe URL attacks from HTML text input, where attackers can attempt to access unsafe local or network paths in the server environment by injecting them into HTML.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = "value_example"; // String | User-facing HTML input.

var opts = { 
  'allowCidScheme': true // Boolean | Optional: Set to true to allow cid: scheme URLs for email message attachments.  Default is false.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckHtmlSsrf(value, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**| User-facing HTML input. | 
 **allowCidScheme** | **Boolean**| Optional: Set to true to allow cid: scheme URLs for email message attachments.  Default is false. | [optional] 

### Return type

[**HtmlSsrfDetectionResult**](HtmlSsrfDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckSqlInjection"></a>
# **textInputCheckSqlInjection**
> SqlInjectionDetectionResult textInputCheckSqlInjection(value, opts)

Check text input for SQL Injection (SQLI) attacks

Detects SQL Injection (SQLI) attacks from text input.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = "value_example"; // String | User-facing text input.

var opts = { 
  'detectionLevel': "detectionLevel_example" // String | Set to Normal to target a high-security SQL Injection detection level with a very low false positive rate; select High to target a very-high security SQL Injection detection level with higher false positives.  Default is Normal (recommended).
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckSqlInjection(value, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**| User-facing text input. | 
 **detectionLevel** | **String**| Set to Normal to target a high-security SQL Injection detection level with a very low false positive rate; select High to target a very-high security SQL Injection detection level with higher false positives.  Default is Normal (recommended). | [optional] 

### Return type

[**SqlInjectionDetectionResult**](SqlInjectionDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckSqlInjectionBatch"></a>
# **textInputCheckSqlInjectionBatch**
> SqlInjectionCheckBatchResponse textInputCheckSqlInjectionBatch(value)

Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch

Detects SQL Injection (SQLI) attacks from multiple text inputs.  Output preverses order of input items.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = new CloudmersiveValidateApiClient.SqlInjectionCheckBatchRequest(); // SqlInjectionCheckBatchRequest | User-facing text input.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckSqlInjectionBatch(value, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**SqlInjectionCheckBatchRequest**](SqlInjectionCheckBatchRequest.md)| User-facing text input. | 

### Return type

[**SqlInjectionCheckBatchResponse**](SqlInjectionCheckBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckXss"></a>
# **textInputCheckXss**
> XssProtectionResult textInputCheckXss(value)

Check text input for Cross-Site-Scripting (XSS) attacks

Detects XSS (Cross-Site-Scripting) attacks from text input.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = "value_example"; // String | User-facing text input.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckXss(value, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**| User-facing text input. | 

### Return type

[**XssProtectionResult**](XssProtectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckXssBatch"></a>
# **textInputCheckXssBatch**
> XssProtectionBatchResponse textInputCheckXssBatch(value)

Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch

Detects XSS (Cross-Site-Scripting) attacks from multiple text inputs.  Output preverses order of input items.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = new CloudmersiveValidateApiClient.XssProtectionBatchRequest(); // XssProtectionBatchRequest | User-facing text input.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckXssBatch(value, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**XssProtectionBatchRequest**](XssProtectionBatchRequest.md)| User-facing text input. | 

### Return type

[**XssProtectionBatchResponse**](XssProtectionBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckXxe"></a>
# **textInputCheckXxe**
> XxeDetectionResult textInputCheckXxe(value, opts)

Protect text input from XML External Entity (XXE) attacks

Detects XXE (XML External Entity) attacks from text input.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = "value_example"; // String | User-facing text input.

var opts = { 
  'allowInternetUrls': true, // Boolean | Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false.
  'knownSafeUrls': "knownSafeUrls_example", // String | Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe.
  'knownUnsafeUrls': "knownUnsafeUrls_example" // String | Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckXxe(value, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**| User-facing text input. | 
 **allowInternetUrls** | **Boolean**| Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false. | [optional] 
 **knownSafeUrls** | **String**| Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe. | [optional] 
 **knownUnsafeUrls** | **String**| Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe. | [optional] 

### Return type

[**XxeDetectionResult**](XxeDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputCheckXxeBatch"></a>
# **textInputCheckXxeBatch**
> XxeDetectionBatchResponse textInputCheckXxeBatch(request)

Protect text input from XML External Entity (XXE) attacks

Detects XXE (XML External Entity) attacks from text input.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var request = new CloudmersiveValidateApiClient.XxeDetectionBatchRequest(); // XxeDetectionBatchRequest | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputCheckXxeBatch(request, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**XxeDetectionBatchRequest**](XxeDetectionBatchRequest.md)|  | 

### Return type

[**XxeDetectionBatchResponse**](XxeDetectionBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="textInputProtectXss"></a>
# **textInputProtectXss**
> XssProtectionResult textInputProtectXss(value)

Protect text input from Cross-Site-Scripting (XSS) attacks through normalization

Detects and removes XSS (Cross-Site-Scripting) attacks from text input through normalization.  Returns the normalized result, as well as information on whether the original input contained an XSS risk.

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.TextInputApi();

var value = "value_example"; // String | User-facing text input.


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.textInputProtectXss(value, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **String**| User-facing text input. | 

### Return type

[**XssProtectionResult**](XssProtectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

