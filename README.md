# AdsQuery
Post your Ads for Free on AdsQuery. And get potential customers.

Checkout the project live here: https://adsquery.herokuapp.com/

If you find any bugs, please open an issue and I will look into it.
I will soon add contributing guidelines, if you are interested then you can
contribute to this project.

# DESIGN AND IMPLEMENTATION
3.1 System Design
	The system design process involves developing several modules of the system at different levels of the abstraction. AdQuery’s web app is built by combining multiple technologies and that is what we will be discussing in this section. This is divided into the backend and frontend part of the app.

3.1.1 Backend Technologies
Backend Architecture of AdQuery includes:
Django : 
“Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so that we can focus on writing your app without needing to reinvent the wheel. It’s free and open source.”
Django version used in the project is Django 3.1.4
We are using django-social-auth library to Authorize and Login using third party accounts based on the OAuth2 protocol, currently we use Google, Twitter and GitHub for our Login functionality, there is no Signup feature on our platform, when a user visits the site for the time they just have to login using any of the above mentioned third party accounts and use the app.
The Advantages of using Django or The Reason we chose Django:
Fast Paced Development: Django was designed to help developers take applications from concept to completion as quickly as possible.
Reassuringly secure: Django takes security seriously and helps developers avoid many common security mistakes.
Exceedingly scalable: Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.
Open Source: Django is open source and its community is really helpful and encouraging.
PostgreSQL: 
PostgreSQL is the database that we chose as our RDBMS. There are a lot of advantages of using PostgreSQL as a Database for our project. PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help manage our project data no matter how big or small the dataset.
PostgreSQL version used in the Project is Django 13.1
Advantages of using PostgreSQL:
Open Source DBMS: PostgreSQL is the only open source DBMS that provides enterprise-class performance and functions
ACID and Transaction: PostgreSQL supports ACID (Atomicity, Consistency, Isolation, Durability)
Function Support: Custom functions can be written, also PostgreSQL supports SQL functions called “Stored Procedure” which can be used for server environments.
Multiple Language Adapter Support: PostgreSQL has multiple language adapters to support in its development such as Python, C++, Java etc.
Psycopg2:
Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It is designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent INSERTs or UPDATEs.
Psycopg version used in the project is psycopg 2.8.6
3.1.2 Frontend Technologies
We use the following frontend technologies on AdQuery:
HTML: 
Hypertext Markup Language is the most basic building block of the Web. It defines the meaning and structure of web content. “Hypertext” refers to links that connect web pages to one another either within a single website or between websites. Links are a fundamental aspect of the Web.
HTML uses “markup” to annotate text, images and other content for display in a web browser. HTML markup includes special “elements” such as <head>,<title>,<body> and many others. Those were just to name a few.
Django provides us something known as “Django Templating Language” which eases the development of HTML and allows us to dynamically generate our HTML files and helps us with context variables to be used in a template. And Django templates help us in building forms. There is also a library called “crispy forms”  which helps us in generating the html for the required forms written in python in our django app. Internally crispy forms does make use of Bootstrap CSS, so we had to include that too.
Materialize:
	As HTML helps us in structuring our content. CSS helps us style the web page which in turn helps us to provide a better user experience to the user. 
AdQuery uses Materialize CSS Framework to style the web pages and display them in a proper manner. Materialize accelerates the development of the project in terms of styling and aligning all the elements of the HTML correctly. It also helps in making the web app responsive, meaning that the styling of the HTML templates would work according to the view port of the device. Thus making the web app responsive in mobile, tablet and all other devices of standard width and height. Materialize also provides us with their icons to use.
Fontawesome is another icon library that is being used for a small section.
Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology. Google's goal is to develop a system of design that allows for a unified user experience across all their products on any platform.
jQuery:
	jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. With a combination of versatility and extensibility, jQuery has changed the way that millions of people write JavaScript.
The main use of jQuery in our project was because of Materialize CSS. There are some small parts in our project where we have used jQuery for making AJAX post requests. But mostly it is used by Materialize. Also the advantage of using jQuery is that it supports cross browser APIs. That was the main reason we chose to use jQuery.
