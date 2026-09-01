"""
LedgerAI - routes/transactions.py
3 Years of dynamically generated corporate transactions.
"""

from fastapi import APIRouter

router = APIRouter()

TRANSACTIONS = [
    {
        "id": 1,
        "date": "2024-01-01",
        "description": "Office rent paid",
        "amount": 49187.02,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 2,
        "date": "2024-01-01",
        "description": "Salary paid to employees",
        "amount": 85619.88,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 3,
        "date": "2024-01-01",
        "description": "Vendor payment against outstanding",
        "amount": 132123.33,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 4,
        "date": "2024-01-02",
        "description": "Sales to Bombay Fashion House",
        "amount": 348964.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 5,
        "date": "2024-01-02",
        "description": "GST collected on sales",
        "amount": 62813.6,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 6,
        "date": "2024-01-03",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 249739.49,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 7,
        "date": "2024-01-03",
        "description": "GST input on inventory",
        "amount": 44953.11,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 8,
        "date": "2024-01-05",
        "description": "Electricity bill payment",
        "amount": 10411.91,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 9,
        "date": "2024-01-05",
        "description": "Water and utility charges",
        "amount": 3269.98,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 10,
        "date": "2024-01-05",
        "description": "Sales to Rajan Fabrics",
        "amount": 287948.38,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 11,
        "date": "2024-01-05",
        "description": "GST collected on sales",
        "amount": 51830.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 12,
        "date": "2024-01-06",
        "description": "Software license capitalization",
        "amount": 51752.09,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 13,
        "date": "2024-01-08",
        "description": "Vendor payment against outstanding",
        "amount": 81175.46,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 14,
        "date": "2024-01-09",
        "description": "Sales to Lucky Hosiery",
        "amount": 283063.53,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 15,
        "date": "2024-01-09",
        "description": "GST collected on sales",
        "amount": 50951.44,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 16,
        "date": "2024-01-09",
        "description": "Vendor payment against outstanding",
        "amount": 135578.84,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 17,
        "date": "2024-01-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 18,
        "date": "2024-01-10",
        "description": "Interest paid on bank loan",
        "amount": 12028.67,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 19,
        "date": "2024-01-10",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 275301.52,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 20,
        "date": "2024-01-10",
        "description": "GST input on inventory",
        "amount": 49554.27,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 21,
        "date": "2024-01-12",
        "description": "Sales to Lucky Hosiery",
        "amount": 169520.82,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 22,
        "date": "2024-01-12",
        "description": "GST collected on sales",
        "amount": 30513.75,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 23,
        "date": "2024-01-15",
        "description": "GST payment to government",
        "amount": 62136.67,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 24,
        "date": "2024-01-15",
        "description": "TDS payment to government",
        "amount": 8333.39,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 25,
        "date": "2024-01-16",
        "description": "Sales to Lucky Hosiery",
        "amount": 236532.8,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 26,
        "date": "2024-01-16",
        "description": "GST collected on sales",
        "amount": 42575.9,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 27,
        "date": "2024-01-17",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 212658.68,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 28,
        "date": "2024-01-17",
        "description": "GST input on inventory",
        "amount": 38278.56,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 29,
        "date": "2024-01-17",
        "description": "Digital marketing campaign",
        "amount": 20006.48,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 30,
        "date": "2024-01-18",
        "description": "Statutory audit fees",
        "amount": 42566.91,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 31,
        "date": "2024-01-19",
        "description": "Sales to Lucky Hosiery",
        "amount": 153090.02,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 32,
        "date": "2024-01-19",
        "description": "GST collected on sales",
        "amount": 27556.2,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 33,
        "date": "2024-01-19",
        "description": "Advance received for large order",
        "amount": 51106.88,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 34,
        "date": "2024-01-20",
        "description": "Payment received from customer",
        "amount": 198255.83,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 35,
        "date": "2024-01-23",
        "description": "Sales to Bombay Fashion House",
        "amount": 344867.04,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 36,
        "date": "2024-01-23",
        "description": "GST collected on sales",
        "amount": 62076.07,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 37,
        "date": "2024-01-23",
        "description": "Sale of old machinery",
        "amount": 72507.75,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 38,
        "date": "2024-01-24",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 184620.61,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 39,
        "date": "2024-01-24",
        "description": "GST input on inventory",
        "amount": 33231.71,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 40,
        "date": "2024-01-25",
        "description": "Fuel for delivery vehicles",
        "amount": 11140.53,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 41,
        "date": "2024-01-26",
        "description": "Sales to Rajan Fabrics",
        "amount": 322767.61,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 42,
        "date": "2024-01-26",
        "description": "GST collected on sales",
        "amount": 58098.17,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 43,
        "date": "2024-01-26",
        "description": "Sales return from customer",
        "amount": 28004.11,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 44,
        "date": "2024-01-28",
        "description": "Advance corporate tax payment",
        "amount": 60778.12,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 45,
        "date": "2024-01-28",
        "description": "Sale of old machinery",
        "amount": 85132.15,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 46,
        "date": "2024-01-30",
        "description": "Sales to Bombay Fashion House",
        "amount": 215588.82,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 47,
        "date": "2024-01-30",
        "description": "GST collected on sales",
        "amount": 38805.99,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 48,
        "date": "2024-01-31",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 211651.11,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 49,
        "date": "2024-01-31",
        "description": "GST input on inventory",
        "amount": 38097.2,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 50,
        "date": "2024-02-01",
        "description": "Office rent paid",
        "amount": 43242.64,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 51,
        "date": "2024-02-01",
        "description": "Salary paid to employees",
        "amount": 75851.98,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 52,
        "date": "2024-02-02",
        "description": "Sales to Rajan Fabrics",
        "amount": 297387.15,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 53,
        "date": "2024-02-02",
        "description": "GST collected on sales",
        "amount": 53529.69,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 54,
        "date": "2024-02-05",
        "description": "Electricity bill payment",
        "amount": 11953.34,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 55,
        "date": "2024-02-05",
        "description": "Water and utility charges",
        "amount": 5004.29,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 56,
        "date": "2024-02-06",
        "description": "Sales to Rajan Fabrics",
        "amount": 165329.87,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 57,
        "date": "2024-02-06",
        "description": "GST collected on sales",
        "amount": 29759.38,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 58,
        "date": "2024-02-06",
        "description": "Customs duty on imports",
        "amount": 30573.67,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 59,
        "date": "2024-02-07",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 233645.06,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 60,
        "date": "2024-02-07",
        "description": "GST input on inventory",
        "amount": 42056.11,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 61,
        "date": "2024-02-08",
        "description": "Digital marketing campaign",
        "amount": 17224.53,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 62,
        "date": "2024-02-09",
        "description": "Sales to Mehta Garments",
        "amount": 172318.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 63,
        "date": "2024-02-09",
        "description": "GST collected on sales",
        "amount": 31017.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 64,
        "date": "2024-02-09",
        "description": "Depreciation charged on assets",
        "amount": 28312.49,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 65,
        "date": "2024-02-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 66,
        "date": "2024-02-10",
        "description": "Interest paid on bank loan",
        "amount": 13447.56,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 67,
        "date": "2024-02-10",
        "description": "Forex loss on import payables",
        "amount": 7310.31,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 68,
        "date": "2024-02-13",
        "description": "Sales to Lucky Hosiery",
        "amount": 259176.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 69,
        "date": "2024-02-13",
        "description": "GST collected on sales",
        "amount": 46651.86,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 70,
        "date": "2024-02-14",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 233617.2,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 71,
        "date": "2024-02-14",
        "description": "GST input on inventory",
        "amount": 42051.1,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 72,
        "date": "2024-02-14",
        "description": "Scrap sale proceeds",
        "amount": 3515.16,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 73,
        "date": "2024-02-15",
        "description": "GST payment to government",
        "amount": 65497.67,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 74,
        "date": "2024-02-15",
        "description": "TDS payment to government",
        "amount": 10236.3,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 75,
        "date": "2024-02-15",
        "description": "GST reversal on sales return",
        "amount": 1866.28,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 76,
        "date": "2024-02-16",
        "description": "Sales to Rajan Fabrics",
        "amount": 286143.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 77,
        "date": "2024-02-16",
        "description": "GST collected on sales",
        "amount": 51505.85,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 78,
        "date": "2024-02-17",
        "description": "Interim dividend payout",
        "amount": 102238.68,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 79,
        "date": "2024-02-20",
        "description": "Sales to Mehta Garments",
        "amount": 315715.13,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 80,
        "date": "2024-02-20",
        "description": "GST collected on sales",
        "amount": 56828.72,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 81,
        "date": "2024-02-20",
        "description": "Employee performance bonus",
        "amount": 43552.13,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 82,
        "date": "2024-02-21",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 260716.28,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 83,
        "date": "2024-02-21",
        "description": "GST input on inventory",
        "amount": 46928.93,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 84,
        "date": "2024-02-22",
        "description": "Advance corporate tax payment",
        "amount": 99614.0,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 85,
        "date": "2024-02-23",
        "description": "Sales to Bombay Fashion House",
        "amount": 244553.65,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 86,
        "date": "2024-02-23",
        "description": "GST collected on sales",
        "amount": 44019.66,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 87,
        "date": "2024-02-25",
        "description": "Customs duty on imports",
        "amount": 42783.96,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 88,
        "date": "2024-02-25",
        "description": "Further equity capital introduced",
        "amount": 652728.51,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 89,
        "date": "2024-02-27",
        "description": "Sales to Lucky Hosiery",
        "amount": 265115.2,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 90,
        "date": "2024-02-27",
        "description": "GST collected on sales",
        "amount": 47720.74,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 91,
        "date": "2024-02-28",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 216048.27,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 92,
        "date": "2024-02-28",
        "description": "GST input on inventory",
        "amount": 38888.69,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 93,
        "date": "2024-03-01",
        "description": "Office rent paid",
        "amount": 44613.68,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 94,
        "date": "2024-03-01",
        "description": "Salary paid to employees",
        "amount": 82737.75,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 95,
        "date": "2024-03-01",
        "description": "Sales to Bombay Fashion House",
        "amount": 276190.55,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 96,
        "date": "2024-03-01",
        "description": "GST collected on sales",
        "amount": 49714.3,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 97,
        "date": "2024-03-03",
        "description": "Payment received from customer",
        "amount": 188679.2,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 98,
        "date": "2024-03-05",
        "description": "Electricity bill payment",
        "amount": 15993.07,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 99,
        "date": "2024-03-05",
        "description": "Water and utility charges",
        "amount": 4332.05,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 100,
        "date": "2024-03-05",
        "description": "Sales to Lucky Hosiery",
        "amount": 262929.97,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 101,
        "date": "2024-03-05",
        "description": "GST collected on sales",
        "amount": 47327.39,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 102,
        "date": "2024-03-05",
        "description": "Employee performance bonus",
        "amount": 43699.19,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 103,
        "date": "2024-03-06",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 214254.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 104,
        "date": "2024-03-06",
        "description": "GST input on inventory",
        "amount": 38565.74,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 105,
        "date": "2024-03-07",
        "description": "Forex loss on import payables",
        "amount": 7929.79,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 106,
        "date": "2024-03-08",
        "description": "Sales to Bombay Fashion House",
        "amount": 256015.28,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 107,
        "date": "2024-03-08",
        "description": "GST collected on sales",
        "amount": 46082.75,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 108,
        "date": "2024-03-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 109,
        "date": "2024-03-10",
        "description": "Interest paid on bank loan",
        "amount": 14358.42,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 110,
        "date": "2024-03-11",
        "description": "Advance corporate tax payment",
        "amount": 73499.64,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 111,
        "date": "2024-03-12",
        "description": "Sales to Rajan Fabrics",
        "amount": 197552.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 112,
        "date": "2024-03-12",
        "description": "GST collected on sales",
        "amount": 35559.43,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 113,
        "date": "2024-03-13",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 250272.94,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 114,
        "date": "2024-03-13",
        "description": "GST input on inventory",
        "amount": 45049.13,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 115,
        "date": "2024-03-15",
        "description": "GST payment to government",
        "amount": 58424.58,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 116,
        "date": "2024-03-15",
        "description": "TDS payment to government",
        "amount": 14749.03,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 117,
        "date": "2024-03-15",
        "description": "Sales to Bombay Fashion House",
        "amount": 294424.2,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 118,
        "date": "2024-03-15",
        "description": "GST collected on sales",
        "amount": 52996.36,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 119,
        "date": "2024-03-16",
        "description": "Miscellaneous office expenses",
        "amount": 1790.09,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 120,
        "date": "2024-03-19",
        "description": "Sales to Rajan Fabrics",
        "amount": 183779.93,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 121,
        "date": "2024-03-19",
        "description": "GST collected on sales",
        "amount": 33080.39,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 122,
        "date": "2024-03-20",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 209985.22,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 123,
        "date": "2024-03-20",
        "description": "GST input on inventory",
        "amount": 37797.34,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 124,
        "date": "2024-03-20",
        "description": "Customs duty on imports",
        "amount": 24511.14,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 125,
        "date": "2024-03-20",
        "description": "Sale of old machinery",
        "amount": 79555.99,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 126,
        "date": "2024-03-21",
        "description": "Purchase of new office equipment",
        "amount": 110072.74,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 127,
        "date": "2024-03-22",
        "description": "Sales to Bombay Fashion House",
        "amount": 185437.44,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 128,
        "date": "2024-03-22",
        "description": "GST collected on sales",
        "amount": 33378.74,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 129,
        "date": "2024-03-26",
        "description": "Sales to Mehta Garments",
        "amount": 225081.47,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 130,
        "date": "2024-03-26",
        "description": "GST collected on sales",
        "amount": 40514.66,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 131,
        "date": "2024-03-26",
        "description": "Employee travel reimbursement",
        "amount": 11068.25,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 132,
        "date": "2024-03-27",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 263559.83,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 133,
        "date": "2024-03-27",
        "description": "GST input on inventory",
        "amount": 47440.77,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 134,
        "date": "2024-03-29",
        "description": "Sales to Mehta Garments",
        "amount": 242679.85,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 135,
        "date": "2024-03-29",
        "description": "GST collected on sales",
        "amount": 43682.37,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 136,
        "date": "2024-04-01",
        "description": "Office rent paid",
        "amount": 40876.19,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 137,
        "date": "2024-04-01",
        "description": "Salary paid to employees",
        "amount": 78710.42,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 138,
        "date": "2024-04-02",
        "description": "Sales to Lucky Hosiery",
        "amount": 202800.93,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 139,
        "date": "2024-04-02",
        "description": "GST collected on sales",
        "amount": 36504.17,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 140,
        "date": "2024-04-02",
        "description": "Monthly bank processing fees",
        "amount": 1755.94,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 141,
        "date": "2024-04-03",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 266455.49,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 142,
        "date": "2024-04-03",
        "description": "GST input on inventory",
        "amount": 47961.99,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 143,
        "date": "2024-04-03",
        "description": "Software license capitalization",
        "amount": 60550.71,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 144,
        "date": "2024-04-03",
        "description": "GST reversal on sales return",
        "amount": 3814.58,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 145,
        "date": "2024-04-05",
        "description": "Electricity bill payment",
        "amount": 15468.87,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 146,
        "date": "2024-04-05",
        "description": "Water and utility charges",
        "amount": 4912.18,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 147,
        "date": "2024-04-05",
        "description": "Sales to Mehta Garments",
        "amount": 334632.69,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 148,
        "date": "2024-04-05",
        "description": "GST collected on sales",
        "amount": 60233.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 149,
        "date": "2024-04-05",
        "description": "Purchase of new office equipment",
        "amount": 108220.48,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 150,
        "date": "2024-04-09",
        "description": "Sales to Lucky Hosiery",
        "amount": 310387.28,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 151,
        "date": "2024-04-09",
        "description": "GST collected on sales",
        "amount": 55869.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 152,
        "date": "2024-04-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 153,
        "date": "2024-04-10",
        "description": "Interest paid on bank loan",
        "amount": 12206.98,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 154,
        "date": "2024-04-10",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 215548.98,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 155,
        "date": "2024-04-10",
        "description": "GST input on inventory",
        "amount": 38798.82,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 156,
        "date": "2024-04-12",
        "description": "Sales to Lucky Hosiery",
        "amount": 231381.72,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 157,
        "date": "2024-04-12",
        "description": "GST collected on sales",
        "amount": 41648.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 158,
        "date": "2024-04-12",
        "description": "Vendor payment against outstanding",
        "amount": 89683.39,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 159,
        "date": "2024-04-13",
        "description": "Sale of old machinery",
        "amount": 87421.7,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 160,
        "date": "2024-04-14",
        "description": "Brokerage and commission paid",
        "amount": 17936.92,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 161,
        "date": "2024-04-14",
        "description": "Forex loss on import payables",
        "amount": 2164.6,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 162,
        "date": "2024-04-15",
        "description": "GST payment to government",
        "amount": 63498.08,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 163,
        "date": "2024-04-15",
        "description": "TDS payment to government",
        "amount": 9854.87,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 164,
        "date": "2024-04-15",
        "description": "Vehicle maintenance and repair",
        "amount": 9912.58,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 165,
        "date": "2024-04-16",
        "description": "Sales to Lucky Hosiery",
        "amount": 325801.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 166,
        "date": "2024-04-16",
        "description": "GST collected on sales",
        "amount": 58644.19,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 167,
        "date": "2024-04-17",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 200776.01,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 168,
        "date": "2024-04-17",
        "description": "GST input on inventory",
        "amount": 36139.68,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 169,
        "date": "2024-04-19",
        "description": "Sales to Rajan Fabrics",
        "amount": 314577.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 170,
        "date": "2024-04-19",
        "description": "GST collected on sales",
        "amount": 56624.03,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 171,
        "date": "2024-04-19",
        "description": "Vendor payment against outstanding",
        "amount": 131013.15,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 172,
        "date": "2024-04-23",
        "description": "Sales to Lucky Hosiery",
        "amount": 156674.91,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 173,
        "date": "2024-04-23",
        "description": "GST collected on sales",
        "amount": 28201.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 174,
        "date": "2024-04-24",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 232359.28,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 175,
        "date": "2024-04-24",
        "description": "GST input on inventory",
        "amount": 41824.67,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 176,
        "date": "2024-04-24",
        "description": "Fuel for delivery vehicles",
        "amount": 12466.36,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 177,
        "date": "2024-04-26",
        "description": "Sales to Mehta Garments",
        "amount": 215250.54,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 178,
        "date": "2024-04-26",
        "description": "GST collected on sales",
        "amount": 38745.1,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 179,
        "date": "2024-04-27",
        "description": "Customs duty on imports",
        "amount": 34921.65,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 180,
        "date": "2024-04-28",
        "description": "Forex gain on export receivables",
        "amount": 3521.72,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 181,
        "date": "2024-04-29",
        "description": "Scrap sale proceeds",
        "amount": 4659.57,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 182,
        "date": "2024-04-30",
        "description": "Sales to Rajan Fabrics",
        "amount": 224795.7,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 183,
        "date": "2024-04-30",
        "description": "GST collected on sales",
        "amount": 40463.23,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 184,
        "date": "2024-05-01",
        "description": "Office rent paid",
        "amount": 48496.46,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 185,
        "date": "2024-05-01",
        "description": "Salary paid to employees",
        "amount": 72906.02,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 186,
        "date": "2024-05-01",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 270320.83,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 187,
        "date": "2024-05-01",
        "description": "GST input on inventory",
        "amount": 48657.75,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 188,
        "date": "2024-05-01",
        "description": "Payment received from customer",
        "amount": 102164.03,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 189,
        "date": "2024-05-02",
        "description": "Digital marketing campaign",
        "amount": 23249.32,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 190,
        "date": "2024-05-03",
        "description": "Sales to Lucky Hosiery",
        "amount": 321476.48,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 191,
        "date": "2024-05-03",
        "description": "GST collected on sales",
        "amount": 57865.77,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 192,
        "date": "2024-05-04",
        "description": "Employee travel reimbursement",
        "amount": 4738.0,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 193,
        "date": "2024-05-04",
        "description": "Courier and postage charges",
        "amount": 1222.66,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 194,
        "date": "2024-05-05",
        "description": "Electricity bill payment",
        "amount": 12304.46,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 195,
        "date": "2024-05-05",
        "description": "Water and utility charges",
        "amount": 3949.67,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 196,
        "date": "2024-05-07",
        "description": "Sales to Bombay Fashion House",
        "amount": 333465.33,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 197,
        "date": "2024-05-07",
        "description": "GST collected on sales",
        "amount": 60023.76,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 198,
        "date": "2024-05-08",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 191704.94,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 199,
        "date": "2024-05-08",
        "description": "GST input on inventory",
        "amount": 34506.89,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 200,
        "date": "2024-05-08",
        "description": "Forex gain on export receivables",
        "amount": 6455.59,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 201,
        "date": "2024-05-08",
        "description": "Advance corporate tax payment",
        "amount": 65702.87,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 202,
        "date": "2024-05-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 203,
        "date": "2024-05-10",
        "description": "Interest paid on bank loan",
        "amount": 14186.04,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 204,
        "date": "2024-05-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 317970.91,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 205,
        "date": "2024-05-10",
        "description": "GST collected on sales",
        "amount": 57234.76,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 206,
        "date": "2024-05-11",
        "description": "Fuel for delivery vehicles",
        "amount": 14033.41,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 207,
        "date": "2024-05-11",
        "description": "Accumulated depreciation recorded",
        "amount": 19953.77,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 208,
        "date": "2024-05-13",
        "description": "Interim dividend payout",
        "amount": 100314.71,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 209,
        "date": "2024-05-14",
        "description": "Sales to Rajan Fabrics",
        "amount": 319017.13,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 210,
        "date": "2024-05-14",
        "description": "GST collected on sales",
        "amount": 57423.08,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 211,
        "date": "2024-05-15",
        "description": "GST payment to government",
        "amount": 63032.25,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 212,
        "date": "2024-05-15",
        "description": "TDS payment to government",
        "amount": 13623.4,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 213,
        "date": "2024-05-15",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 195712.22,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 214,
        "date": "2024-05-15",
        "description": "GST input on inventory",
        "amount": 35228.2,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 215,
        "date": "2024-05-15",
        "description": "Customs duty on imports",
        "amount": 44076.85,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 216,
        "date": "2024-05-17",
        "description": "Sales to Mehta Garments",
        "amount": 225159.21,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 217,
        "date": "2024-05-17",
        "description": "GST collected on sales",
        "amount": 40528.66,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 218,
        "date": "2024-05-18",
        "description": "Forex gain on export receivables",
        "amount": 3721.73,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 219,
        "date": "2024-05-18",
        "description": "Interim dividend payout",
        "amount": 155889.74,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 220,
        "date": "2024-05-21",
        "description": "Sales to Lucky Hosiery",
        "amount": 263040.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 221,
        "date": "2024-05-21",
        "description": "GST collected on sales",
        "amount": 47347.21,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 222,
        "date": "2024-05-22",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 234241.37,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 223,
        "date": "2024-05-22",
        "description": "GST input on inventory",
        "amount": 42163.45,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 224,
        "date": "2024-05-22",
        "description": "Purchase return to vendor",
        "amount": 23260.49,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 225,
        "date": "2024-05-24",
        "description": "Sales to Mehta Garments",
        "amount": 284981.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 226,
        "date": "2024-05-24",
        "description": "GST collected on sales",
        "amount": 51296.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 227,
        "date": "2024-05-24",
        "description": "Legal and consultancy fees",
        "amount": 25979.31,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 228,
        "date": "2024-05-24",
        "description": "Interim dividend payout",
        "amount": 142795.47,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 229,
        "date": "2024-05-25",
        "description": "Printing and stationery",
        "amount": 2471.98,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 230,
        "date": "2024-05-27",
        "description": "Payment received from customer",
        "amount": 178363.85,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 231,
        "date": "2024-05-27",
        "description": "Digital marketing campaign",
        "amount": 17319.86,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 232,
        "date": "2024-05-28",
        "description": "Sales to Bombay Fashion House",
        "amount": 201629.91,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 233,
        "date": "2024-05-28",
        "description": "GST collected on sales",
        "amount": 36293.38,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 234,
        "date": "2024-05-28",
        "description": "GST reversal on sales return",
        "amount": 4695.67,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 235,
        "date": "2024-05-29",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 258269.53,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 236,
        "date": "2024-05-29",
        "description": "GST input on inventory",
        "amount": 46488.52,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 237,
        "date": "2024-05-29",
        "description": "Sale of old machinery",
        "amount": 73543.2,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 238,
        "date": "2024-05-30",
        "description": "Monthly bank processing fees",
        "amount": 958.43,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 239,
        "date": "2024-05-31",
        "description": "Sales to Lucky Hosiery",
        "amount": 197991.44,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 240,
        "date": "2024-05-31",
        "description": "GST collected on sales",
        "amount": 35638.46,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 241,
        "date": "2024-06-01",
        "description": "Office rent paid",
        "amount": 46884.0,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 242,
        "date": "2024-06-01",
        "description": "Salary paid to employees",
        "amount": 86406.94,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 243,
        "date": "2024-06-01",
        "description": "Mutual fund investment",
        "amount": 58780.16,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 244,
        "date": "2024-06-04",
        "description": "Sales to Lucky Hosiery",
        "amount": 269166.54,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 245,
        "date": "2024-06-04",
        "description": "GST collected on sales",
        "amount": 48449.98,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 246,
        "date": "2024-06-04",
        "description": "Printing and stationery",
        "amount": 7654.28,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 247,
        "date": "2024-06-05",
        "description": "Electricity bill payment",
        "amount": 11305.6,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 248,
        "date": "2024-06-05",
        "description": "Water and utility charges",
        "amount": 5610.94,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 249,
        "date": "2024-06-05",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 204162.9,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 250,
        "date": "2024-06-05",
        "description": "GST input on inventory",
        "amount": 36749.32,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 251,
        "date": "2024-06-07",
        "description": "Sales to Bombay Fashion House",
        "amount": 221150.7,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 252,
        "date": "2024-06-07",
        "description": "GST collected on sales",
        "amount": 39807.13,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 253,
        "date": "2024-06-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 254,
        "date": "2024-06-10",
        "description": "Interest paid on bank loan",
        "amount": 13385.44,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 255,
        "date": "2024-06-10",
        "description": "Forex gain on export receivables",
        "amount": 8886.63,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 256,
        "date": "2024-06-10",
        "description": "Software license capitalization",
        "amount": 42214.63,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 257,
        "date": "2024-06-11",
        "description": "Sales to Rajan Fabrics",
        "amount": 241823.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 258,
        "date": "2024-06-11",
        "description": "GST collected on sales",
        "amount": 43528.21,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 259,
        "date": "2024-06-12",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 216223.65,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 260,
        "date": "2024-06-12",
        "description": "GST input on inventory",
        "amount": 38920.26,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 261,
        "date": "2024-06-13",
        "description": "Advance received for large order",
        "amount": 85203.41,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 262,
        "date": "2024-06-14",
        "description": "Sales to Rajan Fabrics",
        "amount": 329502.3,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 263,
        "date": "2024-06-14",
        "description": "GST collected on sales",
        "amount": 59310.41,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 264,
        "date": "2024-06-15",
        "description": "GST payment to government",
        "amount": 48861.14,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 265,
        "date": "2024-06-15",
        "description": "TDS payment to government",
        "amount": 12203.84,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 266,
        "date": "2024-06-15",
        "description": "GST reversal on sales return",
        "amount": 3690.64,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 267,
        "date": "2024-06-18",
        "description": "Sales to Lucky Hosiery",
        "amount": 170628.83,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 268,
        "date": "2024-06-18",
        "description": "GST collected on sales",
        "amount": 30713.19,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 269,
        "date": "2024-06-19",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 188682.07,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 270,
        "date": "2024-06-19",
        "description": "GST input on inventory",
        "amount": 33962.77,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 271,
        "date": "2024-06-21",
        "description": "Sales to Rajan Fabrics",
        "amount": 199036.23,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 272,
        "date": "2024-06-21",
        "description": "GST collected on sales",
        "amount": 35826.52,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 273,
        "date": "2024-06-21",
        "description": "GST reversal on sales return",
        "amount": 4359.65,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 274,
        "date": "2024-06-23",
        "description": "Employee travel reimbursement",
        "amount": 8518.21,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 275,
        "date": "2024-06-25",
        "description": "Sales to Mehta Garments",
        "amount": 338920.42,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 276,
        "date": "2024-06-25",
        "description": "GST collected on sales",
        "amount": 61005.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 277,
        "date": "2024-06-26",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 251074.2,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 278,
        "date": "2024-06-26",
        "description": "GST input on inventory",
        "amount": 45193.36,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 279,
        "date": "2024-06-27",
        "description": "Monthly bank processing fees",
        "amount": 578.17,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 280,
        "date": "2024-06-28",
        "description": "Sales to Bombay Fashion House",
        "amount": 170626.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 281,
        "date": "2024-06-28",
        "description": "GST collected on sales",
        "amount": 30712.73,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 282,
        "date": "2024-06-30",
        "description": "Customs duty on imports",
        "amount": 39779.39,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 283,
        "date": "2024-07-01",
        "description": "Office rent paid",
        "amount": 49528.29,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 284,
        "date": "2024-07-01",
        "description": "Salary paid to employees",
        "amount": 81409.12,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 285,
        "date": "2024-07-01",
        "description": "Vendor payment against outstanding",
        "amount": 129145.95,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 286,
        "date": "2024-07-02",
        "description": "Sales to Bombay Fashion House",
        "amount": 296727.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 287,
        "date": "2024-07-02",
        "description": "GST collected on sales",
        "amount": 53410.87,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 288,
        "date": "2024-07-02",
        "description": "Mutual fund investment",
        "amount": 160384.03,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 289,
        "date": "2024-07-03",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 257668.49,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 290,
        "date": "2024-07-03",
        "description": "GST input on inventory",
        "amount": 46380.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 291,
        "date": "2024-07-03",
        "description": "Legal and consultancy fees",
        "amount": 37741.65,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 292,
        "date": "2024-07-04",
        "description": "Miscellaneous office expenses",
        "amount": 1235.02,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 293,
        "date": "2024-07-05",
        "description": "Electricity bill payment",
        "amount": 15015.51,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 294,
        "date": "2024-07-05",
        "description": "Water and utility charges",
        "amount": 3796.35,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 295,
        "date": "2024-07-05",
        "description": "Sales to Rajan Fabrics",
        "amount": 233628.67,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 296,
        "date": "2024-07-05",
        "description": "GST collected on sales",
        "amount": 42053.16,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 297,
        "date": "2024-07-06",
        "description": "Customs duty on imports",
        "amount": 23197.96,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 298,
        "date": "2024-07-07",
        "description": "Employee travel reimbursement",
        "amount": 11004.09,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 299,
        "date": "2024-07-08",
        "description": "Vendor payment against outstanding",
        "amount": 94749.01,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 300,
        "date": "2024-07-09",
        "description": "Sales to Rajan Fabrics",
        "amount": 189434.26,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 301,
        "date": "2024-07-09",
        "description": "GST collected on sales",
        "amount": 34098.17,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 302,
        "date": "2024-07-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 303,
        "date": "2024-07-10",
        "description": "Interest paid on bank loan",
        "amount": 13809.91,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 304,
        "date": "2024-07-10",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 218565.88,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 305,
        "date": "2024-07-10",
        "description": "GST input on inventory",
        "amount": 39341.86,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 306,
        "date": "2024-07-10",
        "description": "Depreciation charged on assets",
        "amount": 25435.08,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 307,
        "date": "2024-07-10",
        "description": "Legal and consultancy fees",
        "amount": 36025.12,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 308,
        "date": "2024-07-12",
        "description": "Sales to Lucky Hosiery",
        "amount": 183786.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 309,
        "date": "2024-07-12",
        "description": "GST collected on sales",
        "amount": 33081.64,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 310,
        "date": "2024-07-12",
        "description": "Interest earned on FD",
        "amount": 6340.69,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 311,
        "date": "2024-07-12",
        "description": "Printing and stationery",
        "amount": 2349.96,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 312,
        "date": "2024-07-15",
        "description": "GST payment to government",
        "amount": 53769.37,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 313,
        "date": "2024-07-15",
        "description": "TDS payment to government",
        "amount": 10822.03,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 314,
        "date": "2024-07-16",
        "description": "Sales to Bombay Fashion House",
        "amount": 273959.61,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 315,
        "date": "2024-07-16",
        "description": "GST collected on sales",
        "amount": 49312.73,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 316,
        "date": "2024-07-16",
        "description": "Employee performance bonus",
        "amount": 32668.27,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 317,
        "date": "2024-07-16",
        "description": "Digital marketing campaign",
        "amount": 16139.1,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 318,
        "date": "2024-07-17",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 232209.06,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 319,
        "date": "2024-07-17",
        "description": "GST input on inventory",
        "amount": 41797.63,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 320,
        "date": "2024-07-17",
        "description": "Miscellaneous office expenses",
        "amount": 2145.44,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 321,
        "date": "2024-07-18",
        "description": "Digital marketing campaign",
        "amount": 15445.92,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 322,
        "date": "2024-07-18",
        "description": "Purchase of new office equipment",
        "amount": 91136.44,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 323,
        "date": "2024-07-19",
        "description": "Sales to Bombay Fashion House",
        "amount": 219307.07,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 324,
        "date": "2024-07-19",
        "description": "GST collected on sales",
        "amount": 39475.27,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 325,
        "date": "2024-07-19",
        "description": "Monthly bank processing fees",
        "amount": 721.25,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 326,
        "date": "2024-07-20",
        "description": "Advance received for large order",
        "amount": 87289.58,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 327,
        "date": "2024-07-23",
        "description": "Sales to Lucky Hosiery",
        "amount": 262526.72,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 328,
        "date": "2024-07-23",
        "description": "GST collected on sales",
        "amount": 47254.81,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 329,
        "date": "2024-07-24",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 219216.32,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 330,
        "date": "2024-07-24",
        "description": "GST input on inventory",
        "amount": 39458.94,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 331,
        "date": "2024-07-25",
        "description": "Further equity capital introduced",
        "amount": 914342.25,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 332,
        "date": "2024-07-26",
        "description": "Sales to Lucky Hosiery",
        "amount": 281676.92,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 333,
        "date": "2024-07-26",
        "description": "GST collected on sales",
        "amount": 50701.85,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 334,
        "date": "2024-07-28",
        "description": "Advance corporate tax payment",
        "amount": 87045.92,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 335,
        "date": "2024-07-29",
        "description": "Annual insurance premium",
        "amount": 22964.8,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 336,
        "date": "2024-07-30",
        "description": "Sales to Mehta Garments",
        "amount": 165599.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 337,
        "date": "2024-07-30",
        "description": "GST collected on sales",
        "amount": 29807.99,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 338,
        "date": "2024-07-31",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 245194.29,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 339,
        "date": "2024-07-31",
        "description": "GST input on inventory",
        "amount": 44134.97,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 340,
        "date": "2024-07-31",
        "description": "Advance corporate tax payment",
        "amount": 79375.58,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 341,
        "date": "2024-08-01",
        "description": "Office rent paid",
        "amount": 42073.05,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 342,
        "date": "2024-08-01",
        "description": "Salary paid to employees",
        "amount": 86008.31,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 343,
        "date": "2024-08-02",
        "description": "Sales to Mehta Garments",
        "amount": 257136.52,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 344,
        "date": "2024-08-02",
        "description": "GST collected on sales",
        "amount": 46284.57,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 345,
        "date": "2024-08-02",
        "description": "Digital marketing campaign",
        "amount": 22017.86,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 346,
        "date": "2024-08-02",
        "description": "Vehicle maintenance and repair",
        "amount": 13671.43,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 347,
        "date": "2024-08-05",
        "description": "Electricity bill payment",
        "amount": 15321.0,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 348,
        "date": "2024-08-05",
        "description": "Water and utility charges",
        "amount": 3526.66,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 349,
        "date": "2024-08-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 262197.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 350,
        "date": "2024-08-06",
        "description": "GST collected on sales",
        "amount": 47195.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 351,
        "date": "2024-08-06",
        "description": "Interest earned on FD",
        "amount": 6991.98,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 352,
        "date": "2024-08-06",
        "description": "Vendor payment against outstanding",
        "amount": 136570.81,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 353,
        "date": "2024-08-07",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 218847.85,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 354,
        "date": "2024-08-07",
        "description": "GST input on inventory",
        "amount": 39392.61,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 355,
        "date": "2024-08-08",
        "description": "Legal and consultancy fees",
        "amount": 24399.66,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 356,
        "date": "2024-08-09",
        "description": "Sales to Rajan Fabrics",
        "amount": 209289.35,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 357,
        "date": "2024-08-09",
        "description": "GST collected on sales",
        "amount": 37672.08,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 358,
        "date": "2024-08-09",
        "description": "Forex loss on import payables",
        "amount": 7179.01,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 359,
        "date": "2024-08-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 360,
        "date": "2024-08-10",
        "description": "Interest paid on bank loan",
        "amount": 12617.29,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 361,
        "date": "2024-08-11",
        "description": "GST reversal on sales return",
        "amount": 3566.69,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 362,
        "date": "2024-08-11",
        "description": "Vendor payment against outstanding",
        "amount": 120518.2,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 363,
        "date": "2024-08-13",
        "description": "Sales to Rajan Fabrics",
        "amount": 242205.58,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 364,
        "date": "2024-08-13",
        "description": "GST collected on sales",
        "amount": 43597.01,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 365,
        "date": "2024-08-14",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 267036.55,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 366,
        "date": "2024-08-14",
        "description": "GST input on inventory",
        "amount": 48066.58,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 367,
        "date": "2024-08-15",
        "description": "GST payment to government",
        "amount": 45850.74,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 368,
        "date": "2024-08-15",
        "description": "TDS payment to government",
        "amount": 10047.16,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 369,
        "date": "2024-08-16",
        "description": "Sales to Rajan Fabrics",
        "amount": 348428.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 370,
        "date": "2024-08-16",
        "description": "GST collected on sales",
        "amount": 62717.09,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 371,
        "date": "2024-08-18",
        "description": "Advance corporate tax payment",
        "amount": 89651.34,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 372,
        "date": "2024-08-20",
        "description": "Sales to Bombay Fashion House",
        "amount": 294324.38,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 373,
        "date": "2024-08-20",
        "description": "GST collected on sales",
        "amount": 52978.39,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 374,
        "date": "2024-08-20",
        "description": "Fuel for delivery vehicles",
        "amount": 12980.21,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 375,
        "date": "2024-08-21",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 243903.0,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 376,
        "date": "2024-08-21",
        "description": "GST input on inventory",
        "amount": 43902.54,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 377,
        "date": "2024-08-23",
        "description": "Sales to Mehta Garments",
        "amount": 151101.02,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 378,
        "date": "2024-08-23",
        "description": "GST collected on sales",
        "amount": 27198.18,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 379,
        "date": "2024-08-24",
        "description": "Scrap sale proceeds",
        "amount": 8208.41,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 380,
        "date": "2024-08-26",
        "description": "Accumulated depreciation recorded",
        "amount": 34840.4,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 381,
        "date": "2024-08-27",
        "description": "Sales to Rajan Fabrics",
        "amount": 342185.58,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 382,
        "date": "2024-08-27",
        "description": "GST collected on sales",
        "amount": 61593.4,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 383,
        "date": "2024-08-28",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 241491.09,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 384,
        "date": "2024-08-28",
        "description": "GST input on inventory",
        "amount": 43468.4,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 385,
        "date": "2024-08-28",
        "description": "Digital marketing campaign",
        "amount": 22403.55,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 386,
        "date": "2024-08-30",
        "description": "Sales to Lucky Hosiery",
        "amount": 262592.38,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 387,
        "date": "2024-08-30",
        "description": "GST collected on sales",
        "amount": 47266.63,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 388,
        "date": "2024-08-30",
        "description": "Forex loss on import payables",
        "amount": 7811.23,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 389,
        "date": "2024-08-31",
        "description": "Legal and consultancy fees",
        "amount": 25357.48,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 390,
        "date": "2024-09-01",
        "description": "Office rent paid",
        "amount": 44271.52,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 391,
        "date": "2024-09-01",
        "description": "Salary paid to employees",
        "amount": 73731.31,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 392,
        "date": "2024-09-01",
        "description": "Printing and stationery",
        "amount": 7864.95,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 393,
        "date": "2024-09-03",
        "description": "Sales to Rajan Fabrics",
        "amount": 339767.43,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 394,
        "date": "2024-09-03",
        "description": "GST collected on sales",
        "amount": 61158.14,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 395,
        "date": "2024-09-03",
        "description": "Sales return from customer",
        "amount": 27674.52,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 396,
        "date": "2024-09-04",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 268997.43,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 397,
        "date": "2024-09-04",
        "description": "GST input on inventory",
        "amount": 48419.54,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 398,
        "date": "2024-09-05",
        "description": "Electricity bill payment",
        "amount": 15225.1,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 399,
        "date": "2024-09-05",
        "description": "Water and utility charges",
        "amount": 5897.42,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 400,
        "date": "2024-09-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 194076.9,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 401,
        "date": "2024-09-06",
        "description": "GST collected on sales",
        "amount": 34933.84,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 402,
        "date": "2024-09-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 403,
        "date": "2024-09-10",
        "description": "Interest paid on bank loan",
        "amount": 15781.49,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 404,
        "date": "2024-09-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 199707.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 405,
        "date": "2024-09-10",
        "description": "GST collected on sales",
        "amount": 35947.37,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 406,
        "date": "2024-09-11",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 260758.31,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 407,
        "date": "2024-09-11",
        "description": "GST input on inventory",
        "amount": 46936.5,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 408,
        "date": "2024-09-13",
        "description": "Sales to Bombay Fashion House",
        "amount": 239508.25,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 409,
        "date": "2024-09-13",
        "description": "GST collected on sales",
        "amount": 43111.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 410,
        "date": "2024-09-13",
        "description": "Payment received from customer",
        "amount": 182047.68,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 411,
        "date": "2024-09-14",
        "description": "Software license capitalization",
        "amount": 78972.67,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 412,
        "date": "2024-09-15",
        "description": "GST payment to government",
        "amount": 54830.75,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 413,
        "date": "2024-09-15",
        "description": "TDS payment to government",
        "amount": 12966.25,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 414,
        "date": "2024-09-17",
        "description": "Sales to Bombay Fashion House",
        "amount": 287829.17,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 415,
        "date": "2024-09-17",
        "description": "GST collected on sales",
        "amount": 51809.25,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 416,
        "date": "2024-09-17",
        "description": "Sale of old machinery",
        "amount": 66051.86,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 417,
        "date": "2024-09-17",
        "description": "Interim dividend payout",
        "amount": 156044.87,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 418,
        "date": "2024-09-18",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 235200.52,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 419,
        "date": "2024-09-18",
        "description": "GST input on inventory",
        "amount": 42336.09,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 420,
        "date": "2024-09-20",
        "description": "Sales to Rajan Fabrics",
        "amount": 275819.91,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 421,
        "date": "2024-09-20",
        "description": "GST collected on sales",
        "amount": 49647.58,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 422,
        "date": "2024-09-23",
        "description": "Advance received for large order",
        "amount": 51267.14,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 423,
        "date": "2024-09-24",
        "description": "Sales to Mehta Garments",
        "amount": 274139.48,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 424,
        "date": "2024-09-24",
        "description": "GST collected on sales",
        "amount": 49345.11,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 425,
        "date": "2024-09-25",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 278473.6,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 426,
        "date": "2024-09-25",
        "description": "GST input on inventory",
        "amount": 50125.25,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 427,
        "date": "2024-09-26",
        "description": "Sales return from customer",
        "amount": 20108.31,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 428,
        "date": "2024-09-27",
        "description": "Sales to Mehta Garments",
        "amount": 227444.56,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 429,
        "date": "2024-09-27",
        "description": "GST collected on sales",
        "amount": 40940.02,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 430,
        "date": "2024-09-28",
        "description": "Interest earned on FD",
        "amount": 5244.28,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 431,
        "date": "2024-09-28",
        "description": "Legal and consultancy fees",
        "amount": 32058.56,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 432,
        "date": "2024-09-29",
        "description": "Digital marketing campaign",
        "amount": 25614.74,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 433,
        "date": "2024-09-30",
        "description": "Sales return from customer",
        "amount": 18726.33,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 434,
        "date": "2024-10-01",
        "description": "Office rent paid",
        "amount": 43528.77,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 435,
        "date": "2024-10-01",
        "description": "Salary paid to employees",
        "amount": 77907.36,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 436,
        "date": "2024-10-01",
        "description": "Sales to Bombay Fashion House",
        "amount": 192240.72,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 437,
        "date": "2024-10-01",
        "description": "GST collected on sales",
        "amount": 34603.33,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 438,
        "date": "2024-10-02",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 188027.1,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 439,
        "date": "2024-10-02",
        "description": "GST input on inventory",
        "amount": 33844.88,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 440,
        "date": "2024-10-02",
        "description": "Fuel for delivery vehicles",
        "amount": 19416.41,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 441,
        "date": "2024-10-03",
        "description": "Forex gain on export receivables",
        "amount": 5285.33,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 442,
        "date": "2024-10-04",
        "description": "Sales to Lucky Hosiery",
        "amount": 216701.78,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 443,
        "date": "2024-10-04",
        "description": "GST collected on sales",
        "amount": 39006.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 444,
        "date": "2024-10-05",
        "description": "Electricity bill payment",
        "amount": 12209.13,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 445,
        "date": "2024-10-05",
        "description": "Water and utility charges",
        "amount": 5173.72,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 446,
        "date": "2024-10-06",
        "description": "Fuel for delivery vehicles",
        "amount": 19396.64,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 447,
        "date": "2024-10-08",
        "description": "Sales to Rajan Fabrics",
        "amount": 295983.82,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 448,
        "date": "2024-10-08",
        "description": "GST collected on sales",
        "amount": 53277.09,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 449,
        "date": "2024-10-09",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 202641.76,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 450,
        "date": "2024-10-09",
        "description": "GST input on inventory",
        "amount": 36475.52,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 451,
        "date": "2024-10-09",
        "description": "Digital marketing campaign",
        "amount": 26753.64,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 452,
        "date": "2024-10-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 453,
        "date": "2024-10-10",
        "description": "Interest paid on bank loan",
        "amount": 12121.38,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 454,
        "date": "2024-10-11",
        "description": "Sales to Bombay Fashion House",
        "amount": 261573.89,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 455,
        "date": "2024-10-11",
        "description": "GST collected on sales",
        "amount": 47083.3,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 456,
        "date": "2024-10-11",
        "description": "Monthly bank processing fees",
        "amount": 1727.18,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 457,
        "date": "2024-10-15",
        "description": "GST payment to government",
        "amount": 67431.97,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 458,
        "date": "2024-10-15",
        "description": "TDS payment to government",
        "amount": 9500.56,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 459,
        "date": "2024-10-15",
        "description": "Sales to Rajan Fabrics",
        "amount": 234400.85,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 460,
        "date": "2024-10-15",
        "description": "GST collected on sales",
        "amount": 42192.15,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 461,
        "date": "2024-10-16",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 252535.38,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 462,
        "date": "2024-10-16",
        "description": "GST input on inventory",
        "amount": 45456.37,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 463,
        "date": "2024-10-17",
        "description": "Purchase of new office equipment",
        "amount": 106786.63,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 464,
        "date": "2024-10-18",
        "description": "Sales to Bombay Fashion House",
        "amount": 303689.74,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 465,
        "date": "2024-10-18",
        "description": "GST collected on sales",
        "amount": 54664.15,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 466,
        "date": "2024-10-21",
        "description": "Depreciation charged on assets",
        "amount": 29737.8,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 467,
        "date": "2024-10-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 240936.06,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 468,
        "date": "2024-10-22",
        "description": "GST collected on sales",
        "amount": 43368.49,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 469,
        "date": "2024-10-23",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 203964.06,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 470,
        "date": "2024-10-23",
        "description": "GST input on inventory",
        "amount": 36713.53,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 471,
        "date": "2024-10-25",
        "description": "Sales to Mehta Garments",
        "amount": 245524.53,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 472,
        "date": "2024-10-25",
        "description": "GST collected on sales",
        "amount": 44194.42,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 473,
        "date": "2024-10-26",
        "description": "Employee performance bonus",
        "amount": 45099.11,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 474,
        "date": "2024-10-29",
        "description": "Sales to Mehta Garments",
        "amount": 174253.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 475,
        "date": "2024-10-29",
        "description": "GST collected on sales",
        "amount": 31365.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 476,
        "date": "2024-10-30",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 254878.96,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 477,
        "date": "2024-10-30",
        "description": "GST input on inventory",
        "amount": 45878.21,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 478,
        "date": "2024-11-01",
        "description": "Office rent paid",
        "amount": 40750.74,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 479,
        "date": "2024-11-01",
        "description": "Salary paid to employees",
        "amount": 77875.34,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 480,
        "date": "2024-11-01",
        "description": "Sales to Lucky Hosiery",
        "amount": 340639.67,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 481,
        "date": "2024-11-01",
        "description": "GST collected on sales",
        "amount": 61315.14,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 482,
        "date": "2024-11-03",
        "description": "Software license capitalization",
        "amount": 72816.16,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 483,
        "date": "2024-11-05",
        "description": "Electricity bill payment",
        "amount": 10215.83,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 484,
        "date": "2024-11-05",
        "description": "Water and utility charges",
        "amount": 4435.77,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 485,
        "date": "2024-11-05",
        "description": "Sales to Lucky Hosiery",
        "amount": 252389.3,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 486,
        "date": "2024-11-05",
        "description": "GST collected on sales",
        "amount": 45430.07,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 487,
        "date": "2024-11-06",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 180333.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 488,
        "date": "2024-11-06",
        "description": "GST input on inventory",
        "amount": 32459.95,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 489,
        "date": "2024-11-08",
        "description": "Sales to Lucky Hosiery",
        "amount": 226506.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 490,
        "date": "2024-11-08",
        "description": "GST collected on sales",
        "amount": 40771.2,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 491,
        "date": "2024-11-08",
        "description": "GST reversal on sales return",
        "amount": 2700.17,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 492,
        "date": "2024-11-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 493,
        "date": "2024-11-10",
        "description": "Interest paid on bank loan",
        "amount": 14037.75,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 494,
        "date": "2024-11-10",
        "description": "Purchase return to vendor",
        "amount": 24650.07,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 495,
        "date": "2024-11-11",
        "description": "Fuel for delivery vehicles",
        "amount": 10333.37,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 496,
        "date": "2024-11-11",
        "description": "Depreciation charged on assets",
        "amount": 34585.34,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 497,
        "date": "2024-11-12",
        "description": "Sales to Rajan Fabrics",
        "amount": 188684.28,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 498,
        "date": "2024-11-12",
        "description": "GST collected on sales",
        "amount": 33963.17,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 499,
        "date": "2024-11-13",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 250796.46,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 500,
        "date": "2024-11-13",
        "description": "GST input on inventory",
        "amount": 45143.36,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 501,
        "date": "2024-11-14",
        "description": "Sale of old machinery",
        "amount": 62111.22,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 502,
        "date": "2024-11-15",
        "description": "GST payment to government",
        "amount": 49016.57,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 503,
        "date": "2024-11-15",
        "description": "TDS payment to government",
        "amount": 9167.61,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 504,
        "date": "2024-11-15",
        "description": "Sales to Mehta Garments",
        "amount": 200183.21,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 505,
        "date": "2024-11-15",
        "description": "GST collected on sales",
        "amount": 36032.98,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 506,
        "date": "2024-11-15",
        "description": "Further equity capital introduced",
        "amount": 935749.83,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 507,
        "date": "2024-11-18",
        "description": "Depreciation charged on assets",
        "amount": 23879.41,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 508,
        "date": "2024-11-19",
        "description": "Sales to Bombay Fashion House",
        "amount": 314833.51,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 509,
        "date": "2024-11-19",
        "description": "GST collected on sales",
        "amount": 56670.03,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 510,
        "date": "2024-11-20",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 208039.67,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 511,
        "date": "2024-11-20",
        "description": "GST input on inventory",
        "amount": 37447.14,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 512,
        "date": "2024-11-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 173698.37,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 513,
        "date": "2024-11-22",
        "description": "GST collected on sales",
        "amount": 31265.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 514,
        "date": "2024-11-26",
        "description": "Sales to Rajan Fabrics",
        "amount": 277883.6,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 515,
        "date": "2024-11-26",
        "description": "GST collected on sales",
        "amount": 50019.05,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 516,
        "date": "2024-11-27",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 191184.45,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 517,
        "date": "2024-11-27",
        "description": "GST input on inventory",
        "amount": 34413.2,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 518,
        "date": "2024-11-29",
        "description": "Sales to Rajan Fabrics",
        "amount": 186914.39,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 519,
        "date": "2024-11-29",
        "description": "GST collected on sales",
        "amount": 33644.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 520,
        "date": "2024-12-01",
        "description": "Office rent paid",
        "amount": 49699.19,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 521,
        "date": "2024-12-01",
        "description": "Salary paid to employees",
        "amount": 71815.21,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 522,
        "date": "2024-12-01",
        "description": "Depreciation charged on assets",
        "amount": 19645.12,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 523,
        "date": "2024-12-02",
        "description": "Purchase of new office equipment",
        "amount": 65121.41,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 524,
        "date": "2024-12-03",
        "description": "Sales to Lucky Hosiery",
        "amount": 301491.49,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 525,
        "date": "2024-12-03",
        "description": "GST collected on sales",
        "amount": 54268.47,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 526,
        "date": "2024-12-04",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 272042.67,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 527,
        "date": "2024-12-04",
        "description": "GST input on inventory",
        "amount": 48967.68,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 528,
        "date": "2024-12-04",
        "description": "Employee performance bonus",
        "amount": 29612.7,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 529,
        "date": "2024-12-05",
        "description": "Electricity bill payment",
        "amount": 10614.16,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 530,
        "date": "2024-12-05",
        "description": "Water and utility charges",
        "amount": 5377.1,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 531,
        "date": "2024-12-05",
        "description": "Employee performance bonus",
        "amount": 44111.58,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 532,
        "date": "2024-12-06",
        "description": "Sales to Rajan Fabrics",
        "amount": 156726.75,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 533,
        "date": "2024-12-06",
        "description": "GST collected on sales",
        "amount": 28210.81,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 534,
        "date": "2024-12-07",
        "description": "Fuel for delivery vehicles",
        "amount": 13824.86,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 535,
        "date": "2024-12-08",
        "description": "Interim dividend payout",
        "amount": 121121.94,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 536,
        "date": "2024-12-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 537,
        "date": "2024-12-10",
        "description": "Interest paid on bank loan",
        "amount": 13436.57,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 538,
        "date": "2024-12-10",
        "description": "Sales to Mehta Garments",
        "amount": 303461.51,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 539,
        "date": "2024-12-10",
        "description": "GST collected on sales",
        "amount": 54623.07,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 540,
        "date": "2024-12-11",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 266810.81,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 541,
        "date": "2024-12-11",
        "description": "GST input on inventory",
        "amount": 48025.95,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 542,
        "date": "2024-12-13",
        "description": "Sales to Bombay Fashion House",
        "amount": 275826.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 543,
        "date": "2024-12-13",
        "description": "GST collected on sales",
        "amount": 49648.73,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 544,
        "date": "2024-12-15",
        "description": "GST payment to government",
        "amount": 61097.37,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 545,
        "date": "2024-12-15",
        "description": "TDS payment to government",
        "amount": 12867.14,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 546,
        "date": "2024-12-15",
        "description": "Digital marketing campaign",
        "amount": 20152.63,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 547,
        "date": "2024-12-17",
        "description": "Sales to Lucky Hosiery",
        "amount": 317281.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 548,
        "date": "2024-12-17",
        "description": "GST collected on sales",
        "amount": 57110.64,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 549,
        "date": "2024-12-18",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 201930.31,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 550,
        "date": "2024-12-18",
        "description": "GST input on inventory",
        "amount": 36347.46,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 551,
        "date": "2024-12-20",
        "description": "Sales to Mehta Garments",
        "amount": 285516.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 552,
        "date": "2024-12-20",
        "description": "GST collected on sales",
        "amount": 51392.96,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 553,
        "date": "2024-12-22",
        "description": "Forex loss on import payables",
        "amount": 7090.31,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 554,
        "date": "2024-12-22",
        "description": "Annual insurance premium",
        "amount": 22821.89,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 555,
        "date": "2024-12-23",
        "description": "Interest earned on FD",
        "amount": 5022.84,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 556,
        "date": "2024-12-24",
        "description": "Sales to Bombay Fashion House",
        "amount": 205126.56,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 557,
        "date": "2024-12-24",
        "description": "GST collected on sales",
        "amount": 36922.78,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 558,
        "date": "2024-12-24",
        "description": "Depreciation charged on assets",
        "amount": 33882.88,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 559,
        "date": "2024-12-25",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 192042.57,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 560,
        "date": "2024-12-25",
        "description": "GST input on inventory",
        "amount": 34567.66,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 561,
        "date": "2024-12-25",
        "description": "Miscellaneous office expenses",
        "amount": 3931.05,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 562,
        "date": "2024-12-27",
        "description": "Sales to Rajan Fabrics",
        "amount": 217344.6,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 563,
        "date": "2024-12-27",
        "description": "GST collected on sales",
        "amount": 39122.03,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 564,
        "date": "2024-12-27",
        "description": "Annual insurance premium",
        "amount": 21083.13,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 565,
        "date": "2024-12-29",
        "description": "GST reversal on sales return",
        "amount": 3738.72,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 566,
        "date": "2024-12-29",
        "description": "Miscellaneous office expenses",
        "amount": 1333.97,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 567,
        "date": "2024-12-30",
        "description": "Employee performance bonus",
        "amount": 46819.56,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 568,
        "date": "2024-12-31",
        "description": "Sales to Rajan Fabrics",
        "amount": 169768.75,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 569,
        "date": "2024-12-31",
        "description": "GST collected on sales",
        "amount": 30558.37,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 570,
        "date": "2024-12-31",
        "description": "Printing and stationery",
        "amount": 5296.53,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 571,
        "date": "2025-01-01",
        "description": "Office rent paid",
        "amount": 49360.33,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 572,
        "date": "2025-01-01",
        "description": "Salary paid to employees",
        "amount": 82242.44,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 573,
        "date": "2025-01-01",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 219323.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 574,
        "date": "2025-01-01",
        "description": "GST input on inventory",
        "amount": 39478.15,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 575,
        "date": "2025-01-02",
        "description": "GST reversal on sales return",
        "amount": 4627.67,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 576,
        "date": "2025-01-03",
        "description": "Sales to Mehta Garments",
        "amount": 349833.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 577,
        "date": "2025-01-03",
        "description": "GST collected on sales",
        "amount": 62970.05,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 578,
        "date": "2025-01-03",
        "description": "Software license capitalization",
        "amount": 41890.11,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 579,
        "date": "2025-01-05",
        "description": "Electricity bill payment",
        "amount": 15892.91,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 580,
        "date": "2025-01-05",
        "description": "Water and utility charges",
        "amount": 5861.01,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 581,
        "date": "2025-01-05",
        "description": "Employee performance bonus",
        "amount": 31952.89,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 582,
        "date": "2025-01-07",
        "description": "Sales to Rajan Fabrics",
        "amount": 271396.89,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 583,
        "date": "2025-01-07",
        "description": "GST collected on sales",
        "amount": 48851.44,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 584,
        "date": "2025-01-08",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 249538.59,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 585,
        "date": "2025-01-08",
        "description": "GST input on inventory",
        "amount": 44916.95,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 586,
        "date": "2025-01-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 587,
        "date": "2025-01-10",
        "description": "Interest paid on bank loan",
        "amount": 12064.1,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 588,
        "date": "2025-01-10",
        "description": "Sales to Lucky Hosiery",
        "amount": 320685.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 589,
        "date": "2025-01-10",
        "description": "GST collected on sales",
        "amount": 57723.35,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 590,
        "date": "2025-01-10",
        "description": "Purchase of new office equipment",
        "amount": 91754.27,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 591,
        "date": "2025-01-12",
        "description": "Purchase return to vendor",
        "amount": 17495.54,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 592,
        "date": "2025-01-14",
        "description": "Sales to Rajan Fabrics",
        "amount": 247833.22,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 593,
        "date": "2025-01-14",
        "description": "GST collected on sales",
        "amount": 44609.98,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 594,
        "date": "2025-01-14",
        "description": "Legal and consultancy fees",
        "amount": 18264.06,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 595,
        "date": "2025-01-14",
        "description": "Vehicle maintenance and repair",
        "amount": 9532.23,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 596,
        "date": "2025-01-15",
        "description": "GST payment to government",
        "amount": 66441.6,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 597,
        "date": "2025-01-15",
        "description": "TDS payment to government",
        "amount": 9198.67,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 598,
        "date": "2025-01-15",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 205285.7,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 599,
        "date": "2025-01-15",
        "description": "GST input on inventory",
        "amount": 36951.43,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 600,
        "date": "2025-01-17",
        "description": "Sales to Lucky Hosiery",
        "amount": 251020.37,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 601,
        "date": "2025-01-17",
        "description": "GST collected on sales",
        "amount": 45183.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 602,
        "date": "2025-01-17",
        "description": "Interim dividend payout",
        "amount": 125367.82,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 603,
        "date": "2025-01-18",
        "description": "Miscellaneous office expenses",
        "amount": 1956.2,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 604,
        "date": "2025-01-20",
        "description": "Forex loss on import payables",
        "amount": 8105.7,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 605,
        "date": "2025-01-21",
        "description": "Sales to Lucky Hosiery",
        "amount": 260079.54,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 606,
        "date": "2025-01-21",
        "description": "GST collected on sales",
        "amount": 46814.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 607,
        "date": "2025-01-21",
        "description": "Advance corporate tax payment",
        "amount": 85578.11,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 608,
        "date": "2025-01-22",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 229716.28,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 609,
        "date": "2025-01-22",
        "description": "GST input on inventory",
        "amount": 41348.93,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 610,
        "date": "2025-01-24",
        "description": "Sales to Mehta Garments",
        "amount": 189284.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 611,
        "date": "2025-01-24",
        "description": "GST collected on sales",
        "amount": 34071.24,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 612,
        "date": "2025-01-25",
        "description": "Monthly bank processing fees",
        "amount": 2432.15,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 613,
        "date": "2025-01-28",
        "description": "Sales to Lucky Hosiery",
        "amount": 169209.33,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 614,
        "date": "2025-01-28",
        "description": "GST collected on sales",
        "amount": 30457.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 615,
        "date": "2025-01-29",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 268503.92,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 616,
        "date": "2025-01-29",
        "description": "GST input on inventory",
        "amount": 48330.71,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 617,
        "date": "2025-01-31",
        "description": "Sales to Mehta Garments",
        "amount": 342507.71,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 618,
        "date": "2025-01-31",
        "description": "GST collected on sales",
        "amount": 61651.39,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 619,
        "date": "2025-02-01",
        "description": "Office rent paid",
        "amount": 40834.05,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 620,
        "date": "2025-02-01",
        "description": "Salary paid to employees",
        "amount": 71520.23,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 621,
        "date": "2025-02-04",
        "description": "Sales to Lucky Hosiery",
        "amount": 259548.18,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 622,
        "date": "2025-02-04",
        "description": "GST collected on sales",
        "amount": 46718.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 623,
        "date": "2025-02-04",
        "description": "Sale of old machinery",
        "amount": 48719.65,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 624,
        "date": "2025-02-05",
        "description": "Electricity bill payment",
        "amount": 14567.07,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 625,
        "date": "2025-02-05",
        "description": "Water and utility charges",
        "amount": 3573.27,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 626,
        "date": "2025-02-05",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 202893.95,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 627,
        "date": "2025-02-05",
        "description": "GST input on inventory",
        "amount": 36520.91,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 628,
        "date": "2025-02-05",
        "description": "Annual insurance premium",
        "amount": 21668.85,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 629,
        "date": "2025-02-05",
        "description": "Interim dividend payout",
        "amount": 111284.86,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 630,
        "date": "2025-02-05",
        "description": "Vendor payment against outstanding",
        "amount": 106708.07,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 631,
        "date": "2025-02-07",
        "description": "Sales to Mehta Garments",
        "amount": 340298.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 632,
        "date": "2025-02-07",
        "description": "GST collected on sales",
        "amount": 61253.69,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 633,
        "date": "2025-02-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 634,
        "date": "2025-02-10",
        "description": "Interest paid on bank loan",
        "amount": 14748.42,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 635,
        "date": "2025-02-11",
        "description": "Sales to Mehta Garments",
        "amount": 199398.87,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 636,
        "date": "2025-02-11",
        "description": "GST collected on sales",
        "amount": 35891.8,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 637,
        "date": "2025-02-12",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 269914.14,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 638,
        "date": "2025-02-12",
        "description": "GST input on inventory",
        "amount": 48584.55,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 639,
        "date": "2025-02-14",
        "description": "Sales to Bombay Fashion House",
        "amount": 266470.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 640,
        "date": "2025-02-14",
        "description": "GST collected on sales",
        "amount": 47964.76,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 641,
        "date": "2025-02-15",
        "description": "GST payment to government",
        "amount": 70983.54,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 642,
        "date": "2025-02-15",
        "description": "TDS payment to government",
        "amount": 11870.04,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 643,
        "date": "2025-02-16",
        "description": "Payment received from customer",
        "amount": 133797.07,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 644,
        "date": "2025-02-18",
        "description": "Sales to Lucky Hosiery",
        "amount": 296355.74,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 645,
        "date": "2025-02-18",
        "description": "GST collected on sales",
        "amount": 53344.03,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 646,
        "date": "2025-02-19",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 239979.14,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 647,
        "date": "2025-02-19",
        "description": "GST input on inventory",
        "amount": 43196.24,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 648,
        "date": "2025-02-20",
        "description": "Further equity capital introduced",
        "amount": 681435.03,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 649,
        "date": "2025-02-21",
        "description": "Sales to Lucky Hosiery",
        "amount": 258925.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 650,
        "date": "2025-02-21",
        "description": "GST collected on sales",
        "amount": 46606.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 651,
        "date": "2025-02-21",
        "description": "Payment received from customer",
        "amount": 162655.18,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 652,
        "date": "2025-02-24",
        "description": "Employee travel reimbursement",
        "amount": 6052.84,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 653,
        "date": "2025-02-25",
        "description": "Sales to Lucky Hosiery",
        "amount": 330696.25,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 654,
        "date": "2025-02-25",
        "description": "GST collected on sales",
        "amount": 59525.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 655,
        "date": "2025-02-26",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 278500.65,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 656,
        "date": "2025-02-26",
        "description": "GST input on inventory",
        "amount": 50130.12,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 657,
        "date": "2025-02-26",
        "description": "Employee performance bonus",
        "amount": 47407.04,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 658,
        "date": "2025-02-28",
        "description": "Sales to Rajan Fabrics",
        "amount": 213063.77,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 659,
        "date": "2025-02-28",
        "description": "GST collected on sales",
        "amount": 38351.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 660,
        "date": "2025-03-01",
        "description": "Office rent paid",
        "amount": 46619.29,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 661,
        "date": "2025-03-01",
        "description": "Salary paid to employees",
        "amount": 84708.44,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 662,
        "date": "2025-03-01",
        "description": "Customs duty on imports",
        "amount": 35176.59,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 663,
        "date": "2025-03-01",
        "description": "Brokerage and commission paid",
        "amount": 15397.31,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 664,
        "date": "2025-03-01",
        "description": "Sales return from customer",
        "amount": 21732.06,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 665,
        "date": "2025-03-02",
        "description": "Employee travel reimbursement",
        "amount": 8598.68,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 666,
        "date": "2025-03-02",
        "description": "Employee performance bonus",
        "amount": 48301.87,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 667,
        "date": "2025-03-03",
        "description": "Purchase of new office equipment",
        "amount": 92260.86,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 668,
        "date": "2025-03-04",
        "description": "Sales to Bombay Fashion House",
        "amount": 342714.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 669,
        "date": "2025-03-04",
        "description": "GST collected on sales",
        "amount": 61688.57,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 670,
        "date": "2025-03-05",
        "description": "Electricity bill payment",
        "amount": 11992.11,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 671,
        "date": "2025-03-05",
        "description": "Water and utility charges",
        "amount": 5167.84,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 672,
        "date": "2025-03-05",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 197320.14,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 673,
        "date": "2025-03-05",
        "description": "GST input on inventory",
        "amount": 35517.62,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 674,
        "date": "2025-03-06",
        "description": "Payment received from customer",
        "amount": 121860.22,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 675,
        "date": "2025-03-07",
        "description": "Sales to Mehta Garments",
        "amount": 150224.68,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 676,
        "date": "2025-03-07",
        "description": "GST collected on sales",
        "amount": 27040.44,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 677,
        "date": "2025-03-07",
        "description": "Sales return from customer",
        "amount": 10782.73,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 678,
        "date": "2025-03-09",
        "description": "Fuel for delivery vehicles",
        "amount": 12812.47,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 679,
        "date": "2025-03-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 680,
        "date": "2025-03-10",
        "description": "Interest paid on bank loan",
        "amount": 14823.71,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 681,
        "date": "2025-03-11",
        "description": "Sales to Rajan Fabrics",
        "amount": 314895.94,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 682,
        "date": "2025-03-11",
        "description": "GST collected on sales",
        "amount": 56681.27,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 683,
        "date": "2025-03-12",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 211325.15,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 684,
        "date": "2025-03-12",
        "description": "GST input on inventory",
        "amount": 38038.53,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 685,
        "date": "2025-03-14",
        "description": "Sales to Rajan Fabrics",
        "amount": 225698.07,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 686,
        "date": "2025-03-14",
        "description": "GST collected on sales",
        "amount": 40625.65,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 687,
        "date": "2025-03-14",
        "description": "Mutual fund investment",
        "amount": 246091.92,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 688,
        "date": "2025-03-15",
        "description": "GST payment to government",
        "amount": 74904.54,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 689,
        "date": "2025-03-15",
        "description": "TDS payment to government",
        "amount": 8987.03,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 690,
        "date": "2025-03-18",
        "description": "Sales to Bombay Fashion House",
        "amount": 300602.7,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 691,
        "date": "2025-03-18",
        "description": "GST collected on sales",
        "amount": 54108.49,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 692,
        "date": "2025-03-19",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 244282.16,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 693,
        "date": "2025-03-19",
        "description": "GST input on inventory",
        "amount": 43970.79,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 694,
        "date": "2025-03-21",
        "description": "Sales to Bombay Fashion House",
        "amount": 242382.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 695,
        "date": "2025-03-21",
        "description": "GST collected on sales",
        "amount": 43628.87,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 696,
        "date": "2025-03-21",
        "description": "Courier and postage charges",
        "amount": 2715.38,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 697,
        "date": "2025-03-22",
        "description": "Depreciation charged on assets",
        "amount": 34235.73,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 698,
        "date": "2025-03-23",
        "description": "Scrap sale proceeds",
        "amount": 9225.41,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 699,
        "date": "2025-03-25",
        "description": "Sales to Rajan Fabrics",
        "amount": 242872.0,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 700,
        "date": "2025-03-25",
        "description": "GST collected on sales",
        "amount": 43716.96,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 701,
        "date": "2025-03-26",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 200955.5,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 702,
        "date": "2025-03-26",
        "description": "GST input on inventory",
        "amount": 36171.99,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 703,
        "date": "2025-03-28",
        "description": "Sales to Rajan Fabrics",
        "amount": 166066.23,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 704,
        "date": "2025-03-28",
        "description": "GST collected on sales",
        "amount": 29891.92,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 705,
        "date": "2025-03-28",
        "description": "Vendor payment against outstanding",
        "amount": 88453.44,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 706,
        "date": "2025-03-31",
        "description": "Statutory audit fees",
        "amount": 49480.04,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 707,
        "date": "2025-03-31",
        "description": "Mutual fund investment",
        "amount": 135858.88,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 708,
        "date": "2025-04-01",
        "description": "Office rent paid",
        "amount": 42025.48,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 709,
        "date": "2025-04-01",
        "description": "Salary paid to employees",
        "amount": 78523.72,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 710,
        "date": "2025-04-01",
        "description": "Sales to Mehta Garments",
        "amount": 205393.55,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 711,
        "date": "2025-04-01",
        "description": "GST collected on sales",
        "amount": 36970.84,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 712,
        "date": "2025-04-02",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 208475.55,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 713,
        "date": "2025-04-02",
        "description": "GST input on inventory",
        "amount": 37525.6,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 714,
        "date": "2025-04-02",
        "description": "Miscellaneous office expenses",
        "amount": 3468.08,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 715,
        "date": "2025-04-02",
        "description": "Legal and consultancy fees",
        "amount": 38543.43,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 716,
        "date": "2025-04-03",
        "description": "GST reversal on sales return",
        "amount": 3295.71,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 717,
        "date": "2025-04-04",
        "description": "Sales to Bombay Fashion House",
        "amount": 320224.3,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 718,
        "date": "2025-04-04",
        "description": "GST collected on sales",
        "amount": 57640.37,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 719,
        "date": "2025-04-04",
        "description": "Sales return from customer",
        "amount": 19595.76,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 720,
        "date": "2025-04-04",
        "description": "Customs duty on imports",
        "amount": 36115.56,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 721,
        "date": "2025-04-05",
        "description": "Electricity bill payment",
        "amount": 13901.88,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 722,
        "date": "2025-04-05",
        "description": "Water and utility charges",
        "amount": 3879.99,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 723,
        "date": "2025-04-05",
        "description": "Miscellaneous office expenses",
        "amount": 3913.07,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 724,
        "date": "2025-04-08",
        "description": "Sales to Lucky Hosiery",
        "amount": 278201.19,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 725,
        "date": "2025-04-08",
        "description": "GST collected on sales",
        "amount": 50076.21,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 726,
        "date": "2025-04-09",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 227532.86,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 727,
        "date": "2025-04-09",
        "description": "GST input on inventory",
        "amount": 40955.92,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 728,
        "date": "2025-04-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 729,
        "date": "2025-04-10",
        "description": "Interest paid on bank loan",
        "amount": 12279.37,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 730,
        "date": "2025-04-11",
        "description": "Sales to Rajan Fabrics",
        "amount": 262081.81,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 731,
        "date": "2025-04-11",
        "description": "GST collected on sales",
        "amount": 47174.73,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 732,
        "date": "2025-04-14",
        "description": "Miscellaneous office expenses",
        "amount": 1847.14,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 733,
        "date": "2025-04-15",
        "description": "GST payment to government",
        "amount": 48865.09,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 734,
        "date": "2025-04-15",
        "description": "TDS payment to government",
        "amount": 12331.62,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 735,
        "date": "2025-04-15",
        "description": "Sales to Bombay Fashion House",
        "amount": 344346.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 736,
        "date": "2025-04-15",
        "description": "GST collected on sales",
        "amount": 61982.33,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 737,
        "date": "2025-04-15",
        "description": "Miscellaneous office expenses",
        "amount": 1796.26,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 738,
        "date": "2025-04-16",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 232415.35,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 739,
        "date": "2025-04-16",
        "description": "GST input on inventory",
        "amount": 41834.76,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 740,
        "date": "2025-04-18",
        "description": "Sales to Mehta Garments",
        "amount": 348793.36,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 741,
        "date": "2025-04-18",
        "description": "GST collected on sales",
        "amount": 62782.8,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 742,
        "date": "2025-04-18",
        "description": "Advance corporate tax payment",
        "amount": 99787.32,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 743,
        "date": "2025-04-20",
        "description": "Vendor payment against outstanding",
        "amount": 107718.35,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 744,
        "date": "2025-04-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 161829.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 745,
        "date": "2025-04-22",
        "description": "GST collected on sales",
        "amount": 29129.38,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 746,
        "date": "2025-04-23",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 252191.92,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 747,
        "date": "2025-04-23",
        "description": "GST input on inventory",
        "amount": 45394.55,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 748,
        "date": "2025-04-25",
        "description": "Sales to Lucky Hosiery",
        "amount": 340463.43,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 749,
        "date": "2025-04-25",
        "description": "GST collected on sales",
        "amount": 61283.42,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 750,
        "date": "2025-04-29",
        "description": "Sales to Mehta Garments",
        "amount": 270494.72,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 751,
        "date": "2025-04-29",
        "description": "GST collected on sales",
        "amount": 48689.05,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 752,
        "date": "2025-04-30",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 254867.69,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 753,
        "date": "2025-04-30",
        "description": "GST input on inventory",
        "amount": 45876.18,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 754,
        "date": "2025-04-30",
        "description": "Sales return from customer",
        "amount": 25735.66,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 755,
        "date": "2025-04-30",
        "description": "Advance received for large order",
        "amount": 54451.57,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 756,
        "date": "2025-05-01",
        "description": "Office rent paid",
        "amount": 41399.63,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 757,
        "date": "2025-05-01",
        "description": "Salary paid to employees",
        "amount": 83716.17,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 758,
        "date": "2025-05-02",
        "description": "Sales to Bombay Fashion House",
        "amount": 347823.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 759,
        "date": "2025-05-02",
        "description": "GST collected on sales",
        "amount": 62608.26,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 760,
        "date": "2025-05-02",
        "description": "Miscellaneous office expenses",
        "amount": 3307.46,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 761,
        "date": "2025-05-03",
        "description": "Employee performance bonus",
        "amount": 23962.48,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 762,
        "date": "2025-05-05",
        "description": "Electricity bill payment",
        "amount": 15546.88,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 763,
        "date": "2025-05-05",
        "description": "Water and utility charges",
        "amount": 4035.46,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 764,
        "date": "2025-05-06",
        "description": "Sales to Mehta Garments",
        "amount": 242249.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 765,
        "date": "2025-05-06",
        "description": "GST collected on sales",
        "amount": 43604.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 766,
        "date": "2025-05-06",
        "description": "Vehicle maintenance and repair",
        "amount": 14925.3,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 767,
        "date": "2025-05-07",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 234936.82,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 768,
        "date": "2025-05-07",
        "description": "GST input on inventory",
        "amount": 42288.63,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 769,
        "date": "2025-05-09",
        "description": "Sales to Rajan Fabrics",
        "amount": 246014.36,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 770,
        "date": "2025-05-09",
        "description": "GST collected on sales",
        "amount": 44282.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 771,
        "date": "2025-05-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 772,
        "date": "2025-05-10",
        "description": "Interest paid on bank loan",
        "amount": 12096.81,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 773,
        "date": "2025-05-11",
        "description": "Scrap sale proceeds",
        "amount": 8706.75,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 774,
        "date": "2025-05-13",
        "description": "Sales to Lucky Hosiery",
        "amount": 310424.76,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 775,
        "date": "2025-05-13",
        "description": "GST collected on sales",
        "amount": 55876.46,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 776,
        "date": "2025-05-14",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 229762.32,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 777,
        "date": "2025-05-14",
        "description": "GST input on inventory",
        "amount": 41357.22,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 778,
        "date": "2025-05-15",
        "description": "GST payment to government",
        "amount": 71083.08,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 779,
        "date": "2025-05-15",
        "description": "TDS payment to government",
        "amount": 14392.01,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 780,
        "date": "2025-05-15",
        "description": "Customs duty on imports",
        "amount": 39237.57,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 781,
        "date": "2025-05-16",
        "description": "Sales to Rajan Fabrics",
        "amount": 235641.67,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 782,
        "date": "2025-05-16",
        "description": "GST collected on sales",
        "amount": 42415.5,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 783,
        "date": "2025-05-16",
        "description": "Advance received for large order",
        "amount": 98809.38,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 784,
        "date": "2025-05-20",
        "description": "Sales to Mehta Garments",
        "amount": 244385.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 785,
        "date": "2025-05-20",
        "description": "GST collected on sales",
        "amount": 43989.38,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 786,
        "date": "2025-05-20",
        "description": "Advance received for large order",
        "amount": 63593.51,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 787,
        "date": "2025-05-21",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 244415.85,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 788,
        "date": "2025-05-21",
        "description": "GST input on inventory",
        "amount": 43994.85,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 789,
        "date": "2025-05-23",
        "description": "Sales to Mehta Garments",
        "amount": 270413.49,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 790,
        "date": "2025-05-23",
        "description": "GST collected on sales",
        "amount": 48674.43,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 791,
        "date": "2025-05-24",
        "description": "Payment received from customer",
        "amount": 103279.46,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 792,
        "date": "2025-05-25",
        "description": "Forex gain on export receivables",
        "amount": 6181.13,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 793,
        "date": "2025-05-27",
        "description": "Sales to Rajan Fabrics",
        "amount": 282441.85,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 794,
        "date": "2025-05-27",
        "description": "GST collected on sales",
        "amount": 50839.53,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 795,
        "date": "2025-05-27",
        "description": "Forex gain on export receivables",
        "amount": 5220.06,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 796,
        "date": "2025-05-28",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 262171.43,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 797,
        "date": "2025-05-28",
        "description": "GST input on inventory",
        "amount": 47190.86,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 798,
        "date": "2025-05-30",
        "description": "Sales to Mehta Garments",
        "amount": 202001.57,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 799,
        "date": "2025-05-30",
        "description": "GST collected on sales",
        "amount": 36360.28,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 800,
        "date": "2025-06-01",
        "description": "Office rent paid",
        "amount": 42540.51,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 801,
        "date": "2025-06-01",
        "description": "Salary paid to employees",
        "amount": 72045.3,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 802,
        "date": "2025-06-02",
        "description": "Advance corporate tax payment",
        "amount": 69410.9,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 803,
        "date": "2025-06-03",
        "description": "Sales to Mehta Garments",
        "amount": 261110.13,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 804,
        "date": "2025-06-03",
        "description": "GST collected on sales",
        "amount": 46999.82,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 805,
        "date": "2025-06-03",
        "description": "Forex loss on import payables",
        "amount": 7997.95,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 806,
        "date": "2025-06-04",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 230888.12,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 807,
        "date": "2025-06-04",
        "description": "GST input on inventory",
        "amount": 41559.86,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 808,
        "date": "2025-06-05",
        "description": "Electricity bill payment",
        "amount": 14378.54,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 809,
        "date": "2025-06-05",
        "description": "Water and utility charges",
        "amount": 3806.04,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 810,
        "date": "2025-06-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 311432.81,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 811,
        "date": "2025-06-06",
        "description": "GST collected on sales",
        "amount": 56057.91,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 812,
        "date": "2025-06-07",
        "description": "Brokerage and commission paid",
        "amount": 8151.61,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 813,
        "date": "2025-06-07",
        "description": "Purchase return to vendor",
        "amount": 18247.4,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 814,
        "date": "2025-06-08",
        "description": "Sale of old machinery",
        "amount": 73949.66,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 815,
        "date": "2025-06-08",
        "description": "Annual insurance premium",
        "amount": 27863.58,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 816,
        "date": "2025-06-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 817,
        "date": "2025-06-10",
        "description": "Interest paid on bank loan",
        "amount": 15724.94,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 818,
        "date": "2025-06-10",
        "description": "Sales to Bombay Fashion House",
        "amount": 301815.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 819,
        "date": "2025-06-10",
        "description": "GST collected on sales",
        "amount": 54326.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 820,
        "date": "2025-06-11",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 244551.58,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 821,
        "date": "2025-06-11",
        "description": "GST input on inventory",
        "amount": 44019.28,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 822,
        "date": "2025-06-12",
        "description": "GST reversal on sales return",
        "amount": 5287.91,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 823,
        "date": "2025-06-13",
        "description": "Sales to Rajan Fabrics",
        "amount": 299942.89,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 824,
        "date": "2025-06-13",
        "description": "GST collected on sales",
        "amount": 53989.72,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 825,
        "date": "2025-06-15",
        "description": "GST payment to government",
        "amount": 50202.88,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 826,
        "date": "2025-06-15",
        "description": "TDS payment to government",
        "amount": 9388.49,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 827,
        "date": "2025-06-15",
        "description": "Interim dividend payout",
        "amount": 191244.18,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 828,
        "date": "2025-06-17",
        "description": "Sales to Mehta Garments",
        "amount": 208731.03,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 829,
        "date": "2025-06-17",
        "description": "GST collected on sales",
        "amount": 37571.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 830,
        "date": "2025-06-17",
        "description": "Employee travel reimbursement",
        "amount": 5870.15,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 831,
        "date": "2025-06-17",
        "description": "Fuel for delivery vehicles",
        "amount": 13975.04,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 832,
        "date": "2025-06-17",
        "description": "Advance received for large order",
        "amount": 90856.04,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 833,
        "date": "2025-06-18",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 193169.56,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 834,
        "date": "2025-06-18",
        "description": "GST input on inventory",
        "amount": 34770.52,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 835,
        "date": "2025-06-18",
        "description": "Software license capitalization",
        "amount": 61980.05,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 836,
        "date": "2025-06-18",
        "description": "Printing and stationery",
        "amount": 4932.16,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 837,
        "date": "2025-06-19",
        "description": "Printing and stationery",
        "amount": 6337.59,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 838,
        "date": "2025-06-20",
        "description": "Sales to Bombay Fashion House",
        "amount": 267427.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 839,
        "date": "2025-06-20",
        "description": "GST collected on sales",
        "amount": 48136.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 840,
        "date": "2025-06-24",
        "description": "Sales to Mehta Garments",
        "amount": 161382.2,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 841,
        "date": "2025-06-24",
        "description": "GST collected on sales",
        "amount": 29048.8,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 842,
        "date": "2025-06-25",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 262333.26,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 843,
        "date": "2025-06-25",
        "description": "GST input on inventory",
        "amount": 47219.99,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 844,
        "date": "2025-06-25",
        "description": "Forex gain on export receivables",
        "amount": 6559.06,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 845,
        "date": "2025-06-26",
        "description": "Software license capitalization",
        "amount": 75102.36,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 846,
        "date": "2025-06-27",
        "description": "Sales to Bombay Fashion House",
        "amount": 163079.52,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 847,
        "date": "2025-06-27",
        "description": "GST collected on sales",
        "amount": 29354.31,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 848,
        "date": "2025-06-27",
        "description": "Courier and postage charges",
        "amount": 2731.29,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 849,
        "date": "2025-06-29",
        "description": "Advance corporate tax payment",
        "amount": 83921.44,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 850,
        "date": "2025-06-30",
        "description": "Forex gain on export receivables",
        "amount": 7998.71,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 851,
        "date": "2025-07-01",
        "description": "Office rent paid",
        "amount": 44054.48,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 852,
        "date": "2025-07-01",
        "description": "Salary paid to employees",
        "amount": 70983.51,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 853,
        "date": "2025-07-01",
        "description": "Sales to Mehta Garments",
        "amount": 173433.35,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 854,
        "date": "2025-07-01",
        "description": "GST collected on sales",
        "amount": 31218.0,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 855,
        "date": "2025-07-02",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 215225.5,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 856,
        "date": "2025-07-02",
        "description": "GST input on inventory",
        "amount": 38740.59,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 857,
        "date": "2025-07-03",
        "description": "Interim dividend payout",
        "amount": 133665.89,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 858,
        "date": "2025-07-03",
        "description": "Advance received for large order",
        "amount": 71668.27,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 859,
        "date": "2025-07-03",
        "description": "Forex gain on export receivables",
        "amount": 6225.48,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 860,
        "date": "2025-07-03",
        "description": "Interest earned on FD",
        "amount": 11466.31,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 861,
        "date": "2025-07-03",
        "description": "Mutual fund investment",
        "amount": 82470.88,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 862,
        "date": "2025-07-04",
        "description": "Sales to Bombay Fashion House",
        "amount": 206808.42,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 863,
        "date": "2025-07-04",
        "description": "GST collected on sales",
        "amount": 37225.52,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 864,
        "date": "2025-07-05",
        "description": "Electricity bill payment",
        "amount": 15636.78,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 865,
        "date": "2025-07-05",
        "description": "Water and utility charges",
        "amount": 4902.52,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 866,
        "date": "2025-07-08",
        "description": "Sales to Mehta Garments",
        "amount": 184116.54,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 867,
        "date": "2025-07-08",
        "description": "GST collected on sales",
        "amount": 33140.98,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 868,
        "date": "2025-07-09",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 237824.94,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 869,
        "date": "2025-07-09",
        "description": "GST input on inventory",
        "amount": 42808.49,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 870,
        "date": "2025-07-09",
        "description": "Sale of old machinery",
        "amount": 82791.45,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 871,
        "date": "2025-07-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 872,
        "date": "2025-07-10",
        "description": "Interest paid on bank loan",
        "amount": 13452.24,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 873,
        "date": "2025-07-10",
        "description": "Fuel for delivery vehicles",
        "amount": 18099.78,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 874,
        "date": "2025-07-11",
        "description": "Sales to Rajan Fabrics",
        "amount": 232148.77,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 875,
        "date": "2025-07-11",
        "description": "GST collected on sales",
        "amount": 41786.78,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 876,
        "date": "2025-07-15",
        "description": "GST payment to government",
        "amount": 61572.98,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 877,
        "date": "2025-07-15",
        "description": "TDS payment to government",
        "amount": 8832.39,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 878,
        "date": "2025-07-15",
        "description": "Sales to Mehta Garments",
        "amount": 190571.04,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 879,
        "date": "2025-07-15",
        "description": "GST collected on sales",
        "amount": 34302.79,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 880,
        "date": "2025-07-15",
        "description": "Interest earned on FD",
        "amount": 7884.79,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 881,
        "date": "2025-07-15",
        "description": "Advance corporate tax payment",
        "amount": 88627.85,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 882,
        "date": "2025-07-16",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 191856.1,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 883,
        "date": "2025-07-16",
        "description": "GST input on inventory",
        "amount": 34534.1,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 884,
        "date": "2025-07-18",
        "description": "Sales to Bombay Fashion House",
        "amount": 309372.36,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 885,
        "date": "2025-07-18",
        "description": "GST collected on sales",
        "amount": 55687.02,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 886,
        "date": "2025-07-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 234668.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 887,
        "date": "2025-07-22",
        "description": "GST collected on sales",
        "amount": 42240.29,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 888,
        "date": "2025-07-22",
        "description": "Customs duty on imports",
        "amount": 43469.79,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 889,
        "date": "2025-07-23",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 197852.81,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 890,
        "date": "2025-07-23",
        "description": "GST input on inventory",
        "amount": 35613.51,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 891,
        "date": "2025-07-25",
        "description": "Sales to Lucky Hosiery",
        "amount": 340563.9,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 892,
        "date": "2025-07-25",
        "description": "GST collected on sales",
        "amount": 61301.5,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 893,
        "date": "2025-07-29",
        "description": "Sales to Bombay Fashion House",
        "amount": 165209.28,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 894,
        "date": "2025-07-29",
        "description": "GST collected on sales",
        "amount": 29737.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 895,
        "date": "2025-07-29",
        "description": "Payment received from customer",
        "amount": 120382.11,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 896,
        "date": "2025-07-30",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 191373.54,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 897,
        "date": "2025-07-30",
        "description": "GST input on inventory",
        "amount": 34447.24,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 898,
        "date": "2025-08-01",
        "description": "Office rent paid",
        "amount": 48685.45,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 899,
        "date": "2025-08-01",
        "description": "Salary paid to employees",
        "amount": 80119.9,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 900,
        "date": "2025-08-01",
        "description": "Sales to Mehta Garments",
        "amount": 321453.96,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 901,
        "date": "2025-08-01",
        "description": "GST collected on sales",
        "amount": 57861.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 902,
        "date": "2025-08-04",
        "description": "Sale of old machinery",
        "amount": 57019.29,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 903,
        "date": "2025-08-05",
        "description": "Electricity bill payment",
        "amount": 15926.27,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 904,
        "date": "2025-08-05",
        "description": "Water and utility charges",
        "amount": 4638.63,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 905,
        "date": "2025-08-05",
        "description": "Sales to Bombay Fashion House",
        "amount": 236998.93,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 906,
        "date": "2025-08-05",
        "description": "GST collected on sales",
        "amount": 42659.81,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 907,
        "date": "2025-08-06",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 204854.22,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 908,
        "date": "2025-08-06",
        "description": "GST input on inventory",
        "amount": 36873.76,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 909,
        "date": "2025-08-08",
        "description": "Sales to Lucky Hosiery",
        "amount": 215171.67,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 910,
        "date": "2025-08-08",
        "description": "GST collected on sales",
        "amount": 38730.9,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 911,
        "date": "2025-08-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 912,
        "date": "2025-08-10",
        "description": "Interest paid on bank loan",
        "amount": 12014.2,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 913,
        "date": "2025-08-10",
        "description": "Sales return from customer",
        "amount": 14293.19,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 914,
        "date": "2025-08-10",
        "description": "Advance corporate tax payment",
        "amount": 77229.38,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 915,
        "date": "2025-08-12",
        "description": "Sales to Lucky Hosiery",
        "amount": 175524.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 916,
        "date": "2025-08-12",
        "description": "GST collected on sales",
        "amount": 31594.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 917,
        "date": "2025-08-13",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 268522.18,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 918,
        "date": "2025-08-13",
        "description": "GST input on inventory",
        "amount": 48333.99,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 919,
        "date": "2025-08-15",
        "description": "GST payment to government",
        "amount": 45274.77,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 920,
        "date": "2025-08-15",
        "description": "TDS payment to government",
        "amount": 10648.3,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 921,
        "date": "2025-08-15",
        "description": "Sales to Bombay Fashion House",
        "amount": 211080.13,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 922,
        "date": "2025-08-15",
        "description": "GST collected on sales",
        "amount": 37994.42,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 923,
        "date": "2025-08-15",
        "description": "Accumulated depreciation recorded",
        "amount": 24120.27,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 924,
        "date": "2025-08-17",
        "description": "Monthly bank processing fees",
        "amount": 697.86,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 925,
        "date": "2025-08-19",
        "description": "Sales to Rajan Fabrics",
        "amount": 155944.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 926,
        "date": "2025-08-19",
        "description": "GST collected on sales",
        "amount": 28070.1,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 927,
        "date": "2025-08-20",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 204435.5,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 928,
        "date": "2025-08-20",
        "description": "GST input on inventory",
        "amount": 36798.39,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 929,
        "date": "2025-08-21",
        "description": "Accumulated depreciation recorded",
        "amount": 25436.65,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 930,
        "date": "2025-08-21",
        "description": "Brokerage and commission paid",
        "amount": 12930.48,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 931,
        "date": "2025-08-22",
        "description": "Sales to Lucky Hosiery",
        "amount": 161342.03,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 932,
        "date": "2025-08-22",
        "description": "GST collected on sales",
        "amount": 29041.57,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 933,
        "date": "2025-08-26",
        "description": "Sales to Mehta Garments",
        "amount": 237750.25,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 934,
        "date": "2025-08-26",
        "description": "GST collected on sales",
        "amount": 42795.04,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 935,
        "date": "2025-08-27",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 231240.41,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 936,
        "date": "2025-08-27",
        "description": "GST input on inventory",
        "amount": 41623.27,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 937,
        "date": "2025-08-28",
        "description": "Fuel for delivery vehicles",
        "amount": 19147.99,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 938,
        "date": "2025-08-29",
        "description": "Sales to Lucky Hosiery",
        "amount": 214893.75,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 939,
        "date": "2025-08-29",
        "description": "GST collected on sales",
        "amount": 38680.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 940,
        "date": "2025-08-29",
        "description": "Brokerage and commission paid",
        "amount": 12702.03,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 941,
        "date": "2025-09-01",
        "description": "Office rent paid",
        "amount": 48872.52,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 942,
        "date": "2025-09-01",
        "description": "Salary paid to employees",
        "amount": 82356.01,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 943,
        "date": "2025-09-02",
        "description": "Sales to Rajan Fabrics",
        "amount": 325211.82,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 944,
        "date": "2025-09-02",
        "description": "GST collected on sales",
        "amount": 58538.13,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 945,
        "date": "2025-09-02",
        "description": "Advance received for large order",
        "amount": 62378.66,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 946,
        "date": "2025-09-03",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 244590.58,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 947,
        "date": "2025-09-03",
        "description": "GST input on inventory",
        "amount": 44026.3,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 948,
        "date": "2025-09-03",
        "description": "Annual insurance premium",
        "amount": 24382.02,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 949,
        "date": "2025-09-04",
        "description": "Payment received from customer",
        "amount": 138576.7,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 950,
        "date": "2025-09-05",
        "description": "Electricity bill payment",
        "amount": 10934.02,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 951,
        "date": "2025-09-05",
        "description": "Water and utility charges",
        "amount": 4858.73,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 952,
        "date": "2025-09-05",
        "description": "Sales to Mehta Garments",
        "amount": 204882.18,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 953,
        "date": "2025-09-05",
        "description": "GST collected on sales",
        "amount": 36878.79,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 954,
        "date": "2025-09-09",
        "description": "Sales to Bombay Fashion House",
        "amount": 195498.33,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 955,
        "date": "2025-09-09",
        "description": "GST collected on sales",
        "amount": 35189.7,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 956,
        "date": "2025-09-09",
        "description": "Interest earned on FD",
        "amount": 13476.42,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 957,
        "date": "2025-09-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 958,
        "date": "2025-09-10",
        "description": "Interest paid on bank loan",
        "amount": 15506.33,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 959,
        "date": "2025-09-10",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 215700.74,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 960,
        "date": "2025-09-10",
        "description": "GST input on inventory",
        "amount": 38826.13,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 961,
        "date": "2025-09-12",
        "description": "Sales to Mehta Garments",
        "amount": 257548.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 962,
        "date": "2025-09-12",
        "description": "GST collected on sales",
        "amount": 46358.76,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 963,
        "date": "2025-09-14",
        "description": "Forex loss on import payables",
        "amount": 3617.88,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 964,
        "date": "2025-09-15",
        "description": "GST payment to government",
        "amount": 57382.77,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 965,
        "date": "2025-09-15",
        "description": "TDS payment to government",
        "amount": 11913.18,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 966,
        "date": "2025-09-16",
        "description": "Sales to Bombay Fashion House",
        "amount": 225942.1,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 967,
        "date": "2025-09-16",
        "description": "GST collected on sales",
        "amount": 40669.58,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 968,
        "date": "2025-09-17",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 226623.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 969,
        "date": "2025-09-17",
        "description": "GST input on inventory",
        "amount": 40792.15,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 970,
        "date": "2025-09-19",
        "description": "Sales to Mehta Garments",
        "amount": 153083.31,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 971,
        "date": "2025-09-19",
        "description": "GST collected on sales",
        "amount": 27555.0,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 972,
        "date": "2025-09-21",
        "description": "Accumulated depreciation recorded",
        "amount": 20381.04,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 973,
        "date": "2025-09-22",
        "description": "Sale of old machinery",
        "amount": 85861.52,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 974,
        "date": "2025-09-23",
        "description": "Sales to Rajan Fabrics",
        "amount": 175883.9,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 975,
        "date": "2025-09-23",
        "description": "GST collected on sales",
        "amount": 31659.1,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 976,
        "date": "2025-09-24",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 235439.79,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 977,
        "date": "2025-09-24",
        "description": "GST input on inventory",
        "amount": 42379.16,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 978,
        "date": "2025-09-26",
        "description": "Sales to Bombay Fashion House",
        "amount": 329578.22,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 979,
        "date": "2025-09-26",
        "description": "GST collected on sales",
        "amount": 59324.08,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 980,
        "date": "2025-09-29",
        "description": "Mutual fund investment",
        "amount": 97100.69,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 981,
        "date": "2025-09-30",
        "description": "Sales to Rajan Fabrics",
        "amount": 201771.15,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 982,
        "date": "2025-09-30",
        "description": "GST collected on sales",
        "amount": 36318.81,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 983,
        "date": "2025-09-30",
        "description": "Advance corporate tax payment",
        "amount": 65847.46,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 984,
        "date": "2025-10-01",
        "description": "Office rent paid",
        "amount": 45247.54,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 985,
        "date": "2025-10-01",
        "description": "Salary paid to employees",
        "amount": 79978.22,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 986,
        "date": "2025-10-01",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 216904.05,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 987,
        "date": "2025-10-01",
        "description": "GST input on inventory",
        "amount": 39042.73,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 988,
        "date": "2025-10-01",
        "description": "Digital marketing campaign",
        "amount": 24543.43,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 989,
        "date": "2025-10-03",
        "description": "Sales to Mehta Garments",
        "amount": 170788.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 990,
        "date": "2025-10-03",
        "description": "GST collected on sales",
        "amount": 30742.02,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 991,
        "date": "2025-10-03",
        "description": "Sales return from customer",
        "amount": 26559.12,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 992,
        "date": "2025-10-03",
        "description": "Monthly bank processing fees",
        "amount": 1780.97,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 993,
        "date": "2025-10-04",
        "description": "Vendor payment against outstanding",
        "amount": 110061.65,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 994,
        "date": "2025-10-05",
        "description": "Electricity bill payment",
        "amount": 14098.01,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 995,
        "date": "2025-10-05",
        "description": "Water and utility charges",
        "amount": 4735.73,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 996,
        "date": "2025-10-07",
        "description": "Sales to Bombay Fashion House",
        "amount": 298737.72,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 997,
        "date": "2025-10-07",
        "description": "GST collected on sales",
        "amount": 53772.79,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 998,
        "date": "2025-10-07",
        "description": "Brokerage and commission paid",
        "amount": 12097.14,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 999,
        "date": "2025-10-08",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 208198.27,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1000,
        "date": "2025-10-08",
        "description": "GST input on inventory",
        "amount": 37475.69,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1001,
        "date": "2025-10-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1002,
        "date": "2025-10-10",
        "description": "Interest paid on bank loan",
        "amount": 14040.81,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1003,
        "date": "2025-10-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 155309.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1004,
        "date": "2025-10-10",
        "description": "GST collected on sales",
        "amount": 27955.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1005,
        "date": "2025-10-10",
        "description": "Monthly bank processing fees",
        "amount": 650.9,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 1006,
        "date": "2025-10-11",
        "description": "Further equity capital introduced",
        "amount": 905895.94,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1007,
        "date": "2025-10-13",
        "description": "Software license capitalization",
        "amount": 45596.96,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 1008,
        "date": "2025-10-14",
        "description": "Sales to Mehta Garments",
        "amount": 192751.78,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1009,
        "date": "2025-10-14",
        "description": "GST collected on sales",
        "amount": 34695.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1010,
        "date": "2025-10-15",
        "description": "GST payment to government",
        "amount": 73551.14,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1011,
        "date": "2025-10-15",
        "description": "TDS payment to government",
        "amount": 9420.63,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1012,
        "date": "2025-10-15",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 201946.55,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1013,
        "date": "2025-10-15",
        "description": "GST input on inventory",
        "amount": 36350.38,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1014,
        "date": "2025-10-15",
        "description": "Advance corporate tax payment",
        "amount": 72925.86,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1015,
        "date": "2025-10-17",
        "description": "Sales to Mehta Garments",
        "amount": 197341.43,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1016,
        "date": "2025-10-17",
        "description": "GST collected on sales",
        "amount": 35521.46,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1017,
        "date": "2025-10-19",
        "description": "Courier and postage charges",
        "amount": 4141.19,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1018,
        "date": "2025-10-20",
        "description": "GST reversal on sales return",
        "amount": 2236.49,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1019,
        "date": "2025-10-20",
        "description": "Advance received for large order",
        "amount": 71489.3,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1020,
        "date": "2025-10-21",
        "description": "Sales to Bombay Fashion House",
        "amount": 150615.79,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1021,
        "date": "2025-10-21",
        "description": "GST collected on sales",
        "amount": 27110.84,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1022,
        "date": "2025-10-21",
        "description": "Courier and postage charges",
        "amount": 3402.68,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1023,
        "date": "2025-10-22",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 269698.82,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1024,
        "date": "2025-10-22",
        "description": "GST input on inventory",
        "amount": 48545.79,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1025,
        "date": "2025-10-23",
        "description": "Legal and consultancy fees",
        "amount": 33596.51,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 1026,
        "date": "2025-10-24",
        "description": "Sales to Rajan Fabrics",
        "amount": 203518.24,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1027,
        "date": "2025-10-24",
        "description": "GST collected on sales",
        "amount": 36633.28,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1028,
        "date": "2025-10-25",
        "description": "Purchase return to vendor",
        "amount": 18010.52,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1029,
        "date": "2025-10-28",
        "description": "Sales to Lucky Hosiery",
        "amount": 272793.14,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1030,
        "date": "2025-10-28",
        "description": "GST collected on sales",
        "amount": 49102.77,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1031,
        "date": "2025-10-29",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 225645.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1032,
        "date": "2025-10-29",
        "description": "GST input on inventory",
        "amount": 40616.11,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1033,
        "date": "2025-10-31",
        "description": "Sales to Lucky Hosiery",
        "amount": 284285.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1034,
        "date": "2025-10-31",
        "description": "GST collected on sales",
        "amount": 51171.48,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1035,
        "date": "2025-11-01",
        "description": "Office rent paid",
        "amount": 43436.35,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1036,
        "date": "2025-11-01",
        "description": "Salary paid to employees",
        "amount": 77846.92,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1037,
        "date": "2025-11-01",
        "description": "Advance received for large order",
        "amount": 90852.71,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1038,
        "date": "2025-11-02",
        "description": "Vehicle maintenance and repair",
        "amount": 14887.35,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1039,
        "date": "2025-11-03",
        "description": "Annual insurance premium",
        "amount": 34333.89,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 1040,
        "date": "2025-11-04",
        "description": "Sales to Rajan Fabrics",
        "amount": 291231.21,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1041,
        "date": "2025-11-04",
        "description": "GST collected on sales",
        "amount": 52421.62,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1042,
        "date": "2025-11-05",
        "description": "Electricity bill payment",
        "amount": 10467.83,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1043,
        "date": "2025-11-05",
        "description": "Water and utility charges",
        "amount": 5503.35,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1044,
        "date": "2025-11-05",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 226333.49,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1045,
        "date": "2025-11-05",
        "description": "GST input on inventory",
        "amount": 40740.03,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1046,
        "date": "2025-11-06",
        "description": "Depreciation charged on assets",
        "amount": 22767.41,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1047,
        "date": "2025-11-07",
        "description": "Sales to Rajan Fabrics",
        "amount": 216373.24,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1048,
        "date": "2025-11-07",
        "description": "GST collected on sales",
        "amount": 38947.18,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1049,
        "date": "2025-11-08",
        "description": "Digital marketing campaign",
        "amount": 22361.66,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1050,
        "date": "2025-11-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1051,
        "date": "2025-11-10",
        "description": "Interest paid on bank loan",
        "amount": 14828.51,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1052,
        "date": "2025-11-10",
        "description": "Accumulated depreciation recorded",
        "amount": 24988.85,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1053,
        "date": "2025-11-10",
        "description": "Annual insurance premium",
        "amount": 23928.68,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 1054,
        "date": "2025-11-11",
        "description": "Sales to Bombay Fashion House",
        "amount": 289168.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1055,
        "date": "2025-11-11",
        "description": "GST collected on sales",
        "amount": 52050.3,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1056,
        "date": "2025-11-12",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 232204.25,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1057,
        "date": "2025-11-12",
        "description": "GST input on inventory",
        "amount": 41796.77,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1058,
        "date": "2025-11-12",
        "description": "Employee travel reimbursement",
        "amount": 9055.99,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1059,
        "date": "2025-11-13",
        "description": "Vendor payment against outstanding",
        "amount": 104118.8,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1060,
        "date": "2025-11-14",
        "description": "Sales to Lucky Hosiery",
        "amount": 166016.44,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1061,
        "date": "2025-11-14",
        "description": "GST collected on sales",
        "amount": 29882.96,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1062,
        "date": "2025-11-15",
        "description": "GST payment to government",
        "amount": 53196.42,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1063,
        "date": "2025-11-15",
        "description": "TDS payment to government",
        "amount": 12716.86,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1064,
        "date": "2025-11-18",
        "description": "Sales to Rajan Fabrics",
        "amount": 234797.83,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1065,
        "date": "2025-11-18",
        "description": "GST collected on sales",
        "amount": 42263.61,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1066,
        "date": "2025-11-19",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 210260.46,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1067,
        "date": "2025-11-19",
        "description": "GST input on inventory",
        "amount": 37846.88,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1068,
        "date": "2025-11-21",
        "description": "Sales to Bombay Fashion House",
        "amount": 158136.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1069,
        "date": "2025-11-21",
        "description": "GST collected on sales",
        "amount": 28464.53,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1070,
        "date": "2025-11-21",
        "description": "Depreciation charged on assets",
        "amount": 24371.94,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1071,
        "date": "2025-11-24",
        "description": "Statutory audit fees",
        "amount": 34452.45,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1072,
        "date": "2025-11-24",
        "description": "Fuel for delivery vehicles",
        "amount": 16824.13,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 1073,
        "date": "2025-11-25",
        "description": "Sales to Mehta Garments",
        "amount": 204807.22,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1074,
        "date": "2025-11-25",
        "description": "GST collected on sales",
        "amount": 36865.3,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1075,
        "date": "2025-11-25",
        "description": "Vehicle maintenance and repair",
        "amount": 14771.41,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1076,
        "date": "2025-11-26",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 238304.77,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1077,
        "date": "2025-11-26",
        "description": "GST input on inventory",
        "amount": 42894.86,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1078,
        "date": "2025-11-26",
        "description": "Fuel for delivery vehicles",
        "amount": 10086.49,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 1079,
        "date": "2025-11-27",
        "description": "Sale of old machinery",
        "amount": 53447.58,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 1080,
        "date": "2025-11-27",
        "description": "Further equity capital introduced",
        "amount": 597387.52,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1081,
        "date": "2025-11-27",
        "description": "Sales return from customer",
        "amount": 14102.62,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1082,
        "date": "2025-11-28",
        "description": "Sales to Lucky Hosiery",
        "amount": 209307.94,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1083,
        "date": "2025-11-28",
        "description": "GST collected on sales",
        "amount": 37675.43,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1084,
        "date": "2025-11-30",
        "description": "Statutory audit fees",
        "amount": 49209.58,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1085,
        "date": "2025-12-01",
        "description": "Office rent paid",
        "amount": 43452.24,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1086,
        "date": "2025-12-01",
        "description": "Salary paid to employees",
        "amount": 70873.61,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1087,
        "date": "2025-12-02",
        "description": "Sales to Mehta Garments",
        "amount": 162021.61,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1088,
        "date": "2025-12-02",
        "description": "GST collected on sales",
        "amount": 29163.89,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1089,
        "date": "2025-12-03",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 250148.51,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1090,
        "date": "2025-12-03",
        "description": "GST input on inventory",
        "amount": 45026.73,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1091,
        "date": "2025-12-04",
        "description": "Scrap sale proceeds",
        "amount": 6800.49,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1092,
        "date": "2025-12-05",
        "description": "Electricity bill payment",
        "amount": 11051.8,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1093,
        "date": "2025-12-05",
        "description": "Water and utility charges",
        "amount": 4044.35,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1094,
        "date": "2025-12-05",
        "description": "Sales to Rajan Fabrics",
        "amount": 344811.68,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1095,
        "date": "2025-12-05",
        "description": "GST collected on sales",
        "amount": 62066.1,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1096,
        "date": "2025-12-07",
        "description": "Brokerage and commission paid",
        "amount": 13187.27,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1097,
        "date": "2025-12-09",
        "description": "Sales to Lucky Hosiery",
        "amount": 288755.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1098,
        "date": "2025-12-09",
        "description": "GST collected on sales",
        "amount": 51976.01,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1099,
        "date": "2025-12-09",
        "description": "Statutory audit fees",
        "amount": 47696.27,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1100,
        "date": "2025-12-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1101,
        "date": "2025-12-10",
        "description": "Interest paid on bank loan",
        "amount": 15114.8,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1102,
        "date": "2025-12-10",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 238894.27,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1103,
        "date": "2025-12-10",
        "description": "GST input on inventory",
        "amount": 43000.97,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1104,
        "date": "2025-12-10",
        "description": "Advance received for large order",
        "amount": 84960.32,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1105,
        "date": "2025-12-12",
        "description": "Sales to Lucky Hosiery",
        "amount": 207034.6,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1106,
        "date": "2025-12-12",
        "description": "GST collected on sales",
        "amount": 37266.23,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1107,
        "date": "2025-12-12",
        "description": "Printing and stationery",
        "amount": 3391.84,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1108,
        "date": "2025-12-15",
        "description": "GST payment to government",
        "amount": 70374.11,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1109,
        "date": "2025-12-15",
        "description": "TDS payment to government",
        "amount": 9150.12,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1110,
        "date": "2025-12-15",
        "description": "Vehicle maintenance and repair",
        "amount": 10533.99,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1111,
        "date": "2025-12-16",
        "description": "Sales to Lucky Hosiery",
        "amount": 267236.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1112,
        "date": "2025-12-16",
        "description": "GST collected on sales",
        "amount": 48102.5,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1113,
        "date": "2025-12-16",
        "description": "Scrap sale proceeds",
        "amount": 5044.66,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1114,
        "date": "2025-12-17",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 201861.35,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1115,
        "date": "2025-12-17",
        "description": "GST input on inventory",
        "amount": 36335.04,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1116,
        "date": "2025-12-19",
        "description": "Sales to Bombay Fashion House",
        "amount": 279085.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1117,
        "date": "2025-12-19",
        "description": "GST collected on sales",
        "amount": 50235.47,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1118,
        "date": "2025-12-21",
        "description": "Vehicle maintenance and repair",
        "amount": 7485.76,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1119,
        "date": "2025-12-23",
        "description": "Sales to Rajan Fabrics",
        "amount": 300098.67,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1120,
        "date": "2025-12-23",
        "description": "GST collected on sales",
        "amount": 54017.76,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1121,
        "date": "2025-12-24",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 188551.9,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1122,
        "date": "2025-12-24",
        "description": "GST input on inventory",
        "amount": 33939.34,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1123,
        "date": "2025-12-24",
        "description": "Advance received for large order",
        "amount": 89845.73,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1124,
        "date": "2025-12-25",
        "description": "Further equity capital introduced",
        "amount": 555022.13,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1125,
        "date": "2025-12-26",
        "description": "Sales to Rajan Fabrics",
        "amount": 179959.92,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1126,
        "date": "2025-12-26",
        "description": "GST collected on sales",
        "amount": 32392.79,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1127,
        "date": "2025-12-26",
        "description": "Purchase return to vendor",
        "amount": 20569.02,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1128,
        "date": "2025-12-29",
        "description": "Forex gain on export receivables",
        "amount": 2728.39,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1129,
        "date": "2025-12-29",
        "description": "Vehicle maintenance and repair",
        "amount": 9208.79,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1130,
        "date": "2025-12-30",
        "description": "Sales to Bombay Fashion House",
        "amount": 191494.47,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1131,
        "date": "2025-12-30",
        "description": "GST collected on sales",
        "amount": 34469.0,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1132,
        "date": "2025-12-31",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 261779.62,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1133,
        "date": "2025-12-31",
        "description": "GST input on inventory",
        "amount": 47120.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1134,
        "date": "2025-12-31",
        "description": "Forex loss on import payables",
        "amount": 3487.99,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1135,
        "date": "2026-01-01",
        "description": "Office rent paid",
        "amount": 44738.26,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1136,
        "date": "2026-01-01",
        "description": "Salary paid to employees",
        "amount": 85625.97,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1137,
        "date": "2026-01-02",
        "description": "Sales to Lucky Hosiery",
        "amount": 165585.84,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1138,
        "date": "2026-01-02",
        "description": "GST collected on sales",
        "amount": 29805.45,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1139,
        "date": "2026-01-05",
        "description": "Electricity bill payment",
        "amount": 10970.07,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1140,
        "date": "2026-01-05",
        "description": "Water and utility charges",
        "amount": 5505.2,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1141,
        "date": "2026-01-05",
        "description": "Further equity capital introduced",
        "amount": 726809.16,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1142,
        "date": "2026-01-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 237213.84,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1143,
        "date": "2026-01-06",
        "description": "GST collected on sales",
        "amount": 42698.49,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1144,
        "date": "2026-01-07",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 249814.26,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1145,
        "date": "2026-01-07",
        "description": "GST input on inventory",
        "amount": 44966.57,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1146,
        "date": "2026-01-08",
        "description": "Purchase return to vendor",
        "amount": 19353.72,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1147,
        "date": "2026-01-09",
        "description": "Sales to Lucky Hosiery",
        "amount": 346775.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1148,
        "date": "2026-01-09",
        "description": "GST collected on sales",
        "amount": 62419.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1149,
        "date": "2026-01-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1150,
        "date": "2026-01-10",
        "description": "Interest paid on bank loan",
        "amount": 14452.85,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1151,
        "date": "2026-01-13",
        "description": "Sales to Rajan Fabrics",
        "amount": 199104.57,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1152,
        "date": "2026-01-13",
        "description": "GST collected on sales",
        "amount": 35838.82,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1153,
        "date": "2026-01-14",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 233546.31,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1154,
        "date": "2026-01-14",
        "description": "GST input on inventory",
        "amount": 42038.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1155,
        "date": "2026-01-14",
        "description": "Fuel for delivery vehicles",
        "amount": 16010.91,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 1156,
        "date": "2026-01-14",
        "description": "Sales return from customer",
        "amount": 11425.88,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1157,
        "date": "2026-01-15",
        "description": "GST payment to government",
        "amount": 72896.36,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1158,
        "date": "2026-01-15",
        "description": "TDS payment to government",
        "amount": 11781.68,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1159,
        "date": "2026-01-15",
        "description": "Further equity capital introduced",
        "amount": 700887.37,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1160,
        "date": "2026-01-16",
        "description": "Sales to Bombay Fashion House",
        "amount": 185373.43,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1161,
        "date": "2026-01-16",
        "description": "GST collected on sales",
        "amount": 33367.22,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1162,
        "date": "2026-01-16",
        "description": "Employee travel reimbursement",
        "amount": 11154.31,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1163,
        "date": "2026-01-16",
        "description": "Forex loss on import payables",
        "amount": 7027.5,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1164,
        "date": "2026-01-18",
        "description": "Forex gain on export receivables",
        "amount": 2853.24,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1165,
        "date": "2026-01-20",
        "description": "Sales to Lucky Hosiery",
        "amount": 213737.3,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1166,
        "date": "2026-01-20",
        "description": "GST collected on sales",
        "amount": 38472.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1167,
        "date": "2026-01-21",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 263674.57,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1168,
        "date": "2026-01-21",
        "description": "GST input on inventory",
        "amount": 47461.42,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1169,
        "date": "2026-01-21",
        "description": "GST reversal on sales return",
        "amount": 2982.8,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1170,
        "date": "2026-01-22",
        "description": "Legal and consultancy fees",
        "amount": 15993.0,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 1171,
        "date": "2026-01-23",
        "description": "Sales to Rajan Fabrics",
        "amount": 328405.68,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1172,
        "date": "2026-01-23",
        "description": "GST collected on sales",
        "amount": 59113.02,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1173,
        "date": "2026-01-23",
        "description": "Interim dividend payout",
        "amount": 190972.23,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1174,
        "date": "2026-01-23",
        "description": "Employee performance bonus",
        "amount": 47102.59,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 1175,
        "date": "2026-01-25",
        "description": "Interim dividend payout",
        "amount": 132941.99,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1176,
        "date": "2026-01-26",
        "description": "Depreciation charged on assets",
        "amount": 29896.5,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1177,
        "date": "2026-01-27",
        "description": "Sales to Mehta Garments",
        "amount": 237072.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1178,
        "date": "2026-01-27",
        "description": "GST collected on sales",
        "amount": 42672.98,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1179,
        "date": "2026-01-28",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 266811.69,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1180,
        "date": "2026-01-28",
        "description": "GST input on inventory",
        "amount": 48026.11,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1181,
        "date": "2026-01-29",
        "description": "Purchase return to vendor",
        "amount": 21175.0,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1182,
        "date": "2026-01-30",
        "description": "Sales to Mehta Garments",
        "amount": 349109.01,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1183,
        "date": "2026-01-30",
        "description": "GST collected on sales",
        "amount": 62839.62,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1184,
        "date": "2026-02-01",
        "description": "Office rent paid",
        "amount": 42682.05,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1185,
        "date": "2026-02-01",
        "description": "Salary paid to employees",
        "amount": 83239.59,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1186,
        "date": "2026-02-03",
        "description": "Sales to Rajan Fabrics",
        "amount": 321838.28,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1187,
        "date": "2026-02-03",
        "description": "GST collected on sales",
        "amount": 57930.89,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1188,
        "date": "2026-02-03",
        "description": "Brokerage and commission paid",
        "amount": 14012.76,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1189,
        "date": "2026-02-04",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 249942.89,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1190,
        "date": "2026-02-04",
        "description": "GST input on inventory",
        "amount": 44989.72,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1191,
        "date": "2026-02-04",
        "description": "Scrap sale proceeds",
        "amount": 5157.05,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1192,
        "date": "2026-02-05",
        "description": "Electricity bill payment",
        "amount": 15345.21,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1193,
        "date": "2026-02-05",
        "description": "Water and utility charges",
        "amount": 3139.74,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1194,
        "date": "2026-02-06",
        "description": "Sales to Lucky Hosiery",
        "amount": 259904.37,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1195,
        "date": "2026-02-06",
        "description": "GST collected on sales",
        "amount": 46782.79,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1196,
        "date": "2026-02-09",
        "description": "Printing and stationery",
        "amount": 2168.85,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1197,
        "date": "2026-02-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1198,
        "date": "2026-02-10",
        "description": "Interest paid on bank loan",
        "amount": 13283.35,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1199,
        "date": "2026-02-10",
        "description": "Sales to Mehta Garments",
        "amount": 332759.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1200,
        "date": "2026-02-10",
        "description": "GST collected on sales",
        "amount": 59896.64,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1201,
        "date": "2026-02-11",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 278297.61,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1202,
        "date": "2026-02-11",
        "description": "GST input on inventory",
        "amount": 50093.57,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1203,
        "date": "2026-02-13",
        "description": "Sales to Lucky Hosiery",
        "amount": 224718.75,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1204,
        "date": "2026-02-13",
        "description": "GST collected on sales",
        "amount": 40449.38,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1205,
        "date": "2026-02-14",
        "description": "Forex gain on export receivables",
        "amount": 3027.23,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1206,
        "date": "2026-02-15",
        "description": "GST payment to government",
        "amount": 67255.6,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1207,
        "date": "2026-02-15",
        "description": "TDS payment to government",
        "amount": 11197.18,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1208,
        "date": "2026-02-15",
        "description": "Digital marketing campaign",
        "amount": 17304.55,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1209,
        "date": "2026-02-16",
        "description": "Customs duty on imports",
        "amount": 32291.94,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1210,
        "date": "2026-02-17",
        "description": "Sales to Bombay Fashion House",
        "amount": 230514.96,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1211,
        "date": "2026-02-17",
        "description": "GST collected on sales",
        "amount": 41492.69,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1212,
        "date": "2026-02-17",
        "description": "Purchase return to vendor",
        "amount": 21579.38,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1213,
        "date": "2026-02-17",
        "description": "Depreciation charged on assets",
        "amount": 22558.55,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1214,
        "date": "2026-02-18",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 263697.55,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1215,
        "date": "2026-02-18",
        "description": "GST input on inventory",
        "amount": 47465.56,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1216,
        "date": "2026-02-20",
        "description": "Sales to Bombay Fashion House",
        "amount": 206765.08,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1217,
        "date": "2026-02-20",
        "description": "GST collected on sales",
        "amount": 37217.71,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1218,
        "date": "2026-02-24",
        "description": "Sales to Mehta Garments",
        "amount": 318094.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1219,
        "date": "2026-02-24",
        "description": "GST collected on sales",
        "amount": 57257.04,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1220,
        "date": "2026-02-25",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 213418.88,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1221,
        "date": "2026-02-25",
        "description": "GST input on inventory",
        "amount": 38415.4,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1222,
        "date": "2026-02-27",
        "description": "Sales to Bombay Fashion House",
        "amount": 341966.18,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1223,
        "date": "2026-02-27",
        "description": "GST collected on sales",
        "amount": 61553.91,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1224,
        "date": "2026-02-27",
        "description": "Scrap sale proceeds",
        "amount": 3968.37,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1225,
        "date": "2026-02-28",
        "description": "Accumulated depreciation recorded",
        "amount": 16910.69,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1226,
        "date": "2026-03-01",
        "description": "Office rent paid",
        "amount": 42224.21,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1227,
        "date": "2026-03-01",
        "description": "Salary paid to employees",
        "amount": 75570.69,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1228,
        "date": "2026-03-03",
        "description": "Sales to Bombay Fashion House",
        "amount": 310829.47,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1229,
        "date": "2026-03-03",
        "description": "GST collected on sales",
        "amount": 55949.3,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1230,
        "date": "2026-03-04",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 255912.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1231,
        "date": "2026-03-04",
        "description": "GST input on inventory",
        "amount": 46064.17,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1232,
        "date": "2026-03-05",
        "description": "Electricity bill payment",
        "amount": 12895.05,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1233,
        "date": "2026-03-05",
        "description": "Water and utility charges",
        "amount": 3371.6,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1234,
        "date": "2026-03-05",
        "description": "Courier and postage charges",
        "amount": 2451.22,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1235,
        "date": "2026-03-05",
        "description": "Purchase return to vendor",
        "amount": 23916.31,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1236,
        "date": "2026-03-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 191530.82,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1237,
        "date": "2026-03-06",
        "description": "GST collected on sales",
        "amount": 34475.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1238,
        "date": "2026-03-06",
        "description": "Legal and consultancy fees",
        "amount": 18632.66,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 1239,
        "date": "2026-03-06",
        "description": "Employee travel reimbursement",
        "amount": 9988.34,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1240,
        "date": "2026-03-08",
        "description": "Forex gain on export receivables",
        "amount": 6214.0,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1241,
        "date": "2026-03-09",
        "description": "Interest earned on FD",
        "amount": 9055.64,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 1242,
        "date": "2026-03-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1243,
        "date": "2026-03-10",
        "description": "Interest paid on bank loan",
        "amount": 13621.97,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1244,
        "date": "2026-03-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 238646.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1245,
        "date": "2026-03-10",
        "description": "GST collected on sales",
        "amount": 42956.34,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1246,
        "date": "2026-03-11",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 232674.32,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1247,
        "date": "2026-03-11",
        "description": "GST input on inventory",
        "amount": 41881.38,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1248,
        "date": "2026-03-13",
        "description": "Sales to Rajan Fabrics",
        "amount": 225676.86,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1249,
        "date": "2026-03-13",
        "description": "GST collected on sales",
        "amount": 40621.83,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1250,
        "date": "2026-03-13",
        "description": "Vehicle maintenance and repair",
        "amount": 12237.77,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1251,
        "date": "2026-03-13",
        "description": "Payment received from customer",
        "amount": 167396.72,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1252,
        "date": "2026-03-14",
        "description": "Monthly bank processing fees",
        "amount": 548.07,
        "type": "debit",
        "category": "Bank Charges"
    },
    {
        "id": 1253,
        "date": "2026-03-15",
        "description": "GST payment to government",
        "amount": 71558.56,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1254,
        "date": "2026-03-15",
        "description": "TDS payment to government",
        "amount": 8398.3,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1255,
        "date": "2026-03-16",
        "description": "Digital marketing campaign",
        "amount": 21853.9,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1256,
        "date": "2026-03-17",
        "description": "Sales to Bombay Fashion House",
        "amount": 344526.71,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1257,
        "date": "2026-03-17",
        "description": "GST collected on sales",
        "amount": 62014.81,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1258,
        "date": "2026-03-17",
        "description": "Vehicle maintenance and repair",
        "amount": 9951.83,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1259,
        "date": "2026-03-18",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 204470.23,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1260,
        "date": "2026-03-18",
        "description": "GST input on inventory",
        "amount": 36804.64,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1261,
        "date": "2026-03-18",
        "description": "Sales return from customer",
        "amount": 11471.04,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1262,
        "date": "2026-03-20",
        "description": "Sales to Mehta Garments",
        "amount": 228818.53,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1263,
        "date": "2026-03-20",
        "description": "GST collected on sales",
        "amount": 41187.33,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1264,
        "date": "2026-03-23",
        "description": "Accumulated depreciation recorded",
        "amount": 28283.34,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1265,
        "date": "2026-03-23",
        "description": "Further equity capital introduced",
        "amount": 616244.15,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1266,
        "date": "2026-03-24",
        "description": "Sales to Rajan Fabrics",
        "amount": 300483.53,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1267,
        "date": "2026-03-24",
        "description": "GST collected on sales",
        "amount": 54087.04,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1268,
        "date": "2026-03-25",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 189939.73,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1269,
        "date": "2026-03-25",
        "description": "GST input on inventory",
        "amount": 34189.15,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1270,
        "date": "2026-03-26",
        "description": "Printing and stationery",
        "amount": 7119.42,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1271,
        "date": "2026-03-27",
        "description": "Sales to Mehta Garments",
        "amount": 297325.27,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1272,
        "date": "2026-03-27",
        "description": "GST collected on sales",
        "amount": 53518.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1273,
        "date": "2026-03-27",
        "description": "Sales return from customer",
        "amount": 21800.96,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1274,
        "date": "2026-03-28",
        "description": "Mutual fund investment",
        "amount": 215815.69,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 1275,
        "date": "2026-03-29",
        "description": "Forex loss on import payables",
        "amount": 9353.2,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1276,
        "date": "2026-03-30",
        "description": "Purchase return to vendor",
        "amount": 24233.06,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1277,
        "date": "2026-03-31",
        "description": "Sales to Bombay Fashion House",
        "amount": 329911.73,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1278,
        "date": "2026-03-31",
        "description": "GST collected on sales",
        "amount": 59384.11,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1279,
        "date": "2026-04-01",
        "description": "Office rent paid",
        "amount": 48005.74,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1280,
        "date": "2026-04-01",
        "description": "Salary paid to employees",
        "amount": 85847.47,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1281,
        "date": "2026-04-01",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 235154.43,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1282,
        "date": "2026-04-01",
        "description": "GST input on inventory",
        "amount": 42327.8,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1283,
        "date": "2026-04-02",
        "description": "Printing and stationery",
        "amount": 3405.72,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1284,
        "date": "2026-04-03",
        "description": "Sales to Mehta Garments",
        "amount": 302403.07,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1285,
        "date": "2026-04-03",
        "description": "GST collected on sales",
        "amount": 54432.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1286,
        "date": "2026-04-03",
        "description": "Miscellaneous office expenses",
        "amount": 2256.63,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 1287,
        "date": "2026-04-04",
        "description": "Interim dividend payout",
        "amount": 122245.27,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1288,
        "date": "2026-04-04",
        "description": "Statutory audit fees",
        "amount": 33853.82,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1289,
        "date": "2026-04-05",
        "description": "Electricity bill payment",
        "amount": 11243.61,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1290,
        "date": "2026-04-05",
        "description": "Water and utility charges",
        "amount": 5363.33,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1291,
        "date": "2026-04-05",
        "description": "Printing and stationery",
        "amount": 4115.8,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1292,
        "date": "2026-04-06",
        "description": "Interim dividend payout",
        "amount": 161079.59,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1293,
        "date": "2026-04-07",
        "description": "Sales to Rajan Fabrics",
        "amount": 275630.04,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1294,
        "date": "2026-04-07",
        "description": "GST collected on sales",
        "amount": 49613.41,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1295,
        "date": "2026-04-08",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 227601.13,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1296,
        "date": "2026-04-08",
        "description": "GST input on inventory",
        "amount": 40968.2,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1297,
        "date": "2026-04-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1298,
        "date": "2026-04-10",
        "description": "Interest paid on bank loan",
        "amount": 12412.27,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1299,
        "date": "2026-04-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 273726.68,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1300,
        "date": "2026-04-10",
        "description": "GST collected on sales",
        "amount": 49270.8,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1301,
        "date": "2026-04-12",
        "description": "Courier and postage charges",
        "amount": 2996.57,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1302,
        "date": "2026-04-14",
        "description": "Sales to Bombay Fashion House",
        "amount": 200327.04,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1303,
        "date": "2026-04-14",
        "description": "GST collected on sales",
        "amount": 36058.87,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1304,
        "date": "2026-04-14",
        "description": "Printing and stationery",
        "amount": 4003.64,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1305,
        "date": "2026-04-15",
        "description": "GST payment to government",
        "amount": 73746.68,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1306,
        "date": "2026-04-15",
        "description": "TDS payment to government",
        "amount": 10391.57,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1307,
        "date": "2026-04-15",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 236457.4,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1308,
        "date": "2026-04-15",
        "description": "GST input on inventory",
        "amount": 42562.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1309,
        "date": "2026-04-15",
        "description": "Brokerage and commission paid",
        "amount": 12148.69,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1310,
        "date": "2026-04-17",
        "description": "Sales to Lucky Hosiery",
        "amount": 256417.87,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1311,
        "date": "2026-04-17",
        "description": "GST collected on sales",
        "amount": 46155.22,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1312,
        "date": "2026-04-17",
        "description": "Purchase of new office equipment",
        "amount": 148717.11,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 1313,
        "date": "2026-04-19",
        "description": "Software license capitalization",
        "amount": 44410.0,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 1314,
        "date": "2026-04-20",
        "description": "Payment received from customer",
        "amount": 109211.23,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1315,
        "date": "2026-04-21",
        "description": "Sales to Mehta Garments",
        "amount": 337606.29,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1316,
        "date": "2026-04-21",
        "description": "GST collected on sales",
        "amount": 60769.13,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1317,
        "date": "2026-04-22",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 257454.54,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1318,
        "date": "2026-04-22",
        "description": "GST input on inventory",
        "amount": 46341.82,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1319,
        "date": "2026-04-22",
        "description": "Forex loss on import payables",
        "amount": 6701.15,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1320,
        "date": "2026-04-22",
        "description": "Forex loss on import payables",
        "amount": 9365.04,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1321,
        "date": "2026-04-24",
        "description": "Sales to Mehta Garments",
        "amount": 255651.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1322,
        "date": "2026-04-24",
        "description": "GST collected on sales",
        "amount": 46017.25,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1323,
        "date": "2026-04-28",
        "description": "Sales to Bombay Fashion House",
        "amount": 251046.16,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1324,
        "date": "2026-04-28",
        "description": "GST collected on sales",
        "amount": 45188.31,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1325,
        "date": "2026-04-29",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 277582.26,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1326,
        "date": "2026-04-29",
        "description": "GST input on inventory",
        "amount": 49964.81,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1327,
        "date": "2026-04-30",
        "description": "Scrap sale proceeds",
        "amount": 4392.4,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1328,
        "date": "2026-04-30",
        "description": "Employee travel reimbursement",
        "amount": 6243.51,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1329,
        "date": "2026-05-01",
        "description": "Office rent paid",
        "amount": 47012.23,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1330,
        "date": "2026-05-01",
        "description": "Salary paid to employees",
        "amount": 85525.98,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1331,
        "date": "2026-05-01",
        "description": "Sales to Bombay Fashion House",
        "amount": 272950.55,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1332,
        "date": "2026-05-01",
        "description": "GST collected on sales",
        "amount": 49131.1,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1333,
        "date": "2026-05-01",
        "description": "Forex gain on export receivables",
        "amount": 5959.67,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1334,
        "date": "2026-05-03",
        "description": "Purchase of new office equipment",
        "amount": 110703.87,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 1335,
        "date": "2026-05-05",
        "description": "Electricity bill payment",
        "amount": 12022.63,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1336,
        "date": "2026-05-05",
        "description": "Water and utility charges",
        "amount": 3696.49,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1337,
        "date": "2026-05-05",
        "description": "Sales to Bombay Fashion House",
        "amount": 319818.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1338,
        "date": "2026-05-05",
        "description": "GST collected on sales",
        "amount": 57567.4,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1339,
        "date": "2026-05-06",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 214714.48,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1340,
        "date": "2026-05-06",
        "description": "GST input on inventory",
        "amount": 38648.61,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1341,
        "date": "2026-05-08",
        "description": "Sales to Rajan Fabrics",
        "amount": 173235.71,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1342,
        "date": "2026-05-08",
        "description": "GST collected on sales",
        "amount": 31182.43,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1343,
        "date": "2026-05-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1344,
        "date": "2026-05-10",
        "description": "Interest paid on bank loan",
        "amount": 13229.72,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1345,
        "date": "2026-05-10",
        "description": "Accumulated depreciation recorded",
        "amount": 19261.23,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1346,
        "date": "2026-05-10",
        "description": "Customs duty on imports",
        "amount": 44834.7,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1347,
        "date": "2026-05-11",
        "description": "Digital marketing campaign",
        "amount": 21695.48,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1348,
        "date": "2026-05-12",
        "description": "Sales to Mehta Garments",
        "amount": 180957.57,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1349,
        "date": "2026-05-12",
        "description": "GST collected on sales",
        "amount": 32572.36,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1350,
        "date": "2026-05-13",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 198635.19,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1351,
        "date": "2026-05-13",
        "description": "GST input on inventory",
        "amount": 35754.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1352,
        "date": "2026-05-15",
        "description": "GST payment to government",
        "amount": 46826.92,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1353,
        "date": "2026-05-15",
        "description": "TDS payment to government",
        "amount": 11875.55,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1354,
        "date": "2026-05-15",
        "description": "Sales to Mehta Garments",
        "amount": 197482.36,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1355,
        "date": "2026-05-15",
        "description": "GST collected on sales",
        "amount": 35546.83,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1356,
        "date": "2026-05-17",
        "description": "Annual insurance premium",
        "amount": 27756.7,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 1357,
        "date": "2026-05-19",
        "description": "Sales to Mehta Garments",
        "amount": 153640.25,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1358,
        "date": "2026-05-19",
        "description": "GST collected on sales",
        "amount": 27655.25,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1359,
        "date": "2026-05-20",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 225815.49,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1360,
        "date": "2026-05-20",
        "description": "GST input on inventory",
        "amount": 40646.79,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1361,
        "date": "2026-05-21",
        "description": "Interim dividend payout",
        "amount": 168527.42,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1362,
        "date": "2026-05-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 173225.08,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1363,
        "date": "2026-05-22",
        "description": "GST collected on sales",
        "amount": 31180.51,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1364,
        "date": "2026-05-22",
        "description": "Statutory audit fees",
        "amount": 32429.19,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1365,
        "date": "2026-05-22",
        "description": "Brokerage and commission paid",
        "amount": 13180.42,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1366,
        "date": "2026-05-22",
        "description": "Advance corporate tax payment",
        "amount": 75421.82,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1367,
        "date": "2026-05-24",
        "description": "Employee performance bonus",
        "amount": 22328.65,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 1368,
        "date": "2026-05-25",
        "description": "Interest earned on FD",
        "amount": 14516.08,
        "type": "credit",
        "category": "Interest Income"
    },
    {
        "id": 1369,
        "date": "2026-05-26",
        "description": "Sales to Rajan Fabrics",
        "amount": 348669.0,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1370,
        "date": "2026-05-26",
        "description": "GST collected on sales",
        "amount": 62760.42,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1371,
        "date": "2026-05-27",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 237888.19,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1372,
        "date": "2026-05-27",
        "description": "GST input on inventory",
        "amount": 42819.87,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1373,
        "date": "2026-05-29",
        "description": "Sales to Rajan Fabrics",
        "amount": 271888.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1374,
        "date": "2026-05-29",
        "description": "GST collected on sales",
        "amount": 48939.91,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1375,
        "date": "2026-06-01",
        "description": "Office rent paid",
        "amount": 48039.18,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1376,
        "date": "2026-06-01",
        "description": "Salary paid to employees",
        "amount": 75500.28,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1377,
        "date": "2026-06-01",
        "description": "Forex loss on import payables",
        "amount": 5478.73,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1378,
        "date": "2026-06-02",
        "description": "Sales to Mehta Garments",
        "amount": 174179.09,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1379,
        "date": "2026-06-02",
        "description": "GST collected on sales",
        "amount": 31352.24,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1380,
        "date": "2026-06-02",
        "description": "Printing and stationery",
        "amount": 5546.08,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1381,
        "date": "2026-06-03",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 190881.26,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1382,
        "date": "2026-06-03",
        "description": "GST input on inventory",
        "amount": 34358.63,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1383,
        "date": "2026-06-03",
        "description": "GST reversal on sales return",
        "amount": 5067.37,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1384,
        "date": "2026-06-04",
        "description": "Courier and postage charges",
        "amount": 3698.64,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1385,
        "date": "2026-06-04",
        "description": "Miscellaneous office expenses",
        "amount": 1361.64,
        "type": "debit",
        "category": "Miscellaneous Expense"
    },
    {
        "id": 1386,
        "date": "2026-06-05",
        "description": "Electricity bill payment",
        "amount": 14400.69,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1387,
        "date": "2026-06-05",
        "description": "Water and utility charges",
        "amount": 5338.33,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1388,
        "date": "2026-06-05",
        "description": "Sales to Bombay Fashion House",
        "amount": 188114.19,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1389,
        "date": "2026-06-05",
        "description": "GST collected on sales",
        "amount": 33860.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1390,
        "date": "2026-06-05",
        "description": "Vehicle maintenance and repair",
        "amount": 13005.02,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1391,
        "date": "2026-06-06",
        "description": "Customs duty on imports",
        "amount": 26228.76,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1392,
        "date": "2026-06-08",
        "description": "Sales return from customer",
        "amount": 11119.24,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1393,
        "date": "2026-06-08",
        "description": "Statutory audit fees",
        "amount": 53737.51,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1394,
        "date": "2026-06-09",
        "description": "Sales to Lucky Hosiery",
        "amount": 271357.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1395,
        "date": "2026-06-09",
        "description": "GST collected on sales",
        "amount": 48844.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1396,
        "date": "2026-06-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1397,
        "date": "2026-06-10",
        "description": "Interest paid on bank loan",
        "amount": 13042.91,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1398,
        "date": "2026-06-10",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 195463.39,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1399,
        "date": "2026-06-10",
        "description": "GST input on inventory",
        "amount": 35183.41,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1400,
        "date": "2026-06-10",
        "description": "Customs duty on imports",
        "amount": 26848.5,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1401,
        "date": "2026-06-12",
        "description": "Sales to Bombay Fashion House",
        "amount": 246984.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1402,
        "date": "2026-06-12",
        "description": "GST collected on sales",
        "amount": 44457.13,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1403,
        "date": "2026-06-14",
        "description": "Vendor payment against outstanding",
        "amount": 114070.31,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1404,
        "date": "2026-06-15",
        "description": "GST payment to government",
        "amount": 74246.24,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1405,
        "date": "2026-06-15",
        "description": "TDS payment to government",
        "amount": 13347.58,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1406,
        "date": "2026-06-15",
        "description": "Sales return from customer",
        "amount": 11946.31,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1407,
        "date": "2026-06-16",
        "description": "Sales to Mehta Garments",
        "amount": 244317.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1408,
        "date": "2026-06-16",
        "description": "GST collected on sales",
        "amount": 43977.13,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1409,
        "date": "2026-06-16",
        "description": "Vendor payment against outstanding",
        "amount": 103538.74,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1410,
        "date": "2026-06-17",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 224139.26,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1411,
        "date": "2026-06-17",
        "description": "GST input on inventory",
        "amount": 40345.07,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1412,
        "date": "2026-06-17",
        "description": "Printing and stationery",
        "amount": 6992.19,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1413,
        "date": "2026-06-19",
        "description": "Sales to Mehta Garments",
        "amount": 341825.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1414,
        "date": "2026-06-19",
        "description": "GST collected on sales",
        "amount": 61528.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1415,
        "date": "2026-06-19",
        "description": "Customs duty on imports",
        "amount": 27491.07,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1416,
        "date": "2026-06-21",
        "description": "Purchase return to vendor",
        "amount": 17285.72,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1417,
        "date": "2026-06-22",
        "description": "Digital marketing campaign",
        "amount": 29233.44,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1418,
        "date": "2026-06-23",
        "description": "Sales to Bombay Fashion House",
        "amount": 184587.32,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1419,
        "date": "2026-06-23",
        "description": "GST collected on sales",
        "amount": 33225.72,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1420,
        "date": "2026-06-24",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 271555.38,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1421,
        "date": "2026-06-24",
        "description": "GST input on inventory",
        "amount": 48879.97,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1422,
        "date": "2026-06-26",
        "description": "Sales to Rajan Fabrics",
        "amount": 203215.65,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1423,
        "date": "2026-06-26",
        "description": "GST collected on sales",
        "amount": 36578.82,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1424,
        "date": "2026-06-26",
        "description": "GST reversal on sales return",
        "amount": 3926.63,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1425,
        "date": "2026-06-26",
        "description": "Scrap sale proceeds",
        "amount": 9082.19,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1426,
        "date": "2026-06-30",
        "description": "Sales to Bombay Fashion House",
        "amount": 198816.97,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1427,
        "date": "2026-06-30",
        "description": "GST collected on sales",
        "amount": 35787.06,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1428,
        "date": "2026-07-01",
        "description": "Office rent paid",
        "amount": 49549.72,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1429,
        "date": "2026-07-01",
        "description": "Salary paid to employees",
        "amount": 75909.1,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1430,
        "date": "2026-07-01",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 224595.69,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1431,
        "date": "2026-07-01",
        "description": "GST input on inventory",
        "amount": 40427.22,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1432,
        "date": "2026-07-02",
        "description": "Sales return from customer",
        "amount": 27228.33,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1433,
        "date": "2026-07-03",
        "description": "Sales to Bombay Fashion House",
        "amount": 266534.48,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1434,
        "date": "2026-07-03",
        "description": "GST collected on sales",
        "amount": 47976.21,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1435,
        "date": "2026-07-04",
        "description": "Printing and stationery",
        "amount": 3163.74,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1436,
        "date": "2026-07-05",
        "description": "Electricity bill payment",
        "amount": 11321.38,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1437,
        "date": "2026-07-05",
        "description": "Water and utility charges",
        "amount": 5346.02,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1438,
        "date": "2026-07-07",
        "description": "Sales to Rajan Fabrics",
        "amount": 278207.59,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1439,
        "date": "2026-07-07",
        "description": "GST collected on sales",
        "amount": 50077.37,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1440,
        "date": "2026-07-08",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 222313.93,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1441,
        "date": "2026-07-08",
        "description": "GST input on inventory",
        "amount": 40016.51,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1442,
        "date": "2026-07-09",
        "description": "Payment received from customer",
        "amount": 118269.15,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1443,
        "date": "2026-07-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1444,
        "date": "2026-07-10",
        "description": "Interest paid on bank loan",
        "amount": 14463.18,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1445,
        "date": "2026-07-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 274786.2,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1446,
        "date": "2026-07-10",
        "description": "GST collected on sales",
        "amount": 49461.52,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1447,
        "date": "2026-07-10",
        "description": "Customs duty on imports",
        "amount": 23531.29,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1448,
        "date": "2026-07-11",
        "description": "Statutory audit fees",
        "amount": 37325.94,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1449,
        "date": "2026-07-12",
        "description": "Depreciation charged on assets",
        "amount": 26507.99,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1450,
        "date": "2026-07-14",
        "description": "Sales to Rajan Fabrics",
        "amount": 190958.93,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1451,
        "date": "2026-07-14",
        "description": "GST collected on sales",
        "amount": 34372.61,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1452,
        "date": "2026-07-15",
        "description": "GST payment to government",
        "amount": 56278.84,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1453,
        "date": "2026-07-15",
        "description": "TDS payment to government",
        "amount": 13125.99,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1454,
        "date": "2026-07-15",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 243357.34,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1455,
        "date": "2026-07-15",
        "description": "GST input on inventory",
        "amount": 43804.32,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1456,
        "date": "2026-07-16",
        "description": "Depreciation charged on assets",
        "amount": 23860.31,
        "type": "debit",
        "category": "Depreciation Expense"
    },
    {
        "id": 1457,
        "date": "2026-07-17",
        "description": "Sales to Rajan Fabrics",
        "amount": 175270.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1458,
        "date": "2026-07-17",
        "description": "GST collected on sales",
        "amount": 31548.77,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1459,
        "date": "2026-07-18",
        "description": "Employee performance bonus",
        "amount": 49499.02,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 1460,
        "date": "2026-07-19",
        "description": "Vendor payment against outstanding",
        "amount": 104430.2,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1461,
        "date": "2026-07-19",
        "description": "Forex loss on import payables",
        "amount": 4247.32,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1462,
        "date": "2026-07-19",
        "description": "Sale of old machinery",
        "amount": 50800.4,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 1463,
        "date": "2026-07-19",
        "description": "Purchase return to vendor",
        "amount": 18692.75,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1464,
        "date": "2026-07-21",
        "description": "Sales to Rajan Fabrics",
        "amount": 316566.62,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1465,
        "date": "2026-07-21",
        "description": "GST collected on sales",
        "amount": 56981.99,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1466,
        "date": "2026-07-22",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 279203.94,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1467,
        "date": "2026-07-22",
        "description": "GST input on inventory",
        "amount": 50256.71,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1468,
        "date": "2026-07-23",
        "description": "Purchase return to vendor",
        "amount": 15875.74,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1469,
        "date": "2026-07-23",
        "description": "Digital marketing campaign",
        "amount": 19714.0,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1470,
        "date": "2026-07-23",
        "description": "Software license capitalization",
        "amount": 52503.9,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 1471,
        "date": "2026-07-24",
        "description": "Sales to Bombay Fashion House",
        "amount": 296281.33,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1472,
        "date": "2026-07-24",
        "description": "GST collected on sales",
        "amount": 53330.64,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1473,
        "date": "2026-07-24",
        "description": "GST reversal on sales return",
        "amount": 3058.65,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1474,
        "date": "2026-07-25",
        "description": "Purchase of new office equipment",
        "amount": 119499.59,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 1475,
        "date": "2026-07-25",
        "description": "Employee travel reimbursement",
        "amount": 5497.1,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1476,
        "date": "2026-07-28",
        "description": "Sales to Lucky Hosiery",
        "amount": 261579.61,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1477,
        "date": "2026-07-28",
        "description": "GST collected on sales",
        "amount": 47084.33,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1478,
        "date": "2026-07-29",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 270579.45,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1479,
        "date": "2026-07-29",
        "description": "GST input on inventory",
        "amount": 48704.3,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1480,
        "date": "2026-07-31",
        "description": "Sales to Mehta Garments",
        "amount": 153688.31,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1481,
        "date": "2026-07-31",
        "description": "GST collected on sales",
        "amount": 27663.9,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1482,
        "date": "2026-07-31",
        "description": "Forex loss on import payables",
        "amount": 3683.44,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1483,
        "date": "2026-07-31",
        "description": "GST reversal on sales return",
        "amount": 3458.8,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1484,
        "date": "2026-08-01",
        "description": "Office rent paid",
        "amount": 42472.73,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1485,
        "date": "2026-08-01",
        "description": "Salary paid to employees",
        "amount": 88521.49,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1486,
        "date": "2026-08-03",
        "description": "Fuel for delivery vehicles",
        "amount": 15826.33,
        "type": "debit",
        "category": "Fuel Expense"
    },
    {
        "id": 1487,
        "date": "2026-08-04",
        "description": "Sales to Mehta Garments",
        "amount": 161014.98,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1488,
        "date": "2026-08-04",
        "description": "GST collected on sales",
        "amount": 28982.7,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1489,
        "date": "2026-08-04",
        "description": "GST reversal on sales return",
        "amount": 2521.84,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1490,
        "date": "2026-08-05",
        "description": "Electricity bill payment",
        "amount": 15052.24,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1491,
        "date": "2026-08-05",
        "description": "Water and utility charges",
        "amount": 5430.08,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1492,
        "date": "2026-08-05",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 200410.02,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1493,
        "date": "2026-08-05",
        "description": "GST input on inventory",
        "amount": 36073.8,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1494,
        "date": "2026-08-05",
        "description": "Further equity capital introduced",
        "amount": 593446.97,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1495,
        "date": "2026-08-05",
        "description": "Forex loss on import payables",
        "amount": 7209.03,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1496,
        "date": "2026-08-07",
        "description": "Sales to Rajan Fabrics",
        "amount": 293053.8,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1497,
        "date": "2026-08-07",
        "description": "GST collected on sales",
        "amount": 52749.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1498,
        "date": "2026-08-07",
        "description": "Payment received from customer",
        "amount": 149324.26,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1499,
        "date": "2026-08-08",
        "description": "Payment received from customer",
        "amount": 111285.86,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1500,
        "date": "2026-08-09",
        "description": "Purchase return to vendor",
        "amount": 21982.32,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1501,
        "date": "2026-08-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1502,
        "date": "2026-08-10",
        "description": "Interest paid on bank loan",
        "amount": 14765.0,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1503,
        "date": "2026-08-11",
        "description": "Sales to Mehta Garments",
        "amount": 328151.62,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1504,
        "date": "2026-08-11",
        "description": "GST collected on sales",
        "amount": 59067.29,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1505,
        "date": "2026-08-12",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 252523.47,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1506,
        "date": "2026-08-12",
        "description": "GST input on inventory",
        "amount": 45454.22,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1507,
        "date": "2026-08-13",
        "description": "Customs duty on imports",
        "amount": 37112.65,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1508,
        "date": "2026-08-13",
        "description": "Advance corporate tax payment",
        "amount": 80676.52,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1509,
        "date": "2026-08-14",
        "description": "Sales to Lucky Hosiery",
        "amount": 220658.57,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1510,
        "date": "2026-08-14",
        "description": "GST collected on sales",
        "amount": 39718.54,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1511,
        "date": "2026-08-14",
        "description": "Advance received for large order",
        "amount": 68095.32,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1512,
        "date": "2026-08-15",
        "description": "GST payment to government",
        "amount": 46087.47,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1513,
        "date": "2026-08-15",
        "description": "TDS payment to government",
        "amount": 14808.88,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1514,
        "date": "2026-08-18",
        "description": "Sales to Rajan Fabrics",
        "amount": 184969.63,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1515,
        "date": "2026-08-18",
        "description": "GST collected on sales",
        "amount": 33294.53,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1516,
        "date": "2026-08-19",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 240492.13,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1517,
        "date": "2026-08-19",
        "description": "GST input on inventory",
        "amount": 43288.58,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1518,
        "date": "2026-08-19",
        "description": "Annual insurance premium",
        "amount": 29558.99,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 1519,
        "date": "2026-08-19",
        "description": "Sales return from customer",
        "amount": 11453.63,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1520,
        "date": "2026-08-21",
        "description": "Sales to Bombay Fashion House",
        "amount": 227991.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1521,
        "date": "2026-08-21",
        "description": "GST collected on sales",
        "amount": 41038.45,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1522,
        "date": "2026-08-21",
        "description": "Forex gain on export receivables",
        "amount": 3050.3,
        "type": "credit",
        "category": "Forex Gain"
    },
    {
        "id": 1523,
        "date": "2026-08-21",
        "description": "Payment received from customer",
        "amount": 141699.82,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1524,
        "date": "2026-08-25",
        "description": "Sales to Bombay Fashion House",
        "amount": 224932.69,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1525,
        "date": "2026-08-25",
        "description": "GST collected on sales",
        "amount": 40487.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1526,
        "date": "2026-08-25",
        "description": "Scrap sale proceeds",
        "amount": 3054.03,
        "type": "credit",
        "category": "Other Income"
    },
    {
        "id": 1527,
        "date": "2026-08-26",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 220693.9,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1528,
        "date": "2026-08-26",
        "description": "GST input on inventory",
        "amount": 39724.9,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1529,
        "date": "2026-08-28",
        "description": "Sales to Bombay Fashion House",
        "amount": 347233.49,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1530,
        "date": "2026-08-28",
        "description": "GST collected on sales",
        "amount": 62502.03,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1531,
        "date": "2026-08-29",
        "description": "Statutory audit fees",
        "amount": 47727.13,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1532,
        "date": "2026-08-30",
        "description": "Courier and postage charges",
        "amount": 4546.89,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1533,
        "date": "2026-08-31",
        "description": "Vehicle maintenance and repair",
        "amount": 7770.51,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1534,
        "date": "2026-09-01",
        "description": "Office rent paid",
        "amount": 48189.21,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1535,
        "date": "2026-09-01",
        "description": "Salary paid to employees",
        "amount": 84739.32,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1536,
        "date": "2026-09-01",
        "description": "Sales to Rajan Fabrics",
        "amount": 262842.46,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1537,
        "date": "2026-09-01",
        "description": "GST collected on sales",
        "amount": 47311.64,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1538,
        "date": "2026-09-02",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 233438.33,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1539,
        "date": "2026-09-02",
        "description": "GST input on inventory",
        "amount": 42018.9,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1540,
        "date": "2026-09-02",
        "description": "Brokerage and commission paid",
        "amount": 17550.55,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1541,
        "date": "2026-09-02",
        "description": "Payment received from customer",
        "amount": 160243.95,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1542,
        "date": "2026-09-04",
        "description": "Sales to Lucky Hosiery",
        "amount": 266024.02,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1543,
        "date": "2026-09-04",
        "description": "GST collected on sales",
        "amount": 47884.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1544,
        "date": "2026-09-04",
        "description": "Purchase return to vendor",
        "amount": 15527.3,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1545,
        "date": "2026-09-05",
        "description": "Electricity bill payment",
        "amount": 15121.11,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1546,
        "date": "2026-09-05",
        "description": "Water and utility charges",
        "amount": 3430.64,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1547,
        "date": "2026-09-06",
        "description": "Payment received from customer",
        "amount": 172941.39,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1548,
        "date": "2026-09-06",
        "description": "Software license capitalization",
        "amount": 69645.37,
        "type": "debit",
        "category": "Intangible Asset"
    },
    {
        "id": 1549,
        "date": "2026-09-08",
        "description": "Sales to Lucky Hosiery",
        "amount": 321168.59,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1550,
        "date": "2026-09-08",
        "description": "GST collected on sales",
        "amount": 57810.35,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1551,
        "date": "2026-09-09",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 197692.47,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1552,
        "date": "2026-09-09",
        "description": "GST input on inventory",
        "amount": 35584.64,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1553,
        "date": "2026-09-09",
        "description": "Customs duty on imports",
        "amount": 21121.65,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1554,
        "date": "2026-09-09",
        "description": "GST reversal on sales return",
        "amount": 4646.46,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1555,
        "date": "2026-09-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1556,
        "date": "2026-09-10",
        "description": "Interest paid on bank loan",
        "amount": 15002.28,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1557,
        "date": "2026-09-11",
        "description": "Sales to Bombay Fashion House",
        "amount": 315528.47,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1558,
        "date": "2026-09-11",
        "description": "GST collected on sales",
        "amount": 56795.12,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1559,
        "date": "2026-09-11",
        "description": "Advance received for large order",
        "amount": 85442.89,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1560,
        "date": "2026-09-15",
        "description": "GST payment to government",
        "amount": 55454.4,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1561,
        "date": "2026-09-15",
        "description": "TDS payment to government",
        "amount": 13033.41,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1562,
        "date": "2026-09-15",
        "description": "Sales to Mehta Garments",
        "amount": 341044.65,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1563,
        "date": "2026-09-15",
        "description": "GST collected on sales",
        "amount": 61388.04,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1564,
        "date": "2026-09-15",
        "description": "Mutual fund investment",
        "amount": 227147.64,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 1565,
        "date": "2026-09-16",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 230091.56,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1566,
        "date": "2026-09-16",
        "description": "GST input on inventory",
        "amount": 41416.48,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1567,
        "date": "2026-09-16",
        "description": "Employee travel reimbursement",
        "amount": 8990.12,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1568,
        "date": "2026-09-18",
        "description": "Sales to Rajan Fabrics",
        "amount": 282327.13,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1569,
        "date": "2026-09-18",
        "description": "GST collected on sales",
        "amount": 50818.88,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1570,
        "date": "2026-09-22",
        "description": "Sales to Rajan Fabrics",
        "amount": 303209.35,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1571,
        "date": "2026-09-22",
        "description": "GST collected on sales",
        "amount": 54577.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1572,
        "date": "2026-09-23",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 196968.5,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1573,
        "date": "2026-09-23",
        "description": "GST input on inventory",
        "amount": 35454.33,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1574,
        "date": "2026-09-25",
        "description": "Sales to Rajan Fabrics",
        "amount": 250277.61,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1575,
        "date": "2026-09-25",
        "description": "GST collected on sales",
        "amount": 45049.97,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1576,
        "date": "2026-09-27",
        "description": "Printing and stationery",
        "amount": 7755.82,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1577,
        "date": "2026-09-27",
        "description": "Interim dividend payout",
        "amount": 116012.69,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1578,
        "date": "2026-09-29",
        "description": "Sales to Mehta Garments",
        "amount": 224081.01,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1579,
        "date": "2026-09-29",
        "description": "GST collected on sales",
        "amount": 40334.58,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1580,
        "date": "2026-09-29",
        "description": "Sale of old machinery",
        "amount": 87451.58,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 1581,
        "date": "2026-09-29",
        "description": "Legal and consultancy fees",
        "amount": 15477.32,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 1582,
        "date": "2026-09-30",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 202491.43,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1583,
        "date": "2026-09-30",
        "description": "GST input on inventory",
        "amount": 36448.46,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1584,
        "date": "2026-10-01",
        "description": "Office rent paid",
        "amount": 47236.28,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1585,
        "date": "2026-10-01",
        "description": "Salary paid to employees",
        "amount": 86738.01,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1586,
        "date": "2026-10-02",
        "description": "Sales to Bombay Fashion House",
        "amount": 222025.97,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1587,
        "date": "2026-10-02",
        "description": "GST collected on sales",
        "amount": 39964.67,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1588,
        "date": "2026-10-05",
        "description": "Electricity bill payment",
        "amount": 14380.24,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1589,
        "date": "2026-10-05",
        "description": "Water and utility charges",
        "amount": 4933.67,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1590,
        "date": "2026-10-05",
        "description": "Further equity capital introduced",
        "amount": 591131.34,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1591,
        "date": "2026-10-06",
        "description": "Sales to Bombay Fashion House",
        "amount": 162054.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1592,
        "date": "2026-10-06",
        "description": "GST collected on sales",
        "amount": 29169.89,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1593,
        "date": "2026-10-07",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 202681.13,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1594,
        "date": "2026-10-07",
        "description": "GST input on inventory",
        "amount": 36482.6,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1595,
        "date": "2026-10-09",
        "description": "Sales to Bombay Fashion House",
        "amount": 259345.85,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1596,
        "date": "2026-10-09",
        "description": "GST collected on sales",
        "amount": 46682.25,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1597,
        "date": "2026-10-09",
        "description": "Employee performance bonus",
        "amount": 41010.65,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 1598,
        "date": "2026-10-09",
        "description": "GST reversal on sales return",
        "amount": 4884.91,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1599,
        "date": "2026-10-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1600,
        "date": "2026-10-10",
        "description": "Interest paid on bank loan",
        "amount": 14244.62,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1601,
        "date": "2026-10-11",
        "description": "Printing and stationery",
        "amount": 4838.3,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1602,
        "date": "2026-10-13",
        "description": "Sales to Lucky Hosiery",
        "amount": 195697.6,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1603,
        "date": "2026-10-13",
        "description": "GST collected on sales",
        "amount": 35225.57,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1604,
        "date": "2026-10-14",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 190929.87,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1605,
        "date": "2026-10-14",
        "description": "GST input on inventory",
        "amount": 34367.38,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1606,
        "date": "2026-10-15",
        "description": "GST payment to government",
        "amount": 58112.33,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1607,
        "date": "2026-10-15",
        "description": "TDS payment to government",
        "amount": 14942.89,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1608,
        "date": "2026-10-16",
        "description": "Sales to Rajan Fabrics",
        "amount": 310227.84,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1609,
        "date": "2026-10-16",
        "description": "GST collected on sales",
        "amount": 55841.01,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1610,
        "date": "2026-10-20",
        "description": "Sales to Bombay Fashion House",
        "amount": 270310.87,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1611,
        "date": "2026-10-20",
        "description": "GST collected on sales",
        "amount": 48655.96,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1612,
        "date": "2026-10-21",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 185444.07,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1613,
        "date": "2026-10-21",
        "description": "GST input on inventory",
        "amount": 33379.93,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1614,
        "date": "2026-10-22",
        "description": "Sales return from customer",
        "amount": 12847.71,
        "type": "debit",
        "category": "Sales Return"
    },
    {
        "id": 1615,
        "date": "2026-10-23",
        "description": "Sales to Mehta Garments",
        "amount": 287750.95,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1616,
        "date": "2026-10-23",
        "description": "GST collected on sales",
        "amount": 51795.17,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1617,
        "date": "2026-10-24",
        "description": "Legal and consultancy fees",
        "amount": 20968.25,
        "type": "debit",
        "category": "Professional Fees"
    },
    {
        "id": 1618,
        "date": "2026-10-24",
        "description": "Interim dividend payout",
        "amount": 158428.96,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1619,
        "date": "2026-10-26",
        "description": "Advance corporate tax payment",
        "amount": 78139.49,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1620,
        "date": "2026-10-27",
        "description": "Sales to Lucky Hosiery",
        "amount": 342738.85,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1621,
        "date": "2026-10-27",
        "description": "GST collected on sales",
        "amount": 61692.99,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1622,
        "date": "2026-10-28",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 211038.66,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1623,
        "date": "2026-10-28",
        "description": "GST input on inventory",
        "amount": 37986.96,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1624,
        "date": "2026-10-28",
        "description": "Employee travel reimbursement",
        "amount": 11773.04,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1625,
        "date": "2026-10-30",
        "description": "Sales to Lucky Hosiery",
        "amount": 341668.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1626,
        "date": "2026-10-30",
        "description": "GST collected on sales",
        "amount": 61500.32,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1627,
        "date": "2026-11-01",
        "description": "Office rent paid",
        "amount": 49087.75,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1628,
        "date": "2026-11-01",
        "description": "Salary paid to employees",
        "amount": 83009.7,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1629,
        "date": "2026-11-01",
        "description": "Purchase return to vendor",
        "amount": 18799.26,
        "type": "credit",
        "category": "Purchase Return"
    },
    {
        "id": 1630,
        "date": "2026-11-03",
        "description": "Sales to Mehta Garments",
        "amount": 170009.01,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1631,
        "date": "2026-11-03",
        "description": "GST collected on sales",
        "amount": 30601.62,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1632,
        "date": "2026-11-04",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 190617.67,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1633,
        "date": "2026-11-04",
        "description": "GST input on inventory",
        "amount": 34311.18,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1634,
        "date": "2026-11-05",
        "description": "Electricity bill payment",
        "amount": 15290.36,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1635,
        "date": "2026-11-05",
        "description": "Water and utility charges",
        "amount": 5288.42,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1636,
        "date": "2026-11-06",
        "description": "Sales to Lucky Hosiery",
        "amount": 211218.84,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1637,
        "date": "2026-11-06",
        "description": "GST collected on sales",
        "amount": 38019.39,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1638,
        "date": "2026-11-06",
        "description": "Customs duty on imports",
        "amount": 31288.73,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1639,
        "date": "2026-11-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1640,
        "date": "2026-11-10",
        "description": "Interest paid on bank loan",
        "amount": 14821.79,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1641,
        "date": "2026-11-10",
        "description": "Sales to Rajan Fabrics",
        "amount": 227745.49,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1642,
        "date": "2026-11-10",
        "description": "GST collected on sales",
        "amount": 40994.19,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1643,
        "date": "2026-11-10",
        "description": "Interim dividend payout",
        "amount": 150988.85,
        "type": "debit",
        "category": "Dividends Paid"
    },
    {
        "id": 1644,
        "date": "2026-11-11",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 256963.36,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1645,
        "date": "2026-11-11",
        "description": "GST input on inventory",
        "amount": 46253.4,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1646,
        "date": "2026-11-13",
        "description": "Sales to Lucky Hosiery",
        "amount": 289656.66,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1647,
        "date": "2026-11-13",
        "description": "GST collected on sales",
        "amount": 52138.2,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1648,
        "date": "2026-11-14",
        "description": "Advance corporate tax payment",
        "amount": 63643.88,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1649,
        "date": "2026-11-15",
        "description": "GST payment to government",
        "amount": 49601.09,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1650,
        "date": "2026-11-15",
        "description": "TDS payment to government",
        "amount": 11682.24,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1651,
        "date": "2026-11-16",
        "description": "Vehicle maintenance and repair",
        "amount": 5853.58,
        "type": "debit",
        "category": "Vehicle Expense"
    },
    {
        "id": 1652,
        "date": "2026-11-17",
        "description": "Sales to Bombay Fashion House",
        "amount": 273152.47,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1653,
        "date": "2026-11-17",
        "description": "GST collected on sales",
        "amount": 49167.44,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1654,
        "date": "2026-11-18",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 272614.4,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1655,
        "date": "2026-11-18",
        "description": "GST input on inventory",
        "amount": 49070.59,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1656,
        "date": "2026-11-19",
        "description": "GST reversal on sales return",
        "amount": 5065.31,
        "type": "debit",
        "category": "GST Adjustment"
    },
    {
        "id": 1657,
        "date": "2026-11-19",
        "description": "Purchase of new office equipment",
        "amount": 102063.6,
        "type": "debit",
        "category": "Fixed Asset"
    },
    {
        "id": 1658,
        "date": "2026-11-20",
        "description": "Sales to Rajan Fabrics",
        "amount": 246753.19,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1659,
        "date": "2026-11-20",
        "description": "GST collected on sales",
        "amount": 44415.57,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1660,
        "date": "2026-11-20",
        "description": "Vendor payment against outstanding",
        "amount": 130923.98,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1661,
        "date": "2026-11-22",
        "description": "Statutory audit fees",
        "amount": 44128.94,
        "type": "debit",
        "category": "Audit Expense"
    },
    {
        "id": 1662,
        "date": "2026-11-23",
        "description": "Printing and stationery",
        "amount": 3527.5,
        "type": "debit",
        "category": "Office Expense"
    },
    {
        "id": 1663,
        "date": "2026-11-24",
        "description": "Sales to Lucky Hosiery",
        "amount": 202516.59,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1664,
        "date": "2026-11-24",
        "description": "GST collected on sales",
        "amount": 36452.99,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1665,
        "date": "2026-11-25",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 255782.12,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1666,
        "date": "2026-11-25",
        "description": "GST input on inventory",
        "amount": 46040.78,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1667,
        "date": "2026-11-27",
        "description": "Sales to Lucky Hosiery",
        "amount": 340908.64,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1668,
        "date": "2026-11-27",
        "description": "GST collected on sales",
        "amount": 61363.55,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1669,
        "date": "2026-11-27",
        "description": "Courier and postage charges",
        "amount": 2156.65,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1670,
        "date": "2026-11-27",
        "description": "Accumulated depreciation recorded",
        "amount": 34945.06,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1671,
        "date": "2026-11-29",
        "description": "Employee performance bonus",
        "amount": 37254.57,
        "type": "debit",
        "category": "Bonus Expense"
    },
    {
        "id": 1672,
        "date": "2026-12-01",
        "description": "Office rent paid",
        "amount": 46122.93,
        "type": "debit",
        "category": "Rent Expense"
    },
    {
        "id": 1673,
        "date": "2026-12-01",
        "description": "Salary paid to employees",
        "amount": 70024.41,
        "type": "debit",
        "category": "Salary Expense"
    },
    {
        "id": 1674,
        "date": "2026-12-01",
        "description": "Sales to Bombay Fashion House",
        "amount": 315909.05,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1675,
        "date": "2026-12-01",
        "description": "GST collected on sales",
        "amount": 56863.63,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1676,
        "date": "2026-12-01",
        "description": "Advance corporate tax payment",
        "amount": 87061.71,
        "type": "debit",
        "category": "Tax Expense"
    },
    {
        "id": 1677,
        "date": "2026-12-02",
        "description": "Inventory purchase from Surat Silk Suppliers",
        "amount": 197307.77,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1678,
        "date": "2026-12-02",
        "description": "GST input on inventory",
        "amount": 35515.4,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1679,
        "date": "2026-12-02",
        "description": "Accumulated depreciation recorded",
        "amount": 33050.43,
        "type": "credit",
        "category": "Accumulated Depreciation"
    },
    {
        "id": 1680,
        "date": "2026-12-04",
        "description": "Sales to Lucky Hosiery",
        "amount": 187865.88,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1681,
        "date": "2026-12-04",
        "description": "GST collected on sales",
        "amount": 33815.86,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1682,
        "date": "2026-12-05",
        "description": "Electricity bill payment",
        "amount": 13243.51,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1683,
        "date": "2026-12-05",
        "description": "Water and utility charges",
        "amount": 4809.08,
        "type": "debit",
        "category": "Utilities"
    },
    {
        "id": 1684,
        "date": "2026-12-05",
        "description": "Vendor payment against outstanding",
        "amount": 102309.65,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1685,
        "date": "2026-12-05",
        "description": "Annual insurance premium",
        "amount": 28412.48,
        "type": "debit",
        "category": "Insurance Expense"
    },
    {
        "id": 1686,
        "date": "2026-12-08",
        "description": "Sales to Bombay Fashion House",
        "amount": 261823.4,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1687,
        "date": "2026-12-08",
        "description": "GST collected on sales",
        "amount": 47128.21,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1688,
        "date": "2026-12-08",
        "description": "Further equity capital introduced",
        "amount": 767171.88,
        "type": "credit",
        "category": "Share Capital"
    },
    {
        "id": 1689,
        "date": "2026-12-09",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 199191.08,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1690,
        "date": "2026-12-09",
        "description": "GST input on inventory",
        "amount": 35854.39,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1691,
        "date": "2026-12-10",
        "description": "Loan EMI repayment",
        "amount": 42000.0,
        "type": "debit",
        "category": "Loan Repayment"
    },
    {
        "id": 1692,
        "date": "2026-12-10",
        "description": "Interest paid on bank loan",
        "amount": 12043.45,
        "type": "debit",
        "category": "Interest Expense"
    },
    {
        "id": 1693,
        "date": "2026-12-10",
        "description": "Courier and postage charges",
        "amount": 1150.65,
        "type": "debit",
        "category": "Administrative Expense"
    },
    {
        "id": 1694,
        "date": "2026-12-10",
        "description": "Employee travel reimbursement",
        "amount": 10657.81,
        "type": "debit",
        "category": "Travel Expense"
    },
    {
        "id": 1695,
        "date": "2026-12-11",
        "description": "Sales to Mehta Garments",
        "amount": 292340.14,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1696,
        "date": "2026-12-11",
        "description": "GST collected on sales",
        "amount": 52621.23,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1697,
        "date": "2026-12-11",
        "description": "Mutual fund investment",
        "amount": 83379.12,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 1698,
        "date": "2026-12-11",
        "description": "Brokerage and commission paid",
        "amount": 11651.31,
        "type": "debit",
        "category": "Commission Expense"
    },
    {
        "id": 1699,
        "date": "2026-12-11",
        "description": "Digital marketing campaign",
        "amount": 20634.48,
        "type": "debit",
        "category": "Marketing Expense"
    },
    {
        "id": 1700,
        "date": "2026-12-12",
        "description": "Advance received for large order",
        "amount": 70452.08,
        "type": "credit",
        "category": "Customer Advance"
    },
    {
        "id": 1701,
        "date": "2026-12-12",
        "description": "Forex loss on import payables",
        "amount": 5839.58,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1702,
        "date": "2026-12-15",
        "description": "GST payment to government",
        "amount": 58778.15,
        "type": "debit",
        "category": "GST Payment"
    },
    {
        "id": 1703,
        "date": "2026-12-15",
        "description": "TDS payment to government",
        "amount": 10925.92,
        "type": "debit",
        "category": "TDS Payment"
    },
    {
        "id": 1704,
        "date": "2026-12-15",
        "description": "Sales to Bombay Fashion House",
        "amount": 206464.39,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1705,
        "date": "2026-12-15",
        "description": "GST collected on sales",
        "amount": 37163.59,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1706,
        "date": "2026-12-16",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 196189.88,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1707,
        "date": "2026-12-16",
        "description": "GST input on inventory",
        "amount": 35314.18,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1708,
        "date": "2026-12-16",
        "description": "Customs duty on imports",
        "amount": 34414.45,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1709,
        "date": "2026-12-17",
        "description": "Vendor payment against outstanding",
        "amount": 127648.74,
        "type": "debit",
        "category": "Vendor Payment"
    },
    {
        "id": 1710,
        "date": "2026-12-18",
        "description": "Sales to Bombay Fashion House",
        "amount": 227649.81,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1711,
        "date": "2026-12-18",
        "description": "GST collected on sales",
        "amount": 40976.96,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1712,
        "date": "2026-12-22",
        "description": "Sales to Mehta Garments",
        "amount": 273331.45,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1713,
        "date": "2026-12-22",
        "description": "GST collected on sales",
        "amount": 49199.66,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1714,
        "date": "2026-12-23",
        "description": "Inventory purchase from Gujarat Cotton Mills",
        "amount": 196132.55,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1715,
        "date": "2026-12-23",
        "description": "GST input on inventory",
        "amount": 35303.86,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1716,
        "date": "2026-12-23",
        "description": "Mutual fund investment",
        "amount": 129144.89,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 1717,
        "date": "2026-12-24",
        "description": "Sale of old machinery",
        "amount": 66725.16,
        "type": "credit",
        "category": "Asset Disposal"
    },
    {
        "id": 1718,
        "date": "2026-12-25",
        "description": "Sales to Bombay Fashion House",
        "amount": 344287.14,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1719,
        "date": "2026-12-25",
        "description": "GST collected on sales",
        "amount": 61971.68,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1720,
        "date": "2026-12-26",
        "description": "Payment received from customer",
        "amount": 136365.56,
        "type": "credit",
        "category": "Customer Payment"
    },
    {
        "id": 1721,
        "date": "2026-12-28",
        "description": "Customs duty on imports",
        "amount": 25565.74,
        "type": "debit",
        "category": "Customs Duty"
    },
    {
        "id": 1722,
        "date": "2026-12-29",
        "description": "Sales to Rajan Fabrics",
        "amount": 349900.36,
        "type": "credit",
        "category": "Sales Revenue"
    },
    {
        "id": 1723,
        "date": "2026-12-29",
        "description": "GST collected on sales",
        "amount": 62982.06,
        "type": "credit",
        "category": "GST Payable"
    },
    {
        "id": 1724,
        "date": "2026-12-30",
        "description": "Inventory purchase from Vardhman Threads",
        "amount": 190276.79,
        "type": "debit",
        "category": "Inventory Purchase"
    },
    {
        "id": 1725,
        "date": "2026-12-30",
        "description": "GST input on inventory",
        "amount": 34249.82,
        "type": "debit",
        "category": "GST Input Credit"
    },
    {
        "id": 1726,
        "date": "2026-12-31",
        "description": "Forex loss on import payables",
        "amount": 6268.45,
        "type": "debit",
        "category": "Forex Loss"
    },
    {
        "id": 1727,
        "date": "2026-12-31",
        "description": "Mutual fund investment",
        "amount": 157703.62,
        "type": "debit",
        "category": "Investments"
    },
    {
        "id": 1728,
        "date": "2026-12-31",
        "description": "Payment received from customer",
        "amount": 149967.17,
        "type": "credit",
        "category": "Customer Payment"
    }
]

@router.get("/all")
def get_transactions():
    return TRANSACTIONS

@router.get("/classify")
def classify_transaction(description: str):
    return {"category": "Miscellaneous"}
