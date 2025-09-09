Quick Start Guide
=================

Getting Started
---------------

1. **Access the Application**: Visit the deployed site at your Render URL or run locally

2. **Browse Properties**: Navigate to the lettings section to view available properties

3. **User Registration**: Create a user profile to access additional features

4. **Admin Access**: Use the Django admin interface at `/admin` for content management

Basic Commands
--------------

.. code-block:: bash

   # Run tests
   python manage.py test

   # Run with coverage
   coverage run manage.py test
   coverage report

   # Run linting
   flake8 .

   # Collect static files
   python manage.py collectstatic