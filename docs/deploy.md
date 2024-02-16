# Deploy

[Cloud Deploy](https://cloud.google.com/deploy) makes continuous delivery of models easy by allowing users to define releases and progress them through environments such as test, stage, and production. It provides easy promotion, approval and rollback of releases. 

We can use Cloud Deploy to deploy the model to a target endpoint. The `build_and_register.sh` builds the Vertex AI model deployer image and registers a Cloud Deploy custom target type that references the image. The script executes these steps:
* Define a custom action in the  file, which is similar to deploy hooks.
* Define a custom target type, which is a Cloud Deploy resource identifying the custom action used by targets of this type.
* Set up a target definition for a custom target, which is similar to any target type but includes additional properties.
* Set up a Cloud Deploy delivery pipeline that references the configured target.

