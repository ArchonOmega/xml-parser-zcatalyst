import zcatalyst_sdk

def handler(request, context):
    """
    Verify if an employee's name exists in the Data Store.
    """
    app = zcatalyst_sdk.initialize()
    datastore = app.datastore()
    employee_table = datastore.table("Employees")

    # Fetch input data
    input_employee = request.get_json()
    first_name = input_employee['first_name']
    last_name = input_employee['last_name']

    stored_employees = employee_table.get_all_rows()
    for employee in stored_employees:
        if (employee['FirstName'].lower() == first_name.lower() and
            employee['LastName'].lower() == last_name.lower()):
            return {"status": "success", "verified": True}
    
    return {"status": "success", "verified": False}
