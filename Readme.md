# Business Information Management System

This is a simple web application for managing business information. It allows you to create, update, delete, and search for businesses.

## Features

- Create a new business with details like name, address, owner information, employee size, investor type, contact email, phone number, investment stage, and company type.
- Update the details of an existing business.
- Delete a business.
- Search for businesses by name.

## Technologies Used

- Python
- Django
- Graphene (for GraphQL)
- Pytest (for testing)

## How to run using Docker

To run the project using Docker, follow these steps:

- Open a terminal or command prompt and navigate to the directory where the Dockerfile and docker-compose.yml files are located.
- Run the command docker-compose up to build the Docker image and start the containers.
- Docker will build the image based on the Dockerfile and start the container for your Django project.
- Once the containers are up and running, you can access your Django application by opening a web browser and navigating to `http://localhost:8000`.
- Make sure you have Docker installed and running on your machine before running the Docker commands.-

## How to run using locally

* Create and activate a virtual environment using `virtualenv venv` and `source venv/bin/activate`.
* Install the project dependencies using `pip install -r requirements.txt`.
* Apply database migrations using `python manage.py makemigrations` and `python manage.py migrate`.
* Start the development server using `python manage.py runserver`.
* \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
* Access the application by opening a web browser and navigating to `http://localhost:8000`

## Usage

You can interact with the application through the GraphQL API. The endpoint for the API is `/graphql`.

Here are some example queries and mutations:

- To fetch all businesses:

  ```graphql
  query {
    allBusinesses {
      id
      name
      address
      ownerInfo
      employeeSize
      investorType
      contactMail
      phoneNumber
      investmentStage
      companyType
    }
  }
  ```
- To search for businesses:

  ```graphql
  query {
    searchBusinesses(search: "Test") {
      id
      name
      address
      ownerInfo
      employeeSize
      investorType
      contactMail
      phoneNumber
      investmentStage
      companyType
    }
  }
  ```
- To create a business:

  ```graphql
  mutation {
    createBusiness(name: "Test", address: "Test Address", ownerInfo: "Test Owner", employeeSize: 10, investorType: "Investor", contactMail: "test@test.com", phoneNumber: 1234567890, investmentStage: "Seed", companyType: "Private") {
      business {
        id
        name
        address
        ownerInfo
        employeeSize
        investorType
        contactMail
        phoneNumber
        investmentStage
        companyType
      }
    }
  }
  ```
- To update a business:

  ```graphql
  mutation {
    updateBusiness(id: 1, name: "Updated") {
      business {
        id
        name
        address
        ownerInfo
        employeeSize
        investorType
        contactMail
        phoneNumber
        investmentStage
        companyType
      }
    }
  }
  ```
- To delete a business:

  ```graphql
  mutation {
    deleteBusiness(id: 1) {
      business {
        id
      }
    }
  }
  ```

## Testing

To run the tests, use the following command:

```bash
pytest
```

## Coverage report

To generate the coverage report, use the following command:

```bash
DJANGO_SETTINGS_MODULE=B_project.settings pytest --cov=B_app
```
