![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d312e322e332d626c7565](https://user-images.githubusercontent.com/86531927/156447715-47323250-a4d0-400d-914c-df659d1666c6.svg)
![GitHub language count](https://img.shields.io/github/languages/count/amarjin6/postgrees-json?color=red&logo=Github) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amarjin6/postgrees-json?logo=gitbook&logoColor=green)
![GitHub commit merge status](https://img.shields.io/github/commit-status/amarjin6/postgrees-json/master/2d50390640570bbef9d750d0beaace5fb8f9508a)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/amarjin6/postgrees-json?label=activity&logo=Python&logoColor=yellow)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/amarjin6/postgrees-json?color=purple&include_prereleases)
## 📌Web page, that writes user data into postgree database as JSON object🏷

## 💡Main idea💡
Create a form with dynamic addition of inputs, not tied to any model (when you click on the button "add", a new input will appear). Store data in the model in a field of type JSON PostgreeSQL. Display data on another page on button "view".

## 🔎How to Install🔍
* **Clone project to your folder:** `git clone https://github.com/amarjin6/postgrees-json.git`
* **Check for updates and install all necessary [plugins](https://github.com/amarjin6/postgrees-json/tree/master/requirements)**
* **Set up database connection, fulfill missing strings in [settings](https://github.com/amarjin6/postgrees-json/blob/master/project_2/project_2/settings.py):**  
`SECRET_KEY = 'Your_secret_key'`      
`DATABASES = {`      
`'NAME': 'Your_name',`    
`'USER': 'Your_user',`    
`'PASSWORD': 'Your_password',`    
`'HOST': 'Your_host',`    
`'PORT': Your_port }`    
* **Сarry out [migrations](https://github.com/amarjin6/postgrees-json/tree/master/project_2/main/migrations) if it's necessary:**  
`python manage.py makemigrations`
`python manage.py migrate`
* **Run project:**
`python manage.py runserver`
## 🛠How to Use🛠
* Run the project in your IDE and open browser
* There you can add some data into a input field
* If you need one more input - click the button "add" and fulfill another input
* At the end of adding data - click the "submit" button on the bottom of dynamic inputs
* If all the data is valid, the programm will writes it in the Postgree database as data & JSON object, otherwise it will throw an error
* After that you can look at your database compose by clicking the "view" button on the left of you
* Completed!

![1](https://user-images.githubusercontent.com/86531927/156452131-e0f61519-0871-41d2-809a-2e88ba3d4fb6.jpg)
  
**For more information use the [docs](https://github.com/amarjin6/postgrees-json/tree/master/docs/docs.md) folder**

## 🔐Tests🔐
**Rigorous testing has been carried out by using:**
* Unit testing
* Functional testing
* Integration testing

*All tests were completed!*

🔑This project is compatible for WIndows and Linux Os
(Tested on Windows 10 PRO, Linux Manjaro(XFCE, KDE, GNOME))

![python-logo (2)](https://user-images.githubusercontent.com/86531927/156536220-5db566c6-9e2d-4c92-a239-2292bad68333.png)
![pngwing com (1)](https://user-images.githubusercontent.com/86531927/156533882-4e032fde-da53-4e4d-b0cf-498cbaa98eea.png)
![kisspng-postgresql-pgadmin-computer-icons-database-depende-elephants-5ad386c474c6b5 5149032415238120364783 (2)](https://user-images.githubusercontent.com/86531927/156536817-2becbc13-c4b4-4f49-b133-6c1940e4fd91.png)

# Python, Django, PostgreeSQL, JSON
