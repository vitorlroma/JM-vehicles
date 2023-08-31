import vehicle_queries as vehq
import sql_connection as db


def main():
    connection = db.server_connection()
    db.execute_query(connection, vehq.remove_vehicle(1))
    vehicles = db.view_query(connection, vehq.view_vehicles())
    for vehicle in vehicles:
        print(vehicle)

    db.close_connection(connection)


if __name__ == '__main__':
    main()

