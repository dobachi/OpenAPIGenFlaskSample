# StockPrice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Price** | Pointer to **float64** | 現在の株価 | [optional] 
**Open** | Pointer to **float64** | 始値 | [optional] 
**High** | Pointer to **float32** | 高値 | [optional] 
**Low** | Pointer to **float32** | 安値 | [optional] 
**Volume** | Pointer to **float32** | 出来高 | [optional] 

## Methods

### NewStockPrice

`func NewStockPrice() *StockPrice`

NewStockPrice instantiates a new StockPrice object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStockPriceWithDefaults

`func NewStockPriceWithDefaults() *StockPrice`

NewStockPriceWithDefaults instantiates a new StockPrice object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrice

`func (o *StockPrice) GetPrice() float64`

GetPrice returns the Price field if non-nil, zero value otherwise.

### GetPriceOk

`func (o *StockPrice) GetPriceOk() (*float64, bool)`

GetPriceOk returns a tuple with the Price field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrice

`func (o *StockPrice) SetPrice(v float64)`

SetPrice sets Price field to given value.

### HasPrice

`func (o *StockPrice) HasPrice() bool`

HasPrice returns a boolean if a field has been set.

### GetOpen

`func (o *StockPrice) GetOpen() float64`

GetOpen returns the Open field if non-nil, zero value otherwise.

### GetOpenOk

`func (o *StockPrice) GetOpenOk() (*float64, bool)`

GetOpenOk returns a tuple with the Open field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOpen

`func (o *StockPrice) SetOpen(v float64)`

SetOpen sets Open field to given value.

### HasOpen

`func (o *StockPrice) HasOpen() bool`

HasOpen returns a boolean if a field has been set.

### GetHigh

`func (o *StockPrice) GetHigh() float32`

GetHigh returns the High field if non-nil, zero value otherwise.

### GetHighOk

`func (o *StockPrice) GetHighOk() (*float32, bool)`

GetHighOk returns a tuple with the High field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHigh

`func (o *StockPrice) SetHigh(v float32)`

SetHigh sets High field to given value.

### HasHigh

`func (o *StockPrice) HasHigh() bool`

HasHigh returns a boolean if a field has been set.

### GetLow

`func (o *StockPrice) GetLow() float32`

GetLow returns the Low field if non-nil, zero value otherwise.

### GetLowOk

`func (o *StockPrice) GetLowOk() (*float32, bool)`

GetLowOk returns a tuple with the Low field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLow

`func (o *StockPrice) SetLow(v float32)`

SetLow sets Low field to given value.

### HasLow

`func (o *StockPrice) HasLow() bool`

HasLow returns a boolean if a field has been set.

### GetVolume

`func (o *StockPrice) GetVolume() float32`

GetVolume returns the Volume field if non-nil, zero value otherwise.

### GetVolumeOk

`func (o *StockPrice) GetVolumeOk() (*float32, bool)`

GetVolumeOk returns a tuple with the Volume field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVolume

`func (o *StockPrice) SetVolume(v float32)`

SetVolume sets Volume field to given value.

### HasVolume

`func (o *StockPrice) HasVolume() bool`

HasVolume returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


