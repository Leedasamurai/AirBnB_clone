# AirBnB Clone

This project is an AirBnB clone developed as part of a larger project. It includes a custom console for managing different classes like BaseModel, State, City, Amenity, Place, and Review. The project uses a custom file storage system for serialization and deserialization of objects.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AirBnB_clone.git
Navigate to the project directory:

bash
Copy code
cd AirBnB_clone
Run the console:

bash
Copy code
./console.py
Usage
The console provides a command-line interface to interact with different classes. You can perform actions like show, create, destroy, update, and all on instances of classes such as BaseModel, State, City, Amenity, Place, and Review.

Example Commands:
Create a new instance:

bash
Copy code
create BaseModel
Show details of an instance:

bash
Copy code
show BaseModel 1234-5678
Destroy an instance:

bash
Copy code
destroy BaseModel 1234-5678
Update an instance attribute:

bash
Copy code
update BaseModel 1234-5678 name "New Name"
List all instances of a class:

bash
Copy code
all BaseModel
Classes
BaseModel
The base class for all other classes. It includes common attributes like id, created_at, and updated_at.

State
Represents a geographical state. Includes a name attribute.

City
Represents a city. Includes state_id (linked to State.id) and a name attribute.

Amenity
Represents an amenity. Includes a name attribute.

Place
Represents a place. Includes attributes like city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, and amenity_ids.

Review
Represents a review for a place. Includes attributes like place_id, user_id, and text.

Contributing

Lesego Phuku
