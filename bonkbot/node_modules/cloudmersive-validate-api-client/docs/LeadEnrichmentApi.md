# CloudmersiveValidateApiClient.LeadEnrichmentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leadEnrichmentEnrichLead**](LeadEnrichmentApi.md#leadEnrichmentEnrichLead) | **POST** /validate/lead-enrichment/lead/enrich | Enrich an input lead with additional fields of data
[**leadEnrichmentGetCompanyInformation**](LeadEnrichmentApi.md#leadEnrichmentGetCompanyInformation) | **POST** /validate/lead-enrichment/lead/email/company-information | Get company information from email address


<a name="leadEnrichmentEnrichLead"></a>
# **leadEnrichmentEnrichLead**
> LeadEnrichmentResponse leadEnrichmentEnrichLead(request)

Enrich an input lead with additional fields of data

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.LeadEnrichmentApi();

var request = new CloudmersiveValidateApiClient.LeadEnrichmentRequest(); // LeadEnrichmentRequest | Input lead with known fields set, and unknown fields left blank (null)


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.leadEnrichmentEnrichLead(request, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LeadEnrichmentRequest**](LeadEnrichmentRequest.md)| Input lead with known fields set, and unknown fields left blank (null) | 

### Return type

[**LeadEnrichmentResponse**](LeadEnrichmentResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

<a name="leadEnrichmentGetCompanyInformation"></a>
# **leadEnrichmentGetCompanyInformation**
> LeadEnrichmentResponse leadEnrichmentGetCompanyInformation(request)

Get company information from email address

### Example
```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');
var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix = 'Token';

var apiInstance = new CloudmersiveValidateApiClient.LeadEnrichmentApi();

var request = new CloudmersiveValidateApiClient.EmailLead(); // EmailLead | Input email address lead


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.leadEnrichmentGetCompanyInformation(request, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailLead**](EmailLead.md)| Input email address lead | 

### Return type

[**LeadEnrichmentResponse**](LeadEnrichmentResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

