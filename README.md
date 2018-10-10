### GIS API

## Briefing

Create an API and a web application to handle/show info about raster file.

#### How to run:

Start application:
```bash
docker-compose up --build
```

Open the link: [http://localhost:3000](http://localhost:3000)

After the tests to shutdown the application use the following command:
```bash
docker-compose down
```

#### How to run manually:
**NOTE**: At this time there's a problem to run locally using Matplotlib/Flask and MacOS Mojave. The problem is based on multithreading.

O Linux/mac run the following commands:

* Frontend:
    ```bash
    make frontend-run
    ```
 
* API:
    ```bash
    make run
    ```

### Dependencies:

* Python:
    * Flask==1.0.2
    * Flask-Cors==3.0.6
    * pytest==3.8.2
    * scikit-learn==0.20.0
    * numpy==1.15.2
    * GDAL==2.3.2
    * rasterio==1.0.8
    * matplotlib==2.2.3
    * Pillow==5.3.0
    
* Frontend:
    * Flask==1.0.2
    * Flask-Cors==3.0.6
    * pytest==3.8.2
    * scikit-learn==0.20.0
    * numpy==1.15.2
    * GDAL==2.3.2
    * rasterio==1.0.8
    * matplotlib==2.2.3
    * Pillow==5.3.0