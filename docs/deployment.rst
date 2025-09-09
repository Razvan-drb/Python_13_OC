Deployment Procedures
=====================

CI/CD Pipeline
--------------

The application uses GitHub Actions for automated deployment:

1. Code push to main branch triggers workflow
2. Tests and linting run automatically
3. Docker image is built and pushed to Docker Hub
4. Render is notified via webhook to deploy new image

Manual Deployment
-----------------
(username is a secret, ask your collegues for that information)

1. Build Docker image locally:
   .. code-block:: bash

      docker build -t yourusername/oc-lettings-app:latest .

2. Push to Docker Hub:
   .. code-block:: bash

      docker push yourusername/oc-lettings-app:latest

3. Trigger Render deployment:
   .. code-block:: bash

      curl -X POST https://api.render.com/deploy/your-deploy-hook

Environment Setup
-----------------

Required Environment Variables:

- ``SECRET_KEY``: Django secret key for encryption
- ``DEBUG``: Set to 0 in production
- ``SENTRY_DSN``: Sentry error tracking DSN (optional)
- ``ALLOWED_HOSTS``: Comma-separated list of allowed domains

Monitoring and Maintenance
--------------------------

- **Sentry**: Error tracking and performance monitoring
- **Render Dashboard**: Deployment status and logs
- **Django Admin**: Content management and user administration