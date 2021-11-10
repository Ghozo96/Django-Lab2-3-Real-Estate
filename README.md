# Django-Lab2-3-Real-Estate
Real estate website project using django

Lab 2:
-Created 3 models: listing, realtor and contact(inquiry)
-Created superuser ghazala, migrated the 3 models and customized the admin area and the list view
-Created a search form in the index page, and another form(modal) to make an inquiry about a certain listing, you can see this modal in the page called listing
-Used static files(images, css, js) and collected these files in a root static file every time I made a change to any of the static files in the RealEstate app.

Lab 3:
-Created the register feature and made the accounts app, added the registered users to the User model
-Used authentication for login and logout
-I used the foreignkey relation field between Listing and Realtor
-I customized the admin area to match the brand colors and customized the list with list_display, also used search_fields. Check ListingAdmin, RealtorAdmin and ContactAdmin.
-Used the ImageField to hold images of the property listings.
-An email is sent to the realtor assosciated with a certain listing that a user inquired about.

Please feel free to run the server and check out the project

P.S: I didn't make the html/css/bootstrap part, I only edited the html files using template tags whenever needed and made the pages dynamic(getting data from database).
