# crispy-forms
Style your forms using django-crispy-forms

# Forms have never been this crispy.

### Why use crispy forms?
#### django provides us with style our forms without css (using form.as_p, form.as_t, or form.as_li)  but even with these forms are still not that appealing to the end users.
#### How then can I style my forms, you ask?

## Guide on how to use crispy forms

#### 1. Open a folder in your desktop.
#### 2. Create a project and app using django. (django-admin startproject proj . & django-admin startapp crispy_app).
#### 3. In your proj folder open settings.py and add crispy_app in the INSTALLED_APPS = [] list.

![set1](https://user-images.githubusercontent.com/78599959/181211003-5ec52c92-418d-4044-bb53-713fccb51d1c.png)

#### 4. In your app (i.e. crispy_app), create a folder called templates. In the templates folder, create another folder named crispy_app.


#### 5. In your app, open views.py create a class UserLogin that uses LoginView().

![views](https://user-images.githubusercontent.com/78599959/181211839-a5e29c54-fbcb-4b86-b8af-173219ba4f8a.png)

#### 6. Create a index.html in the crispy_app (located in the templates folder) and add the create a HTML form.

![index-form](https://user-images.githubusercontent.com/78599959/181211957-d0dbf2a3-40cb-4033-a48e-ff07c580096a.png)

#### Initial Output

![form1](https://user-images.githubusercontent.com/78599959/181208832-84572d89-ce2d-47e7-b901-2d50adfb9780.png)

###### The form rendered above is not appealing. We will use crispy_forms to style it.

###### 1. Open your terminal or cmd.
###### 2. Type pip install django-crispy-forms and press Enter.
###### 3. In your settings.py add the installed app in INSTALLED_APPS = []

![set2](https://user-images.githubusercontent.com/78599959/181211375-e78c3685-b68e-46d2-96af-fad4e9aeaaca.png)

###### 4. Create a variable, CRISPY_TEMPLATE_PACK = ''.
###### 5. Download Boostrap 3 or 4. Extract the zip file.
###### 6. Create a folder named static, to handle all static files. In your static folder, copy and paste extracted boostrap folder.
###### 7. Configure STATICFILES_DIRS = [<include path to locate bootstrap folder>]. I renamed the extracted folder to bootstrap4.

![settings](https://user-images.githubusercontent.com/78599959/181209224-1df8a797-073e-4828-88f6-49dd2e990fad.png)

###### 8. Since our CRISPY_TEMPLATE_PACK is an empty string, we will change it to CRISPY_TEMPLATE_PACK = 'bootstrap4'.

###### 9. In your template (i.e. index.html) load static to include bootstrap.min.css and load crispy tag ({% load crispy_forms_tags  %}). Add crispy tag to your login form.

![index4](https://user-images.githubusercontent.com/78599959/181209081-da5c8270-f713-436c-b8ba-c9a49b4926ae.png)


### Styled form - using crispy-forms

![form2](https://user-images.githubusercontent.com/78599959/181208992-ac7c4a68-75a8-4034-83f3-12548b5e11b5.png)

