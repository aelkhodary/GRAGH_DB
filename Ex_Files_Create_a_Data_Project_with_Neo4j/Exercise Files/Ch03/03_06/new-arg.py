
def create_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_properties = {"name": "John", "age": 30}
create_person(**person_properties)
