# cloudmersive-validate-api-client

CloudmersiveValidateApiClient - JavaScript client for cloudmersive-validate-api-client
The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.
[Cloudmersive Validation API](https://www.cloudmersive.com/validate-api) provides data validation capabilities for validating email addresses, phone numbers, IP addresses, and many other types of business data.

- API version: v1
- Package version: 1.4.8


## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install cloudmersive-validate-api-client --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing 
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your cloudmersive-validate-api-client from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('cloudmersive-validate-api-client')` in javascript files from the directory you ran the last 
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CloudmersiveValidateApiClient = require('cloudmersive-validate-api-client');

var defaultClient = CloudmersiveValidateApiClient.ApiClient.instance;

// Configure API key authorization: Apikey
var Apikey = defaultClient.authentications['Apikey'];
Apikey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Apikey.apiKeyPrefix['Apikey'] = "Token"

var api = new CloudmersiveValidateApiClient.AddressApi()

var input = new CloudmersiveValidateApiClient.ValidateCountryRequest(); // {ValidateCountryRequest} Input request


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.addressCheckEUMembership(input, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CloudmersiveValidateApiClient.AddressApi* | [**addressCheckEUMembership**](docs/AddressApi.md#addressCheckEUMembership) | **POST** /validate/address/country/check-eu-membership | Check if a country is a member of the European Union (EU)
*CloudmersiveValidateApiClient.AddressApi* | [**addressCountry**](docs/AddressApi.md#addressCountry) | **POST** /validate/address/country | Validate and normalize country information, return ISO 3166-1 country codes and country name
*CloudmersiveValidateApiClient.AddressApi* | [**addressCountryList**](docs/AddressApi.md#addressCountryList) | **POST** /validate/address/country/list | Get a list of ISO 3166-1 countries
*CloudmersiveValidateApiClient.AddressApi* | [**addressGeocode**](docs/AddressApi.md#addressGeocode) | **POST** /validate/address/geocode | Geocode a street address into latitude and longitude
*CloudmersiveValidateApiClient.AddressApi* | [**addressGetCountryCurrency**](docs/AddressApi.md#addressGetCountryCurrency) | **POST** /validate/address/country/get-currency | Get the currency of the input country
*CloudmersiveValidateApiClient.AddressApi* | [**addressGetCountryRegion**](docs/AddressApi.md#addressGetCountryRegion) | **POST** /validate/address/country/get-region | Get the region, subregion and continent of the country
*CloudmersiveValidateApiClient.AddressApi* | [**addressGetTimezone**](docs/AddressApi.md#addressGetTimezone) | **POST** /validate/address/country/get-timezones | Gets IANA/Olsen time zones for a country
*CloudmersiveValidateApiClient.AddressApi* | [**addressNormalizeAddress**](docs/AddressApi.md#addressNormalizeAddress) | **POST** /validate/address/street-address/normalize | Normalize a street address
*CloudmersiveValidateApiClient.AddressApi* | [**addressParseString**](docs/AddressApi.md#addressParseString) | **POST** /validate/address/parse | Parse an unstructured input text string into an international, formatted address
*CloudmersiveValidateApiClient.AddressApi* | [**addressReverseGeocodeAddress**](docs/AddressApi.md#addressReverseGeocodeAddress) | **POST** /validate/address/geocode/reverse | Reverse geocode a lattitude and longitude into an address
*CloudmersiveValidateApiClient.AddressApi* | [**addressValidateAddress**](docs/AddressApi.md#addressValidateAddress) | **POST** /validate/address/street-address | Validate a street address
*CloudmersiveValidateApiClient.AddressApi* | [**addressValidateCity**](docs/AddressApi.md#addressValidateCity) | **POST** /validate/address/city | Validate a City and State/Province combination, get location information about it
*CloudmersiveValidateApiClient.AddressApi* | [**addressValidatePostalCode**](docs/AddressApi.md#addressValidatePostalCode) | **POST** /validate/address/postal-code | Validate a postal code, get location information about it
*CloudmersiveValidateApiClient.AddressApi* | [**addressValidateState**](docs/AddressApi.md#addressValidateState) | **POST** /validate/address/state | Validate a state or province, name or abbreviation, get location information about it
*CloudmersiveValidateApiClient.DateTimeApi* | [**dateTimeGetNowSimple**](docs/DateTimeApi.md#dateTimeGetNowSimple) | **GET** /validate/date-time/get/now | Get current date and time as of now
*CloudmersiveValidateApiClient.DateTimeApi* | [**dateTimeGetPublicHolidays**](docs/DateTimeApi.md#dateTimeGetPublicHolidays) | **POST** /validate/date-time/get/holidays | Get public holidays in the specified country and year
*CloudmersiveValidateApiClient.DateTimeApi* | [**dateTimeParseNaturalLanguageDateTime**](docs/DateTimeApi.md#dateTimeParseNaturalLanguageDateTime) | **POST** /validate/date-time/parse/date-time/natural-language | Parses a free-form natural language date and time string into a date and time
*CloudmersiveValidateApiClient.DateTimeApi* | [**dateTimeParseStandardDateTime**](docs/DateTimeApi.md#dateTimeParseStandardDateTime) | **POST** /validate/date-time/parse/date-time/structured | Parses a standardized date and time string into a date and time
*CloudmersiveValidateApiClient.DomainApi* | [**domainCheck**](docs/DomainApi.md#domainCheck) | **POST** /validate/domain/check | Validate a domain name
*CloudmersiveValidateApiClient.DomainApi* | [**domainGetTopLevelDomainFromUrl**](docs/DomainApi.md#domainGetTopLevelDomainFromUrl) | **POST** /validate/domain/url/get-top-level-domain | Get top-level domain name from URL
*CloudmersiveValidateApiClient.DomainApi* | [**domainIsAdminPath**](docs/DomainApi.md#domainIsAdminPath) | **POST** /validate/domain/url/is-admin-path | Check if path is a high-risk or vulnerable server administration path
*CloudmersiveValidateApiClient.DomainApi* | [**domainPhishingCheck**](docs/DomainApi.md#domainPhishingCheck) | **POST** /validate/domain/url/phishing-threat-check | Check a URL for Phishing threats
*CloudmersiveValidateApiClient.DomainApi* | [**domainPost**](docs/DomainApi.md#domainPost) | **POST** /validate/domain/whois | Get WHOIS information for a domain
*CloudmersiveValidateApiClient.DomainApi* | [**domainQualityScore**](docs/DomainApi.md#domainQualityScore) | **POST** /validate/domain/quality-score | Validate a domain name&#39;s quality score
*CloudmersiveValidateApiClient.DomainApi* | [**domainSafetyCheck**](docs/DomainApi.md#domainSafetyCheck) | **POST** /validate/domain/url/safety-threat-check | Check a URL for safety threats
*CloudmersiveValidateApiClient.DomainApi* | [**domainSsrfCheck**](docs/DomainApi.md#domainSsrfCheck) | **POST** /validate/domain/url/ssrf-threat-check | Check a URL for SSRF threats
*CloudmersiveValidateApiClient.DomainApi* | [**domainSsrfCheckBatch**](docs/DomainApi.md#domainSsrfCheckBatch) | **POST** /validate/domain/url/ssrf-threat-check/batch | Check a URL for SSRF threats in batches
*CloudmersiveValidateApiClient.DomainApi* | [**domainUrlFull**](docs/DomainApi.md#domainUrlFull) | **POST** /validate/domain/url/full | Validate a URL fully
*CloudmersiveValidateApiClient.DomainApi* | [**domainUrlHtmlSsrfCheck**](docs/DomainApi.md#domainUrlHtmlSsrfCheck) | **POST** /validate/domain/url/ssrf-threat-check/html-embedded | Check a URL for HTML embedded SSRF threats
*CloudmersiveValidateApiClient.DomainApi* | [**domainUrlSyntaxOnly**](docs/DomainApi.md#domainUrlSyntaxOnly) | **POST** /validate/domain/url/syntax-only | Validate a URL syntactically
*CloudmersiveValidateApiClient.EmailApi* | [**emailAddressGetServers**](docs/EmailApi.md#emailAddressGetServers) | **POST** /validate/email/address/servers | Partially check whether an email address is valid
*CloudmersiveValidateApiClient.EmailApi* | [**emailFullValidation**](docs/EmailApi.md#emailFullValidation) | **POST** /validate/email/address/full | Fully validate an email address
*CloudmersiveValidateApiClient.EmailApi* | [**emailPost**](docs/EmailApi.md#emailPost) | **POST** /validate/email/address/syntaxOnly | Validate email adddress for syntactic correctness only
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressGeolocateStreetAddress**](docs/IPAddressApi.md#iPAddressGeolocateStreetAddress) | **POST** /validate/ip/geolocate/street-address | Geolocate an IP address to a street address
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressIpIntelligence**](docs/IPAddressApi.md#iPAddressIpIntelligence) | **POST** /validate/ip/intelligence | Get intelligence on an IP address
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressIsBot**](docs/IPAddressApi.md#iPAddressIsBot) | **POST** /validate/ip/is-bot | Check if IP address is a Bot client
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressIsThreat**](docs/IPAddressApi.md#iPAddressIsThreat) | **POST** /validate/ip/is-threat | Check if IP address is a known threat
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressIsTorNode**](docs/IPAddressApi.md#iPAddressIsTorNode) | **POST** /validate/ip/is-tor-node | Check if IP address is a Tor node server
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressPost**](docs/IPAddressApi.md#iPAddressPost) | **POST** /validate/ip/geolocate | Geolocate an IP address
*CloudmersiveValidateApiClient.IPAddressApi* | [**iPAddressReverseDomainLookup**](docs/IPAddressApi.md#iPAddressReverseDomainLookup) | **POST** /validate/ip/reverse-domain-lookup | Perform a reverse domain name (DNS) lookup on an IP address
*CloudmersiveValidateApiClient.LeadEnrichmentApi* | [**leadEnrichmentEnrichLead**](docs/LeadEnrichmentApi.md#leadEnrichmentEnrichLead) | **POST** /validate/lead-enrichment/lead/enrich | Enrich an input lead with additional fields of data
*CloudmersiveValidateApiClient.LeadEnrichmentApi* | [**leadEnrichmentGetCompanyInformation**](docs/LeadEnrichmentApi.md#leadEnrichmentGetCompanyInformation) | **POST** /validate/lead-enrichment/lead/email/company-information | Get company information from email address
*CloudmersiveValidateApiClient.NameApi* | [**nameGetGender**](docs/NameApi.md#nameGetGender) | **POST** /validate/name/get-gender | Get the gender of a first name
*CloudmersiveValidateApiClient.NameApi* | [**nameIdentifier**](docs/NameApi.md#nameIdentifier) | **POST** /validate/name/identifier | Validate a code identifier
*CloudmersiveValidateApiClient.NameApi* | [**nameValidateFirstName**](docs/NameApi.md#nameValidateFirstName) | **POST** /validate/name/first | Validate a first name
*CloudmersiveValidateApiClient.NameApi* | [**nameValidateFullName**](docs/NameApi.md#nameValidateFullName) | **POST** /validate/name/full-name | Parse and validate a full name
*CloudmersiveValidateApiClient.NameApi* | [**nameValidateLastName**](docs/NameApi.md#nameValidateLastName) | **POST** /validate/name/last | Validate a last name
*CloudmersiveValidateApiClient.PhoneNumberApi* | [**phoneNumberSyntaxOnly**](docs/PhoneNumberApi.md#phoneNumberSyntaxOnly) | **POST** /validate/phonenumber/basic | Validate phone number (basic)
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckHtmlSsrf**](docs/TextInputApi.md#textInputCheckHtmlSsrf) | **POST** /validate/text-input/html/check/ssrf | Protect html input from Server-side Request Forgery (SSRF) attacks
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckSqlInjection**](docs/TextInputApi.md#textInputCheckSqlInjection) | **POST** /validate/text-input/check/sql-injection | Check text input for SQL Injection (SQLI) attacks
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckSqlInjectionBatch**](docs/TextInputApi.md#textInputCheckSqlInjectionBatch) | **POST** /validate/text-input/check/sql-injection/batch | Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckXss**](docs/TextInputApi.md#textInputCheckXss) | **POST** /validate/text-input/check/xss | Check text input for Cross-Site-Scripting (XSS) attacks
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckXssBatch**](docs/TextInputApi.md#textInputCheckXssBatch) | **POST** /validate/text-input/check-and-protect/xss/batch | Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckXxe**](docs/TextInputApi.md#textInputCheckXxe) | **POST** /validate/text-input/check/xxe | Protect text input from XML External Entity (XXE) attacks
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputCheckXxeBatch**](docs/TextInputApi.md#textInputCheckXxeBatch) | **POST** /validate/text-input/check/xxe/batch | Protect text input from XML External Entity (XXE) attacks
*CloudmersiveValidateApiClient.TextInputApi* | [**textInputProtectXss**](docs/TextInputApi.md#textInputProtectXss) | **POST** /validate/text-input/protect/xss | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization
*CloudmersiveValidateApiClient.UserAgentApi* | [**userAgentParse**](docs/UserAgentApi.md#userAgentParse) | **POST** /validate/useragent/parse | Parse an HTTP User-Agent string, identify robots
*CloudmersiveValidateApiClient.VatApi* | [**vatVatLookup**](docs/VatApi.md#vatVatLookup) | **POST** /validate/vat/lookup | Validate a VAT number


## Documentation for Models

 - [CloudmersiveValidateApiClient.AddressGetServersResponse](docs/AddressGetServersResponse.md)
 - [CloudmersiveValidateApiClient.AddressVerifySyntaxOnlyResponse](docs/AddressVerifySyntaxOnlyResponse.md)
 - [CloudmersiveValidateApiClient.BotCheckResponse](docs/BotCheckResponse.md)
 - [CloudmersiveValidateApiClient.CheckResponse](docs/CheckResponse.md)
 - [CloudmersiveValidateApiClient.CountryDetails](docs/CountryDetails.md)
 - [CloudmersiveValidateApiClient.CountryListResult](docs/CountryListResult.md)
 - [CloudmersiveValidateApiClient.DateTimeNaturalLanguageParseRequest](docs/DateTimeNaturalLanguageParseRequest.md)
 - [CloudmersiveValidateApiClient.DateTimeNowResult](docs/DateTimeNowResult.md)
 - [CloudmersiveValidateApiClient.DateTimeStandardizedParseRequest](docs/DateTimeStandardizedParseRequest.md)
 - [CloudmersiveValidateApiClient.DateTimeStandardizedParseResponse](docs/DateTimeStandardizedParseResponse.md)
 - [CloudmersiveValidateApiClient.DomainQualityResponse](docs/DomainQualityResponse.md)
 - [CloudmersiveValidateApiClient.EmailLead](docs/EmailLead.md)
 - [CloudmersiveValidateApiClient.FirstNameValidationRequest](docs/FirstNameValidationRequest.md)
 - [CloudmersiveValidateApiClient.FirstNameValidationResponse](docs/FirstNameValidationResponse.md)
 - [CloudmersiveValidateApiClient.FullEmailValidationResponse](docs/FullEmailValidationResponse.md)
 - [CloudmersiveValidateApiClient.FullNameValidationRequest](docs/FullNameValidationRequest.md)
 - [CloudmersiveValidateApiClient.FullNameValidationResponse](docs/FullNameValidationResponse.md)
 - [CloudmersiveValidateApiClient.GeolocateResponse](docs/GeolocateResponse.md)
 - [CloudmersiveValidateApiClient.GeolocateStreetAddressResponse](docs/GeolocateStreetAddressResponse.md)
 - [CloudmersiveValidateApiClient.GetGenderRequest](docs/GetGenderRequest.md)
 - [CloudmersiveValidateApiClient.GetGenderResponse](docs/GetGenderResponse.md)
 - [CloudmersiveValidateApiClient.GetPublicHolidaysRequest](docs/GetPublicHolidaysRequest.md)
 - [CloudmersiveValidateApiClient.GetTimezonesRequest](docs/GetTimezonesRequest.md)
 - [CloudmersiveValidateApiClient.GetTimezonesResponse](docs/GetTimezonesResponse.md)
 - [CloudmersiveValidateApiClient.HtmlSsrfDetectionResult](docs/HtmlSsrfDetectionResult.md)
 - [CloudmersiveValidateApiClient.IPIntelligenceResponse](docs/IPIntelligenceResponse.md)
 - [CloudmersiveValidateApiClient.IPReverseDNSLookupResponse](docs/IPReverseDNSLookupResponse.md)
 - [CloudmersiveValidateApiClient.IPThreatResponse](docs/IPThreatResponse.md)
 - [CloudmersiveValidateApiClient.IsAdminPathResponse](docs/IsAdminPathResponse.md)
 - [CloudmersiveValidateApiClient.LastNameValidationRequest](docs/LastNameValidationRequest.md)
 - [CloudmersiveValidateApiClient.LastNameValidationResponse](docs/LastNameValidationResponse.md)
 - [CloudmersiveValidateApiClient.LeadEnrichmentRequest](docs/LeadEnrichmentRequest.md)
 - [CloudmersiveValidateApiClient.LeadEnrichmentResponse](docs/LeadEnrichmentResponse.md)
 - [CloudmersiveValidateApiClient.NormalizeAddressResponse](docs/NormalizeAddressResponse.md)
 - [CloudmersiveValidateApiClient.ParseAddressRequest](docs/ParseAddressRequest.md)
 - [CloudmersiveValidateApiClient.ParseAddressResponse](docs/ParseAddressResponse.md)
 - [CloudmersiveValidateApiClient.PhishingCheckRequest](docs/PhishingCheckRequest.md)
 - [CloudmersiveValidateApiClient.PhishingCheckResponse](docs/PhishingCheckResponse.md)
 - [CloudmersiveValidateApiClient.PhoneNumberValidateRequest](docs/PhoneNumberValidateRequest.md)
 - [CloudmersiveValidateApiClient.PhoneNumberValidationResponse](docs/PhoneNumberValidationResponse.md)
 - [CloudmersiveValidateApiClient.PublicHolidayOccurrence](docs/PublicHolidayOccurrence.md)
 - [CloudmersiveValidateApiClient.PublicHolidaysResponse](docs/PublicHolidaysResponse.md)
 - [CloudmersiveValidateApiClient.ReverseGeocodeAddressRequest](docs/ReverseGeocodeAddressRequest.md)
 - [CloudmersiveValidateApiClient.ReverseGeocodeAddressResponse](docs/ReverseGeocodeAddressResponse.md)
 - [CloudmersiveValidateApiClient.SqlInjectionCheckBatchRequest](docs/SqlInjectionCheckBatchRequest.md)
 - [CloudmersiveValidateApiClient.SqlInjectionCheckBatchResponse](docs/SqlInjectionCheckBatchResponse.md)
 - [CloudmersiveValidateApiClient.SqlInjectionCheckRequestItem](docs/SqlInjectionCheckRequestItem.md)
 - [CloudmersiveValidateApiClient.SqlInjectionDetectionResult](docs/SqlInjectionDetectionResult.md)
 - [CloudmersiveValidateApiClient.Timezone](docs/Timezone.md)
 - [CloudmersiveValidateApiClient.TorNodeResponse](docs/TorNodeResponse.md)
 - [CloudmersiveValidateApiClient.UrlHtmlSsrfRequestFull](docs/UrlHtmlSsrfRequestFull.md)
 - [CloudmersiveValidateApiClient.UrlHtmlSsrfResponseFull](docs/UrlHtmlSsrfResponseFull.md)
 - [CloudmersiveValidateApiClient.UrlSafetyCheckRequestFull](docs/UrlSafetyCheckRequestFull.md)
 - [CloudmersiveValidateApiClient.UrlSafetyCheckResponseFull](docs/UrlSafetyCheckResponseFull.md)
 - [CloudmersiveValidateApiClient.UrlSsrfRequestBatch](docs/UrlSsrfRequestBatch.md)
 - [CloudmersiveValidateApiClient.UrlSsrfRequestFull](docs/UrlSsrfRequestFull.md)
 - [CloudmersiveValidateApiClient.UrlSsrfResponseBatch](docs/UrlSsrfResponseBatch.md)
 - [CloudmersiveValidateApiClient.UrlSsrfResponseFull](docs/UrlSsrfResponseFull.md)
 - [CloudmersiveValidateApiClient.UserAgentValidateRequest](docs/UserAgentValidateRequest.md)
 - [CloudmersiveValidateApiClient.UserAgentValidateResponse](docs/UserAgentValidateResponse.md)
 - [CloudmersiveValidateApiClient.ValidateAddressRequest](docs/ValidateAddressRequest.md)
 - [CloudmersiveValidateApiClient.ValidateAddressResponse](docs/ValidateAddressResponse.md)
 - [CloudmersiveValidateApiClient.ValidateCityRequest](docs/ValidateCityRequest.md)
 - [CloudmersiveValidateApiClient.ValidateCityResponse](docs/ValidateCityResponse.md)
 - [CloudmersiveValidateApiClient.ValidateCountryRequest](docs/ValidateCountryRequest.md)
 - [CloudmersiveValidateApiClient.ValidateCountryResponse](docs/ValidateCountryResponse.md)
 - [CloudmersiveValidateApiClient.ValidateIdentifierRequest](docs/ValidateIdentifierRequest.md)
 - [CloudmersiveValidateApiClient.ValidateIdentifierResponse](docs/ValidateIdentifierResponse.md)
 - [CloudmersiveValidateApiClient.ValidatePostalCodeRequest](docs/ValidatePostalCodeRequest.md)
 - [CloudmersiveValidateApiClient.ValidatePostalCodeResponse](docs/ValidatePostalCodeResponse.md)
 - [CloudmersiveValidateApiClient.ValidateStateRequest](docs/ValidateStateRequest.md)
 - [CloudmersiveValidateApiClient.ValidateStateResponse](docs/ValidateStateResponse.md)
 - [CloudmersiveValidateApiClient.ValidateUrlRequestFull](docs/ValidateUrlRequestFull.md)
 - [CloudmersiveValidateApiClient.ValidateUrlRequestSyntaxOnly](docs/ValidateUrlRequestSyntaxOnly.md)
 - [CloudmersiveValidateApiClient.ValidateUrlResponseFull](docs/ValidateUrlResponseFull.md)
 - [CloudmersiveValidateApiClient.ValidateUrlResponseSyntaxOnly](docs/ValidateUrlResponseSyntaxOnly.md)
 - [CloudmersiveValidateApiClient.VatLookupRequest](docs/VatLookupRequest.md)
 - [CloudmersiveValidateApiClient.VatLookupResponse](docs/VatLookupResponse.md)
 - [CloudmersiveValidateApiClient.WhoisResponse](docs/WhoisResponse.md)
 - [CloudmersiveValidateApiClient.XssProtectionBatchRequest](docs/XssProtectionBatchRequest.md)
 - [CloudmersiveValidateApiClient.XssProtectionBatchResponse](docs/XssProtectionBatchResponse.md)
 - [CloudmersiveValidateApiClient.XssProtectionRequestItem](docs/XssProtectionRequestItem.md)
 - [CloudmersiveValidateApiClient.XssProtectionResult](docs/XssProtectionResult.md)
 - [CloudmersiveValidateApiClient.XxeDetectionBatchRequest](docs/XxeDetectionBatchRequest.md)
 - [CloudmersiveValidateApiClient.XxeDetectionBatchResponse](docs/XxeDetectionBatchResponse.md)
 - [CloudmersiveValidateApiClient.XxeDetectionRequestItem](docs/XxeDetectionRequestItem.md)
 - [CloudmersiveValidateApiClient.XxeDetectionResult](docs/XxeDetectionResult.md)


## Documentation for Authorization


### Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header

