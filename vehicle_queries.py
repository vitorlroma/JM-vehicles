def create_table():
    return """
        CREATE TABLE vehicles(
            veh_id INT PRIMARY KEY auto_increment,
            veh_type varchar(10) not null,
            veh_color varchar(20),
            veh_brand varchar(25) not null,
            veh_model varchar(30) not null,
            veh_year int,
            veh_state varchar(15),
            veh_km float,
            veh_been_auction varchar(5),
            veh_pay_method varchar(15)
        );
        """


def insert_vehicle(veh_type, color, brand, model, year, state, km, auction, pay):
    return f"""
        INSERT INTO vehicles (veh_type, veh_color, veh_brand, veh_model,
        veh_year, veh_state, veh_km, veh_been_auction, veh_pay_method) 
        VALUE ("{veh_type}", "{color}", "{brand}", "{model}", {year}, "{state}", {km}, "{auction}", "{pay}");
        """


def view_vehicles():
    return """
        SELECT * FROM vehicles;
        """


def remove_vehicle(veh_id):
    return f"""
        DELETE FROM vehicles
        WHERE veh_id = {veh_id};
        """
