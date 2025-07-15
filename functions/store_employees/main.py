import zcatalyst_sdk as zsdk

def handler(request, context):
    """
    Store parsed employee data in Catalyst Data Store.
    """
    app = zsdk.initialize()
    datastore = app.datastore()
    employee_table = datastore.table("Employees")  # Table created in Catalyst Console

    employees = request.get_json()  # Assuming employees come as JSON input
    for employee in employees:
        try:
            employee_table.insert_row({
                'FirstName': employee['first_name'],
                'LastName': employee['last_name']
            })
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    return {"status": "success", "message": "Employees stored successfully"}
