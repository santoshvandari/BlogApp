# Blog App
## Introduction
This is the web based application for Posting the Blog. It is developed using the technologies like HTML, CSS, JS and BootStrap in frontend and python(django Framework) in backend as well as sqlite database(default) as a database.

#### Home Page 
![Home Page](/img/home.png)

#### Admin Page 
![Admin Page](/img/admin.png)

## Features
The Blog app has the following features.
 - A new User can Create the Blog.
 - Visitor can view the Posted Blog.
 - User can delete and modify the existing Blog.
 - User can add new User if he/she holds that permission.

## Usages
You System must have the following things to use this Blog App.
 - Installation of `python` and  `pip`

    Python is available for every platform. Download it according to you os. You can download it from [Here.](https://www.python.org/downloads/)


Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
    git clone https://github.com/santoshvandari/BlogApp.git 
    cd BlogApp
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and Windows User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Create Super User
```bash 
    python3 manage.py createsuperuser
    #Fill the Required Information
```

 - Run the Server
```bash
    python3 manage.py runserver #FOr Linux User
```
 - Open the url in Browser
 ```bash
    http://127.0.0.1:8000/  #For Home
    http://127.0.0.1:8000/login # For Login
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Blog app, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this app.

## License
This project is licensed under the [License](LICENSE).