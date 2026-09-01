import random
from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2026, 12, 31)

def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days + 1)
    return start + timedelta(days=random_days)

# We will generate recurring transactions, random business events, and one-offs.
transactions = []
transaction_id = 1

def add_trx(date, desc, amt, t_type, cat):
    global transaction_id
    transactions.append({
        'id': transaction_id,
        'date': date.strftime('%Y-%m-%d'),
        'description': desc,
        'amount': round(amt, 2),
        'type': t_type,
        'category': cat
    })
    transaction_id += 1

# 1. Monthly Recurring (Rent, Salary, Utilities, Loan EMI)
current_date = start_date
while current_date <= end_date:
    # 1st of month
    add_trx(current_date, 'Office rent paid', random.uniform(40000, 50000), 'debit', 'Rent Expense')
    add_trx(current_date, 'Salary paid to employees', random.uniform(70000, 90000), 'debit', 'Salary Expense')
    # 5th of month
    dt5 = current_date + timedelta(days=4)
    add_trx(dt5, 'Electricity bill payment', random.uniform(10000, 16000), 'debit', 'Utilities')
    add_trx(dt5, 'Water and utility charges', random.uniform(3000, 6000), 'debit', 'Utilities')
    # 10th of month
    dt10 = current_date + timedelta(days=9)
    add_trx(dt10, 'Loan EMI repayment', 42000.0, 'debit', 'Loan Repayment')
    add_trx(dt10, 'Interest paid on bank loan', random.uniform(12000, 16000), 'debit', 'Interest Expense')
    # 15th of month
    dt15 = current_date + timedelta(days=14)
    add_trx(dt15, 'GST payment to government', random.uniform(45000, 75000), 'debit', 'GST Payment')
    add_trx(dt15, 'TDS payment to government', random.uniform(8000, 15000), 'debit', 'TDS Payment')
    
    current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)

# 2. Daily/Weekly Sales & Purchases loop
current_date = start_date
while current_date <= end_date:
    # 2 Sales per week
    if current_date.weekday() in [1, 4]:
        amt = random.uniform(150000, 350000)
        add_trx(current_date, f'Sales to {random.choice(["Rajan Fabrics", "Mehta Garments", "Lucky Hosiery", "Bombay Fashion House"])}', amt, 'credit', 'Sales Revenue')
        add_trx(current_date, 'GST collected on sales', amt * 0.18, 'credit', 'GST Payable')
    
    # 1 Purchase per week
    if current_date.weekday() == 2:
        amt = random.uniform(180000, 280000)
        add_trx(current_date, f'Inventory purchase from {random.choice(["Vardhman Threads", "Gujarat Cotton Mills", "Surat Silk Suppliers"])}', amt, 'debit', 'Inventory Purchase')
        add_trx(current_date, 'GST input on inventory', amt * 0.18, 'debit', 'GST Input Credit')
        
    current_date += timedelta(days=1)

# 3. Random specialized events spanning all categories
categories_and_desc = [
    ('Fixed Asset', 'Purchase of new office equipment', 50000, 150000, 'debit'),
    ('Administrative Expense', 'Courier and postage charges', 1000, 5000, 'debit'),
    ('Vendor Payment', 'Vendor payment against outstanding', 80000, 150000, 'debit'),
    ('Bank Charges', 'Monthly bank processing fees', 500, 2500, 'debit'),
    ('Insurance Expense', 'Annual insurance premium', 20000, 35000, 'debit'),
    ('Office Expense', 'Printing and stationery', 2000, 8000, 'debit'),
    ('Customer Payment', 'Payment received from customer', 100000, 200000, 'credit'),
    ('Travel Expense', 'Employee travel reimbursement', 4000, 12000, 'debit'),
    ('Sales Return', 'Sales return from customer', 10000, 30000, 'debit'),
    ('GST Adjustment', 'GST reversal on sales return', 1800, 5400, 'debit'),
    ('Purchase Return', 'Purchase return to vendor', 15000, 25000, 'credit'),
    ('Customer Advance', 'Advance received for large order', 50000, 100000, 'credit'),
    ('Vehicle Expense', 'Vehicle maintenance and repair', 5000, 15000, 'debit'),
    ('Fuel Expense', 'Fuel for delivery vehicles', 10000, 20000, 'debit'),
    ('Other Income', 'Scrap sale proceeds', 3000, 10000, 'credit'),
    ('Investments', 'Mutual fund investment', 50000, 250000, 'debit'),
    ('Bonus Expense', 'Employee performance bonus', 20000, 50000, 'debit'),
    ('Miscellaneous Expense', 'Miscellaneous office expenses', 1000, 4000, 'debit'),
    ('Depreciation Expense', 'Depreciation charged on assets', 15000, 35000, 'debit'),
    ('Accumulated Depreciation', 'Accumulated depreciation recorded', 15000, 35000, 'credit'),
    ('Professional Fees', 'Legal and consultancy fees', 15000, 40000, 'debit'),
    ('Tax Expense', 'Advance corporate tax payment', 50000, 100000, 'debit'),
    ('Interest Income', 'Interest earned on FD', 5000, 15000, 'credit'),
    ('Marketing Expense', 'Digital marketing campaign', 15000, 30000, 'debit'),
    ('Share Capital', 'Further equity capital introduced', 500000, 1000000, 'credit'),
    ('Dividends Paid', 'Interim dividend payout', 100000, 200000, 'debit'),
    ('Forex Gain', 'Forex gain on export receivables', 2000, 10000, 'credit'),
    ('Forex Loss', 'Forex loss on import payables', 2000, 10000, 'debit'),
    ('Customs Duty', 'Customs duty on imports', 20000, 45000, 'debit'),
    ('Intangible Asset', 'Software license capitalization', 40000, 80000, 'debit'),
    ('Audit Expense', 'Statutory audit fees', 30000, 60000, 'debit'),
    ('Asset Disposal', 'Sale of old machinery', 40000, 90000, 'credit'),
    ('Commission Expense', 'Brokerage and commission paid', 8000, 18000, 'debit')
]

for _ in range(500):
    cat, desc, min_amt, max_amt, t_type = random.choice(categories_and_desc)
    amt = random.uniform(min_amt, max_amt)
    dt = random_date(start_date, end_date)
    add_trx(dt, desc, amt, t_type, cat)

# Sort transactions by date
transactions.sort(key=lambda x: x['date'])

# Re-assign sequential IDs
for i, t in enumerate(transactions):
    t['id'] = i + 1

import json

# Generate the new transactions.py file
new_file_content = f'''"""
LedgerAI - routes/transactions.py
3 Years of dynamically generated corporate transactions.
"""

from fastapi import APIRouter

router = APIRouter()

TRANSACTIONS = {json.dumps(transactions, indent=4)}

@router.get("/all")
def get_transactions():
    return TRANSACTIONS

@router.get("/classify")
def classify_transaction(description: str):
    return {{"category": "Miscellaneous"}}
'''

with open('routes/transactions.py', 'w', encoding='utf-8') as f:
    f.write(new_file_content)
    
print(f"Successfully generated {len(transactions)} transactions spanning from 2024 to 2026.")
