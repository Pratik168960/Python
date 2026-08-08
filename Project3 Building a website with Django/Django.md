# Introduction to Django Web Development

Django is a powerful Python web framework used to build the backend infrastructure for massively popular websites like Instagram, Spotify, and YouTube.

### Why do we need a Web Framework?
Building a secure, fast website from scratch involves a lot of complex, repetitive tasks (like handling user passwords, connecting to databases, and managing security). 

A **framework** is a massive library of reusable modules that provides built-in functionality for all of these common tasks, saving developers hundreds of hours of work.

### Framework vs. Library
Technically, a framework is much more than just a library:
* A **library** is just a collection of code you can call whenever you want. You are in control of the architecture.
* A **framework** dictates the *structure* of your application. It tells you exactly what folders and files you must have in your project. This enforces consistency, meaning any developer can jump into any Django project in the world and immediately understand how it is organized.

---

### 1. Installing Django and Starting a Project
To start building our e-commerce site (PyShop), we use the terminal to install Django and generate the project folder.

```bash
# 1. Install the framework via pip
pip install django

# 2. Generate the boilerplate project structure 
# (Adding the '.' at the end builds the files in our current folder)
django-admin startproject pyshop .