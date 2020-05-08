# beanie-api
An API specification for interacting with the Beanie ERP system

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.2
- Package version: 0.8.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/altoyield/python-beanieclient.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/altoyield/python-beanieclient.git`)

Then import the package:
```python
import beanie 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import beanie
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import beanie
from beanie.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
beanie.configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# beanie.configuration.api_key_prefix['ApiKey'] = 'Bearer'
# create an instance of the API class
api_instance = beanie.AddressBlockApi()
address_blocks = beanie.AddressBlockInput() # AddressBlockInput | Address block to add to the system

try:
    api_response = api_instance.add_address_block(address_blocks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->add_address_block: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://bean.ie*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressBlockApi* | [**add_address_block**](docs/AddressBlockApi.md#add_address_block) | **POST** /address_blocks | 
*AddressBlockApi* | [**find_address_block_by_id**](docs/AddressBlockApi.md#find_address_block_by_id) | **GET** /address_blocks/{id} | Find Address block by ID
*AddressBlockApi* | [**find_address_blocks**](docs/AddressBlockApi.md#find_address_blocks) | **GET** /address_blocks | All address block
*BankAccountApi* | [**add_bank_account**](docs/BankAccountApi.md#add_bank_account) | **POST** /bank_accounts | 
*BankAccountApi* | [**find_bank_account_by_id**](docs/BankAccountApi.md#find_bank_account_by_id) | **GET** /bank_accounts/{id} | Find Bank Account by ID
*BankAccountApi* | [**find_bank_accounts**](docs/BankAccountApi.md#find_bank_accounts) | **GET** /bank_accounts | All bank accounts
*BankStatementApi* | [**add_bank_statement**](docs/BankStatementApi.md#add_bank_statement) | **POST** /bank_statements | 
*BankStatementApi* | [**find_bank_statement_by_id**](docs/BankStatementApi.md#find_bank_statement_by_id) | **GET** /bank_statements/{id} | Find Bank statement by ID
*BankStatementApi* | [**find_bank_statements**](docs/BankStatementApi.md#find_bank_statements) | **GET** /bank_statements | All bank statement
*BeanieTaskApi* | [**add_beanie_task**](docs/BeanieTaskApi.md#add_beanie_task) | **POST** /beanie_tasks | 
*BeanieTaskApi* | [**find_beanie_task_by_id**](docs/BeanieTaskApi.md#find_beanie_task_by_id) | **GET** /beanie_tasks/{id} | Find Beanie task by ID
*BeanieTaskApi* | [**find_beanie_tasks**](docs/BeanieTaskApi.md#find_beanie_tasks) | **GET** /beanie_tasks | All beanie task
*BillOfMaterialsApi* | [**add_bill_of_material**](docs/BillOfMaterialsApi.md#add_bill_of_material) | **POST** /bill_of_materials | 
*BillOfMaterialsApi* | [**find_bill_of_material_by_id**](docs/BillOfMaterialsApi.md#find_bill_of_material_by_id) | **GET** /bill_of_materials/{id} | Find Bill of Materials by ID
*BillOfMaterialsApi* | [**find_bill_of_materials**](docs/BillOfMaterialsApi.md#find_bill_of_materials) | **GET** /bill_of_materials | All bill of materials
*BillableApi* | [**add_billable**](docs/BillableApi.md#add_billable) | **POST** /billables | 
*BillableApi* | [**find_billable_by_id**](docs/BillableApi.md#find_billable_by_id) | **GET** /billables/{id} | Find Billable record by ID
*BillableApi* | [**find_billables**](docs/BillableApi.md#find_billables) | **GET** /billables | All billable record
*CompanyApi* | [**find_company_by_id**](docs/CompanyApi.md#find_company_by_id) | **GET** /companies/{id} | Find Company details by ID
*DeliveryNoteApi* | [**add_delivery_note**](docs/DeliveryNoteApi.md#add_delivery_note) | **POST** /delivery_notes | 
*DeliveryNoteApi* | [**find_delivery_note_by_id**](docs/DeliveryNoteApi.md#find_delivery_note_by_id) | **GET** /delivery_notes/{id} | Find Delivery note by ID
*DeliveryNoteApi* | [**find_delivery_notes**](docs/DeliveryNoteApi.md#find_delivery_notes) | **GET** /delivery_notes | All delivery note
*DocumentApi* | [**add_document**](docs/DocumentApi.md#add_document) | **POST** /documents | 
*DocumentApi* | [**find_document_by_id**](docs/DocumentApi.md#find_document_by_id) | **GET** /documents/{id} | Find Document by ID
*DocumentApi* | [**find_documents**](docs/DocumentApi.md#find_documents) | **GET** /documents | All document
*FixedAssetApi* | [**add_fixed_asset**](docs/FixedAssetApi.md#add_fixed_asset) | **POST** /fixed_assets | 
*FixedAssetApi* | [**find_fixed_asset_by_id**](docs/FixedAssetApi.md#find_fixed_asset_by_id) | **GET** /fixed_assets/{id} | Find Fixed asset by ID
*FixedAssetApi* | [**find_fixed_assets**](docs/FixedAssetApi.md#find_fixed_assets) | **GET** /fixed_assets | All fixed asset
*ImageApi* | [**add_image**](docs/ImageApi.md#add_image) | **POST** /images | 
*ImageApi* | [**find_image_by_id**](docs/ImageApi.md#find_image_by_id) | **GET** /images/{id} | Find Image by ID
*ImageApi* | [**find_images**](docs/ImageApi.md#find_images) | **GET** /images | All image
*JournalApi* | [**add_journal**](docs/JournalApi.md#add_journal) | **POST** /journals | 
*JournalApi* | [**find_journal_by_id**](docs/JournalApi.md#find_journal_by_id) | **GET** /journals/{id} | Find Journal by ID
*JournalApi* | [**find_journals**](docs/JournalApi.md#find_journals) | **GET** /journals | All journal
*NominalAccountApi* | [**add_nominal_account**](docs/NominalAccountApi.md#add_nominal_account) | **POST** /nominal_accounts | 
*NominalAccountApi* | [**find_nominal_account_by_id**](docs/NominalAccountApi.md#find_nominal_account_by_id) | **GET** /nominal_accounts/{id} | Find Nominal account by ID
*NominalAccountApi* | [**find_nominal_accounts**](docs/NominalAccountApi.md#find_nominal_accounts) | **GET** /nominal_accounts | All nominal account
*NominalAccountCategoryApi* | [**add_nominal_account_category**](docs/NominalAccountCategoryApi.md#add_nominal_account_category) | **POST** /nominal_account_categories | 
*NominalAccountCategoryApi* | [**find_nominal_account_categories**](docs/NominalAccountCategoryApi.md#find_nominal_account_categories) | **GET** /nominal_account_categories | All nominal account category
*NominalAccountCategoryApi* | [**find_nominal_account_category_by_id**](docs/NominalAccountCategoryApi.md#find_nominal_account_category_by_id) | **GET** /nominal_account_categories/{id} | Find Nominal account category by ID
*PartnerApi* | [**add_partner**](docs/PartnerApi.md#add_partner) | **POST** /partners | 
*PartnerApi* | [**find_partner_by_id**](docs/PartnerApi.md#find_partner_by_id) | **GET** /partners/{id} | Find Partner by ID
*PartnerApi* | [**find_partners**](docs/PartnerApi.md#find_partners) | **GET** /partners | All partners
*PartnerAddressApi* | [**add_partner_address**](docs/PartnerAddressApi.md#add_partner_address) | **POST** /partner_addresses | 
*PartnerAddressApi* | [**find_partner_address_by_id**](docs/PartnerAddressApi.md#find_partner_address_by_id) | **GET** /partner_addresses/{id} | Find Partner address by ID
*PartnerAddressApi* | [**find_partner_addresses**](docs/PartnerAddressApi.md#find_partner_addresses) | **GET** /partner_addresses | All partner address
*ProductApi* | [**add_product**](docs/ProductApi.md#add_product) | **POST** /products | 
*ProductApi* | [**find_product_by_id**](docs/ProductApi.md#find_product_by_id) | **GET** /products/{id} | Find Product by ID
*ProductApi* | [**find_products**](docs/ProductApi.md#find_products) | **GET** /products | All product
*ProductCategoryApi* | [**add_product_category**](docs/ProductCategoryApi.md#add_product_category) | **POST** /product_categories | 
*ProductCategoryApi* | [**find_product_categories**](docs/ProductCategoryApi.md#find_product_categories) | **GET** /product_categories | All product category
*ProductCategoryApi* | [**find_product_category_by_id**](docs/ProductCategoryApi.md#find_product_category_by_id) | **GET** /product_categories/{id} | Find Product category by ID
*ProductPriceApi* | [**add_product_price**](docs/ProductPriceApi.md#add_product_price) | **POST** /product_prices | 
*ProductPriceApi* | [**find_product_price_by_id**](docs/ProductPriceApi.md#find_product_price_by_id) | **GET** /product_prices/{id} | Find Product price by ID
*ProductPriceApi* | [**find_product_prices**](docs/ProductPriceApi.md#find_product_prices) | **GET** /product_prices | All product price
*ProductVariantApi* | [**add_product_variant**](docs/ProductVariantApi.md#add_product_variant) | **POST** /product_variants | 
*ProductVariantApi* | [**find_product_variant_by_id**](docs/ProductVariantApi.md#find_product_variant_by_id) | **GET** /product_variants/{id} | Find Product variant by ID
*ProductVariantApi* | [**find_product_variants**](docs/ProductVariantApi.md#find_product_variants) | **GET** /product_variants | All product variant
*ProductionOrderApi* | [**add_production_order**](docs/ProductionOrderApi.md#add_production_order) | **POST** /production_orders | 
*ProductionOrderApi* | [**find_production_order_by_id**](docs/ProductionOrderApi.md#find_production_order_by_id) | **GET** /production_orders/{id} | Find Production order by ID
*ProductionOrderApi* | [**find_production_orders**](docs/ProductionOrderApi.md#find_production_orders) | **GET** /production_orders | All production order
*PurchaseInvoiceApi* | [**add_purchase_invoice**](docs/PurchaseInvoiceApi.md#add_purchase_invoice) | **POST** /purchase_invoices | 
*PurchaseInvoiceApi* | [**find_purchase_invoice_by_id**](docs/PurchaseInvoiceApi.md#find_purchase_invoice_by_id) | **GET** /purchase_invoices/{id} | Find Purchase invoice by ID
*PurchaseInvoiceApi* | [**find_purchase_invoices**](docs/PurchaseInvoiceApi.md#find_purchase_invoices) | **GET** /purchase_invoices | All purchase invoice
*PurchaseOrderApi* | [**add_purchase_order**](docs/PurchaseOrderApi.md#add_purchase_order) | **POST** /purchase_orders | 
*PurchaseOrderApi* | [**find_purchase_order_by_id**](docs/PurchaseOrderApi.md#find_purchase_order_by_id) | **GET** /purchase_orders/{id} | Find Purchase order by ID
*PurchaseOrderApi* | [**find_purchase_orders**](docs/PurchaseOrderApi.md#find_purchase_orders) | **GET** /purchase_orders | All purchase order
*SalesInvoiceApi* | [**add_sales_invoice**](docs/SalesInvoiceApi.md#add_sales_invoice) | **POST** /sales_invoices | 
*SalesInvoiceApi* | [**find_sales_invoice_by_id**](docs/SalesInvoiceApi.md#find_sales_invoice_by_id) | **GET** /sales_invoices/{id} | Find Sales invoice by ID
*SalesInvoiceApi* | [**find_sales_invoices**](docs/SalesInvoiceApi.md#find_sales_invoices) | **GET** /sales_invoices | All sales invoice
*SalesOrderApi* | [**add_sales_order**](docs/SalesOrderApi.md#add_sales_order) | **POST** /sales_orders | 
*SalesOrderApi* | [**find_sales_order**](docs/SalesOrderApi.md#find_sales_order) | **GET** /sales_orders | All sales order
*SalesOrderApi* | [**find_sales_order_by_id**](docs/SalesOrderApi.md#find_sales_order_by_id) | **GET** /sales_orders/{id} | Find Sales order by ID
*ShippingCentreApi* | [**add_shipping_centre**](docs/ShippingCentreApi.md#add_shipping_centre) | **POST** /shipping_centres | 
*ShippingCentreApi* | [**find_shipping_centre_by_id**](docs/ShippingCentreApi.md#find_shipping_centre_by_id) | **GET** /shipping_centres/{id} | Find Shipping centre by ID
*ShippingCentreApi* | [**find_shipping_centres**](docs/ShippingCentreApi.md#find_shipping_centres) | **GET** /shipping_centres | All shipping centre
*StockAdjustmentApi* | [**add_stock_adjustment**](docs/StockAdjustmentApi.md#add_stock_adjustment) | **POST** /stock_adjustments | 
*StockAdjustmentApi* | [**find_stock_adjustment_by_id**](docs/StockAdjustmentApi.md#find_stock_adjustment_by_id) | **GET** /stock_adjustments/{id} | Find Stock adjustment by ID
*StockAdjustmentApi* | [**find_stock_adjustments**](docs/StockAdjustmentApi.md#find_stock_adjustments) | **GET** /stock_adjustments | All stock adjustment
*StockCategoryApi* | [**add_stock_category**](docs/StockCategoryApi.md#add_stock_category) | **POST** /stock_categories | 
*StockCategoryApi* | [**find_stock_categories**](docs/StockCategoryApi.md#find_stock_categories) | **GET** /stock_categories | All stock category
*StockCategoryApi* | [**find_stock_category_by_id**](docs/StockCategoryApi.md#find_stock_category_by_id) | **GET** /stock_categories/{id} | Find Stock category by ID
*StockItemApi* | [**add_stock_item**](docs/StockItemApi.md#add_stock_item) | **POST** /stock_items | 
*StockItemApi* | [**find_stock_item_by_id**](docs/StockItemApi.md#find_stock_item_by_id) | **GET** /stock_items/{id} | Find Stock item by ID
*StockItemApi* | [**find_stock_items**](docs/StockItemApi.md#find_stock_items) | **GET** /stock_items | All stock item
*StockLocationApi* | [**add_stock_location**](docs/StockLocationApi.md#add_stock_location) | **POST** /stock_locations | 
*StockLocationApi* | [**find_stock_location_by_id**](docs/StockLocationApi.md#find_stock_location_by_id) | **GET** /stock_locations/{id} | Find Stock location by ID
*StockLocationApi* | [**find_stock_locations**](docs/StockLocationApi.md#find_stock_locations) | **GET** /stock_locations | All stock location
*StockSupplierApi* | [**add_stock_supplier**](docs/StockSupplierApi.md#add_stock_supplier) | **POST** /stock_suppliers | 
*StockSupplierApi* | [**find_stock_supplier_by_id**](docs/StockSupplierApi.md#find_stock_supplier_by_id) | **GET** /stock_suppliers/{id} | Find Stock supplier by ID
*StockSupplierApi* | [**find_stock_suppliers**](docs/StockSupplierApi.md#find_stock_suppliers) | **GET** /stock_suppliers | All stock supplier
*VatRecordApi* | [**add_vat_record**](docs/VatRecordApi.md#add_vat_record) | **POST** /vat_records | 
*VatRecordApi* | [**find_vat_record_by_id**](docs/VatRecordApi.md#find_vat_record_by_id) | **GET** /vat_records/{id} | Find VAT record by ID
*VatRecordApi* | [**find_vat_records**](docs/VatRecordApi.md#find_vat_records) | **GET** /vat_records | All vat record
*VatReturnApi* | [**add_vat_return**](docs/VatReturnApi.md#add_vat_return) | **POST** /vat_returns | 
*VatReturnApi* | [**find_vat_return_by_id**](docs/VatReturnApi.md#find_vat_return_by_id) | **GET** /vat_returns/{id} | Find VAT return by ID
*VatReturnApi* | [**find_vat_returns**](docs/VatReturnApi.md#find_vat_returns) | **GET** /vat_returns | All vat return
*WorkCentreApi* | [**find_work_centre_by_id**](docs/WorkCentreApi.md#find_work_centre_by_id) | **GET** /work_centres/{id} | Find Work centre by ID
*WorkCentreApi* | [**find_work_centres**](docs/WorkCentreApi.md#find_work_centres) | **GET** /work_centre_groups/{work_centre_group_id}/work_centres | All work centre
*WorkCentreGroupApi* | [**find_work_centre_group_by_id**](docs/WorkCentreGroupApi.md#find_work_centre_group_by_id) | **GET** /work_centre_groups/{id} | Find Work centre group by ID
*WorkCentreGroupApi* | [**find_work_centre_groups**](docs/WorkCentreGroupApi.md#find_work_centre_groups) | **GET** /work_centre_groups | All work centre group


## Documentation For Models

 - [AddressBlock](docs/AddressBlock.md)
 - [BankAccountInput](docs/BankAccountInput.md)
 - [BankStatement](docs/BankStatement.md)
 - [BankStatementData](docs/BankStatementData.md)
 - [BeanieTask](docs/BeanieTask.md)
 - [BillOfMaterial](docs/BillOfMaterial.md)
 - [Billable](docs/Billable.md)
 - [BomItem](docs/BomItem.md)
 - [Company](docs/Company.md)
 - [DeliveryNote](docs/DeliveryNote.md)
 - [DeliveryNoteItem](docs/DeliveryNoteItem.md)
 - [Document](docs/Document.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [FiscalYear](docs/FiscalYear.md)
 - [FixedAsset](docs/FixedAsset.md)
 - [GoodsReceivedNote](docs/GoodsReceivedNote.md)
 - [Image](docs/Image.md)
 - [Journal](docs/Journal.md)
 - [JournalItem](docs/JournalItem.md)
 - [NominalAccount](docs/NominalAccount.md)
 - [NominalAccountCategory](docs/NominalAccountCategory.md)
 - [PartnerAddress](docs/PartnerAddress.md)
 - [PartnerInput](docs/PartnerInput.md)
 - [PartnerNote](docs/PartnerNote.md)
 - [PayablesLedger](docs/PayablesLedger.md)
 - [Product](docs/Product.md)
 - [ProductCategory](docs/ProductCategory.md)
 - [ProductPrice](docs/ProductPrice.md)
 - [ProductVariant](docs/ProductVariant.md)
 - [ProductionOrderInput](docs/ProductionOrderInput.md)
 - [ProductionOrderLog](docs/ProductionOrderLog.md)
 - [PurchaseInvoice](docs/PurchaseInvoice.md)
 - [PurchaseOrder](docs/PurchaseOrder.md)
 - [PurchaseOrderItem](docs/PurchaseOrderItem.md)
 - [ReceivablesLedger](docs/ReceivablesLedger.md)
 - [SalesInvoice](docs/SalesInvoice.md)
 - [SalesInvoiceItem](docs/SalesInvoiceItem.md)
 - [SalesOrder](docs/SalesOrder.md)
 - [SalesOrderItem](docs/SalesOrderItem.md)
 - [ShippingCentre](docs/ShippingCentre.md)
 - [StockAdjustment](docs/StockAdjustment.md)
 - [StockCategory](docs/StockCategory.md)
 - [StockItem](docs/StockItem.md)
 - [StockLocation](docs/StockLocation.md)
 - [StockSupplier](docs/StockSupplier.md)
 - [VatRecord](docs/VatRecord.md)
 - [VatReturn](docs/VatReturn.md)
 - [WorkCentre](docs/WorkCentre.md)
 - [WorkCentreGroup](docs/WorkCentreGroup.md)
 - [AddressBlockInput](docs/AddressBlockInput.md)
 - [BankAccount](docs/BankAccount.md)
 - [BankStatementDataInput](docs/BankStatementDataInput.md)
 - [BankStatementInput](docs/BankStatementInput.md)
 - [BeanieTaskInput](docs/BeanieTaskInput.md)
 - [BillOfMaterialInput](docs/BillOfMaterialInput.md)
 - [BillableInput](docs/BillableInput.md)
 - [BomItemInput](docs/BomItemInput.md)
 - [DeliveryNoteInput](docs/DeliveryNoteInput.md)
 - [DeliveryNoteItemInput](docs/DeliveryNoteItemInput.md)
 - [DocumentInput](docs/DocumentInput.md)
 - [FixedAssetInput](docs/FixedAssetInput.md)
 - [GoodsReceivedNoteInput](docs/GoodsReceivedNoteInput.md)
 - [ImageInput](docs/ImageInput.md)
 - [JournalInput](docs/JournalInput.md)
 - [JournalItemInput](docs/JournalItemInput.md)
 - [NominalAccountCategoryInput](docs/NominalAccountCategoryInput.md)
 - [NominalAccountInput](docs/NominalAccountInput.md)
 - [Partner](docs/Partner.md)
 - [PartnerAddressInput](docs/PartnerAddressInput.md)
 - [ProductCategoryInput](docs/ProductCategoryInput.md)
 - [ProductInput](docs/ProductInput.md)
 - [ProductPriceInput](docs/ProductPriceInput.md)
 - [ProductVariantInput](docs/ProductVariantInput.md)
 - [ProductionOrder](docs/ProductionOrder.md)
 - [PurchaseInvoiceInput](docs/PurchaseInvoiceInput.md)
 - [PurchaseOrderInput](docs/PurchaseOrderInput.md)
 - [PurchaseOrderItemInput](docs/PurchaseOrderItemInput.md)
 - [SalesInvoiceInput](docs/SalesInvoiceInput.md)
 - [SalesInvoiceItemInput](docs/SalesInvoiceItemInput.md)
 - [SalesOrderInput](docs/SalesOrderInput.md)
 - [SalesOrderItemInput](docs/SalesOrderItemInput.md)
 - [ShippingCentreInput](docs/ShippingCentreInput.md)
 - [StockAdjustmentInput](docs/StockAdjustmentInput.md)
 - [StockCategoryInput](docs/StockCategoryInput.md)
 - [StockItemInput](docs/StockItemInput.md)
 - [StockLocationInput](docs/StockLocationInput.md)
 - [StockSupplierInput](docs/StockSupplierInput.md)
 - [VatRecordInput](docs/VatRecordInput.md)
 - [VatReturnInput](docs/VatReturnInput.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: ApiKey
- **Location**: HTTP header


## Author

dev@bean.ie

