# \StockPriceAPI

All URIs are relative to *http://localhost:3003*

Method | HTTP request | Description
------------- | ------------- | -------------
[**StockPrice**](StockPriceAPI.md#StockPrice) | **Get** /v1/sc/{security_cd}/stockPrice | 株価取得



## StockPrice

> StockPrice StockPrice(ctx, securityCd).Execute()

株価取得



### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
    securityCd := "4722" // string | 証券コードを指定する

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.StockPriceAPI.StockPrice(context.Background(), securityCd).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `StockPriceAPI.StockPrice``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `StockPrice`: StockPrice
    fmt.Fprintf(os.Stdout, "Response from `StockPriceAPI.StockPrice`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**securityCd** | **string** | 証券コードを指定する | 

### Other Parameters

Other parameters are passed through a pointer to a apiStockPriceRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**StockPrice**](StockPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

