API Interfaces
==============

REST API Endpoints
------------------

Lettings API
~~~~~~~~~~~~

- **GET /api/lettings/**: List all lettings
- **GET /api/lettings/{id}/**: Get specific letting
- **POST /api/lettings/**: Create new letting (admin only)
- **PUT /api/lettings/{id}/**: Update letting (admin only)
- **DELETE /api/lettings/{id}/**: Delete letting (admin only)

Profiles API
~~~~~~~~~~~~

- **GET /api/profiles/**: List all profiles
- **GET /api/profiles/{id}/**: Get specific profile
- **POST /api/profiles/**: Create new profile
- **PUT /api/profiles/{id}/**: Update profile
- **DELETE /api/profiles/{id}/**: Delete profile

API Authentication
------------------

Currently, the API uses session-based authentication. Admin endpoints require staff privileges.

Example API Request
-------------------

.. code-block:: bash

   curl -X GET https://oc-lettings-app-6lbz..onrender.com/api/lettings/
   curl -X GET https://oc-lettings-app-6lbz..onrender.com/api/lettings/1/