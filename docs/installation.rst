Installation
============

Prerequisites
-------------
- Python 3.11+
- pip
- virtualenv (recommended)

Local Development Setup
----------------------

1. Clone the repository:
   .. code-block:: bash

      git clone https://github.com/Razvan-drb/Python_13_OC
      cd Python_13_OC

2. Create and activate virtual environment:
   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   .. code-block:: bash

      pip install -r requirements.txt

4. Set up environment variables:
   copy .env_dist into a .env and add the values

5. Run migrations:
   .. code-block:: bash

      python manage.py migrate

6. Start development server:
   .. code-block:: bash

      python manage.py runserver